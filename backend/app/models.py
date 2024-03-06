from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.database import Base

class Tukhum(Base):
    __tablename__ = "tukhums"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)

class Teip(Base):
    __tablename__ = "teips"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    tukhum_id = Column(Integer, ForeignKey('tukhums.id'))
    description = Column(String)
    
    tukhum = relationship("Tukhum", back_populates="teips")

class Person(Base):
    __tablename__ = "people"
    
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    father_id = Column(Integer, ForeignKey('people.id'))
    teip_id = Column(Integer, ForeignKey('teips.id'))
    description = Column(String)
    nek_name = Column(String)
    gar_name = Column(String)
    
    father = relationship("Person", remote_side=[id], back_populates="children")
    children = relationship("Person", back_populates="father")
    teip = relationship("Teip", back_populates="members")

# Make sure to also reflect the relationships in the Tukhum and Teip classes
Tukhum.teips = relationship("Teip", order_by=Teip.id, back_populates="tukhum")
Teip.members = relationship("Person", order_by=Person.id, back_populates="teip")
