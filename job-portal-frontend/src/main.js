import { createApp } from 'vue'
import './style.css' // Ensure your Tailwind CSS is imported here
import App from './App.vue'
import router from './router' // This imports your router configuration

const app = createApp(App)

// Use the router so <router-view> and <router-link> work
app.use(router)

app.mount('#app')