from fastapi import APIRouter, Depends, HTTPException
from apps.db.models import StudentsIn, Students, Complaints, ComplaintsIn
router = APIRouter()


@router.post("/students/attendance")
async def get_students(payload: StudentsIn):

    print(payload)
    se = await Students.create(**payload.model_dump(exclude_unset=True))
    
    return {
        "message": 'success'
    }


@router.post("/complaints")
async def register_complaint(payload: ComplaintsIn):
    se = await Complaints.create(**payload.model_dump(exclude_unset=True))

    return {
        "message": 'success'
    }
