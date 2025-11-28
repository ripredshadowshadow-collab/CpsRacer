# Interactive Grid Game

## Overview
A static HTML5 game application featuring multiple mini-games:
- **Grid Avoidance Game**: Navigate through a grid-based racing game avoiding obstacles
- **CPS Tester**: Test your clicks-per-second performance
- **Reaction Tester**: Measure your reaction time

## Project Structure
```
.
├── index.html           # Main HTML file with embedded CSS and JavaScript
├── server.py           # Python HTTP server for serving static files
├── css/                # CSS files for mobile responsiveness
│   ├── mobile.css
│   └── mobile-ui-overlay.css
├── js/                 # JavaScript files for mobile interactions
│   ├── mobile-touch.js
│   └── mobile-integration.js
└── .gitignore         # Git ignore file for Python and Replit files
```

## Technology Stack
- **Frontend**: HTML5, Tailwind CSS (CDN), Vanilla JavaScript
- **Backend**: Python 3.11 HTTP Server
- **Hosting**: Replit (0.0.0.0:5000)

## Development Setup
The project uses a simple Python HTTP server to serve static files:
- Server binds to `0.0.0.0:5000` for Replit compatibility
- Cache-Control headers prevent caching issues during development
- Auto-restart enabled via workflow

## Running Locally
```bash
python3 server.py
```
The application will be available at `http://0.0.0.0:5000/`

## Deployment
Configured for Replit Autoscale deployment:
- Deployment Target: Autoscale (for simple stateless web apps)
- Run Command: `python3 server.py`
- Port: 5000

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

## Notes
- Missing video file `VID-20251127-WA0002.mp4` - app uses dark background fallback
- Tailwind CSS loaded from CDN (suitable for this static app)
- No build step required - all assets are inline or loaded from CDN

## Recent Changes (Nov 28, 2025)
- Imported from GitHub and set up for Replit environment
- Renamed README.md to index.html
- Organized CSS and JS files into proper directories
- Created Python HTTP server with cache-control headers
- Configured workflow and deployment settings
- Added .gitignore for Python and Replit files
- Added mobile touch controls for Grid Game (W, S, GO! buttons)
