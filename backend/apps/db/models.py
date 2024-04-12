from pydantic import BaseModel
from datetime import datetime
from tortoise.models import Model
from tortoise import fields


class User(Model):
    id: int
    username: str
    password: str
    email: str
    role: str
    first_name: str
    last_name: str
    phone: str
    address: str
    is_active: bool
    is_superuser: bool
    created_at: datetime
    updated_at: datetime


class StudentsIn(BaseModel):
    usn: str
    name: str
    branch: str
    semester: int


class Students(Model):
    usn: str = fields.CharField(max_length=20, null=False)
    name = fields.CharField(max_length=50, null=False)
    branch = fields.CharField(max_length=256, null=False)
    semester = fields.IntField(null=False)
    attendence_date = fields.DatetimeField(auto_now_add=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Config:
        from_attributes = True


class Complaints(Model):
    title = fields.CharField(max_length=20, null=False)
    message = fields.TextField(null=False)
    category = fields.CharField(max_length=256, null=False)
    full_name = fields.CharField(max_length=256, null=False)
    email_address = fields.CharField(max_length=256,null=False)
    phone_number=fields.CharField(max_length=20,null=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)


class ComplaintsIn(BaseModel):
    title:str
    message:str
    category :str
    full_name :str
    email_address :str
    phone_number:str