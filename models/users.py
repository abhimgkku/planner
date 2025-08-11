from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from models.events import Event

class User(BaseModel):
    email: EmailStr
    password: str
    events: Optional[List[Event]]
    
    class Config:
        schema_extra = {
            "example": {
                "email": "abhinav@gmail.com",
                "password": "securepassword123",
                "events": [],
            }
        }
class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "abhinav@gmail.com",
                "password": "securepassword123",
                "events": []
            }
        }