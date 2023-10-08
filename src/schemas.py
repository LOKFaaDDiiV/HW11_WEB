from datetime import date
from typing import List, Optional
from pydantic import BaseModel, Field, EmailStr


class ContactModel(BaseModel):
    name: str = Field(max_length=25)
    lastname: str = Field(max_length=25)
    email: EmailStr
    phone: str = Field(max_length=20)
    birth_date: date


class ContactUpdate(ContactModel):
    name: str = Field(max_length=25)
    lastname: str = Field(max_length=25)
    email: EmailStr
    phone: str = Field(max_length=20)
    birth_date: date


class ContactResponse(ContactModel):
    id: int
    name: str = Field(max_length=25)
    lastname: str = Field(max_length=25)
    email: EmailStr
    phone: str = Field(max_length=20)
    birth_date: date

    class Config:
        from_attributes = True
