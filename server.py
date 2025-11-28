#!/usr/bin/env python3
"""
FastAPI server with WebSocket support for multiplayer online racing.
Handles lobby management, real-time player synchronization, and race results.
"""

import os
import random
import string
import json
import time
from typing import Dict, List, Optional
from dataclasses import dataclass, field, asdict
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import uvicorn

app = FastAPI()

# --- Data Classes ---

@dataclass
class Player:
    """Represents a player in an online race."""
    player_id: str
    username: str
    websocket: WebSocket = field(repr=False, compare=False)
    lobby_code: Optional[str] = None
    car_id: str = "AE86"
    is_ready: bool = False
    is_crashed: bool = False
    grids_survived: int = 0
    survival_time_ms: int = 0
    crash_timestamp: Optional[float] = None
    current_lane: int = 2

    def to_dict(self) -> dict:
        """Convert player to dictionary for JSON serialization (without websocket)."""
        return {
            "player_id": self.player_id,
            "username": self.username,
            "car_id": self.car_id,
            "is_ready": self.is_ready,
            "is_crashed": self.is_crashed,
            "grids_survived": self.grids_survived,
            "survival_time_ms": self.survival_time_ms,
            "current_lane": self.current_lane
        }


@dataclass
class Lobby:
    """Represents a game lobby/room."""
    code: str
    host_id: str
    state: str = "waiting"  # waiting, countdown, in_race, finished
    created_at: float = field(default_factory=time.time)
    players: Dict[str, Player] = field(default_factory=dict)
    trap_seed: Optional[int] = None
    race_start_time: Optional[float] = None
    max_players: int = 6

    def to_dict(self) -> dict:
        """Convert lobby to dictionary for JSON serialization."""
        return {
            "code": self.code,
            "host_id": self.host_id,
            "state": self.state,
            "players": [p.to_dict() for p in self.players.values()],
            "player_count": len(self.players),
            "max_players": self.max_players,
            "trap_seed": self.trap_seed
        }

    def get_leaderboard(self) -> List[dict]:
        """Generate sorted leaderboard based on grids survived and time."""
        players_list = list(self.players.values())
        # Sort by grids_survived (desc), then survival_time_ms (desc)
        sorted_players = sorted(
            players_list,
            key=lambda p: (p.grids_survived, p.survival_time_ms),
            reverse=True
        )
        return [
            {
                "rank": i + 1,
                "username": p.username,
                "car_id": p.car_id,
                "grids_survived": p.grids_survived,
                "survival_time_ms": p.survival_time_ms
            }
            for i, p in enumerate(sorted_players)
        ]


# --- Lobby Manager ---

class LobbyManager:
    """Manages all active lobbies and connected players."""

    def __init__(self):
        self.lobbies: Dict[str, Lobby] = {}
        self.players: Dict[str, Player] = {}  # player_id -> Player

    def generate_lobby_code(self) -> str:
        """Generate a unique 6-character lobby code."""
        while True:
            code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            if code not in self.lobbies:
                return code

    def generate_player_id(self) -> str:
        """Generate a unique player ID."""
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=12))

    def create_lobby(self, host_player: Player) -> Lobby:
        """Create a new lobby with the given player as host."""
        code = self.generate_lobby_code()
        lobby = Lobby(code=code, host_id=host_player.player_id)
        lobby.players[host_player.player_id] = host_player
        host_player.lobby_code = code
        self.lobbies[code] = lobby
        return lobby

    def join_lobby(self, code: str, player: Player) -> Optional[Lobby]:
        """Join an existing lobby. Returns None if lobby not found or full."""
        lobby = self.lobbies.get(code.upper())
        if not lobby:
            return None
        if len(lobby.players) >= lobby.max_players:
            return None
        if lobby.state != "waiting":
            return None
        
        lobby.players[player.player_id] = player
        player.lobby_code = code.upper()
        return lobby

    def leave_lobby(self, player_id: str) -> Optional[str]:
        """Remove a player from their lobby. Returns the lobby code if lobby still exists."""
        player = self.players.get(player_id)
        if not player or not player.lobby_code:
            return None
        
        lobby = self.lobbies.get(player.lobby_code)
        if not lobby:
            return None

        code = player.lobby_code
        del lobby.players[player_id]
        player.lobby_code = None

        # If lobby is empty, delete it
        if len(lobby.players) == 0:
            del self.lobbies[code]
            return None

        # If host left, assign new host
        if lobby.host_id == player_id:
            lobby.host_id = list(lobby.players.keys())[0]

        return code

    def get_lobby(self, code: str) -> Optional[Lobby]:
        """Get a lobby by code."""
        return self.lobbies.get(code.upper())

    def register_player(self, player_id: str, username: str, websocket: WebSocket) -> Player:
        """Register a new player or update existing one."""
        if player_id in self.players:
            player = self.players[player_id]
            player.websocket = websocket
            player.username = username
        else:
            player = Player(player_id=player_id, username=username, websocket=websocket)
            self.players[player_id] = player
        return player

    def remove_player(self, player_id: str):
        """Completely remove a player."""
        if player_id in self.players:
            self.leave_lobby(player_id)
            del self.players[player_id]


