from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Cell(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, index=True)
    sector = relationship(
        'Sector', primaryjoin='Cell.sector_id == Sector.id')
    sector_id = Column(Integer, ForeignKey('sector.id'))
