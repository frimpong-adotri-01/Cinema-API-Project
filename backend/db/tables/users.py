from sqlalchemy import Column,Integer, String,Boolean
from sqlalchemy.orm import relationship

from db.base_class import Base


class User(Base):
    id = Column(Integer,primary_key=True,index=True)
    username = Column(String,unique=True,nullable=False)
    email = Column(String,nullable=False,unique=True,index=True)
    hashed_password = Column(String,nullable=False)
    is_admin = Column(Boolean(),default=False)
    films = relationship("Film",back_populates="owner")
    seances = relationship("Seance",back_populates="owner")