# Global lobby manager instance
lobby_manager = LobbyManager()


# --- WebSocket Connection Manager ---

class ConnectionManager:
    """Manages WebSocket connections for broadcasting messages."""

    async def broadcast_to_lobby(self, lobby_code: str, message: dict, exclude_player_id: Optional[str] = None):
        """Send a message to all players in a lobby."""
        lobby = lobby_manager.get_lobby(lobby_code)
        if not lobby:
            return
        
        message_json = json.dumps(message)
        for player in lobby.players.values():
            if exclude_player_id and player.player_id == exclude_player_id:
                continue
            try:
                await player.websocket.send_text(message_json)
            except Exception:
                pass  # Player may have disconnected

    async def send_to_player(self, player_id: str, message: dict):
        """Send a message to a specific player."""
        player = lobby_manager.players.get(player_id)
        if player:
            try:
                await player.websocket.send_text(json.dumps(message))
            except Exception:
                pass


connection_manager = ConnectionManager()


# --- WebSocket Endpoint ---

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """Main WebSocket endpoint for all game communication."""
    await websocket.accept()
    player_id = None
    
    try:
        while True:
            data = await websocket.receive_text()
            message = json.loads(data)
            msg_type = message.get("type")

            # --- Player Registration ---
            if msg_type == "register":
                username = message.get("username", "Player")
                player_id = message.get("player_id") or lobby_manager.generate_player_id()
                car_id = message.get("car_id", "AE86")
                
                player = lobby_manager.register_player(player_id, username, websocket)
                player.car_id = car_id
                
                await websocket.send_text(json.dumps({
                    "type": "registered",
                    "player_id": player_id,
                    "username": username
                }))

            # --- Create Lobby (Host Race) ---
            elif msg_type == "create_lobby":
                if not player_id or player_id not in lobby_manager.players:
                    await websocket.send_text(json.dumps({
                        "type": "error",
                        "message": "Please register first"
                    }))
                    continue

                player = lobby_manager.players[player_id]
                
                # Leave current lobby if in one
                if player.lobby_code:
                    old_code = lobby_manager.leave_lobby(player_id)
                    if old_code:
                        await connection_manager.broadcast_to_lobby(old_code, {
                            "type": "player_left",
                            "player_id": player_id,
                            "username": player.username
                        })

                lobby = lobby_manager.create_lobby(player)
                
                await websocket.send_text(json.dumps({
                    "type": "lobby_created",
                    "lobby": lobby.to_dict()
                }))

            # --- Join Lobby (Join Race) ---
            elif msg_type == "join_lobby":
                if not player_id or player_id not in lobby_manager.players:
                    await websocket.send_text(json.dumps({
                        "type": "error",
                        "message": "Please register first"
                    }))
                    continue

                code = message.get("code", "").upper()
                player = lobby_manager.players[player_id]
                
                # Leave current lobby if in one
                if player.lobby_code:
                    old_code = lobby_manager.leave_lobby(player_id)
                    if old_code:
                        await connection_manager.broadcast_to_lobby(old_code, {
                            "type": "player_left",
                            "player_id": player_id,
                            "username": player.username
                        })

                lobby = lobby_manager.join_lobby(code, player)
                
                if not lobby:
                    await websocket.send_text(json.dumps({
                        "type": "error",
                        "message": "Lobby not found, full, or already started"
                    }))
                    continue

                # Send lobby info to the joining player
                await websocket.send_text(json.dumps({
                    "type": "lobby_joined",
                    "lobby": lobby.to_dict()
                }))

                # Notify other players
                await connection_manager.broadcast_to_lobby(code, {
                    "type": "player_joined",
                    "player": player.to_dict(),
                    "lobby": lobby.to_dict()
                }, exclude_player_id=player_id)

            # --- Leave Lobby ---
            elif msg_type == "leave_lobby":
                if not player_id:
                    continue
                    
                player = lobby_manager.players.get(player_id)
                if not player or not player.lobby_code:
                    continue

                code = player.lobby_code
                remaining_code = lobby_manager.leave_lobby(player_id)
                
                await websocket.send_text(json.dumps({
                    "type": "lobby_left"
                }))

                if remaining_code:
                    lobby = lobby_manager.get_lobby(remaining_code)
                    await connection_manager.broadcast_to_lobby(remaining_code, {
                        "type": "player_left",
                        "player_id": player_id,
                        "username": player.username,
                        "lobby": lobby.to_dict() if lobby else None
                    })

            # --- Update Car Selection ---
            elif msg_type == "update_car":
                if not player_id:
                    continue
                    
                player = lobby_manager.players.get(player_id)
                if not player:
                    continue
                    
                player.car_id = message.get("car_id", "AE86")
                
                if player.lobby_code:
                    lobby = lobby_manager.get_lobby(player.lobby_code)
                    if lobby:
                        await connection_manager.broadcast_to_lobby(player.lobby_code, {
                            "type": "player_updated",
                            "player": player.to_dict(),
                            "lobby": lobby.to_dict()
                        })

            # --- Toggle Ready Status ---
            elif msg_type == "toggle_ready":
                if not player_id:
                    continue
                    
                player = lobby_manager.players.get(player_id)
                if not player or not player.lobby_code:
                    continue

                player.is_ready = not player.is_ready
                lobby = lobby_manager.get_lobby(player.lobby_code)
                
                if lobby:
                    await connection_manager.broadcast_to_lobby(player.lobby_code, {
                        "type": "player_updated",
                        "player": player.to_dict(),
                        "lobby": lobby.to_dict()
                    })

            # --- Start Race (Host Only) ---
            elif msg_type == "start_race":
                if not player_id:
                    continue
                    
                player = lobby_manager.players.get(player_id)
                if not player or not player.lobby_code:
                    continue

                lobby = lobby_manager.get_lobby(player.lobby_code)
                if not lobby:
                    continue

                # Only host can start
                if lobby.host_id != player_id:
                    await websocket.send_text(json.dumps({
                        "type": "error",
                        "message": "Only the host can start the race"
                    }))
                    continue

                # Need at least 1 player (can play solo for testing)
                if len(lobby.players) < 1:
                    await websocket.send_text(json.dumps({
                        "type": "error",
                        "message": "Need at least 1 player to start"
                    }))
                    continue

                # Generate deterministic trap seed
                lobby.trap_seed = random.randint(1, 1000000)
                lobby.state = "countdown"
                lobby.race_start_time = time.time() + 3  # 3 second countdown

                # Reset all player stats
                for p in lobby.players.values():
                    p.is_crashed = False
                    p.grids_survived = 0
                    p.survival_time_ms = 0
                    p.crash_timestamp = None
                    p.current_lane = 2

                await connection_manager.broadcast_to_lobby(player.lobby_code, {
                    "type": "race_starting",
                    "countdown": 3,
                    "trap_seed": lobby.trap_seed,
                    "lobby": lobby.to_dict()
                })

            # --- Race Started Confirmation ---
            elif msg_type == "race_started":
                if not player_id:
                    continue
                    
                player = lobby_manager.players.get(player_id)
                if not player or not player.lobby_code:
                    continue

                lobby = lobby_manager.get_lobby(player.lobby_code)
                if lobby and lobby.state == "countdown":
                    lobby.state = "in_race"
                    lobby.race_start_time = time.time()

            # --- Player State Update During Race ---
            elif msg_type == "player_state":
                if not player_id:
                    continue
                    
                player = lobby_manager.players.get(player_id)
                if not player or not player.lobby_code:
                    continue

                lobby = lobby_manager.get_lobby(player.lobby_code)
                if not lobby or lobby.state != "in_race":
                    continue

                # Update player state
                player.current_lane = message.get("lane", player.current_lane)
                player.grids_survived = message.get("grids", player.grids_survived)
                player.survival_time_ms = message.get("time_ms", player.survival_time_ms)

                # Broadcast to other players
                await connection_manager.broadcast_to_lobby(player.lobby_code, {
                    "type": "player_state_update",
                    "player_id": player_id,
                    "lane": player.current_lane,
                    "grids": player.grids_survived,
                    "time_ms": player.survival_time_ms
                }, exclude_player_id=player_id)

            # --- Player Crashed ---
            elif msg_type == "player_crashed":
                if not player_id:
                    continue
                    
                player = lobby_manager.players.get(player_id)
                if not player or not player.lobby_code:
                    continue

                lobby = lobby_manager.get_lobby(player.lobby_code)
                if not lobby:
                    continue

                # Update crash data
                player.is_crashed = True
                player.grids_survived = message.get("grids", player.grids_survived)
                player.survival_time_ms = message.get("time_ms", player.survival_time_ms)
                player.crash_timestamp = time.time()

                # Notify all players
                await connection_manager.broadcast_to_lobby(player.lobby_code, {
                    "type": "player_crashed",
                    "player_id": player_id,
                    "username": player.username,
                    "grids": player.grids_survived,
                    "time_ms": player.survival_time_ms
                })

                # Check if all players have crashed
                all_crashed = all(p.is_crashed for p in lobby.players.values())
                if all_crashed:
                    lobby.state = "finished"
                    leaderboard = lobby.get_leaderboard()
                    
                    await connection_manager.broadcast_to_lobby(player.lobby_code, {
                        "type": "race_finished",
                        "leaderboard": leaderboard,
                        "lobby": lobby.to_dict()
                    })

            # --- Return to Lobby ---
            elif msg_type == "return_to_lobby":
                if not player_id:
                    continue
                    
                player = lobby_manager.players.get(player_id)
                if not player or not player.lobby_code:
                    continue

                lobby = lobby_manager.get_lobby(player.lobby_code)
                if not lobby:
                    continue

                # Reset player state
                player.is_ready = False
                player.is_crashed = False
                player.grids_survived = 0
                player.survival_time_ms = 0

                # Check if all players want to return
                all_returned = all(not p.is_crashed for p in lobby.players.values())
                if all_returned or lobby.state == "finished":
                    lobby.state = "waiting"
                    for p in lobby.players.values():
                        p.is_ready = False
                        p.is_crashed = False

                await connection_manager.broadcast_to_lobby(player.lobby_code, {
                    "type": "lobby_updated",
                    "lobby": lobby.to_dict()
                })

    except WebSocketDisconnect:
        pass
    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        # Clean up on disconnect
        if player_id:
            player = lobby_manager.players.get(player_id)
            if player and player.lobby_code:
                code = player.lobby_code
                lobby_manager.leave_lobby(player_id)
                lobby = lobby_manager.get_lobby(code)
                if lobby:
                    await connection_manager.broadcast_to_lobby(code, {
                        "type": "player_left",
                        "player_id": player_id,
                        "username": player.username if player else "Unknown",
                        "lobby": lobby.to_dict()
                    })
            lobby_manager.remove_player(player_id)


# --- Static Files ---

# Serve static files from current directory
@app.get("/")
async def read_index():
    """Serve the main index.html file."""
    return FileResponse("index.html")


@app.get("/{file_path:path}")
async def read_file(file_path: str):
    """Serve static files."""
    # Security check - prevent directory traversal
    if ".." in file_path:
        raise HTTPException(status_code=403, detail="Forbidden")
    
    full_path = os.path.join(".", file_path)
    if os.path.isfile(full_path):
        return FileResponse(
            full_path,
            headers={
                "Cache-Control": "no-cache, no-store, must-revalidate",
                "Pragma": "no-cache",
                "Expires": "0"
            }
        )
    raise HTTPException(status_code=404, detail="File not found")


if __name__ == "__main__":
    print("Starting FastAPI server with WebSocket support...")
    print("Server running at http://0.0.0.0:5000/")
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")
