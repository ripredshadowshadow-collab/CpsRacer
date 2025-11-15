#
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
    </style>
</head>
<body class="bg-gray-100 min-h-screen flex items-center justify-center py-12">

    <div class="w-full max-w-sm mx-auto p-4">
        
        <!-- Main Menu Title -->
        <h1 id="main-title" class="text-3xl font-bold text-center text-gray-800 mb-6 transition-opacity duration-300">Main Menu</h1>
        
        <!-- Navigation Menu (Always visible for main selection) -->
        <nav id="menu-nav" class="bg-white rounded-lg shadow-xl mb-8 transition-opacity duration-300">
            <ul class="flex flex-col">
                <!-- CPS Tester Option (First) -->
                <li>
                    <a href="javascript:void(0)" onclick="showPage('cps-tester')"
                       class="flex items-center justify-center w-full px-6 py-4 text-lg font-medium text-gray-700 rounded-t-lg hover:bg-indigo-50 transition-colors duration-200">
                        <!-- Mouse Click Icon -->
                        <svg class="w-5 h-5 mr-3 text-red-500" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 15l-2 5L9 9l11 4-5 2zm0 0l5 5M7.188 2.239l.777 2.897M5.136 7.965l-2.898-.777M13.95 4.05l-2.122 2.122m-5.657 5.656l-2.12 2.122"></path></svg>
                        CPS Tester
                    </a>
                </li>
                
                <!-- Separator -->
                <li class="border-t border-gray-200"></li>

                <!-- Reaction Tester Option (Second) -->
                <li>
                    <a href="javascript:void(0)" onclick="showPage('reaction-tester')"
                       class="flex items-center justify-center w-full px-6 py-4 text-lg font-medium text-gray-700 hover:bg-indigo-50 transition-colors duration-200">
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
                       class="flex items-center justify-center w-full px-6 py-4 text-lg font-medium text-white bg-indigo-600 rounded-b-lg hover:bg-indigo-700 transition-colors duration-200">
                        <!-- Gamepad Icon -->
                        <svg class="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 20l-1-7-5.5 2.5v1.5L11 20zM13 20l1-7 5.5 2.5v1.5L13 20zM2 10l5.5-2.5L11 10h2l3.5-1.5L22 10V6a2 2 0 00-2-2H4a2 2 0 00-2 2v4z"></path></svg>
                        Play Online
                    </a>
                </li>
            </ul>
        </nav>

        <!-- Dynamic Content Pages -->
        <div id="pages-container" class="mt-8">

            <!-- 1. Play Online Page Content (Updated ID) -->
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

            <!-- 2. CPS Tester Page Content (Same as before) -->
            <div id="cps-tester" class="page bg-white rounded-lg shadow-xl p-6">
                <h2 class="text-2xl font-semibold mb-4 text-gray-700">Click Per Second Tester</h2>
                <p class="text-gray-600 mb-6">
                    This screen would host the functionality for measuring a user's clicking speed over a set time.
                </p>
                <!-- Placeholder for actual CPS logic -->
                <div class="p-8 bg-red-100 border-2 border-red-500 rounded-lg text-center font-mono text-xl mb-6">
                    [CPS Test Interface goes here]
                </div>
                <!-- Back Button -->
                <button onclick="showPage('menu')" class="w-full bg-indigo-500 text-white font-bold py-2 px-4 rounded-lg hover:bg-indigo-600 transition-colors">
                    ← Back to Menu
                </button>
            </div>

            <!-- 3. Reaction Tester Page Content (Same as before) -->
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
        // Initial state is the menu
        let currentPage = 'menu';

        /**
         * Switches the view between the main menu and a content page.
         * @param {string} pageId - The ID of the page to show ('menu', 'play-online', 'cps-tester', 'reaction-tester').
         */
        function showPage(pageId) {
            
            // Get all page elements
            const pages = document.querySelectorAll('.page');
            
            // 1. Hide/Show Menu and Title
            if (pageId === 'menu') {
                menuNav.classList.remove('hidden', 'opacity-0');
                mainTitle.classList.remove('hidden', 'opacity-0');
            } else {
                menuNav.classList.add('hidden', 'opacity-0');
                mainTitle.classList.add('hidden', 'opacity-0');
            }
            
            // 2. Hide all content pages
            pages.forEach(page => {
                page.classList.remove('page-visible');
            });
            
            // 3. Show the requested content page (if not the menu)
            if (pageId !== 'menu') {
                const newPage = document.getElementById(pageId);
                if (newPage) {
                    newPage.classList.add('page-visible');
                }
            }
            
            currentPage = pageId;
        }

        // Initialize the view to show the menu
        showPage('menu');
    </script>

</body>
</html>
