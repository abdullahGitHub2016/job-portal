<template>
  <div class="bg-[#F2F2F2] min-h-screen pb-10">
    <div class="bg-white border-b py-6 shadow-sm">
      <div class="max-w-[1140px] mx-auto px-4">
        <div class="flex flex-col md:flex-row gap-4 items-center">
          <input 
            v-model="searchQuery" 
            type="text" 
            placeholder="Enter Job Title or Company Name" 
            class="flex-1 border border-gray-300 p-3 rounded text-sm focus:ring-1 focus:ring-blue-500 outline-none"
          />
          <button class="bg-[#0072BC] text-white px-10 py-3 rounded font-bold hover:bg-blue-800 transition shadow-md">
            SEARCH JOBS
          </button>
        </div>
      </div>
    </div>

    <div class="max-w-[1140px] mx-auto grid grid-cols-12 gap-6 mt-6 px-4">
      
      <aside class="col-span-12 lg:col-span-3 space-y-4">
        <div class="bg-white border border-[#DDD] p-4 rounded shadow-sm">
          <h3 class="font-bold text-sm text-[#333] mb-2 uppercase border-b pb-2">Support</h3>
          <p class="text-[12px] text-gray-500 leading-tight mb-3">
            Available 9 am to 8 pm (Sat to Thurs).
          </p>
          <div class="text-[#0072BC] font-bold text-lg">09638666444</div>
          <div class="text-[#0072BC] font-bold text-lg">01897627858</div>
        </div>

        <div class="bg-white border border-[#DDD] p-4 rounded shadow-sm">
          <h3 class="font-bold text-sm text-[#333] mb-2 uppercase border-b pb-2">Quick Filter</h3>
          <ul class="text-[13px] space-y-2 text-blue-600">
            <li class="cursor-pointer hover:underline">Government Jobs</li>
            <li class="cursor-pointer hover:underline">Private Company</li>
            <li class="cursor-pointer hover:underline">Part-time Jobs</li>
          </ul>
        </div>
      </aside>

      <main class="col-span-12 lg:col-span-9 space-y-4">
        <div class="bg-[#FFF8E1] border border-[#FFD54F] p-3 flex justify-between items-center text-sm rounded-sm">
          <span class="font-bold text-gray-700">
            {{ filteredJobs.length }} Active Jobs Found
          </span>
          <div class="hidden md:block">Showing Page 1 of 1</div>
        </div>

        <div 
          v-for="job in filteredJobs" 
          :key="job.id" 
          class="bg-white border border-[#DDD] hover:border-[#0072BC] transition-all relative group shadow-sm overflow-hidden"
        >
          <div class="p-5 flex flex-col md:flex-row justify-between gap-4">
            <div class="flex-1">
              <router-link 
                :to="{ name: 'job-detail', params: { id: job.id } }"
                class="text-[#0072BC] text-[18px] font-bold hover:underline leading-tight block mb-1"
              >
                {{ job.title }}
              </router-link>
              
              <div class="text-[#333] font-bold text-[14px]">{{ job.company }}</div>
              <div class="text-[13px] text-gray-500 mt-1 flex items-center">
                <span class="mr-1">📍</span> {{ job.location }}
              </div>

              <div class="mt-3 bg-[#F9FBFC] p-3 rounded border-l-2 border-blue-300">
                <div class="text-[13px] font-bold text-gray-700">{{ job.education_title }}</div>
                <div class="text-[12px] text-gray-600 mt-1 leading-snug truncate md:whitespace-normal">
                  {{ job.education_detail }}
                </div>
              </div>

              <div class="mt-4 flex flex-wrap gap-x-6 text-[13px] text-gray-600 border-t border-dotted pt-2">
                <span><strong>Experience:</strong> {{ job.experience }}</span>
                <span><strong>Salary:</strong> {{ job.salary }}</span>
              </div>
            </div>

            <div class="flex flex-col justify-between items-end md:w-36 border-l-0 md:border-l md:pl-4 border-gray-100">
              <div class="text-right">
                <div class="text-[10px] font-bold text-gray-400 uppercase">Deadline</div>
                <div class="text-[13px] font-bold text-red-600 mt-1">
                  {{ job.deadline }}
                </div>
              </div>
              
              <router-link 
                :to="{ name: 'job-detail', params: { id: job.id } }"
                class="bg-[#28A745] text-white px-5 py-2 rounded text-[13px] font-bold mt-4 hover:bg-[#218838] transition w-full text-center"
              >
                View Details
              </router-link>
            </div>
          </div>
          <div class="h-[3px] w-0 group-hover:w-full bg-[#0072BC] transition-all duration-500 absolute bottom-0 left-0"></div>
        </div>

        <div v-if="filteredJobs.length > 0" class="flex justify-center mt-8 space-x-2 pb-10">
          <button class="px-4 py-2 bg-white border border-gray-300 rounded text-sm hover:bg-gray-50">1</button>
          <button class="px-4 py-2 bg-white border border-gray-300 rounded text-sm hover:bg-gray-50">Next</button>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';

const jobs = ref([]);
const searchQuery = ref('');

// Fetch all jobs from the FastAPI backend
const fetchJobs = async () => {
  try {
    const response = await fetch('http://127.0.0.1:8000/api/jobs');
    if (!response.ok) throw new Error('Network error');
    jobs.value = await response.json();
  } catch (error) {
    console.error("Backend connection failed. Is main.py running?");
  }
};

// Search filter logic
const filteredJobs = computed(() => {
  if (!searchQuery.value) return jobs.value;
  const query = searchQuery.value.toLowerCase();
  return jobs.value.filter(j => 
    j.title.toLowerCase().includes(query) || 
    j.company.toLowerCase().includes(query)
  );
});

onMounted(fetchJobs);
</script>