# backend/app/crud.py
from sqlalchemy.orm import Session
from . import models, schemas

def create_person(db: Session, person: schemas.PersonCreate):
    db_person = models.Person(**person.dict())
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person
