from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Job(BaseModel):
    id: int
    company: str
    title: str
    logo: str
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
    company_website: str
    company_business: str

jobs_db = [
    {
        "id": 1,
        "company": "Alam Textile & Garments",
        "title": "Head of Operations, Cozy Cub",
        "logo": "https://corporate.bdjobs.com/logos/47268_2.png",
        "deadline": "15 Feb 2026",
        "location": "Dhaka (Shyampur)",
        "salary": "Negotiable",
        "experience": "8 to 10 years",
        "published_date": "28 Jan 2026",
        "vacancy": "01",
        "employment_status": "Full Time",
        "workplace": "Work at office",
        "education_requirements": [
            "Bachelor/Honors",
            "Bachelor’s/Master’s degree in Business Administration, Fashion Merchandising, Textile Engineering, or relevant discipline."
        ],
        "additional_requirements": [
            "Minimum 8–10 years of experience in fashion retail operations, baby & kids wear brands (mandatory).",
            "Proven experience in managing end-to-end operations from design to store sales.",
            "Strong leadership, planning, and decision-making skills.",
            "Excellent communication and stakeholder management ability.",
            "Sound knowledge of retail systems and supply chain processes."
        ],
        "context": "Cozy Cub, a growing retail clothing brand specializing in baby & kids wear, is seeking an experienced and dynamic Head of Operations to lead end-to-end operations from product design and development through retail sales and customer experience.",
        "responsibilities": [
            "Lead and oversee all operational functions including design, merchandising, and production.",
            "Ensure smooth execution of product development from concept to store availability.",
            "Drive sales performance and operational efficiency across all retail outlets.",
            "Develop and implement operational strategies and SOPs.",
            "Ensure effective inventory management and stock planning."
        ],
        "skills": ["Apparel merchandising", "CRM", "Fashion Design", "Operation Management", "Sales & Marketing"],
        "company_address": "Plot No #23, Road No #10, Shyampur Industrial Area, Dhaka.",
        "company_website": "https://alamgarments.com/",
        "company_business": "Bangladesh’s leading manufacturer of baby wear, specializing in comfortable and affordable clothing for kids."
    },
    {
        "id": 2,
        "company": "TechVision Solutions Ltd.",
        "title": "Senior Full Stack Developer (Node.js & Vue.js)",
        "logo": "https://via.placeholder.com/150",
        "deadline": "20 Feb 2026",
        "location": "Dhaka (Gulshan)",
        "salary": "80,000 - 1,20,000 (Monthly)",
        "experience": "5 to 7 years",
        "published_date": "27 Jan 2026",
        "vacancy": "03",
        "employment_status": "Full Time",
        "workplace": "Hybrid",
        "education_requirements": [
            "B.Sc in Computer Science & Engineering (CSE) from any reputed university.",
            "Certifications in AWS or Azure will be an added advantage."
        ],
        "additional_requirements": [
            "Expertise in JavaScript (ES6+), Node.js, and Vue.js 3.",
            "Deep understanding of RESTful API design and PostgreSQL.",
            "Experience with Docker, Kubernetes, and CI/CD pipelines.",
            "Ability to lead a team of 4-5 junior developers.",
            "Strong problem-solving skills and algorithmic thinking."
        ],
        "context": "We are a fast-growing Fintech startup building the next generation of digital payment solutions in Bangladesh. We are looking for a tech-heavy leader to scale our infrastructure.",
        "responsibilities": [
            "Design and implement scalable backend services using Node.js.",
            "Develop high-performance frontend components using Vue.js 3.",
            "Optimize database queries and ensure data security protocols.",
            "Collaborate with Product Managers to define feature specifications.",
            "Perform code reviews and mentor junior engineering staff."
        ],
        "skills": ["Node.js", "Vue.js", "PostgreSQL", "Docker", "AWS", "TypeScript"],
        "company_address": "Level 4, House 12, Road 90, Gulshan 2, Dhaka.",
        "company_website": "https://techvision.io",
        "company_business": "A software innovation hub focusing on Fintech and E-commerce automation."
    },
    {
        "id": 3,
        "company": "Global Pharma Group",
        "title": "Manager, Human Resources",
        "logo": "https://via.placeholder.com/150",
        "deadline": "10 Feb 2026",
        "location": "Gazipur",
        "salary": "Negotiable",
        "experience": "10 to 12 years",
        "published_date": "25 Jan 2026",
        "vacancy": "01",
        "employment_status": "Full Time",
        "workplace": "Work at office",
        "education_requirements": [
            "MBA in HRM from a top-tier university.",
            "PGDHRM is highly preferred.",
            "Bachelor degree in any discipline."
        ],
        "additional_requirements": [
            "Extensive experience in Factory HR management and compliance.",
            "Expertise in Bangladesh Labor Law 2006 (Amended 2013).",
            "Proven track record in talent acquisition and performance appraisal.",
            "Excellent negotiation and conflict resolution skills."
        ],
        "context": "As one of the leading pharmaceutical companies, we prioritize our people. We are looking for an HR veteran to manage our Gazipur manufacturing plant's workforce.",
        "responsibilities": [
            "Manage end-to-end recruitment for factory staff and corporate roles.",
            "Ensure 100% compliance with national labor laws and safety standards.",
            "Oversee payroll processing and employee benefit programs.",
            "Conduct training needs analysis and coordinate development programs.",
            "Handle employee grievances and disciplinary actions."
        ],
        "skills": ["HRIS", "Labor Law", "Performance Management", "Payroll Administration", "Compliance"],
        "company_address": "Sreepur, Gazipur, Bangladesh.",
        "company_website": "https://globalpharma.com.bd",
        "company_business": "A leading pharmaceutical manufacturer exporting to over 20 countries."
    }
]

@app.get("/api/jobs", response_model=List[Job])
def get_jobs():
    return jobs_db

@app.get("/api/jobs/{job_id}", response_model=Job)
def get_job(job_id: int):
    job = next((j for j in jobs_db if j["id"] == job_id), None)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job