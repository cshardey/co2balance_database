from __future__ import annotations

from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String

from app.db.base_class import Base


class Village(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(256), nullable=False)
    district = Column(String(256), nullable=False)
    sector = Column(String(256), nullable=False)
    region_id = Column(Integer, ForeignKey('region.id'))
