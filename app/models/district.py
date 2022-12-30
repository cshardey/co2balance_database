from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class District(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, index=True)
    region = relationship(
        'Region', primaryjoin='District.region_id == Region.id')
    region_id = Column(Integer, ForeignKey('region.id'))
