<!DOCTYPE:html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interactive Grid Game</title>
    <!-- Load Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Configure Tailwind to use Inter font -->
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                    },
                    colors: {
                        'pixel-gray': '#e5e7eb',
                    }
                },
            },
        }
    </script>
    <style>
        /* CRITICAL: Ensure HTML and Body fill the viewport */
        html, body {
            height: 100%;
            width: 100%;
        }
        
        /* Basic body styling */
        body {
            font-family: 'Inter', 'sans-serif';
            background-color: transparent; 
            display: flex;
            align-items: center;
            justify-content: center;
            padding-top: 3rem;
            padding-bottom: 3rem;
            min-height: 100vh;
            overflow-y: auto; 
        }
        
        /* 1. Full-screen Video Background Implementation */
        #background-video {
            position: fixed; 
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            object-fit: cover; 
            z-index: 0; 
            background-color: #333; 
            filter: brightness(0.6) grayscale(0.1); 
        }

        /* 2. Main Content Container Styling for Readability */
        .main-menu-container {
            z-index: 10; 
            position: relative;
            background-color: rgba(255, 255, 255, 0.9); 
            backdrop-filter: blur(5px); 
            
            /* CRITICAL FIX: Constrain height and allow internal scrolling */
            max-height: calc(100vh - 6rem); 
            overflow-y: auto; /* IMPORTANT: Enable internal vertical scrolling */
        }

        /* Hide pages by default */
        .page {
            display: none;
            transition: opacity 0.3s ease-in-out;
            opacity: 0;
        }
        /* Style for the currently visible page */
        .page-visible {
            display: block;
            opacity: 1;
        }
        .duration-btn {
            @apply shadow-sm transition-all duration-150;
        }
        /* Hide scrollbar for Chrome, Safari and Opera */
        .no-scrollbar::-webkit-scrollbar {
            display: none;
        }
        /* Hide scrollbar for IE, Edge and Firefox */
        .no-scrollbar {
            -ms-overflow-style: none;
            scrollbar-width: none;
        }
        
        /* Utility for smooth view transitions within a page */
        .view-transition {
            transition: opacity 0.3s ease-in-out;
        }
        
        /* Styling for the car card selection to make it look professional */
        .car-card {
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -2px rgba(0, 0, 0, 0.1);
            background-color: #f7f7f7; 
        }
        .car-card:hover {
            transform: scale(1.02);
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.1);
        }
        
        /* Custom CSS for the Game Track Visuals (GRID GAME) */
        #game-track {
            position: relative;
            background-color: #1a1a1a; /* Dark road color */
            overflow: hidden;
            cursor: pointer; /* Indicate it is clickable */
            border-left: 10px solid #555;
            border-right: 10px solid #555;
            
            /* Add lane dividers for a visual grid effect */
            background-image: linear-gradient(to bottom, #444 2px, transparent 2px);
            background-size: 100% 20%; /* 5 lanes total (100% / 5 = 20%) */
        }
        
        /* Style for the car (fixed X position, dynamic Y position) */
        #game-car {
            transition: top 0.15s ease-in-out; /* Smooth vertical lane change */
        }
        
        /* Style for the traps (dynamic X and Y position) */
        .trap {
            position: absolute;
            width: 20%; /* Same width as the car */
            height: 20%; /* Same height as a lane */
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2rem;
            transition: left 0.1s linear, opacity 0.1s linear; /* Smooth trap movement */
            pointer-events: none; /* Make sure clicks pass through traps to the track */
        }
        
        /* Style for game over message */
        #game-over-message {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(220, 38, 38, 0.9);
            color: white;
            z-index: 20;
            display: none;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
        }

    </style>
