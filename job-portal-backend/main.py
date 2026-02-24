from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Query 
from sqlalchemy.orm import Session
from typing import List, Optional


# Import our database configuration
from database import engine, Base, get_db
import models  # We will create this file next

# Create the tables in MySQL if they don't exist
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Routes ---

@app.get("/api/jobs", response_model=List[models.JobSchema])
def get_jobs(db: Session = Depends(get_db)):
    # Fetch all jobs from MySQL
    jobs = db.query(models.Job).all()
    return jobs

@app.get("/api/jobs/{job_id}", response_model=models.JobSchema)
def get_job(job_id: int, db: Session = Depends(get_db)):
    # Find job by ID in MySQL
    job = db.query(models.Job).filter(models.Job.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job

@app.get("/api/search")
def search_jobs(
    q: Optional[str] = None,
    category: Optional[str] = None,
    location: Optional[str] = None,
    job_type: Optional[str] = None,
    job_level: Optional[str] = None,
    gender: Optional[str] = None,
    wfh: Optional[bool] = None,
    newspaper: Optional[bool] = None,
    army: Optional[bool] = None,
    disability: Optional[bool] = None,
    db: Session = Depends(get_db)
):
    query = db.query(models.Job)

    # Text Search (Title or Company)
    if q:
        query = query.filter(models.Job.title.contains(q) | models.Job.company.contains(q))
    
    # Exact Match Filters
    if category:
        query = query.filter(models.Job.category == category)
    if location:
        query = query.filter(models.Job.location.ilike(f"%{location}%"))
    if job_type:
        query = query.filter(models.Job.employment_status == job_type)
    if job_level:
        query = query.filter(models.Job.job_level == job_level)
    
    # Gender Logic (Show the specific gender + jobs marked as 'Both')
    if gender:
        query = query.filter(models.Job.gender == gender)
    
    # Boolean Filters
    if wfh is not None:
        query = query.filter(models.Job.is_wfh == wfh)
    if army:
        query = query.filter(models.Job.is_army_retired == True)
    if disability:
        query = query.filter(models.Job.is_disability_accessible == True)
    if newspaper:
        query = query.filter(models.Job.is_newspaper_job == True)

    return query.all()

@app.post("/api/jobs", response_model=models.JobSchema)
def create_job(job_data: models.JobCreate, db: Session = Depends(get_db)):
    # 1. Convert the Pydantic model to a dictionary
    new_job_dict = job_data.dict()
    
    # 2. Create the SQLAlchemy model instance
    db_job = models.Job(**new_job_dict)
    
    # 3. Add to database and commit
    db.add(db_job)
    db.commit()
    db.refresh(db_job) # This gets the auto-generated ID back
    
    return db_job
