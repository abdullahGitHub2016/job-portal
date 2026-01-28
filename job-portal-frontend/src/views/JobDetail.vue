<template>
  <div class="bg-[#F4F7F9] min-h-screen pb-20">
    <div class="bg-white border-b mb-6">
      <div class="max-w-[1140px] mx-auto px-4 py-3 text-[13px] text-gray-500">
        <router-link to="/" class="hover:text-blue-600">Home</router-link> 
        <span class="mx-2">/</span> 
        <span class="text-gray-400">Job Details</span>
      </div>
    </div>

    <div v-if="loading" class="text-center py-20">
      <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-700 mx-auto"></div>
    </div>

    <div v-else-if="job" class="max-w-[1140px] mx-auto px-4 grid grid-cols-12 gap-6">
      
      <div class="col-span-12 lg:col-span-8 space-y-6">
        
        <div class="bg-white border border-[#DDD] p-8 rounded-sm shadow-sm">
          <h1 class="text-2xl font-bold text-blue-700 leading-tight">{{ job.title }}</h1>
          <h2 class="text-xl font-bold text-gray-800 mt-2">{{ job.company }}</h2>
          <div class="mt-4 flex flex-wrap gap-4 text-sm text-gray-600">
            <span class="flex items-center">📍 {{ job.location }}</span>
            <span class="flex items-center font-bold text-red-600">📅 Deadline: {{ job.deadline }}</span>
          </div>
        </div>

        <div class="bg-white border border-[#DDD] p-8 rounded-sm shadow-sm">
          <h3 class="font-bold text-lg text-gray-800 border-b pb-3 mb-5 uppercase tracking-wide">Job Summary</h3>
          
          <div class="space-y-6">
            <div>
              <h4 class="font-bold text-[#0072BC] mb-2 flex items-center">
                <span class="mr-2 italic font-serif">i</span> Educational Requirements
              </h4>
              <p class="font-bold text-gray-800 text-[15px]">{{ job.education_title }}</p>
              <p class="text-gray-600 mt-1 text-[14px] leading-relaxed">{{ job.education_detail }}</p>
            </div>

            <div>
              <h4 class="font-bold text-[#0072BC] mb-2">Experience Requirements</h4>
              <ul class="list-disc ml-5 text-[14px] text-gray-600">
                <li>{{ job.experience }}</li>
                <li>Professional knowledge in the relevant industry is preferred.</li>
              </ul>
            </div>

            <div>
              <h4 class="font-bold text-[#0072BC] mb-2">Additional Requirements</h4>
              <p class="text-[14px] text-gray-600 leading-relaxed">
                {{ job.description || 'Candidates must have good communication skills and a positive attitude towards team collaboration.' }}
              </p>
            </div>
          </div>
        </div>
      </div>

      <aside class="col-span-12 lg:col-span-4 space-y-6">
        <div class="bg-[#FFF8E1] border border-[#FFD54F] p-6 rounded-sm text-center">
          <p class="text-sm font-bold text-gray-700 mb-4">Are you the right person for this job?</p>
          <button class="w-full bg-[#28A745] hover:bg-[#218838] text-white py-3 rounded font-black text-lg shadow-md transition transform hover:scale-105">
            APPLY ONLINE
          </button>
          <p class="text-[11px] text-gray-500 mt-3 italic">Deadline: {{ job.deadline }}</p>
        </div>

        <div class="bg-white border border-[#DDD] p-6 rounded-sm shadow-sm">
          <h3 class="font-bold text-gray-800 border-b pb-2 mb-4">Job Highlights</h3>
          <div class="space-y-3 text-sm">
            <div class="flex justify-between">
              <span class="text-gray-500">Salary:</span>
              <span class="font-bold">{{ job.salary }}</span>
            </div>
            <div class="flex justify-between">
              <span class="text-gray-500">Location:</span>
              <span class="font-bold">{{ job.location }}</span>
            </div>
            <div class="flex justify-between">
              <span class="text-gray-500">Experience:</span>
              <span class="font-bold">{{ job.experience }}</span>
            </div>
          </div>
        </div>
      </aside>

    </div>

    <div v-else class="text-center py-20">
      <h2 class="text-2xl text-red-600 font-bold">Job Not Found</h2>
      <router-link to="/" class="text-blue-600 underline mt-4 inline-block">Back to Job List</router-link>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();
const job = ref(null);
const loading = ref(true);

const fetchJobDetail = async () => {
  const jobId = route.params.id; // Gets the ID from the URL (e.g. /job/1)
  try {
    const response = await fetch(`http://127.0.0.1:8000/api/jobs/${jobId}`);
    if (response.ok) {
      job.value = await response.json();
    }
  } catch (error) {
    console.error("Error fetching job details:", error);
  } finally {
    loading.value = false;
  }
};

onMounted(fetchJobDetail);
</script>

<style scoped>
/* Specific fonts to match the data-heavy job circular look */
h1, h2, h3 {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
</style>