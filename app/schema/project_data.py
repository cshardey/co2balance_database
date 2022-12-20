from __future__ import annotations

from datetime import datetime
from typing import List
from typing import Optional

from pydantic import BaseModel


class ProjectData(BaseModel):
    id: int
    start_date: datetime
    end_date: datetime
    house_number: str | None
    created_date: datetime
    surveyor: str | None
    current_weather: str
    comments: str | None
    meals_pp: int
    enumerator: str | None
    total_people: int
    weight_of_wood_pile: float
    gps_longitude: float
    gps_latitude: float
    gps_altitude: float
    head_of_household: str | None
    improved_wood_stove: int
    improved_charcoal_stove: int
    number_of_stoves: int
    stove_type: str
    confirm_all_fuels: str
    consent_to_survey: str


class ProjectDataResponses(BaseModel):
    village: str
    project_data: list[ProjectData]
