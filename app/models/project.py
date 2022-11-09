from __future__ import annotations

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.sql import func

from app.db.base_class import Base


class Project(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(256), nullable=False)
    description = Column(Text)
    company = Column(String(400), nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime)
    type = Column(String(400), nullable=False)
    created_date = Column(DateTime(timezone=True), server_default=func.now())
    country_id = Column(Integer, ForeignKey('country.id'))
