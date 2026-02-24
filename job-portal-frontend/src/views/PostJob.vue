<template>
  <div class="max-w-5xl mx-auto p-8 bg-white shadow-xl rounded-xl my-10 border border-gray-100">
    <h2 class="text-3xl font-extrabold mb-8 text-blue-900 border-b pb-4">Post a Professional Job</h2>
    
    <form @submit.prevent="submitJob" class="space-y-8">
      
      <div class="bg-blue-50 p-6 rounded-lg border border-blue-100">
        <h3 class="text-lg font-bold text-blue-800 mb-4 flex items-center">
          <span class="bg-blue-600 text-white w-6 h-6 rounded-full flex items-center justify-center text-xs mr-2">1</span>
          Company & Basic Info
        </h3>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <input v-model="job.title" placeholder="Job Title *" class="w-full border border-gray-300 p-3 rounded-md focus:ring-2 focus:ring-blue-500 outline-none" required />
          <input v-model="job.company" placeholder="Company Name *" class="w-full border border-gray-300 p-3 rounded-md focus:ring-2 focus:ring-blue-500 outline-none" required />
          <input v-model="job.location" placeholder="Location (e.g. Dhaka)" class="w-full border border-gray-300 p-3 rounded-md focus:ring-2 focus:ring-blue-500 outline-none" />
          <input v-model="job.salary" placeholder="Salary Range" class="w-full border border-gray-300 p-3 rounded-md focus:ring-2 focus:ring-blue-500 outline-none" />
        </div>
      </div>

      <div class="space-y-6">
        
        <div class="bg-purple-50 p-6 rounded-lg border border-purple-100">
          <h3 class="text-lg font-bold text-purple-800 mb-4">Education Requirements</h3>
          <div v-for="(item, index) in dynamicLists.education" :key="'edu-'+index" class="flex gap-2 mb-2">
            <input v-model="dynamicLists.education[index]" placeholder="e.g. B.Sc in CSE" class="w-full border border-gray-300 p-2 rounded-md focus:ring-2 focus:ring-purple-400 outline-none" />
            <button type="button" @click="removeItem('education', index)" class="text-red-500 px-2 font-bold hover:bg-red-50 rounded">✕</button>
          </div>
          <button type="button" @click="addItem('education')" class="text-purple-700 text-sm font-bold hover:underline">+ Add Education Line</button>
        </div>

        <div class="bg-green-50 p-6 rounded-lg border border-green-100">
          <h3 class="text-lg font-bold text-green-800 mb-4">Key Responsibilities</h3>
          <div v-for="(item, index) in dynamicLists.responsibilities" :key="'res-'+index" class="flex gap-2 mb-2">
            <textarea v-model="dynamicLists.responsibilities[index]" rows="1" placeholder="e.g. Develop and maintain APIs" class="w-full border border-gray-300 p-2 rounded-md focus:ring-2 focus:ring-green-400 outline-none"></textarea>
            <button type="button" @click="removeItem('responsibilities', index)" class="text-red-500 px-2 font-bold hover:bg-red-50 rounded">✕</button>
          </div>
          <button type="button" @click="addItem('responsibilities')" class="text-green-700 text-sm font-bold hover:underline">+ Add Responsibility Line</button>
        </div>

        <div class="bg-orange-50 p-6 rounded-lg border border-orange-100">
          <h3 class="text-lg font-bold text-orange-800 mb-4">Required Skills</h3>
          <div v-for="(item, index) in dynamicLists.skills" :key="'skill-'+index" class="flex gap-2 mb-2">
            <input v-model="dynamicLists.skills[index]" placeholder="e.g. Python" class="w-full border border-gray-300 p-2 rounded-md focus:ring-2 focus:ring-orange-400 outline-none" />
            <button type="button" @click="removeItem('skills', index)" class="text-red-500 px-2 font-bold hover:bg-red-50 rounded">✕</button>
          </div>
          <button type="button" @click="addItem('skills')" class="text-orange-700 text-sm font-bold hover:underline">+ Add Skill Line</button>
        </div>

      </div>

      <div class="bg-gray-50 p-6 rounded-lg border border-gray-200">
        <h3 class="text-lg font-bold text-gray-800 mb-4">Filters & Levels</h3>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <select v-model="job.job_level" class="w-full border border-gray-300 p-3 rounded-md bg-white">
            <option value="Entry Level">Entry Level</option>
            <option value="Mid Level">Mid Level</option>
            <option value="Top Level">Top Level</option>
          </select>
          <select v-model="job.gender" class="w-full border border-gray-300 p-3 rounded-md bg-white">
            <option value="Both">Both Genders</option>
            <option value="Male">Male Only</option>
            <option value="Female">Female Only</option>
          </select>
          <div class="flex flex-col gap-2 justify-center">
            <label class="flex items-center space-x-2 cursor-pointer">
              <input type="checkbox" v-model="job.is_wfh" class="w-4 h-4" />
              <span class="text-sm font-semibold">Work from Home</span>
            </label>
            <label class="flex items-center space-x-2 cursor-pointer">
              <input type="checkbox" v-model="job.is_newspaper_job" class="w-4 h-4" />
              <span class="text-sm font-semibold text-gray-700">Newspaper Job</span>
            </label>
          </div>
        </div>
      </div>

      <div class="flex gap-4 pt-4">
        <button type="button" @click="router.push('/')" class="w-32 py-4 rounded-lg font-bold text-gray-700 bg-gray-200 hover:bg-gray-300 transition">Cancel</button>
        <button type="submit" class="flex-1 py-4 rounded-lg font-bold text-white bg-blue-600 hover:bg-blue-700 transition shadow-lg shadow-blue-200">
          Publish to Database
        </button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

// Handles all dynamic line-by-line inputs
const dynamicLists = reactive({
  education: [""],
  responsibilities: [""],
  skills: [""]
});

const job = ref({
  company: "", title: "", location: "", salary: "",
  deadline: "2026-12-31", experience: "1-3 years",
  published_date: new Date().toLocaleDateString(),
  vacancy: "1", employment_status: "Full-time", workplace: "Office",
  category: "IT", job_level: "Entry Level", gender: "Both",
  is_wfh: false, is_newspaper_job: false, 
  education_requirements: [], responsibilities: [], skills: []
});

// Helper to add a new line to any list
const addItem = (listKey) => {
  dynamicLists[listKey].push("");
};

// Helper to remove a line
const removeItem = (listKey, index) => {
  if (dynamicLists[listKey].length > 1) {
    dynamicLists[listKey].splice(index, 1);
  } else {
    dynamicLists[listKey][0] = ""; 
  }
};

const submitJob = async () => {
  // Clean dynamic lists: Remove empty strings and trim whitespace
  const cleanList = (arr) => arr.map(i => i.trim()).filter(i => i !== "");

  job.value.education_requirements = cleanList(dynamicLists.education);
  job.value.responsibilities = cleanList(dynamicLists.responsibilities);
  job.value.skills = cleanList(dynamicLists.skills);

  try {
    const response = await fetch('http://127.0.0.1:8000/api/jobs', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(job.value)
    });

    if (response.ok) {
      alert("Job posted successfully!");
      router.push('/');
    } else {
      alert("Error saving job. Please check your backend.");
    }
  } catch (err) {
    alert("Backend connection failed.");
  }
};
</script>