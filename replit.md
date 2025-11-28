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

## Recent Changes (Nov 28, 2025)
- Added in-game timer showing elapsed seconds during gameplay
  - Timer starts when game begins
  - Displays real-time counter in blue box below score
  - Shows total time on game over screen: "X Grids in Ys"
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
