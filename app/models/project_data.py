from __future__ import annotations

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.sql import func

from app.db.base_class import Base


class ProjectData(Base):
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey('project.id'))
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime)
    house_number = Column(Integer, nullable=False)
    surveyor_id = Column(Integer, ForeignKey('surveyor.id'))
    created_date = Column(DateTime(timezone=True), server_default=func.now())
    current_weather = Column(String(256), nullable=False)
    country_id = Column(Integer, ForeignKey('country.id'))
    comments = Column(Text)
