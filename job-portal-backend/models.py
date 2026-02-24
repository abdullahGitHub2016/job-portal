from sqlalchemy import Column, Integer, String, Text, JSON, Boolean
from database import Base
from pydantic import BaseModel
from typing import List, Optional

# ==========================================
# 1. SQLAlchemy Model (MySQL Table Structure)
# ==========================================
class Job(Base):
    __tablename__ = "jobs"
    
    # Fixes SQLAlchemy 2.0 type-hinting issues
    __allow_unmapped__ = True 

    id = Column(Integer, primary_key=True, index=True)
    company = Column(String(255), nullable=False)
    title = Column(String(255), nullable=False)
    logo = Column(String(500))
    deadline = Column(String(100))
    location = Column(String(255))
    salary = Column(String(100))
    experience = Column(String(100))
    published_date = Column(String(100))
    vacancy = Column(String(50))
    employment_status = Column(String(100))
    workplace = Column(String(100))
    
    # JSON types for lists
    education_requirements = Column(JSON)
    additional_requirements = Column(JSON)
    context = Column(Text)
    responsibilities = Column(JSON)
    skills = Column(JSON)
    
    company_address = Column(Text)
    company_website = Column(String(255))
    company_business = Column(Text)

    # --- 10 Advanced Criteria Columns ---
    category = Column(String(100), index=True)
    is_newspaper_job = Column(Boolean, default=False)
    job_level = Column(String(50))
    gender = Column(String(20), default="Both")
    is_wfh = Column(Boolean, default=False)
    is_army_retired = Column(Boolean, default=False)
    is_disability_accessible = Column(Boolean, default=False)


# ==========================================
# 2. Pydantic Schemas (FastAPI Data Validation)
# ==========================================

class JobBase(BaseModel):
    company: str
    title: str
    logo: Optional[str] = None
    deadline: str
    location: str
    salary: str
    experience: str
    published_date: str
    vacancy: str
    employment_status: str
    workplace: str
    education_requirements: List[str]
    additional_requirements: List[str]
    context: str
    responsibilities: List[str]
    skills: List[str]
    company_address: str
    company_website: Optional[str] = None
    company_business: str
    
    # --- CRITICAL FIX: Made these Optional to avoid 500 errors ---
    # We set default values so the frontend doesn't get 'null'
    category: Optional[str] = "General"
    is_newspaper_job: Optional[bool] = False
    job_level: Optional[str] = "Not Specified"
    gender: Optional[str] = "Both"
    is_wfh: Optional[bool] = False
    is_army_retired: Optional[bool] = False
    is_disability_accessible: Optional[bool] = False

class JobCreate(JobBase):
    pass

class JobSchema(JobBase):
    id: int

    class Config:
        # This allows Pydantic to read data from SQLAlchemy objects
        from_attributes = True