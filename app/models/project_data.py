from __future__ import annotations

from sqlalchemy import Column, Float
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
    meals_pp = Column(Integer, nullable=False)
    enumerator_id = Column(Integer, ForeignKey('enumerator.id'))
    village_id = Column(Integer, ForeignKey('village.id'))
    fuel_type_id = Column(Integer, ForeignKey('fuel_type.id'))
    total_people = Column(Integer, nullable=False)
    weight_of_wood_pile = Column(Float, nullable=False)
    gps_longitude = Column(String(256), nullable=False)
    gps_latitude = Column(String(256), nullable=False)
    gps_altitude = Column(String(256), nullable=False)
    head_of_household = Column(String(256), nullable=False)
    improved_wood_stove = Column(String(256), nullable=False)
    improved_charcoal_stove = Column(String(256), nullable=False)
    number_of_stoves = Column(Integer, nullable=False)
    stove_type = Column(String(256), nullable=False)
    confirm_all_fuels = Column(String(256), nullable=False)
    consent_to_survey = Column(String(256), nullable=False)
