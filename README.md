# MyJobs - Full Stack Job Portal

A professional job portal application inspired by clean, data-driven circular designs. This project features a **FastAPI** backend and a **Vue.js 3** frontend, allowing users to browse job listings and view detailed job requirements.

## 🚀 Features
- **Job Listings:** Real-time job feed fetched from a REST API.
- **Dynamic Details Page:** Specific views for every job using Vue Router.
- **Advanced Filtering:** Instant search by job title or company name.
- **Responsive Design:** Fully optimized for Mobile, Tablet, and Desktop using Tailwind CSS.
- **Professional Layout:** Includes a comprehensive footer, support contact info, and "Apply" workflow.

## 🛠️ Tech Stack
- **Frontend:** Vue.js 3 (Composition API), Vite, Vue Router, Tailwind CSS.
- **Backend:** FastAPI (Python), Pydantic, Uvicorn (CORS enabled).
- **Database:** Mock JSON database (Ready for PostgreSQL integration).

---

## 📁 Project Structure
```text
job-portal/
├── job-portal-backend/    # FastAPI Python code
│   ├── main.py            # API endpoints & Data logic
│   └── requirements.txt   # Backend dependencies
└── job-portal-frontend/   # Vue.js code
    ├── src/
    │   ├── views/         # HomeView.vue & JobDetail.vue
    │   ├── router/        # Navigation logic
    │   └── App.vue        # Main application shell
    └── package.json       # Frontend dependencies