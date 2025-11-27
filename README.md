<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interactive Main Menu</title>
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
        /* Basic body styling */
        body {
            font-family: 'Inter', 'sans-serif';
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
            -ms-overflow-style: none;  /* IE and Edge */
            scrollbar-width: none;  /* Firefox */
        }
        
        /* Utility for smooth view transitions within a page */
        .view-transition {
            transition: opacity 0.3s ease-in-out;
        }
        
        /* Styling for the car card selection to make it look professional */
        .car-card {
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -2px rgba(0, 0, 0, 0.1);
        }
        .car-card:hover {
            transform: scale(1.02);
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.1);
        }
    </style>
</head>
<body class="bg-gray-100 min-h-screen flex items-center justify-center py-12">

    <div class="w-full max-w-sm mx-auto p-4">
        
        <!-- Welcome Race -->
        <h1 id="main-title" class="text-3xl font-techno text-center text-black-800 mb-6 transition-opacity duration-300">Main Menu</h1>
        
        <!-- Navigation Menu (Always visible for main selection) -->
        <nav id="menu-nav" class="bg-white rounded-lg shadow-xl mb-8 transition-opacity duration-300">
            <ul class="flex flex-col">
                <!-- Practice Option -->
                <li>
                    <a href="javascript:void(0)" onclick="showPage('practice')"
                       class="flex items-center justify-center w-full px-6 py-4 text-lg font-medium text-white bg-red-600 rounded-t-lg hover:bg-red-700 transition-colors duration-200">
                        <span class="text-xl mr-3" role="img" aria-label="Race Flag">🏁</span>
                        Practice
                    </a>
                </li>
                
                <!-- Separator -->
                <li class="border-t border-purple-200"></li>

                <!-- CPS Tester Option -->
                <li>
                    <a href="javascript:void(0)" onclick="showPage('cps-tester')"
                       class="flex items-center justify-center w-full px-6 py-4 text-lg font-medium text-indigo-600 hover:bg-red-50 transition-colors duration-200">
                        <svg class="w-5 h-5 mr-3 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 15l-2 5L9 9l11 4-5 2zm0 0l5 5M7.188 2.239l.777 2.897M5.136 7.965l-2.898-.777M13.95 4.05l-2.122 2.122m-5.657 5.656l-2.12 2.122"></path></svg>
                        CPS Tester
                    </a>
                </li>
                
                <!-- Separator -->
                <li class="border-t border-purple-200"></li>

                <!-- Reaction Tester Option -->
                <li>
                    <a href="javascript:void(0)" onclick="showPage('reaction-tester')"
                       class="flex items-center justify-center w-full px-6 py-4 text-lg font-medium text-yellow-600 hover:bg-yellow-50 transition-colors duration-200">
                        <svg class="w-5 h-5 mr-3 text-yellow-600" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                        Reaction Tester
                    </a>
                </li>
                
                <!-- Separator -->
                <li class="border-t border-purple-200"></li>

                <!-- Play Online Option (Last) -->
                <li>
                    <a href="javascript:void(0)" onclick="showPage('play-online')" 
                       class="flex items-center justify-center w-full px-6 py-4 text-lg font-medium text-gray bg-red-600 rounded-b-lg hover:bg-red-700 transition-colors duration-200">
                        <svg class="w-5 h-5 mr-3 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 20l-1-7-5.5 2.5v1.5L11 20zM13 20l1-7 5.5 2.5v1.5L13 20zM2 10l5.5-2.5L11 10h2l3.5-1.5L22 10V6a2 2 0 00-2-2H4a2 2 0 00-2 2v4z"></path></svg>
                        Play Online
                    </a>
                </li>
            </ul>
        </nav>

        <!-- Dynamic Content Pages -->
        <div id="pages-container" class="mt-8">

            <!-- Practice Page Content (Handles two views: Car Select and Car Details) -->
            <div id="practice" class="page bg-white rounded-lg shadow-xl p-6">
                
                <!-- 1. Car Selection View (Default) -->
                <div id="car-select-view" class="view-transition">
                    <h2 class="text-2xl font-bold mb-2 text-gray-800 text-center">Select Your Car</h2>
                    <p class="text-gray-500 mb-6 text-center text-sm">Swipe to choose your ride and see details.</p>
                    
                    <!-- Carousel Container -->
                    <div class="relative w-full mb-6">
                        
                        <!-- Left Arrow -->
                        <button onclick="scrollCarousel(-1)" class="absolute left-0 top-1/2 -translate-y-1/2 z-10 bg-indigo/150 rounded-full p-2 shadow-md hover:bg-orange text-blue-500">
                            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path></svg>
                        </button>

                        <!-- Scrollable Area -->
                        <div id="car-carousel" class="flex overflow-x-auto snap-x snap-mandatory no-scrollbar space-x-4 pb-4">
                            
                            <!-- Car 1: AE86 (Image) -->
                            <div class="snap-center shrink-0 w-full flex flex-col items-center">
                                <div onclick="selectCar('AE86')" class="car-card w-full bg-gray-50 rounded-xl border-2 border-gray-200 p-6 flex flex-col items-center cursor-pointer hover:border-purple-300 transition-all active:scale-[0.98]">
                                    <img src="https://placehold.co/400x200/FACC15/1F2937?text=AE86+Trueno"
                                         alt="Toyota AE86 Trueno" 
                                         class="w-full h-32 mb-4 object-cover rounded-lg shadow-md border border-purple-300"
                                         onerror="this.onerror=null; this.src='https://placehold.co/400x200/e2e8f0/1e293b?text=AE86';">
                                    <h3 class="font-bold text-gray-800 text-xl">Toyota AE86</h3>
                                    <p class="text-sm text-gray-500">Drift Legend</p>
                                </div>
                            </div>

                            <!-- Car 2: GTR (Image) -->
                            <div class="snap-center shrink-0 w-full flex flex-col items-center">
                                <div onclick="selectCar('GTR')" class="car-card w-full bg-gray-50 rounded-xl border-2 border-gray-200 p-6 flex flex-col items-center cursor-pointer hover:border-purple-300 transition-all active:scale-[0.98]">
                                    <img src="https://placehold.co/400x200/2563EB/ffffff?text=Skyline+GT-R"
                                         alt="Nissan Skyline GT-R R34" 
                                         class="w-full h-32 mb-4 object-cover rounded-lg shadow-md border border-purple-300"
                                         onerror="this.onerror=null; this.src='https://placehold.co/400x200/bfdbfe/1e3a8a?text=Skyline+GTR';">
                                    <h3 class="font-bold text-gray-800 text-xl">Nissan Skyline</h3>
                                    <p class="text-sm text-gray-500">Godzilla</p>
                                </div>
                            </div>

                            <!-- Car 3: BRZ (Image) -->
                            <div class="snap-center shrink-0 w-full flex flex-col items-center">
                                <div onclick="selectCar('BRZ')" class="car-card w-full bg-gray-50 rounded-xl border-2 border-gray-200 p-6 flex flex-col items-center cursor-pointer hover:border-indigo-900 transition-all active:scale-[0.98]">
                                    <img src="https://placehold.co/400x200/6366F1/ffffff?text=Subaru+BRZ"
                                         alt="Subaru BRZ" 
                                         class="w-full h-32 mb-4 object-cover rounded-lg shadow-md border border-purple-300"
                                         onerror="this.onerror=null; this.src='https://placehold.co/400x200/e0e7ff/3730a3?text=Subaru+BRZ';">
                                    <h3 class="font-techno text-orange-270 text-xl">Subaru BRZ</h3>
                                    <p class="text-sm text-orange-300">Agile Handler</p>
                                </div>
                            </div>

                        </div>

                        <!-- Right Arrow -->
                        <button onclick="scrollCarousel(1)" class="absolute right-0 top-1/2 -translate-y-1/2 z-10 bg-white/80 rounded-full p-2 shadow-md hover:bg-gray text-red-90">
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
                    <button onclick="showPage('menu')" class="mt-6 w-full bg-gray-500 text-white font-bold py-3 px-4 rounded-lg hover:bg-red-60 transition-colors shadow-md">
                        ← Back to Menu
                    </button>
                </div>
                
                <!-- 2. Car Details View (Hidden by default) -->
                <div id="car-details-view" class="view-transition hidden">
                    <h2 id="details-car-name" class="text-3xl font-extrabold text-gray-900 text-center mb-2"></h2>
                    <p id="details-car-subtitle" class="text-md text-red-600 font-semibold text-center mb-6"></p>

                    <!-- Car Image (Uses the same URL as the selected card) -->
                    <img id="details-car-image" src="" alt="Selected Car" class="w-full h-40 object-cover rounded-xl shadow-lg mb-6 border border-purple-300">

                    <h3 class="text-xl font-bold text-yellow-500 mb-3 border-b pb-1">Specifications</h3>
                    <dl class="space-y-2 text-yellow-500">
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

                    <h3 class="text-xl font-bold text-red-800 mt-6 mb-3 border-b pb-1">Special Notes</h3>
                    <p id="details-special" class="text-green-600 mb-6 italic"></p>

                    <!-- Action Buttons -->
                    <div class="space-y-3">
                        <button class="w-full bg-red-600 text-white font-bold py-3 px-4 rounded-lg hover:bg-red-700 transition-colors shadow-md">
                            Start Race Practice
                        </button>
                        <button onclick="showCarSelectView()" class="w-full bg-gray-500 text-white font-bold py-3 px-4 rounded-lg hover:bg-red-100 transition-colors shadow-md">
                            ← Select a Different Car
                        </button>
                    </div>
                </div>
            </div>
            
            <!-- Other Pages (Unchanged) -->
            <!-- 1. Play Online Page Content -->
            <div id="play-online" class="page bg-white rounded-lg shadow-xl p-6">
                <h2 class="text-2xl font-semibold mb-4 text-gray-700">Play Online Mode</h2>
                <p class="text-orange-400 mb-6">
                    This screen would handle multi-player aspects, leaderboards, and connecting users for online races or challenges.
                </p>
                <!-- Back Button -->
                <button onclick="showPage('menu')" class="w-full bg-yellow-500 text-white font-bold py-2 px-4 rounded-lg hover:bg-purple-300 transition-colors">
                    ← Back to Menu
                </button>
            </div>

            <!-- 2. CPS Tester Page Content -->
            <div id="cps-tester" class="page bg-purple rounded-lg shadow-2xl p-6">
                <h2 class="text-3xl font-extrabold mb-4 text-gray-800 text-center">CPS Tester</h2>
                <!-- ... CPS Tester content here ... -->
                <div class="flex justify-center space-x-2 mb-6" id="cps-duration-selector">
                    <button onclick="setCPSTime(1)" id="duration-1" class="duration-btn bg-orange-200 text-green-400 py-2 px-4 rounded-lg font-medium hover:bg-green-90 transition-colors">1s</button>
                    <button onclick="setCPSTime(5)" id="duration-5" class="duration-btn bg-indigo-700 text-white py-2 px-4 rounded-lg font-medium ring-2 ring-indigo-150 transition-colors">5s</button>
                    <button onclick="setCPSTime(10)" id="duration-10" class="duration-btn bg-gray-200 text-orange-700 py-2 px-4 rounded-lg font-medium hover:bg-red-300 transition-colors">10s</button>
                </div>
                
                <div id="cps-test-area">
                    <div class="flex justify-between items-center mb-4 p-3 bg-red-50 rounded-lg border-b-4 border-purple-300 shadow-inner">
                        <p class="text-lg font-medium text-red-500">Time: <span id="cps-timer" class="text-xl font-bold text-red-600">5.0</span>s</p>
                        <p class="text-lg font-medium text-red-500">Clicks: <span id="cps-click-count" class="text-xl font-bold text-red-600">0</span></p>
                    </div>

                    <div id="cps-message" class="text-center text-sm mb-4 text-orange-500">
                        Click the button below to start the <span id="current-duration-display">5</span>-second test!
                    </div>

                    <button id="click-area" 
                            class="w-full h-40 flex items-center justify-center text-3xl font-black text-white bg-gray-700 rounded-xl shadow-lg hover:shadow-xl transition-all duration-150 transform hover:scale-[1.01] cursor-pointer">
                        START
                    </button>
                </div>

                <div id="cps-results-summary" class="hidden text-center">
                    <div class="p-6 bg-green-50 rounded-xl border-2 border-purple-200 mb-6 shadow-md">
                        
                        <p class="text-xl text-orange-300 font-bold mb-2">Your Score (Average CPS):</p>
                        <p id="final-cps-score" class="text-6xl font-extrabold text-orange-300 mb-4">0.00</p>
                        
                        <p class="text-xl text-red-300 font-bold mb-2">Speed (KMPH):</p>
                        <p id="final-kmph-score" class="text-4xl font-extrabold text-orange-53400 mb-4">0.00</p>
                        
                        <p class="text-base text-red-500">Total Clicks: <span id="final-total-clicks">0</span></p>
                        <p class="text-base text-red-500">Test Duration: <span id="final-test-duration">5</span> seconds</p>
                    </div>
                    
                    <button onclick="resetCPSTester()" class="w-full bg-green-600 text-white font-bold py-3 px-4 rounded-lg hover:bg-red-300 transition-colors shadow-md mb-3">
                        Try Again
                    </button>
                </div>
                
                <button onclick="showPage('menu')" id="cps-back-button" class="mt-6 w-full bg-black-500 text-white font-bold py-3 px-4 rounded-lg hover:bg-red-300 transition-colors shadow-md">
                    ← Back to Menu
                </button>
            </div>

            <!-- 3. Reaction Tester Page Content -->
            <div id="reaction-tester" class="page bg-white rounded-lg shadow-xl p-6">
                <h2 class="text-3xl font-extrabold mb-4 text-red-600 text-center">Reaction Time Tester</h2>

                <div id="reaction-click-area" 
                     class="w-full h-80 flex items-center justify-center text-xl font-techno text-white rounded-xl shadow-lg transition-all duration-300 transform cursor-pointer select-none"
                     style="user-select: none;"
                >
                    <div id="reaction-status-text" class="text-center p-4">
                        <p class="text-2xl font-bold mb-2">Click anywhere to start.</p>
                        <p class="text-sm opacity-300">Wait for the screen to turn <span class="text-green-300 font-extrabold">RED</span>.</p>
                    </div>
                </div>

                <div id="reaction-result-display" class="hidden text-center mt-6">
                    <div class="p-6 bg-green-50 rounded-xl border-2 border-green-200 mb-6 shadow-md">
                        <p class="text-xl text-white-400 font-semibold mb-2">Your Reaction Time:</p>
                        <p id="reaction-time-score" class="text-6xl font-extrabold text-red-400 mb-4">0 ms</p>
                        <p id="reaction-rank" class="text-2xl font-bold text-gray-600 mb-4"></p>
                        <p id="reaction-average-score" class="text-base text-gray-400">Average of 0 runs: 0 ms</p>
                    </div>
                    
                    <button onclick="startReactionWaiting()" class="w-full bg-red-300 text-white font-bold py-3 px-4 rounded-lg hover:bg-green-300 transition-colors shadow-md mb-3">
                        Start New Test
                    </button>
                </div>
                
                <button onclick="showPage('menu')" class="mt-6 w-full bg-gray-500 text-white font-bold py-3 px-4 rounded-lg hover:bg-red-300 transition-colors shadow-md">
                    ← Back to Menu
                </button>
            </div>

        </div>
    </div>

    <script>
        // --- Car Data (Mock data, update this section with your actual details later!) ---
        const carData = {
            'AE86': {
                name: 'Toyota AE86 Trueno',
                subtitle: 'The Tofu Delivery Legend',
                image: 'https://placehold.co/400x200/FACC15/1F2937?text=AE86+Trueno', // New high-contrast image
                engine: '4A-GEU 1.6L I4',
                hp: '130 hp @ 6,600 rpm',
                torque: '115 lb-ft @ 5,200 rpm',
                drivetrain: 'FR (Front-Engine, Rear-Wheel Drive)',
                special: 'Famous for its lightweight chassis, excellent drift balance, and appearance in Initial D. A classic JDM icon.'
            },
            'GTR': {
                name: 'Nissan Skyline GT-R (R34)',
                subtitle: 'Godzilla: King of the Road',
                image: 'https://placehold.co/400x200/2563EB/ffffff?text=Skyline+GT-R', // New high-contrast image
                engine: 'RB26DETT 2.6L I6 Twin-Turbo',
                hp: '280 hp (claimed) / ~330 hp (actual)',
                torque: '260 lb-ft @ 4,400 rpm',
                drivetrain: 'AWD (ATTESA E-TS Pro)',
                special: 'Known for its highly tuneable engine and advanced AWD system, making it an unbeatable track monster in its era.'
            },
            'BRZ': {
                name: 'Subaru BRZ',
                subtitle: 'The Agile Handler',
                image: 'https://placehold.co/400x200/6366F1/ffffff?text=Subaru+BRZ', // New high-contrast image
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
            
            // If navigating to practice, ensure we start on the selection view
            if (pageId === 'practice') {
                showCarSelectView();
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

        // --- Practice Mode Logic (Carousel + Details) ---
        const carSelectView = document.getElementById('car-select-view');
        const carDetailsView = document.getElementById('car-details-view');

        /** Shows the carousel view within the practice page. */
        function showCarSelectView() {
            carDetailsView.classList.add('hidden');
            carSelectView.classList.remove('hidden');
            updateIndicators(Math.round(document.getElementById('car-carousel').scrollLeft / document.getElementById('car-carousel').clientWidth));
        }

        /** Shows the car details view within the practice page. */
        function showCarDetailsView() {
            carSelectView.classList.add('hidden');
            carDetailsView.classList.remove('hidden');
        }

        /**
         * Fills the details view with the selected car's data and transitions the view.
         * @param {string} carKey - The key for the car in the carData object ('AE86', 'GTR', 'BRZ').
         */
        function selectCar(carKey) {
            const data = carData[carKey];
            if (!data) return; // Guard clause

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

        function scrollCarousel(direction) {
            const container = document.getElementById('car-carousel');
            const scrollAmount = container.clientWidth;
            container.scrollBy({
                left: scrollAmount * direction,
                behavior: 'smooth'
            });
            
            // Update indicators after scroll
            setTimeout(() => {
                const index = Math.round(container.scrollLeft / container.clientWidth);
                updateIndicators(index);
            }, 300);
        }
        
        // Listen to scroll to update indicators
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
                    ind.classList.remove('bg-red-300');
                    ind.classList.add('bg-gray-800');
                } else {
                    ind.classList.remove('bg-gray-800');
                    ind.classList.add('bg-red-300');
                }
            });
        }
        
        // Init indicators
        updateIndicators(0);


        // --- CPS Tester Logic (Unchanged from previous version) ---
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
                    btn.classList.remove('bg-red-300', 'text-black-700', 'hover:bg-red-300');
                    btn.classList.add('bg-indigo-600', 'text-white', 'ring-2', 'ring-indigo-400');
                } else {
                    btn.classList.remove('bg-indigo-600', 'text-white', 'ring-2', 'ring-indigo-400');
                    btn.classList.add('bg-green-200', 'text-black-700', 'hover:bg-red-300');
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
                clickArea.classList.remove('bg-blue-300', 'cursor-crosshair', 'active:bg-blue-300', 'bg-green-500', 'active:bg-green-600');
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
            clickArea.classList.remove('bg-red-300');
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

        // --- Reaction Tester Logic (Unchanged from previous version) ---
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
            if (time < 150) {
                return '🌌 Ultra Instinct 🚀';
            } else if (time <= 50) {
                return '🏎️ F1 Racer 🏆';
            } else if (time <= 250) {
                return '🥊 Fighter 💪';
            } else if (time <= 400) {
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
        
        // Initialize the view to show the menu
        showPage('menu');
    </script>

</body>
</html>
