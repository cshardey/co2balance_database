from __future__ import annotations

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.db.base_class import Base


class Region(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(256), nullable=False)
