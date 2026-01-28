<template>
  <div class="bg-[#F4F7F9] min-h-screen pb-12 font-sans">
    <div class="bg-white border-b sticky top-0 z-20">
      <div class="max-w-5xl mx-auto px-4 py-3 text-sm">
        <router-link to="/" class="text-blue-600 hover:underline flex items-center gap-1">
          <span>←</span> Back to Job List
        </router-link>
      </div>
    </div>

    <div v-if="loading" class="flex justify-center items-center py-20">
      <div class="animate-spin rounded-full h-10 w-10 border-t-2 border-b-2 border-blue-600"></div>
    </div>

    <div v-else-if="job" class="max-w-5xl mx-auto px-4 mt-6 grid grid-cols-12 gap-6">
      
      <div class="col-span-12 lg:col-span-8 space-y-6">
        
        <div class="bg-white border rounded shadow-sm p-6">
          <div class="flex flex-col md:flex-row justify-between gap-4">
            <div class="flex-1">
              <h1 class="text-2xl font-bold text-gray-900">{{ job.title }}</h1>
              <p class="text-xl text-blue-700 font-semibold mt-1">{{ job.company }}</p>
              <div class="mt-4 flex flex-wrap gap-4 text-sm text-gray-500">
                <span class="flex items-center gap-1">📍 {{ job.location }}</span>
                <span class="flex items-center gap-1">💼 {{ job.employment_status }}</span>
                <span class="flex items-center gap-1 text-red-600 font-bold">⏰ Deadline: {{ job.deadline }}</span>
              </div>
            </div>
            <div class="w-24 h-24 border rounded flex items-center justify-center p-2 self-start bg-white">
              <img :src="job.logo" class="max-w-full max-h-full object-contain" alt="Company Logo" />
            </div>
          </div>
          
          <div class="mt-6 flex gap-3">
            <button class="bg-green-600 hover:bg-green-700 text-white px-8 py-2.5 rounded font-bold shadow-md transition">
              Apply Online
            </button>
            <button class="border border-blue-600 text-blue-600 hover:bg-blue-50 px-6 py-2.5 rounded font-bold transition">
              Shortlist
            </button>
          </div>
        </div>

        <div class="bg-white border rounded shadow-sm p-6 md:p-8 space-y-8">
          
          <section>
            <h3 class="text-lg font-bold text-gray-800 border-b-2 border-blue-600 inline-block mb-4">Job Context</h3>
            <p class="text-gray-700 leading-relaxed">{{ job.context }}</p>
          </section>

          <section>
            <h3 class="text-lg font-bold text-gray-800 border-b-2 border-blue-600 inline-block mb-4">Responsibilities</h3>
            <ul class="list-disc pl-5 space-y-2 text-gray-700">
              <li v-for="(item, index) in job.responsibilities" :key="index">{{ item }}</li>
            </ul>
          </section>

          <section>
            <h3 class="text-lg font-bold text-gray-800 border-b-2 border-blue-600 inline-block mb-4">Educational Requirements</h3>
            <ul class="list-disc pl-5 space-y-2 text-gray-700 font-semibold">
              <li v-for="(edu, index) in job.education_requirements" :key="index">{{ edu }}</li>
            </ul>
          </section>

          <section>
            <h3 class="text-lg font-bold text-gray-800 border-b-2 border-blue-600 inline-block mb-4">Additional Requirements</h3>
            <ul class="list-disc pl-5 space-y-2 text-gray-700">
              <li v-for="(req, index) in job.additional_requirements" :key="index">{{ req }}</li>
            </ul>
          </section>

          <section>
            <h3 class="text-lg font-bold text-gray-800 border-b-2 border-blue-600 inline-block mb-4">Skills & Expertise</h3>
            <div class="flex flex-wrap gap-2">
              <span v-for="skill in job.skills" :key="skill" 
                class="bg-blue-50 text-blue-700 px-3 py-1 rounded-full text-xs font-bold border border-blue-100">
                {{ skill }}
              </span>
            </div>
          </section>
        </div>
      </div>

      <div class="col-span-12 lg:col-span-4 space-y-6">
        <div class="bg-white border rounded shadow-sm p-5">
          <h3 class="font-bold text-gray-800 mb-4 border-b pb-2">Job Summary</h3>
          <div class="space-y-4 text-sm">
            <div class="flex justify-between">
              <span class="text-gray-500">Published on:</span>
              <span class="font-semibold">{{ job.published_date }}</span>
            </div>
            <div class="flex justify-between">
              <span class="text-gray-500">Vacancy:</span>
              <span class="font-semibold">{{ job.vacancy }}</span>
            </div>
            <div class="flex justify-between">
              <span class="text-gray-500">Employment Status:</span>
              <span class="font-semibold">{{ job.employment_status }}</span>
            </div>
            <div class="flex justify-between">
              <span class="text-gray-500">Experience:</span>
              <span class="font-semibold">{{ job.experience }}</span>
            </div>
            <div class="flex justify-between">
              <span class="text-gray-500">Workplace:</span>
              <span class="font-semibold">{{ job.workplace }}</span>
            </div>
            <div class="flex justify-between">
              <span class="text-gray-500">Salary:</span>
              <span class="font-semibold text-blue-700">{{ job.salary }}</span>
            </div>
          </div>
        </div>

        <div class="bg-blue-900 text-white border rounded shadow-sm p-6">
          <h3 class="font-bold mb-4 border-b border-blue-700 pb-2">Company Information</h3>
          <div class="space-y-4 text-sm">
            <p class="font-bold text-lg">{{ job.company }}</p>
            <p><span class="text-blue-300">Address:</span><br/>{{ job.company_address }}</p>
            <p v-if="job.company_website"><span class="text-blue-300">Web:</span><br/>
              <a :href="job.company_website" target="_blank" class="underline hover:text-blue-200">Visit Website</a>
            </p>
            <div class="bg-blue-800 p-3 rounded text-xs leading-relaxed italic">
              {{ job.company_business }}
            </div>
          </div>
        </div>
      </div>

    </div>

    <div v-else class="text-center py-20 text-gray-500">
      Job listing not found or server error.
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();
const job = ref(null);
const loading = ref(true);

const fetchJobDetails = async () => {
  try {
    const res = await fetch(`http://127.0.0.1:8000/api/jobs/${route.params.id}`);
    if (!res.ok) throw new Error("Failed to fetch");
    job.value = await res.json();
  } catch (error) {
    console.error("Error:", error);
  } finally {
    loading.value = false;
  }
};

onMounted(fetchJobDetails);
</script>