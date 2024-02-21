# backend/app/schemas.py
from pydantic import BaseModel

class PersonCreate(BaseModel):
    first_name: str
    father_id: int = None
    teip_id: int
    description: str = None
    nek_name: str = None
    gar_name: str = None
