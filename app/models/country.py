from __future__ import annotations

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.db.base_class import Base


class Country(Base):
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(2), unique=True, index=True)
    name = Column(String(50), unique=True, index=True)
