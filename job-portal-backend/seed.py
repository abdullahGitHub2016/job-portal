from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models  # This assumes you have the 'Job' model we discussed

def seed_data():
    # 1. Your original data from main.py
    jobs_to_seed = [
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
    },
    {
        "id": 4,
        "company": "Defense Logistics Corp",
        "title": "Security Operations Manager",
        "logo": "https://corporate.bdjobs.com/logos/defense_log.png",
        "deadline": "18 Feb 2026",
        "location": "Dhaka Cantonment",
        "salary": "Negotiable",
        "experience": "15+ years",
        "published_date": "05 Jan 2026",
        "vacancy": "01",
        "employment_status": "Full-time",
        "workplace": "Office",
        "education_requirements": ["Bachelor's degree"],
        "additional_requirements": ["Retired military personnel preferred"],
        "context": "Providing logistics for specialized security firms.",
        "responsibilities": ["Oversee perimeter security", "Staff training"],
        "skills": ["Security Management", "Tactical Planning"],
        "company_address": "Cantonment, Dhaka",
        "company_website": "https://defenselog.com.bd",
        "company_business": "Security Services",
        "category": "Security/Law Enforcement",
        "gender": "Male",
        "job_level": "Top Level",
        "is_wfh": False,
        "is_newspaper_job": False,
        "is_army_retired": True,
        "is_disability_accessible": False
    },
    {
        "id": 5,
        "company": "Blue Ocean Media",
        "title": "Content Writer (Part-Time)",
        "logo": "https://corporate.bdjobs.com/logos/blue_ocean.png",
        "deadline": "25 Feb 2026",
        "location": "Chittagong",
        "salary": "20,000 BDT",
        "experience": "1 to 2 years",
        "published_date": "14 Jan 2026",
        "vacancy": "02",
        "employment_status": "Part-time",
        "workplace": "Work from home",
        "education_requirements": ["B.A in English or Journalism"],
        "additional_requirements": ["Excellent writing skills"],
        "context": "A creative agency focusing on digital marketing.",
        "responsibilities": ["Write blog posts", "Social media copy"],
        "skills": ["Copywriting", "SEO", "Creative Writing"],
        "company_address": "Agrabad, Chittagong",
        "company_website": "https://blueocean.com",
        "company_business": "Advertising & Media",
        "category": "Marketing/Creative",
        "gender": "Both",
        "job_level": "Entry Level",
        "is_wfh": True,
        "is_newspaper_job": False,
        "is_army_retired": False,
        "is_disability_accessible": True
    },
    {
        "id": 6,
        "company": "Apex Healthcare Ltd",
        "title": "Hospital Administrator",
        "logo": "https://corporate.bdjobs.com/logos/apex_health.png",
        "deadline": "10 Mar 2026",
        "location": "Dhanmondi, Dhaka",
        "salary": "60,000 - 75,000 BDT",
        "experience": "5 to 7 years",
        "published_date": "20 Jan 2026",
        "vacancy": "01",
        "employment_status": "Full-time",
        "workplace": "On-site",
        "education_requirements": ["Masters in Health Administration"],
        "additional_requirements": ["Previous hospital experience is a must"],
        "context": "Modern specialized hospital in Dhaka.",
        "responsibilities": ["Manage daily operations", "Patient billing"],
        "skills": ["Management", "Patient Care Coordination"],
        "company_address": "Dhanmondi, Dhaka",
        "company_website": "https://apexhealth.com.bd",
        "company_business": "Medical & Pharmaceuticals",
        "category": "Medical/Pharma",
        "gender": "Both",
        "job_level": "Mid Level",
        "is_wfh": False,
        "is_newspaper_job": True,
        "is_army_retired": False,
        "is_disability_accessible": True
    },
    {
        "id": 7,
        "company": "Standard Bank",
        "title": "Relationship Manager",
        "logo": "https://corporate.bdjobs.com/logos/std_bank.png",
        "deadline": "05 Mar 2026",
        "location": "Motijheel, Dhaka",
        "salary": "70,000 BDT",
        "experience": "4 to 6 years",
        "published_date": "15 Jan 2026",
        "vacancy": "10",
        "employment_status": "Full-time",
        "workplace": "Office",
        "education_requirements": ["MBA from a reputed university"],
        "additional_requirements": ["Good sales track record"],
        "context": "Expanding corporate banking division.",
        "responsibilities": ["Client acquisition", "Portfolio management"],
        "skills": ["Sales", "Finance", "Negotiation"],
        "company_address": "Motijheel C/A, Dhaka",
        "company_website": "https://standardbank.com.bd",
        "company_business": "Banking & Finance",
        "category": "Bank/Fin. Institute",
        "gender": "Both",
        "job_level": "Mid Level",
        "is_wfh": False,
        "is_newspaper_job": False,
        "is_army_retired": False,
        "is_disability_accessible": False
    },
    {
        "id": 8,
        "company": "Sunrise Garments",
        "title": "Quality Control Inspector",
        "logo": "https://corporate.bdjobs.com/logos/sunrise_g.png",
        "deadline": "15 Feb 2026",
        "location": "Gazipur",
        "salary": "35,000 BDT",
        "experience": "3 to 5 years",
        "published_date": "08 Jan 2026",
        "vacancy": "04",
        "employment_status": "Full-time",
        "workplace": "Factory",
        "education_requirements": ["Diploma in Textile Engineering"],
        "additional_requirements": ["Attention to detail"],
        "context": "100% export-oriented garment factory.",
        "responsibilities": ["Inspect fabric quality", "Maintain production standards"],
        "skills": ["Quality Control", "Textile Manufacturing"],
        "company_address": "Konabari, Gazipur",
        "company_website": "https://sunrisegarments.com",
        "company_business": "Garments/Textile",
        "category": "Garments/Textile",
        "gender": "Male",
        "job_level": "Entry Level",
        "is_wfh": False,
        "is_newspaper_job": False,
        "is_army_retired": False,
        "is_disability_accessible": False
    },
    {
        "id": 9,
        "company": "TechVision Solutions Ltd.",
        "title": "Senior Full Stack Developer",
        "logo": "https://corporate.bdjobs.com/logos/techvision_logo.png",
        "deadline": "20 Feb 2026",
        "location": "Gulshan, Dhaka",
        "salary": "80,000 - 120,000 BDT",
        "experience": "5 to 8 years",
        "published_date": "10 Jan 2026",
        "vacancy": "03",
        "employment_status": "Full-time",
        "workplace": "Remote",
        "education_requirements": ["B.Sc in Computer Science"],
        "additional_requirements": ["Strong knowledge of FastAPI and Vue.js"],
        "context": "Leading software firm specializing in Fintech.",
        "responsibilities": ["Develop scalable APIs", "Mentor junior devs"],
        "skills": ["Python", "Vue.js", "MySQL", "AWS"],
        "company_address": "Gulshan 2, Dhaka",
        "company_website": "https://techvision.com",
        "company_business": "Software Development",
        "category": "IT & Telecommunication",
        "gender": "Both",
        "job_level": "Mid Level",
        "is_wfh": True,
        "is_newspaper_job": False,
        "is_army_retired": False,
        "is_disability_accessible": True
    },
    {
        "id": 10,
        "company": "Green Horizon NGO",
        "title": "Field Program Officer",
        "logo": "https://corporate.bdjobs.com/logos/gh_ngo.png",
        "deadline": "01 Mar 2026",
        "location": "Sylhet",
        "salary": "45,000 BDT",
        "experience": "2 to 3 years",
        "published_date": "12 Jan 2026",
        "vacancy": "05",
        "employment_status": "Contractual",
        "workplace": "On-site",
        "education_requirements": ["Bachelor in Social Science"],
        "additional_requirements": ["Experience in rural development preferred"],
        "context": "Focusing on climate change and reforestation.",
        "responsibilities": ["Coordinate field activities", "Report writing"],
        "skills": ["Communication", "Planning", "MS Office"],
        "company_address": "Zindabazar, Sylhet",
        "company_website": "https://greenhorizon.org",
        "company_business": "Non-Profit Organization",
        "category": "NGO/Development",
        "gender": "Female",
        "job_level": "Entry Level",
        "is_wfh": False,
        "is_newspaper_job": True,
        "is_army_retired": False,
        "is_disability_accessible": False
    }
]

    db = SessionLocal()
    try:
        print("Starting Seeding...")
        for job_data in jobs_to_seed:
            # Check if job already exists to avoid duplicates
            existing_job = db.query(models.Job).filter(models.Job.id == job_data["id"]).first()
            if not existing_job:
                # Create the Job object
                new_job = models.Job(**job_data)
                db.add(new_job)
        
        db.commit()
        print("MASHALLAH! Data seeded successfully.")
    except Exception as e:
        print(f"Error during seeding: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_data()