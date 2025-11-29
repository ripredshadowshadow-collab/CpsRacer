# Interactive Grid Game

## Overview
A dynamic HTML5 game application featuring multiple mini-games with online multiplayer support:
- **Grid Avoidance Game**: Navigate through a grid-based racing game avoiding obstacles
- **CPS Tester**: Test your clicks-per-second performance
- **Reaction Tester**: Measure your reaction time
- **Online Mode**: Race against other players in real-time multiplayer lobbies (up to 6 players)

## Project Structure
```
.
├── index.html           # Main HTML file with embedded CSS and JavaScript
├── server.py           # FastAPI server with WebSocket support for multiplayer
├── pyproject.toml      # Python dependencies (FastAPI, uvicorn, websockets)
└── .gitignore         # Git ignore file for Python and Replit files
```

## Technology Stack
- **Frontend**: HTML5, Tailwind CSS (CDN), Vanilla JavaScript, WebSocket Client
- **Backend**: FastAPI with WebSocket support (Python 3.11)
- **Real-time Communication**: WebSocket for lobby management and race synchronization
- **Hosting**: Replit (0.0.0.0:5000)

## Development Setup
The project uses FastAPI with WebSocket support:
- Server binds to `0.0.0.0:5000` for Replit compatibility
- WebSocket endpoint at `/ws` for real-time multiplayer communication
- Cache-Control headers prevent caching issues during development
- Auto-restart enabled via workflow
- Dependencies managed via `uv` and `pyproject.toml`
- Python 3.11 with FastAPI, Uvicorn, and WebSockets installed

## Running Locally
```bash
python3 server.py
```
The application will be available at `http://0.0.0.0:5000/`

## Deployment
Configured for Replit Autoscale deployment:
- Deployment Target: Autoscale (for stateless web apps with WebSocket support)
- Run Command: `python3 server.py`
- Port: 5000
- Ready to publish: Click the "Publish" button in Replit to deploy

## Features
- Fully responsive mobile and desktop design
- Touch controls for mobile devices
- Multiple game modes with different difficulty levels
- Score tracking and performance metrics
- Car selection system with vehicle specifications

## Mobile Controls (Grid Game)
The Grid Game features dedicated mobile touch controls that appear on mobile devices:
- **W Button (Blue)**: Move up one lane + step forward
- **GO! Button (Green)**: Step forward without changing lane
- **S Button (Red)**: Move down one lane + step forward

These controls are automatically shown on:
- Screens smaller than 768px
- Devices with touch capability (no hover support)

Desktop users can use:
- **W key**: Move up + step forward
- **S key**: Move down + step forward
- **Click/Touch on track**: Step forward

## Online Mode (Multiplayer)
The game now supports online multiplayer racing with up to 6 players:

### How to Play Online
1. Click **Online Mode** from the main menu
2. Enter your username
3. Select your car (AE86, GT-R, or BRZ)
4. Choose to **Host Race** or **Join Race**:
   - **Host Race**: Creates a lobby with a unique 6-character code to share
   - **Join Race**: Enter a lobby code to join an existing race

### Lobby Features
- Real-time player list updates
- Host can start the race when ready
- Up to 6 players per lobby
- Players see who's the host

### Racing
- All players race simultaneously with synchronized obstacles
- Real-time score and survival tracking
- When a player crashes, others continue until all crash
- Live status shows how many players are still alive

### Leaderboard
After all players crash, a leaderboard displays:
- Final rankings based on grids survived
- Survival time for each player
- Medal system (gold, silver, bronze for top 3)
- Option to return to lobby for another race

### Technical Details
- Uses WebSocket for real-time communication
- Deterministic trap generation with shared seed ensures fair gameplay
- Server manages lobby state and race synchronization

## Notes
- Tailwind CSS loaded from CDN (suitable for this static app)
- No build step required - all assets are inline or loaded from CDN

## GitHub Export Ready

This project is now configured for GitHub with:
- Comprehensive README.md for documentation
- Updated .gitignore excluding large video files (*.mp4)
- Clean project structure suitable for open source
- Python server for local/Replit hosting

## How to Push to GitHub

1. **Create a GitHub repository** at https://github.com/new
2. **Copy the repository URL** (HTTPS or SSH)
3. **In Replit terminal**, run:
   ```bash
   git remote set-url origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   git branch -M main
   git add .
   git commit -m "Initial commit: Interactive Grid Game with video backgrounds"
   git push -u origin main
   ```
4. **Add video files** to GitHub Releases (optional, for download)

## Recent Changes (Nov 29, 2025)
- **Replit Environment Setup Complete**
  - Installed Python dependencies via uv (FastAPI, Uvicorn, WebSockets)
  - Configured workflow to run FastAPI server on port 5000
  - Set up deployment configuration for Autoscale
  - Updated .gitignore to exclude Python virtual environment
  - Verified all features working (Practice, CPS Tester, Reaction Tester, Online Mode)
  - Server successfully serving static files and WebSocket connections

## Previous Changes (Nov 28, 2025)
- **NEW: Online Multiplayer Mode**
  - Added Online Mode button to main menu
  - Username entry system for online players
  - Host Race: Create a lobby with shareable 6-character code
  - Join Race: Enter code to join existing lobbies
  - Real-time lobby with player list (up to 6 players)
  - Synchronized racing with deterministic trap generation
  - Live player status tracking during race
  - Leaderboard with rankings after all players crash
  - Return to lobby for rematches
- Upgraded server from SimpleHTTPServer to FastAPI with WebSocket support
- Added real-time WebSocket communication for multiplayer

### Previous Changes (Nov 28, 2025)
- Improved in-game timer with smart start/stop:
  - Timer starts only when the car first moves
  - Displays real-time counter in blue box below score
  - Shows "0s" before any movement
  - Stops immediately when car crashes
  - Game over screen displays: "X Grids in Ys" (e.g., "5 Grids in 8s")
- Simplified car designs to side-view perspective (2 visible wheels):
  - Removed top wheels for cleaner side-profile appearance
  - Kept front and rear wheels only showing realistic side view
- Enhanced car realism with gradient shading and detailed features:
  - **AE86**: Gradient body shading, curved windshields, pop-up style headlights, detailed rims with spokes, brake lights, hood vents
  - **GT-R**: Body gradient, aggressive hood scoops, angled windshields, iconic gold stripe, triple headlight design, LED-style taillights, star-pattern sport rims, rear wing
  - **BRZ**: Smooth body curves with gradient, lower accent stripe, rounded LED headlights, clean square taillights, mesh-pattern lightweight wheels
- Trap difficulty restored to original (every 10 points, 1-2 safe lanes)

## Previous Session Changes (Nov 28, 2025)
- Imported from GitHub and set up for Replit environment
- Renamed README.md to index.html
- Organized CSS and JS files into proper directories
- Created Python HTTP server with cache-control headers
- Configured workflow and deployment settings
- Added .gitignore for Python and Replit files
- Added mobile touch controls for Grid Game (W, S, GO! buttons)
- Added menu video background with sound toggle button
- Added practice mode video background with separate sound toggle
- Implemented smart background video management:
  - Menu video plays on main menu
  - Menu video pauses when entering Practice mode
  - Practice video plays during car selection and details views
  - Practice video pauses when starting the game
  - All videos resume/pause correctly when navigating between screens
- Created comprehensive README.md for GitHub
- Updated .gitignore to exclude video files and temporary assets
- Project is GitHub-ready for export