</head>
<body class="min-h-screen flex items-center justify-center py-12">

    <!-- Video Background Element (Autoplay, Loop, and Muted) -->
    <video autoplay muted loop id="background-video">
        <source src="VID-20251127-WA0002.mp4" type="video/mp4">
        <!-- Fallback message -->
        Your browser does not support the video tag.
    </video>

    <!-- Main Menu Content Container -->
    <div class="w-full max-w-sm mx-auto p-4 main-menu-container rounded-xl shadow-2xl">
        
        <!-- Welcome Race -->
        <h1 id="main-title" class="text-3xl font-bold text-center text-gray-800 mb-6 transition-opacity duration-300">Main Menu</h1>
        
        <!-- Navigation Menu (Always visible for main selection) -->
        <nav id="menu-nav" class="bg-white rounded-lg shadow-xl mb-8 transition-opacity duration-300">
            <ul class="flex flex-col">
                <!-- Practice Option -->
                <li>
                    <a href="javascript:void(0)" onclick="showPage('practice')"
                       class="flex items-center justify-center w-full px-6 py-4 text-lg font-medium text-white bg-red-600 rounded-t-lg hover:bg-red-700 transition-colors duration-200">
                        <span class="text-xl mr-3" role="img" aria-label="Race Flag">🏁</span>
                        Practice (Grid Game)
                    </a>
                </li>
                
                <!-- Separator -->
                <li class="border-t border-gray-200"></li>

                <!-- CPS Tester Option -->
                <li>
                    <a href="javascript:void(0)" onclick="showPage('cps-tester')"
                       class="flex items-center justify-center w-full px-6 py-4 text-lg font-medium text-red-600 hover:bg-red-50 transition-colors duration-200">
                        <svg class="w-5 h-5 mr-3 text-red-600" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 15l-2 5L9 9l11 4-5 2zm0 0l5 5M7.188 2.239l.777 2.897M5.136 7.965l-2.898-.777M13.95 4.05l-2.122 2.122m-5.657 5.656l-2.12 2.122"></path></svg>
                        CPS Tester
                    </a>
                </li>
                
                <!-- Separator -->
                <li class="border-t border-gray-200"></li>

                <!-- Reaction Tester Option (Now the last item, so rounded-b-lg added) -->
                <li>
                    <a href="javascript:void(0)" onclick="showPage('reaction-tester')"
                       class="flex items-center justify-center w-full px-6 py-4 text-lg font-medium text-yellow-600 hover:bg-yellow-50 rounded-b-lg transition-colors duration-200">
                        <svg class="w-5 h-5 mr-3 text-yellow-600" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                        Reaction Tester
                    </a>
                </li>
            </ul>
        </nav>

        <!-- Dynamic Content Pages -->
        <div id="pages-container" class="mt-8">

            <!-- Practice Page Content (Handles four views: Car Select, Car Details, Map Selection, Driving View) -->
            <div id="practice" class="page bg-white rounded-lg shadow-xl p-6">
                
                <!-- 1. Car Selection View (Default) -->
                <div id="car-select-view" class="view-transition">
                    <h2 class="text-2xl font-bold mb-2 text-gray-800 text-center">Select Your Car</h2>
                    <p class="text-gray-500 mb-6 text-center text-sm">Swipe to choose your ride and see details.</p>
                    
                    <!-- Carousel Container -->
                    <div class="relative w-full mb-6">
                        
                        <!-- Left Arrow -->
                        <button onclick="scrollCarousel(-1)" class="absolute left-0 top-1/2 -translate-y-1/2 z-10 bg-white/80 rounded-full p-2 shadow-md hover:bg-white text-gray-600">
                            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path></svg>
                        </button>

                        <!-- Scrollable Area -->
                        <div id="car-carousel" class="flex overflow-x-auto snap-x snap-mandatory no-scrollbar space-x-4 pb-4">
                            
                            <!-- Car 1: AE86 (Image) -->
                            <div class="snap-center shrink-0 w-full flex flex-col items-center">
                                <div onclick="selectCar('AE86')" class="car-card w-full bg-gray-50 rounded-xl border-2 border-gray-200 p-6 flex flex-col items-center cursor-pointer hover:border-gray-800 transition-all active:scale-[0.98]">
                                    <img src="https://placehold.co/400x200/FACC15/1F2937?text=AE86+Trueno"
                                         alt="Toyota AE86 Trueno" 
                                         class="w-full h-32 mb-4 object-contain rounded-lg shadow-md border border-gray-300"
                                         onerror="this.onerror=null; this.src='https://placehold.co/400x200/e2e8f0/1e293b?text=AE86';">
                                    <h3 class="font-bold text-gray-800 text-xl">Toyota AE86</h3>
                                    <p class="text-sm text-gray-500">Drift Legend</p>
                                </div>
                            </div>

                            <!-- Car 2: GTR (Image) -->
                            <div class="snap-center shrink-0 w-full flex flex-col items-center">
                                <div onclick="selectCar('GTR')" class="car-card w-full bg-gray-50 rounded-xl border-2 border-gray-200 p-6 flex flex-col items-center cursor-pointer hover:border-blue-600 transition-all active:scale-[0.98]">
                                    <img src="https://placehold.co/400x200/2563EB/ffffff?text=Skyline+GT-R"
                                         alt="Nissan Skyline GT-R R34" 
                                         class="w-full h-32 mb-4 object-contain rounded-lg shadow-md border border-gray-300"
                                         onerror="this.onerror=null; this.src='https://placehold.co/400x200/bfdbfe/1e3a8a?text=Skyline+GTR';">
                                    <h3 class="font-bold text-gray-800 text-xl">Nissan Skyline</h3>
                                    <p class="text-sm text-gray-500">Godzilla</p>
                                </div>
                            </div>

                            <!-- Car 3: BRZ (Image) -->
                            <div class="snap-center shrink-0 w-full flex flex-col items-center">
                                <div onclick="selectCar('BRZ')" class="car-card w-full bg-gray-50 rounded-xl border-2 border-gray-200 p-6 flex flex-col items-center cursor-pointer hover:border-indigo-600 transition-all active:scale-[0.98]">
                                    <img src="https://placehold.co/400x200/4F46E5/ffffff?text=Subaru+BRZ"
                                         alt="Subaru BRZ Placeholder" 
                                         class="w-full h-32 mb-4 object-contain rounded-lg shadow-md border border-gray-300"
                                         onerror="this.onerror=null; this.src='https://placehold.co/400x200/bfdbfe/1e3a8a?text=BRZ';">
                                    <h3 class="font-bold text-gray-800 text-xl">Subaru BRZ</h3>
                                    <p class="text-sm text-gray-500">Agile Handler</p>
                                </div>
                            </div>

                        </div>

                        <!-- Right Arrow -->
                        <button onclick="scrollCarousel(1)" class="absolute right-0 top-1/2 -translate-y-1/2 z-10 bg-white/80 rounded-full p-2 shadow-md hover:bg-white text-gray-600">
                            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
                        </button>
                        
                        <!-- Indicators -->
                        <div class="flex justify-center space-x-2 mt-2">
                            <div class="w-2 h-2 rounded-full bg-gray-300 indicator"></div>
                            <div class="w-2 h-2 rounded-full bg-gray-300 indicator"></div>
                            <div class="w-2 h-2 rounded-full bg-gray-300 indicator"></div>
                        </div>

                    </div>
                    
                    <!-- Back Button for main Practice view -->
                    <button onclick="showPage('menu')" class="mt-6 w-full bg-gray-500 text-white font-bold py-3 px-4 rounded-lg hover:bg-gray-600 transition-colors shadow-md">
                        ← Back to Menu
                    </button>
                </div>
                
                <!-- 2. Car Details View (Hidden by default) -->
                <div id="car-details-view" class="view-transition hidden">
                    <h2 id="details-car-name" class="text-3xl font-extrabold text-gray-900 text-center mb-2"></h2>
                    <p id="details-car-subtitle" class="text-md text-red-600 font-semibold text-center mb-6"></p>

                    <!-- Car Image -->
                    <img id="details-car-image" src="" alt="Selected Car" class="w-full h-40 object-contain rounded-xl shadow-lg mb-6 border border-gray-200">

                    <h3 class="text-xl font-bold text-gray-800 mb-3 border-b pb-1">Specifications</h3>
                    <dl class="space-y-2 text-gray-700">
                        <div class="flex justify-between">
                            <dt class="font-medium">Engine:</dt>
                            <dd id="details-engine" class="font-semibold"></dd>
                        </div>
                        <div class="flex justify-between">
                            <dt class="font-medium">Horsepower:</dt>
                            <dd id="details-hp" class="font-semibold"></dd>
                        </div>
                        <div class="flex justify-between">
                            <dt class="font-medium">Torque:</dt>
                            <dd id="details-torque" class="font-semibold"></dd>
                        </div>
                        <div class="flex justify-between">
                            <dt class="font-medium">Drivetrain:</dt>
                            <dd id="details-drivetrain" class="font-semibold"></dd>
                        </div>
                    </dl>

                    <h3 class="text-xl font-bold text-gray-800 mt-6 mb-3 border-b pb-1">Special Notes</h3>
                    <p id="details-special" class="text-gray-600 mb-6 italic"></p>

                    <!-- Action Buttons -->
                    <div class="space-y-3">
                        <button onclick="showMapSelectionView()" class="w-full bg-red-600 text-white font-bold py-3 px-4 rounded-lg hover:bg-red-700 transition-colors shadow-md">
                            Start Grid Race
                        </button>
                        <button onclick="showCarSelectView()" class="w-full bg-gray-500 text-white font-bold py-3 px-4 rounded-lg hover:bg-gray-600 transition-colors shadow-md">
                            ← Select a Different Car
                        </button>
                    </div>
                </div>

                <!-- 3. Map Selection View -->
                <div id="map-selection-view" class="view-transition hidden">
                    <h2 class="text-3xl font-extrabold text-gray-900 text-center mb-6">Choose Practice Mode</h2>
                    
                    <!-- Random Map Option (Now starts the game) -->
                    <button onclick="startRace('random')" class="w-full mb-4 p-4 bg-green-600 text-white font-bold text-xl rounded-lg hover:bg-green-700 transition-colors shadow-lg flex items-center justify-center">
                        <span class="mr-3 text-2xl" role="img" aria-label="Dice">🎲</span> Start Grid Game
                    </button>

                    <!-- Maps Option (Placeholder) -->
                    <button onclick="showMapsList()" class="w-full mb-6 p-4 bg-blue-600 text-white font-bold text-xl rounded-lg hover:bg-blue-700 transition-colors shadow-lg flex items-center justify-center">
                        <span class="mr-3 text-2xl" role="img" aria-label="Map">🗺️</span> Map Selection (Disabled)
                    </button>

                    <!-- Back Button -->
                    <button onclick="showCarDetailsView()" class="w-full bg-gray-500 text-white font-bold py-3 px-4 rounded-lg hover:bg-gray-600 transition-colors shadow-md">
                        ← Back to Car Details
                    </button>
                </div>
                
                <!-- 4. Driving View (GRID GAME AREA) -->
                <div id="driving-view" class="view-transition hidden">
                    <h2 class="text-3xl font-extrabold text-red-600 text-center mb-4">Grid Avoidance Game</h2>
                    <p class="text-center text-gray-600 mb-6 font-semibold text-lg">
                        <span class="text-blue-600">W</span> (Up/Step) | 
                        <span class="text-red-600">S</span> (Down/Step) |
                        <span class="text-yellow-600">CLICK/TOUCH</span> (Step Forward)
                    </p>

                    <!-- Game Container -->
                    <div id="game-track" class="w-full h-80 bg-gray-100 rounded-lg border-4 border-gray-800 relative overflow-hidden mb-6">
                        
                        <!-- Game Over Message -->
                        <div id="game-over-message" class="hidden">
                            <p class="text-6xl font-extrabold mb-4">CRASH!</p>
                            <p class="text-2xl font-semibold mb-6">Game Over</p>
                            <p class="text-xl font-medium mb-4">Final Score: <span id="final-game-score" class="font-extrabold">0</span> Grids</p>
                            <button onclick="CarGame.reset();" class="bg-white text-red-600 font-bold py-3 px-6 rounded-lg hover:bg-gray-100 transition-colors shadow-md">
                                Try Again
                            </button>
                        </div>
                        
                        <!-- Car Icon (Fixed on the left, moves vertically) -->
                        <div id="game-car" 
                             class="absolute left-1/4 top-1/2 -translate-y-1/2 w-12 h-12 flex items-center justify-center text-3xl transition-all duration-75 ease-linear" 
                             style="transform: translateY(-50%);">
                            <!-- Top-down view SVG representation of a car -->
                            <svg class="w-full h-full text-red-700" fill="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                <rect x="5" y="5" width="14" height="14" rx="4" ry="4"/>
                                <rect x="6" y="6" width="12" height="12" fill="white"/>
                                <rect x="7" y="7" width="10" height="10" fill="currentColor"/>
                            </svg>
                        </div>
                        
                        <!-- Traps will be rendered here dynamically -->
                        <div id="trap-container">
                            <!-- Traps elements go here -->
                        </div>
                    </div>
                    
                    <!-- Score Display -->
                    <div class="p-4 bg-red-100 rounded-xl shadow-lg flex justify-between items-center border-b-4 border-red-400">
                        <div>
                            <p class="text-sm font-medium text-gray-500">Grids Safely Passed</p>
                        </div>
                        <p id="current-score-display" class="text-5xl font-extrabold text-red-700">0</p>
                    </div>

                    <!-- Back Button -->
                    <button onclick="endRacePractice()" class="mt-6 w-full bg-gray-500 text-white font-bold py-3 px-4 rounded-lg hover:bg-gray-600 transition-colors shadow-md">
                        ← End Game
                    </button>
                </div>
            </div>
            
            <!-- 1. CPS Tester Page Content (Unchanged) -->
            <div id="cps-tester" class="page bg-white rounded-lg shadow-2xl p-6">
                <h2 class="text-3xl font-extrabold mb-4 text-gray-800 text-center">CPS Tester</h2>
                <div class="flex justify-center space-x-2 mb-6" id="cps-duration-selector">
                    <button onclick="setCPSTime(1)" id="duration-1" class="duration-btn bg-gray-200 text-gray-700 py-2 px-4 rounded-lg font-medium hover:bg-gray-300 transition-colors">1s</button>
                    <button onclick="setCPSTime(5)" id="duration-5" class="duration-btn bg-indigo-600 text-white py-2 px-4 rounded-lg font-medium ring-2 ring-indigo-400 transition-colors">5s</button>
                    <button onclick="setCPSTime(10)" id="duration-10" class="duration-btn bg-gray-200 text-gray-700 py-2 px-4 rounded-lg font-medium hover:bg-gray-300 transition-colors">10s</button>
                </div>
                
                <div id="cps-test-area">
                    <div class="flex justify-between items-center mb-4 p-3 bg-red-50 rounded-lg border-b-4 border-red-500 shadow-inner">
                        <p class="text-lg font-medium text-red-500">Time: <span id="cps-timer" class="text-xl font-bold text-red-600">5.0</span>s</p>
                        <p class="text-lg font-medium text-red-500">Clicks: <span id="cps-click-count" class="text-xl font-bold text-red-600">0</span></p>
                    </div>

                    <div id="cps-message" class="text-center text-sm mb-4 text-gray-500">
                        Click the button below to start the <span id="current-duration-display">5</span>-second test!
                    </div>

                    <button id="click-area" 
                            class="w-full h-40 flex items-center justify-center text-3xl font-black text-white bg-gray-700 rounded-xl shadow-lg hover:shadow-xl transition-all duration-150 transform hover:scale-[1.01] cursor-pointer">
                        START
                    </button>
                </div>

                <div id="cps-results-summary" class="hidden text-center">
                    <div class="p-6 bg-red-50 rounded-xl border-2 border-red-200 mb-6 shadow-md">
                        
                        <p class="text-xl text-red-500 font-semibold mb-2">Your Score (Average CPS):</p>
                        <p id="final-cps-score" class="text-6xl font-extrabold text-red-600 mb-4">0.00</p>
                        
                        <p class="text-xl text-red-500 font-semibold mb-2">Speed (KMPH):</p>
                        <p id="final-kmph-score" class="text-4xl font-extrabold text-red-600 mb-4">0.00</p>
                        
                        <p class="text-base text-red-500">Total Clicks: <span id="final-total-clicks">0</span></p>
                        <p class="text-base text-red-500">Test Duration: <span id="final-test-duration">5</span> seconds</p>
                    </div>
                    
                    <button onclick="resetCPSTester()" class="w-full bg-green-600 text-white font-bold py-3 px-4 rounded-lg hover:bg-green-700 transition-colors shadow-md mb-3">
                        Try Again
                    </button>
                </div>
                
                <button onclick="showPage('menu')" id="cps-back-button" class="mt-6 w-full bg-gray-500 text-white font-bold py-3 px-4 rounded-lg hover:bg-gray-600 transition-colors shadow-md">
                    ← Back to Menu
                </button>
            </div>

            <!-- 2. Reaction Tester Page Content (Unchanged) -->
            <div id="reaction-tester" class="page bg-white rounded-lg shadow-xl p-6">
                <h2 class="text-3xl font-extrabold mb-4 text-red-600 text-center">Reaction Time Tester</h2>

                <div id="reaction-click-area" 
                     class="w-full h-80 flex items-center justify-center text-xl font-bold text-white rounded-xl shadow-lg transition-all duration-300 transform cursor-pointer select-none"
                     style="user-select: none;"
                >
                    <div id="reaction-status-text" class="text-center p-4">
                        <p class="text-2xl font-bold mb-2">Click anywhere to start.</p>
                        <p class="text-sm opacity-80">Wait for the screen to turn <span class="text-green-300 font-extrabold">GREEN</span>.</p>
                    </div>
                </div>

                <div id="reaction-result-display" class="hidden text-center mt-6">
                    <div class="p-6 bg-green-50 rounded-xl border-2 border-green-200 mb-6 shadow-md">
                        <p class="text-xl text-gray-700 font-semibold mb-2">Your Reaction Time:</p>
                        <p id="reaction-time-score" class="text-6xl font-extrabold text-green-600 mb-4">0 ms</p>
                        <p id="reaction-rank" class="text-2xl font-bold text-gray-800 mb-4"></p>
                        <p id="reaction-average-score" class="text-base text-gray-500">Average of 0 runs: 0 ms</p>
                    </div>
                    
                    <button onclick="startReactionWaiting()" class="w-full bg-green-500 text-white font-bold py-3 px-4 rounded-lg hover:bg-green-600 transition-colors shadow-md mb-3">
                        Start New Test
                    </button>
                </div>
                
                <button onclick="showPage('menu')" class="mt-6 w-full bg-gray-500 text-white font-bold py-3 px-4 rounded-lg hover:bg-gray-600 transition-colors shadow-md">
                    ← Back to Menu
                </button>
            </div>

        </div>
    </div>

    <script>
        // --- Global State ---
        let currentSelectedCarId = null; 

        // --- Car Data (Mock data) ---
        const carData = {
            'AE86': {
                name: 'Toyota AE86 Trueno',
                subtitle: 'The Tofu Delivery Legend',
                image: 'https://placehold.co/400x200/FACC15/1F2937?text=AE86+Trueno', 
                engine: '4A-GEU 1.6L I4',
                hp: '130 hp @ 6,600 rpm',
                torque: '115 lb-ft @ 5,200 rpm',
                drivetrain: 'FR (Front-Engine, Rear-Wheel Drive)',
                special: 'Famous for its lightweight chassis, excellent drift balance, and appearance in Initial D. A classic JDM icon.'
            },
            'GTR': {
                name: 'Nissan Skyline GT-R (R34)',
                subtitle: 'Godzilla: King of the Road',
                image: 'https://placehold.co/400x200/2563EB/ffffff?text=Skyline+GT-R', 
                engine: 'RB26DETT 2.6L I6 Twin-Turbo',
                hp: '280 hp (claimed) / ~330 hp (actual)',
                torque: '260 lb-ft @ 4,400 rpm',
                drivetrain: 'AWD (ATTESA E-TS Pro)',
                special: 'Known for its highly tuneable engine and advanced AWD system, making it an unbeatable track monster in its era.'
            },
            'BRZ': {
                name: 'Subaru BRZ',
                subtitle: 'The Agile Handler',
                image: 'https://placehold.co/400x200/4F46E5/ffffff?text=Subaru+BRZ', 
                engine: 'FA20 2.0L H4 Boxer',
                hp: '200 hp @ 7,000 rpm',
                torque: '151 lb-ft @ 6,400 rpm',
                drivetrain: 'FR (Front-Engine, Rear-Wheel Drive)',
                special: 'Designed purely for driving pleasure and balance. It prioritizes handling and driver feedback over raw straight-line speed.'
            }
        };


        // --- Page Navigation Logic ---
        const menuNav = document.getElementById('menu-nav');
        const mainTitle = document.getElementById('main-title');
        let currentPage = 'menu';

        function showPage(pageId) {
            
            // 1. Reset games if navigating away
            if (currentPage === 'cps-tester' && pageId !== 'cps-tester') resetCPSTester();
            if (currentPage === 'reaction-tester' && pageId !== 'reaction-tester') resetReactionTester();
            if (currentPage === 'driving-view' && pageId !== 'driving-view') CarGame.stop(); // Stop the game loop

            // If navigating to practice, ensure we start on the selection view
            if (pageId === 'practice') {
                if (!currentSelectedCarId || currentPage === 'menu') {
                     showCarSelectView();
                } else {
                    showCarDetailsView(); 
                }
            }

            const pages = document.querySelectorAll('.page');
            
            // 2. Hide/Show Menu and Title
            if (pageId === 'menu') {
                menuNav.classList.remove('hidden', 'opacity-0');
                mainTitle.classList.remove('hidden', 'opacity-0');
            } else {
                menuNav.classList.add('hidden', 'opacity-0');
                mainTitle.classList.add('hidden', 'opacity-0');
            }
            
            // 3. Hide all content pages
            pages.forEach(page => {
                page.classList.remove('page-visible');
            });
            
            // 4. Show the requested content page
            if (pageId !== 'menu') {
                const newPage = document.getElementById(pageId);
                if (newPage) {
                    newPage.classList.add('page-visible');
                }
            }
            
            currentPage = pageId;
        }

        // --- Practice Mode Logic (Carousel + Details + Map Selection + Driving) ---
        const carSelectView = document.getElementById('car-select-view');
        const carDetailsView = document.getElementById('car-details-view');
        const mapSelectionView = document.getElementById('map-selection-view');
        const drivingView = document.getElementById('driving-view');

        /** Transitions to the Car Selection View */
        function showCarSelectView() {
            carDetailsView.classList.add('hidden');
            mapSelectionView.classList.add('hidden'); 
            drivingView.classList.add('hidden'); // Hide driving view
            carSelectView.classList.remove('hidden');
            const carousel = document.getElementById('car-carousel');
            if (carousel) {
                updateIndicators(Math.round(carousel.scrollLeft / carousel.clientWidth));
            }
        }

        /** Transitions to the Car Details View */
        function showCarDetailsView() {
            carSelectView.classList.add('hidden');
            mapSelectionView.classList.add('hidden'); 
            drivingView.classList.add('hidden'); // Hide driving view
            carDetailsView.classList.remove('hidden');
        }

        /** Transitions to the Map Selection View (Random/Maps) */
        function showMapSelectionView() {
            carDetailsView.classList.add('hidden');
            carSelectView.classList.add('hidden');
            drivingView.classList.add('hidden'); // Hide driving view
            mapSelectionView.classList.remove('hidden');
            CarGame.stop(); // Ensure the game stops if we exit via the 'End Practice' button
        }
        
        /** Transitions to the Driving View (Game) */
        function showDrivingView() {
            carDetailsView.classList.add('hidden');
            mapSelectionView.classList.add('hidden'); 
            carSelectView.classList.add('hidden');
            drivingView.classList.remove('hidden');
            CarGame.init(); // Initialize and start the game
        }
        
        /** End the game and return to map selection */
        function endRacePractice() {
            CarGame.stop();
            showMapSelectionView();
        }


        /**
         * Fills the details view with the selected car's data and transitions the view.
         * @param {string} carKey - The key for the car in the carData object ('AE86', 'GTR', 'BRZ').
         */
        function selectCar(carKey) {
            const data = carData[carKey];
            if (!data) return; 

            // Store selected car ID
            currentSelectedCarId = carKey;
            
            // Fill Data in the Details View
            document.getElementById('details-car-name').textContent = data.name;
            document.getElementById('details-car-subtitle').textContent = data.subtitle;
            document.getElementById('details-car-image').src = data.image;
            document.getElementById('details-car-image').alt = data.name;
            document.getElementById('details-engine').textContent = data.engine;
            document.getElementById('details-hp').textContent = data.hp;
            document.getElementById('details-torque').textContent = data.torque;
            document.getElementById('details-drivetrain').textContent = data.drivetrain;
            document.getElementById('details-special').textContent = data.special;

            // Transition to the details view
            showCarDetailsView();
        }

        /** Handles starting the race (now directs to the driving view for 'random') */
        function startRace(mode) {
            if (mode === 'random') {
                showDrivingView();
            } else {
                alertBox('Map selection is disabled for the Grid Game. Please press "Start Grid Game".');
            }
        }

        /** Placeholder for showing the map list (future feature) */
        function showMapsList() {
            alertBox('Functionality to select a specific map is not yet implemented for the Grid Game.');
        }

        function scrollCarousel(direction) {
            const container = document.getElementById('car-carousel');
            if (!container) return;

            const scrollAmount = container.clientWidth;
            container.scrollBy({
                left: scrollAmount * direction,
                behavior: 'smooth'
            });
            
            setTimeout(() => {
                const index = Math.round(container.scrollLeft / container.clientWidth);
                updateIndicators(index);
            }, 300);
        }
        
        const carCarousel = document.getElementById('car-carousel');
        if (carCarousel) {
            carCarousel.addEventListener('scroll', () => {
                const index = Math.round(carCarousel.scrollLeft / carCarousel.clientWidth);
                updateIndicators(index);
            });
        }

        function updateIndicators(activeIndex) {
            const indicators = document.querySelectorAll('.indicator');
            indicators.forEach((ind, i) => {
                if (i === activeIndex) {
                    ind.classList.remove('bg-gray-300');
                    ind.classList.add('bg-gray-800');
                } else {
                    ind.classList.remove('bg-gray-800');
                    ind.classList.add('bg-gray-300');
                }
            });
        }
        
        // --- Grid Game Logic (OVERHAUL) ---
        const CarGame = {
            // Game Constants
            GRID_ROWS: 5,               // 5 vertical lanes
            GRID_HEIGHT_PERCENT: 20,    // 100% / 5 lanes
            MOVE_FORWARD_STEPS: 2,      // 1 click = 2 grids movement
            TRAP_SPAWN_RANGE: 4,        // Traps spawn 4 grids ahead
            
            // DOM Elements
            car: null,
            track: null,
            trapContainer: null,
            scoreDisplay: null,
            gameOverMessage: null,
            finalScoreDisplay: null,

            // Game State
            currentLane: 2, // 0 (top) to 4 (bottom) - Start center
            score: 0,
            traps: [],      // [{lane: 0-4, forwardSteps: 4}]
            isGameOver: true,
            
            init() {
                this.car = document.getElementById('game-car');
                this.track = document.getElementById('game-track');
                this.trapContainer = document.getElementById('trap-container');
                this.scoreDisplay = document.getElementById('current-score-display');
                this.gameOverMessage = document.getElementById('game-over-message');
                this.finalScoreDisplay = document.getElementById('final-game-score');
                
                if (!this.car || !this.track || !this.trapContainer || !this.scoreDisplay || !this.gameOverMessage) {
                    console.error("Game elements not found.");
                    return;
                }
                
                // Set up event listeners
                this.boundHandleKey = this.handleKey.bind(this);
                this.boundHandleClick = this.handleClick.bind(this);
                document.addEventListener('keydown', this.boundHandleKey);
                this.track.addEventListener('mousedown', this.boundHandleClick);
                this.track.addEventListener('touchstart', this.boundHandleClick);
                
                this.reset();
            },
            
            stop() {
                // Clean up listeners
                document.removeEventListener('keydown', this.boundHandleKey);
                this.track.removeEventListener('mousedown', this.boundHandleClick);
                this.track.removeEventListener('touchstart', this.boundHandleClick);
            },

            reset() {
                this.isGameOver = false;
                this.currentLane = 2; // Middle lane
                this.score = 0;
                this.traps = [];
                
                this.gameOverMessage.style.display = 'none';
                
                // Initial render
                this.render();
                this.updateDisplay();
                
                // Spawn first set of traps
                this.spawnTraps(this.TRAP_SPAWN_RANGE);
            },
            
            handleKey(e) {
                if (this.isGameOver) return;
                const key = e.key.toLowerCase();
                
                let direction = 0; // 0 for stationary step, -1 for up, 1 for down

                if (key === 'w') {
                    direction = -1;
                    e.preventDefault(); 
                } else if (key === 's') {
                    direction = 1;
                    e.preventDefault();
                } else {
                    return;
                }
                
                this.changeLaneAndStep(direction);
            },

            handleClick(e) {
                if (this.isGameOver) return;
                e.preventDefault();
                // Click/Touch only triggers a forward step (0 vertical movement)
                this.changeLaneAndStep(0); 
            },
            
            changeLaneAndStep(direction) {
                if (this.isGameOver) return;
                
                // 1. Calculate new lane (if direction is not 0)
                if (direction !== 0) {
                    const newLane = this.currentLane + direction;
                    if (newLane >= 0 && newLane < this.GRID_ROWS) {
                        this.currentLane = newLane;
                    }
                }
                
                // 2. Execute forward step (moves traps)
                this.stepForward();
                
                // 3. Render immediately
                this.render();
            },

            stepForward() {
                if (this.isGameOver) return;
                
                // 1. Collision Check (Trap is at forwardSteps=0)
                const collisionTrap = this.traps.find(trap => 
                    trap.forwardSteps === 0 && trap.lane === this.currentLane
                );
                
                if (collisionTrap) {
                    this.gameOver();
                    return;
                }

                // 2. Move Traps (2 grids forward, towards the car)
                this.traps = this.traps.map(trap => ({
                    ...trap,
                    forwardSteps: trap.forwardSteps - this.MOVE_FORWARD_STEPS
                })).filter(trap => trap.forwardSteps >= -this.MOVE_FORWARD_STEPS); // Remove traps that are now behind the car

                // 3. Update Score
                this.score += this.MOVE_FORWARD_STEPS; 
                this.updateDisplay();

                // 4. Trap Spawning Logic
                // Spawn a new set of traps when the score is a multiple of 10
                if (this.score % 10 === 0 && this.score > 0) { 
                    this.spawnTraps(this.TRAP_SPAWN_RANGE);
                }
            },
            
            spawnTraps(distance) {
                // Do not spawn if the designated spawn spot already has a trap
                const existingTrapAtSpawn = this.traps.find(trap => trap.forwardSteps === distance);
                if (existingTrapAtSpawn) return;

                const availableLanes = [...Array(this.GRID_ROWS).keys()];
                const trapsToSpawn = Math.random() < 0.3 ? 2 : 1; // 30% chance of 2 traps, 70% chance of 1 trap
                
                let spawnedLanes = [];

                for (let i = 0; i < trapsToSpawn; i++) {
                    // Pick a random lane that hasn't been used this step
                    const safeLanes = availableLanes.filter(l => !spawnedLanes.includes(l));
                    if (safeLanes.length === 0) break;

                    const randomLaneIndex = Math.floor(Math.random() * safeLanes.length);
                    const lane = safeLanes[randomLaneIndex];
                    
                    this.traps.push({ lane, forwardSteps: distance });
                    spawnedLanes.push(lane);
                }
            },

            render() {
                // 1. Render Car Position
                const topPercent = this.currentLane * this.GRID_HEIGHT_PERCENT + (this.GRID_HEIGHT_PERCENT / 2);
                this.car.style.top = `${topPercent}%`;
                
                // 2. Render Traps
                this.trapContainer.innerHTML = '';
                this.traps.forEach(trap => {
                    const trapElement = document.createElement('div');
                    trapElement.classList.add('trap');
                    
                    // Vertical position (Y-axis)
                    const trapTopPercent = trap.lane * this.GRID_HEIGHT_PERCENT;
                    trapElement.style.top = `${trapTopPercent}%`;
                    
                    // Horizontal position (X-axis)
                    // The "grids" are horizontal units. If 4 grids ahead is 100% (off-screen)
                    // We need a reference for the "grid" width. Let's assume 1 grid unit = 15% width.
                    // Car is at ~25% left. Traps start at ~100% (off-screen)
                    // We map forwardSteps 4 -> 100% and 0 -> 25% (where car is)
                    const gridWidth = 75; // The range between car and edge (100 - 25)
                    const maxSteps = this.TRAP_SPAWN_RANGE; // 4
                    
                    // Example: 
                    // forwardSteps=4 (spawn) -> left = 100%
                    // forwardSteps=0 (collision) -> left = 25%
                    // forwardSteps=2 (middle) -> left = 62.5%
                    
                    const leftPosition = 25 + (trap.forwardSteps / maxSteps) * gridWidth;
                    
                    // If the left position is less than the car's start position (25%), make it red (danger zone)
                    if (leftPosition < 25) {
                        trapElement.style.opacity = 0.5;
                    }
                    
                    trapElement.style.left = `${leftPosition}%`;
                    trapElement.innerHTML = '💥';
                    
                    this.trapContainer.appendChild(trapElement);
                });
            },

            updateDisplay() {
                this.scoreDisplay.textContent = this.score;
            },

            gameOver() {
                this.isGameOver = true;
                this.finalScoreDisplay.textContent = this.score;
                this.gameOverMessage.style.display = 'flex';
            }
        };

        // --- CUSTOM ALERT BOX (Replaces alert() and confirm()) ---
        function alertBox(message) {
            const existingAlert = document.getElementById('custom-alert');
            if (existingAlert) existingAlert.remove();
            
            const alertHtml = `
                <div id="custom-alert" class="fixed inset-0 bg-gray-900 bg-opacity-75 flex items-center justify-center z-50 p-4">
                    <div class="bg-white rounded-xl p-6 shadow-2xl max-w-sm w-full transform transition-all duration-300 scale-100">
                        <h3 class="text-xl font-bold text-red-600 mb-4">Notification</h3>
                        <p class="text-gray-700 mb-6">${message}</p>
                        <button onclick="document.getElementById('custom-alert').remove()" class="w-full bg-red-600 text-white font-bold py-2 rounded-lg hover:bg-red-700 transition-colors">
                            Close
                        </button>
                    </div>
                </div>
            `;
            document.body.insertAdjacentHTML('beforeend', alertHtml);
        }

        // --- CPS Tester Logic (Unchanged) ---
        let cpsGameState = 'IDLE';
        let clicks = 0;
        let timeLeft = 5; 
        let timerInterval = null;
        let currentDuration = 5;

        const clickArea = document.getElementById('click-area');
        const cpsTimerDisplay = document.getElementById('cps-timer');
        const cpsClickCountDisplay = document.getElementById('cps-click-count');
        const cpsMessage = document.getElementById('cps-message');
        const cpsTestArea = document.getElementById('cps-test-area');
        const cpsResultsSummary = document.getElementById('cps-results-summary');
        const finalCPSScore = document.getElementById('final-cps-score');
        const finalKMPHScore = document.getElementById('final-kmph-score');
        const finalTotalClicks = document.getElementById('final-total-clicks');
        const finalDurationDisplay = document.getElementById('final-test-duration');
        const durationDisplay = document.getElementById('current-duration-display');

        function updateDurationButtons() {
            const buttons = document.querySelectorAll('.duration-btn');
            buttons.forEach(btn => {
                const duration = parseInt(btn.textContent.replace('s', ''));
                if (duration === currentDuration) {
                    btn.classList.remove('bg-gray-200', 'text-gray-700', 'hover:bg-gray-300');
                    btn.classList.add('bg-indigo-600', 'text-white', 'ring-2', 'ring-indigo-400');
                } else {
                    btn.classList.remove('bg-indigo-600', 'text-white', 'ring-2', 'ring-indigo-400');
                    btn.classList.add('bg-gray-200', 'text-gray-700', 'hover:bg-gray-300');
                }
            });
        }

        function setCPSTime(newDuration) {
            if (cpsGameState === 'PLAYING') return; 
            currentDuration = newDuration;
            resetCPSTester(); 
        }


        function resetCPSTester() {
            if (timerInterval) {
                clearInterval(timerInterval);
            }
            
            cpsGameState = 'IDLE';
            clicks = 0;
            timeLeft = currentDuration; 

            if (cpsTestArea) cpsTestArea.classList.remove('hidden');
            if (cpsResultsSummary) cpsResultsSummary.classList.add('hidden');

            if (clickArea) {
                clickArea.removeEventListener('mousedown', handleCPSClick);
                clickArea.removeEventListener('touchstart', handleCPSClick);
                clickArea.addEventListener('mousedown', handleCPSClick);
                clickArea.addEventListener('touchstart', handleCPSClick);
            }

            if (clickArea) {
                clickArea.textContent = 'START';
                clickArea.classList.remove('bg-blue-600', 'cursor-crosshair', 'active:bg-blue-700', 'bg-green-500', 'active:bg-green-600');
                clickArea.classList.add('bg-gray-700'); 
            }
            
            if (cpsTimerDisplay) cpsTimerDisplay.textContent = timeLeft.toFixed(1);
            if (cpsClickCountDisplay) cpsClickCountDisplay.textContent = clicks;
            if (cpsMessage) cpsMessage.textContent = `Click the button below to start the ${currentDuration}-second test!`;
            if (durationDisplay) durationDisplay.textContent = currentDuration;
            
            updateDurationButtons(); 
        }

        function startCPSTest() {
            if (cpsGameState !== 'IDLE') return;

            if (timerInterval) clearInterval(timerInterval);
            
            cpsGameState = 'PLAYING';
            timeLeft = currentDuration;
            
            clickArea.textContent = 'CLICK! CLICK! CLICK!';
            clickArea.classList.remove('bg-gray-700');
            clickArea.classList.add('bg-blue-600', 'cursor-crosshair', 'active:bg-blue-700');
            
            cpsMessage.textContent = 'Test in progress... Click as fast as you can!';
            cpsTimerDisplay.textContent = timeLeft.toFixed(1);

            const startTime = Date.now();
            
            timerInterval = setInterval(() => {
                const elapsed = (Date.now() - startTime) / 1000;
                timeLeft = currentDuration - elapsed;
                
                if (timeLeft <= 0) {
                    endCPSTest(true); 
                } else {
                    cpsTimerDisplay.textContent = timeLeft.toFixed(1);
                }
            }, 100);
        }

        function endCPSTest(completed) {
            clearInterval(timerInterval);
            
            if (completed) {
                const finalCPS = clicks / currentDuration;
                const finalKMPH = finalCPS * 2;
                
                cpsGameState = 'IDLE'; 
                
                if (cpsTestArea) cpsTestArea.classList.add('hidden');
                if (cpsResultsSummary) cpsResultsSummary.classList.remove('hidden');

                if (finalCPSScore) finalCPSScore.textContent = finalCPS.toFixed(2);
                if (finalKMPHScore) finalKMPHScore.textContent = finalKMPH.toFixed(2);
                if (finalTotalClicks) finalTotalClicks.textContent = clicks;
                if (finalDurationDisplay) finalDurationDisplay.textContent = currentDuration;

            } else {
                 cpsGameState = 'IDLE';
                 resetCPSTester();
            }
        }

        function handleCPSClick(event) {
            event.preventDefault();
            
            if (cpsGameState === 'IDLE') {
                startCPSTest();
                clicks++; 
                if (cpsClickCountDisplay) cpsClickCountDisplay.textContent = clicks;

            } else if (cpsGameState === 'PLAYING') {
                clicks++;
                if (cpsClickCountDisplay) cpsClickCountDisplay.textContent = clicks;
            }
        }
        
        document.addEventListener('mousedown', (e) => {
            if (e.target.id === 'click-area' && cpsGameState === 'PLAYING') {
                e.preventDefault();
            }
        });

        // --- Reaction Tester Logic (Unchanged) ---
        let reactionState = 'IDLE'; 
        let timeoutId = null; 
        let startTime = null; 
        let reactionTimes = []; 
        
        const reactionClickArea = document.getElementById('reaction-click-area');
        const reactionStatusText = document.getElementById('reaction-status-text');
        const reactionResultDisplay = document.getElementById('reaction-result-display');
        const reactionTimeScore = document.getElementById('reaction-time-score');
        const reactionAverageScore = document.getElementById('reaction-average-score');
        const reactionRankDisplay = document.getElementById('reaction-rank');
        
        function getReactionRank(time) {
            if (timeoncl50) {
                return '🌌 Ultra Instinct 🚀';
            } else if (time <= 50) {
                return '🏎️ F1 Racer 🏆';
            } else if (time <= 250) {
                return '🥊 Fighter 💪';
            } else if (time <= 300) {
                return '🧍 Average';
            } else {
                return '🐌 Very Slow 🐢';
            }
        }

        function resetReactionTester() {
            clearTimeout(timeoutId);
            reactionState = 'IDLE';
            startTime = null;
            
            reactionClickArea.classList.remove('bg-green-500', 'bg-red-500', 'bg-blue-500', 'hover:bg-green-600');
            reactionClickArea.classList.add('bg-gray-500');
            
            reactionResultDisplay.classList.add('hidden');
            reactionStatusText.innerHTML = '<p class="text-2xl font-bold mb-2">Click anywhere to start.</p><p class="text-sm opacity-80">Wait for the screen to turn <span class="text-green-300 font-extrabold">GREEN</span>.</p>';
            
            reactionRankDisplay.textContent = ''; 
            updateReactionAverage();
        }

        function updateReactionAverage() {
            if (reactionTimes.length > 0) {
                const total = reactionTimes.reduce((a, b) => a + b, 0);
                const average = total / reactionTimes.length;
                reactionAverageScore.textContent = `Average of ${reactionTimes.length} runs: ${Math.round(average)} ms`;
            } else {
                reactionAverageScore.textContent = 'Average of 0 runs: 0 ms';
            }
        }

        function startReactionWaiting() {
            reactionState = 'WAITING';
            reactionResultDisplay.classList.add('hidden');
            reactionClickArea.classList.remove('bg-gray-500', 'bg-green-500', 'bg-red-500', 'bg-blue-500', 'hover:bg-green-600');
            reactionClickArea.classList.add('bg-indigo-600');
            reactionStatusText.innerHTML = '<p class="text-2xl font-bold text-white">...Wait for Green...</p>';

            const randomDelay = Math.random() * 3000 + 2000;
            
            timeoutId = setTimeout(showReactionReady, randomDelay);
        }

        function showReactionReady() {
            reactionState = 'READY';
            startTime = Date.now();
            
            reactionClickArea.classList.remove('bg-indigo-600');
            reactionClickArea.classList.add('bg-green-500', 'hover:bg-green-600');
            reactionStatusText.innerHTML = '<p class="text-4xl font-extrabold text-white">CLICK NOW!</p>';
        }

        function handleReactionClick(event) {
            event.preventDefault();

            if (reactionState === 'IDLE') {
                startReactionWaiting();
            } else if (reactionState === 'WAITING') {
                clearTimeout(timeoutId);
                reactionState = 'RESULT';
                
                reactionClickArea.classList.remove('bg-indigo-600');
                reactionClickArea.classList.add('bg-red-500');
                
                reactionStatusText.innerHTML = '<p class="text-3xl font-bold text-white">TOO SOON!</p><p class="mt-2 text-xl text-white">You clicked before it turned green.</p>';
                
                reactionTimeScore.textContent = 'Failed';
                reactionRankDisplay.textContent = '❌ Failed Test';
                reactionAverageScore.textContent = 'Click too soon penalty';
                reactionResultDisplay.classList.remove('hidden');

            } else if (reactionState === 'READY') {
                const endTime = Date.now();
                const reactionTime = endTime - startTime;
                
                reactionState = 'RESULT';
                reactionTimes.push(reactionTime);

                const rank = getReactionRank(reactionTime);

                reactionClickArea.classList.remove('bg-green-500', 'hover:bg-green-600');
                reactionClickArea.classList.add('bg-blue-500');

                reactionStatusText.innerHTML = '<p class="text-3xl font-bold text-white">Got it!</p><p class="mt-2 text-xl text-white">Your result is below.</p>';

                reactionTimeScore.textContent = `${reactionTime} ms`;
                reactionRankDisplay.textContent = rank;
                reactionResultDisplay.classList.remove('hidden');

                updateReactionAverage();
                
            } else if (reactionState === 'RESULT') {
                startReactionWaiting();
            }
        }
        
        if (reactionClickArea) {
            reactionClickArea.addEventListener('mousedown', (e) => {
                 if (reactionState !== 'RESULT') {
                    e.preventDefault(); 
                    handleReactionClick(e);
                 }
            });
            reactionClickArea.addEventListener('touchstart', (e) => {
                 if (reactionState !== 'RESULT') {
                    e.preventDefault(); 
                    handleReactionClick(e);
                 }
            });
        }
        
        window.onload = function() {
            // Initialize the view to show the menu
            showPage('menu');
            updateIndicators(0);
            
            // Initial element binding for CarGame
            CarGame.car = document.getElementById('game-car');
            CarGame.track = document.getElementById('game-track');
            CarGame.trapContainer = document.getElementById('trap-container');
            CarGame.scoreDisplay = document.getElementById('current-score-display');
            CarGame.gameOverMessage = document.getElementById('game-over-message');
            CarGame.finalScoreDisplay = document.getElementById('final-game-score');
        };
    </script>

</body>
</html>
