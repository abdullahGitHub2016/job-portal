<template>
  <div class="flex flex-col min-h-screen">
    <header class="bg-white border-b p-4">
      <div class="max-w-6xl mx-auto flex justify-between items-center">
        <router-link to="/" class="flex items-center space-x-1">
          <span class="text-blue-600 font-black text-2xl italic">My</span>
          <span class="text-blue-600 font-bold text-2xl">Jobs</span>
        </router-link>
        <nav class="space-x-4 text-sm font-bold text-blue-600">
          <router-link to="/">JOBS</router-link>
          <a href="#">CONTACT</a>
        </nav>
      </div>
    </header>

    <main class="grow">
      <RouterView />
    </main>

    <footer class="bg-[#2F3133] text-white p-10 mt-10">
      <div class="max-w-6xl mx-auto text-center text-gray-400 text-xs">
        © 2026 MyJobs Project - All Rights Reserved
      </div>
    </footer>
  </div>
</template>