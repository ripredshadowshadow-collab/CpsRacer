# CpsRacer
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome Racer</title>
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
    </style>
</head>
<body class="bg-gray-100 min-h-screen flex items-center justify-center">

    <div class="w-full max-w-sm">
        <h1 class="text-2xl font-bold text-center text-gray-800 mb-6">Main Menu</h1>
        
        <!-- Navigation Menu -->
        <nav class="bg-white rounded-lg shadow-lg">
            <ul class="flex flex-col">
                <!-- Play Option -->
                <li>
                    <a href="#" 
                       class="flex items-center justify-center w-full px-6 py-4 text-lg font-medium text-gray-700 rounded-t-lg hover:bg-gray-50 transition-colors duration-200">
                        <!-- Simple Play Icon -->
                        <svg class="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 3l14 9-14 9V3z"></path></svg>
                        Play
                    </a>
                </li>
                
                <!-- Separator -->
                <li class="border-t border-gray-200"></li>

                <!-- CPS Tester Option -->
                <li>
                    <a href="#" 
                       class="flex items-center justify-center w-full px-6 py-4 text-lg font-medium text-gray-700 hover:bg-gray-50 transition-colors duration-200">
                        <!-- Mouse Click Icon -->
                        <svg class="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 15l-2 5L9 9l11 4-5 2zm0 0l5 5M7.188 2.239l.777 2.897M5.136 7.965l-2.898-.777M13.95 4.05l-2.122 2.122m-5.657 5.656l-2.12 2.122"></path></svg>
                        CPS Tester
                    </a>
                </li>
                
                <!-- Separator -->
                <li class="border-t border-gray-200"></li>

                <!-- Reaction Tester Option -->
                <li>
                    <a href="#" 
                       class="flex items-center justify-center w-full px-6 py-4 text-lg font-medium text-gray-700 rounded-b-lg hover:bg-gray-50 transition-colors duration-200">
                        <!-- Lightning Bolt Icon -->
                        <svg class="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                        Reaction Tester
                    </a>
                </li>
            </ul>
        </nav>
    </div>

</body>
</html>
