from pydantic import BaseModel, Field

class Event(BaseModel):
    id: int 
    title: str 
    image: str 
    description: str 
    tags: list[str]
    location: str 
    
    class Config:
        #orm_mode = True
        schema_extra = {
            "example": {
                "title": "FastAPI Workshop launch",
                "image": "Tech Conference 2023",
                "description": "This is a workshop for FastAPI enthusiasts.",
                "tags": ["fastapi", "workshop", "tech"],
                "location": "google meet"
    
            }
        }