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
                },
            },
        }
    </script>
    <style>
        /* Basic body styling */
        body {
            font-family: 'Inter', sans-serif;
        }
        /* Hide pages by default */
        .page {
            display: none;
            /* Simple fade animation for smooth transitions */
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
        /* Active state for click area */
        .click-area-active {
            transform: scale(0.98);
        }
    </style>
</head>
<body class="bg-gray-100 min-h-screen flex items-center justify-center py-12">

    <div class="w-full max-w-sm mx-auto p-4">
        
        <!-- Main Menu Title -->
        <h1 id="main-title" class="text-3xl font-bold text-center text-gray-800 mb-6 transition-opacity duration-300">Main Menu</h1>
        
        <!-- Navigation Menu (Always visible for main selection) -->
        <nav id="menu-nav" class="bg-white rounded-lg shadow-xl mb-8 transition-opacity duration-300">
            <ul class="flex flex-col">
                <!-- Practice Option (NEW - Top) -->
                <li>
                    <a href="javascript:void(0)" onclick="showPage('practice')"
                       class="flex items-center justify-center w-full px-6 py-4 text-lg font-medium text-gray-700 rounded-t-lg hover:bg-indigo-50 transition-colors duration-200">
                        <!-- Race Flag Icon for Practice -->
                        <svg class="w-5 h-5 mr-3 text-black-500" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5s3.332.477 4.5 1.253v13C19.832 18.477 18.246 18 16.5 18s-3.332.477-4.5 1.253"></path></svg>
                        Practice
                    </a>
                </li>
                
                <!-- Separator -->
                <li class="border-t border-gray-200"></li>

                <!-- CPS Tester Option -->
                <li>
                    <a href="javascript:void(0)" onclick="showPage('cps-tester')"
                       class="flex items-center justify-center w-full px-6 py-4 text-lg font-medium text-gray-700 hover:bg-indigo-50 transition-colors duration-200">
                        <!-- Mouse Click Icon -->
                        <svg class="w-5 h-5 mr-3 text-red-500" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 15l-2 5L9 9l11 4-5 2zm0 0l5 5M7.188 2.239l.777 2.897M5.136 7.965l-2.898-.777M13.95 4.05l-2.122 2.122m-5.657 5.656l-2.12 2.122"></path></svg>
                        CPS Tester
                    </a>
                </li>
                
                <!-- Separator -->
                <li class="border-t border-gray-200"></li>

                <!-- Reaction Tester Option -->
                <li>
                    <a href="javascript:void(0)" onclick="showPage('reaction-tester')"
                       class="flex items-center justify-center w-full px-6 py-4 text-lg font-medium text-gray-700 bg-red-600 rounded-b-lg hover:bg-black-50 transition-colors duration-200">
                        <!-- Lightning Bolt Icon -->
                        <svg class="w-5 h-5 mr-3 text-yellow-500" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                        Reaction Tester
                    </a>
                </li>
                
                <!-- Separator -->
                <li class="border-t border-gray-200"></li>

                <!-- Play Online Option (Last) -->
                <li>
                    <a href="javascript:void(0)" onclick="showPage('play-online')" 
                       class="flex items-center justify-center w-full px-6 py-4 text-lg font-medium text-white bg-red-600 rounded-b-lg hover:bg-black-500 transition-colors duration-200">
                        <!-- Gamepad Icon -->
                        <svg class="w-5 h-5 mr-3 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 20l-1-7-5.5 2.5v1.5L11 20zM13 20l1-7 5.5 2.5v1.5L13 20zM2 10l5.5-2.5L11 10h2l3.5-1.5L22 10V6a2 2 0 00-2-2H4a2 2 0 00-2 2v4z"></path></svg>
                        Play Online
                    </a>
                </li>
            </ul>
        </nav>

        <!-- Dynamic Content Pages -->
        <div id="pages-container" class="mt-8">

            <!-- Practice Page Content (NEW) -->
            <div id="practice" class="page bg-white rounded-lg shadow-xl p-6">
                <h2 class="text-2xl font-semibold mb-4 text-gray-700">Practice Zone</h2>
                <p class="text-gray-600 mb-6">
                    This area is reserved for single-player, untimed practice sessions to hone skills before testing or playing online.
                </p>
                <!-- Back Button -->
                <button onclick="showPage('menu')" class="w-full bg-indigo-500 text-white font-bold py-2 px-4 rounded-lg hover:bg-indigo-600 transition-colors">
                    ← Back to Menu
                </button>
            </div>
            
            <!-- 1. Play Online Page Content -->
            <div id="play-online" class="page bg-white rounded-lg shadow-xl p-6">
                <h2 class="text-2xl font-semibold mb-4 text-gray-700">Play Online Mode</h2>
                <p class="text-gray-600 mb-6">
                    This screen would handle multi-player aspects, leaderboards, and connecting users for online races or challenges.
                </p>
                <!-- Back Button -->
                <button onclick="showPage('menu')" class="w-full bg-indigo-500 text-white font-bold py-2 px-4 rounded-lg hover:bg-indigo-600 transition-colors">
                    ← Back to Menu
                </button>
            </div>

            <!-- 2. CPS Tester Page Content (MAJOR UPDATE) -->
            <div id="cps-tester" class="page bg-white rounded-lg shadow-2xl p-6">
                <h2 class="text-3xl font-extrabold mb-4 text-gray-800 text-center">
                    CPS Tester
                </h2>

                <!-- Duration Selection Buttons (1s, 5s, 10s) -->
                <div class="flex justify-center space-x-2 mb-6" id="cps-duration-selector">
                    <button onclick="setCPSTime(1)" id="duration-1" class="duration-btn bg-gray-200 text-gray-700 py-2 px-4 rounded-lg font-medium hover:bg-gray-300 transition-colors">1s</button>
                    <button onclick="setCPSTime(5)" id="duration-5" class="duration-btn bg-indigo-600 text-white py-2 px-4 rounded-lg font-medium transition-colors">5s</button>
                    <button onclick="setCPSTime(10)" id="duration-10" class="duration-btn bg-gray-200 text-gray-700 py-2 px-4 rounded-lg font-medium hover:bg-gray-300 transition-colors">10s</button>
                </div>
                
                <!-- Test Area (Visible when IDLE or PLAYING) -->
                <div id="cps-test-area">
                    <div class="flex justify-between items-center mb-4 p-3 bg-gray-50 rounded-lg border-b-4 border-red-500 shadow-inner">
                        <p class="text-lg font-medium text-gray-700">Time: <span id="cps-timer" class="text-xl font-bold text-red-600">5.0</span>s</p>
                        <p class="text-lg font-medium text-gray-700">Clicks: <span id="cps-click-count" class="text-xl font-bold text-gray-800">0</span></p>
                    </div>

                    <div id="cps-message" class="text-center text-sm mb-4 text-gray-500">
                        Click the button below to start the <span id="current-duration-display">5</span>-second test!
                    </div>

                    <!-- The main clicking area/button -->
                    <!-- REMOVED: onclick="handleCPSClick()" to fix TypeError, using JS listeners instead -->
                    <button id="click-area" 
                            class="w-full h-40 flex items-center justify-center text-3xl font-black text-white bg-green-500 rounded-xl shadow-lg hover:shadow-xl transition-all duration-150 transform hover:scale-[1.01] cursor-pointer">
                        START
                    </button>
                </div>

                <!-- Results Summary (Hidden initially, shown after END) -->
                <div id="cps-results-summary" class="hidden text-center">
                    <div class="p-6 bg-red-50 rounded-xl border-2 border-red-200 mb-6 shadow-md">
                        <p class="text-xl text-gray-700 font-semibold mb-2">Your Score (Average CPS):</p>
                        <p id="final-cps-score" class="text-6xl font-extrabold text-red-600 mb-4">0.00</p>
                        <p class="text-base text-gray-500">Total Clicks: <span id="final-total-clicks">0</span></p>
                        <p class="text-base text-gray-500">Test Duration: <span id="final-test-duration">5</span> seconds</p>
                    </div>
                    
                    <button onclick="resetCPSTester()" class="w-full bg-green-500 text-white font-bold py-3 px-4 rounded-lg hover:bg-green-600 transition-colors shadow-md mb-3">
                        Try Again
                    </button>
                </div>
                
                <!-- Back Button -->
                <button onclick="showPage('menu')" id="cps-back-button" class="mt-6 w-full bg-indigo-500 text-white font-bold py-3 px-4 rounded-lg hover:bg-indigo-600 transition-colors shadow-md">
                    ← Back to Menu
                </button>
            </div>

            <!-- 3. Reaction Tester Page Content (Placeholder) -->
            <div id="reaction-tester" class="page bg-white rounded-lg shadow-xl p-6">
                <h2 class="text-2xl font-semibold mb-4 text-gray-700">Reaction Time Tester</h2>
                <p class="text-gray-600 mb-6">
                    This screen is dedicated to measuring the delay between a visual cue and the user's click response.
                </p>
                <!-- Placeholder for actual Reaction logic -->
                <div class="p-8 bg-yellow-100 border-2 border-yellow-500 rounded-lg text-center font-mono text-xl mb-6">
                    [Reaction Test Interface goes here]
                </div>
                <!-- Back Button -->
                <button onclick="showPage('menu')" class="w-full bg-indigo-500 text-white font-bold py-2 px-4 rounded-lg hover:bg-indigo-600 transition-colors">
                    ← Back to Menu
                </button>
            </div>

        </div>
    </div>

    <script>
        // --- Page Navigation Logic ---
        const menuNav = document.getElementById('menu-nav');
        const mainTitle = document.getElementById('main-title');
        let currentPage = 'menu';

        /**
         * Switches the view between the main menu and a content page.
         * @param {string} pageId - The ID of the page to show ('menu', 'play-online', 'cps-tester', 'reaction-tester', 'practice').
         */
        function showPage(pageId) {
            
            // 1. Reset CPS game if we are navigating away from it
            if (currentPage === 'cps-tester' && pageId !== 'cps-tester') {
                 resetCPSTester();
            }

            // Get all page elements
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
            
            // 4. Show the requested content page (if not the menu)
            if (pageId !== 'menu') {
                const newPage = document.getElementById(pageId);
                if (newPage) {
                    newPage.classList.add('page-visible');
                    // If we are navigating to the CPS tester, ensure it is reset
                    if (pageId === 'cps-tester') {
                        resetCPSTester();
                    }
                }
            }
            
            currentPage = pageId;
        }

        // --- CPS Tester Logic ---
        let cpsGameState = 'IDLE'; // IDLE, PLAYING
        let clicks = 0;
        let timeLeft = 5; // Start with default 5 seconds
        let timerInterval = null;
        let currentDuration = 5;

        // UI Element References
        const clickArea = document.getElementById('click-area');
        const cpsTimerDisplay = document.getElementById('cps-timer');
        const cpsClickCountDisplay = document.getElementById('cps-click-count');
        const cpsMessage = document.getElementById('cps-message');
        const cpsTestArea = document.getElementById('cps-test-area');
        const cpsResultsSummary = document.getElementById('cps-results-summary');
        const finalCPSScore = document.getElementById('final-cps-score');
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
            if (cpsGameState === 'PLAYING') return; // Cannot change during a test
            currentDuration = newDuration;
            resetCPSTester(); // Reset the UI and timer to the new duration
        }


        function resetCPSTester() {
            if (timerInterval) {
                clearInterval(timerInterval);
            }
            
            cpsGameState = 'IDLE';
            clicks = 0;
            timeLeft = currentDuration; 

            // Show Test Area, Hide Results
            if (cpsTestArea) cpsTestArea.classList.remove('hidden');
            if (cpsResultsSummary) cpsResultsSummary.classList.add('hidden');

            // 1. Clear any existing listeners
            if (clickArea) {
                clickArea.removeEventListener('mousedown', handleCPSClick);
                clickArea.removeEventListener('touchstart', handleCPSClick);

                // 2. Attach listeners for both start and counting (mousedown/touchstart are faster than click)
                clickArea.addEventListener('mousedown', handleCPSClick);
                clickArea.addEventListener('touchstart', handleCPSClick);
            }

            // Reset UI state
            if (clickArea) {
                clickArea.textContent = 'START';
                clickArea.classList.remove('bg-blue-600', 'cursor-crosshair', 'active:bg-blue-700');
                clickArea.classList.add('bg-green-500', 'active:bg-green-600');
            }
            
            if (cpsTimerDisplay) cpsTimerDisplay.textContent = timeLeft.toFixed(1);
            if (cpsClickCountDisplay) cpsClickCountDisplay.textContent = clicks;
            if (cpsMessage) cpsMessage.textContent = `Click the button below to start the ${currentDuration}-second test!`;
            if (durationDisplay) durationDisplay.textContent = currentDuration;
            
            updateDurationButtons(); 
        }

        function startCPSTest() {
            // Only proceed if not already playing
            if (cpsGameState !== 'IDLE') return;

            // Ensure any previous test is fully stopped
            if (timerInterval) clearInterval(timerInterval);
            
            cpsGameState = 'PLAYING';
            // Note: clicks is already incremented once in handleCPSClick 
            timeLeft = currentDuration;
            
            clickArea.textContent = 'CLICK! CLICK! CLICK!';
            clickArea.classList.remove('bg-green-500', 'active:bg-green-600');
            clickArea.classList.add('bg-blue-600', 'cursor-crosshair', 'active:bg-blue-700');
            
            cpsMessage.textContent = 'Test in progress... Click as fast as you can!';
            // Click count is updated in handleCPSClick
            cpsTimerDisplay.textContent = timeLeft.toFixed(1);

            const startTime = Date.now();
            
            // Use 100ms interval for smoother visual countdown
            timerInterval = setInterval(() => {
                const elapsed = (Date.now() - startTime) / 1000;
                timeLeft = currentDuration - elapsed;
                
                if (timeLeft <= 0) {
                    endCPSTest(true); // Indicate test completion
                } else {
                    cpsTimerDisplay.textContent = timeLeft.toFixed(1);
                }
            }, 100);
        }

        function endCPSTest(completed) {
            clearInterval(timerInterval);
            
            // Only show results if the test was completed successfully
            if (completed) {
                const finalCPS = clicks / currentDuration;
                
                // Set to IDLE state for restarting
                cpsGameState = 'IDLE'; 
                
                // Hide Test Area, Show Results
                if (cpsTestArea) cpsTestArea.classList.add('hidden');
                if (cpsResultsSummary) cpsResultsSummary.classList.remove('hidden');

                // Update Results Summary UI
                if (finalCPSScore) finalCPSScore.textContent = finalCPS.toFixed(2);
                if (finalTotalClicks) finalTotalClicks.textContent = clicks;
                if (finalDurationDisplay) finalDurationDisplay.textContent = currentDuration;

            } else {
                // If ending prematurely, just reset to IDLE state
                 cpsGameState = 'IDLE';
                 resetCPSTester();
            }
        }

        function handleCPSClick(event) {
            // Prevent default behavior (like text selection or scrolling on touch)
            event.preventDefault();
            
            if (cpsGameState === 'IDLE') {
                // If idle, the first click starts the test
                startCPSTest();
                clicks++; // Count the starting click
                if (cpsClickCountDisplay) cpsClickCountDisplay.textContent = clicks;

            } else if (cpsGameState === 'PLAYING') {
                // If playing, count the click
                clicks++;
                if (cpsClickCountDisplay) cpsClickCountDisplay.textContent = clicks;
            }
        }
        
        // --- Prevent text selection during rapid clicking (still useful for mouse clicks) ---
        document.addEventListener('mousedown', (e) => {
            if (e.target.id === 'click-area' && cpsGameState === 'PLAYING') {
                e.preventDefault();
            }
        });


        // Initialize the view to show the menu
        showPage('menu');
    </script>

</body>
</html>
