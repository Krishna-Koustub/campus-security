from fastapi import FastAPI, Form
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

app = FastAPI()

# Database configuration
SQLALCHEMY_DATABASE_URL = "sqlite:///./attendance.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define the Attendance model
class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    usn = Column(String, index=True)
    name = Column(String)
    branch = Column(String)
    semester = Column(Integer)
    date_time = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(bind=engine)

@app.post("/submit")
async def submit_attendance(usn: str = Form(...), name: str = Form(...), branch: str = Form(...), semester: int = Form(...), dateTime: str = Form(...)):
    # Store the attendance data into the database
    db = SessionLocal()
    db_attendance = Attendance(usn=usn, name=name, branch=branch, semester=semester, date_time=datetime.strptime(dateTime, '%Y-%m-%d %H:%M:%S'))
    db.add(db_attendance)
    db.commit()
    db.refresh(db_attendance)
    db.close()
    
    # Return a response indicating success
    return {"message": "Attendance submitted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
