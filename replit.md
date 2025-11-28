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
