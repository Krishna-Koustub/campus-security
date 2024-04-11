from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = FastAPI()

# Database configuration
SQLALCHEMY_DATABASE_URL = "sqlite:///./complaints.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Complaint(Base):
    __tablename__ = "complaints"

    id = Column(Integer, primary_key=True, index=True)
    complaint_title = Column(String, index=True)
    complaint_message = Column(String)
    complaint_category = Column(String)
    full_name = Column(String)
    email = Column(String)
    phone_number = Column(String)
    evidence_filename = Column(String)

Base.metadata.create_all(bind=engine)

@app.post("/submit_complaint")
async def submit_complaint(complaintTitle: str = Form(...),
                           complaintMessage: str = Form(...),
                           complaintCategory: str = Form(...),
                           fullName: str = Form(...),
                           email: str = Form(...),
                           phoneNumber: str = Form(...),
                           evidence: UploadFile = File(None)):
    # Save the complaint data to the database
    db = SessionLocal()
    db_complaint = Complaint(complaint_title=complaintTitle,
                             complaint_message=complaintMessage,
                             complaint_category=complaintCategory,
                             full_name=fullName,
                             email=email,
                             phone_number=phoneNumber,
                             evidence_filename=evidence.filename if evidence else None)
    db.add(db_complaint)
    db.commit()
    db.refresh(db_complaint)
    db.close()

    # Return a JSON response indicating success
    return JSONResponse(content={"message": "Complaint submitted successfully"})
