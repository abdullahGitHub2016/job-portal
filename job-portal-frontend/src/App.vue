<template>
  <div class="flex flex-col min-h-screen">
    <header class="bg-white border-b sticky top-0 z-50 shadow-sm">
      <div class="max-w-6xl mx-auto px-4 h-16 flex justify-between items-center">
        
        <router-link to="/" class="flex items-center space-x-1">
          <span class="text-blue-600 font-black text-2xl italic">My</span>
          <span class="text-blue-600 font-bold text-2xl">Jobs</span>
        </router-link>

        <nav class="flex items-center space-x-6">
          <router-link to="/" class="text-sm font-bold text-gray-600 hover:text-blue-600 transition">
            JOBS
          </router-link>
          <a href="#" class="text-sm font-bold text-gray-600 hover:text-blue-600 transition">
            CONTACT
          </a>
          
          <router-link 
            to="/post-job" 
            class="bg-green-600 hover:bg-green-700 text-white px-4 py-2 rounded-md font-bold text-sm transition shadow-md"
          >
            + POST A JOB
          </router-link>
        </nav>
      </div>
    </header>

    <main class="grow bg-gray-50">
      <RouterView />
    </main>

    <footer class="bg-[#2F3133] text-white p-10">
      <div class="max-w-6xl mx-auto text-center text-gray-400 text-xs">
        © 2026 MyJobs Project - All Rights Reserved
      </div>
    </footer>
  </div>
</template>

<style>
/* Smooth transitions for all hover effects */
a, button {
  transition: all 0.2s ease-in-out;
}
</style>