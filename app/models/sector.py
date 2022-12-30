from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Sector(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), unique=True, index=True)
    district = relationship(
        'District', primaryjoin='Sector.district_id == District.id')
    district_id = Column(Integer, ForeignKey('district.id'))
