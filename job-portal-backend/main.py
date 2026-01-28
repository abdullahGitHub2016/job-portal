from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Bdjobs Clone API")

# --- 1. CORS Configuration ---
# This allows your Vue frontend (port 5173) to talk to this API (port 8000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- 2. Data Model ---
class Job(BaseModel):
    id: int
    title: str
    company: str
    location: str
    education: Optional[str] = "Na"
    description: Optional[str] = None
    experience: str
    salary: str = "Na"
    deadline: str

# --- 3. Mock Database (Based on your text) ---
jobs_db = [
    {
        "id": 1,
        "title": "Head of Operations, Cozy Cub",
        "company": "Alam Textile & Garments",
        "location": "Dhaka",
        "education": "Bachelor/Honors",
        "description": "Bachelor’s/Master’s degree in Business Administration, Fashion Merchandising, Textile Engineering, or relevant discipline.",
        "experience": "8 to 10 years",
        "salary": "Na",
        "deadline": "15 Feb 2026"
    },
    {
        "id": 2,
        "title": "Senior Officer, Order Development",
        "company": "Ayesha Abed Foundation",
        "location": "Dhaka",
        "education": "Bachelor’s Degree in any discipline (preferably BSc. in Textile)",
        "description": "A Bachelor’s Degree in any discipline (preferably BSc. in Textile) from a reputed university",
        "experience": "Na",
        "salary": "Na",
        "deadline": "07 Feb 2026"
    },
    {
        "id": 3,
        "title": "Sr. Executive/Manager - Marketing",
        "company": "DOM-INNO Developments Ltd.",
        "location": "Dhaka",
        "education": "BBA / MBA in Marketing",
        "description": "Collaboration and Inclusivity. Employee Well-being. Competitive Compensation.",
        "experience": "4 to 8 years",
        "salary": "Na",
        "deadline": "27 Feb 2026"
    },
    {
        "id": 4,
        "title": "Trainee Officer/ Officer - IT",
        "company": "Kazi Farms Group",
        "location": "Jamalpur",
        "education": "Bachelor/Honors",
        "description": "Information Technology management and support.",
        "experience": "1 to 3 years",
        "salary": "Na",
        "deadline": "06 Feb 2026"
    }
]

# --- 4. API Endpoints ---

@app.get("/")
def read_root():
    return {"status": "Online", "message": "Bdjobs Clone API is running"}
    
    
@app.get("/api/jobs/{job_id}", response_model=Job)
async def get_job_details(job_id: int):
    # Find the job with the matching ID
    job = next((item for item in jobs_db if item["id"] == job_id), None)
    if job:
        return job
    return {"error": "Job not found"}
    

@app.get("/api/jobs", response_model=List[Job])
async def get_jobs():
    """Returns all jobs currently in the mock database."""
    return jobs_db

@app.get("/api/jobs/search")
async def search_jobs(keyword: str = ""):
    """Filter jobs by title or company name."""
    if not keyword:
        return jobs_db
    
    filtered = [
        job for job in jobs_db 
        if keyword.lower() in job["title"].lower() or keyword.lower() in job["company"].lower()
    ]
    return filtered

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)