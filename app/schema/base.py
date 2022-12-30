# Path: app/schema/country.py
from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic import Field


class Country(BaseModel):
    id: int
    code: str
    name: str


class Enumerator(BaseModel):
    id: int
    name: str


class FuelType(BaseModel):
    id: int
    name: str


class Photos(BaseModel):
    photo_id: int
    photo_url: str
    type: str


class Region(BaseModel):
    id: int
    name: str


class Village(BaseModel):
    id: int
    name: str
    district: str
    sector: str
    region_id: Optional[int] = Field(None, foreign_key='region.id')


class Surveyor(BaseModel):
    id: int
    name: str
    phone_number: str
    village_id: Optional[int] = Field(None, foreign_key='village.id')
    address: str


class Project(BaseModel):
    id: int
    name: str
    description: str
    start_date: datetime
    end_date: datetime
    country_id: int
    type: str
    country_id: Optional[int] = Field(None, foreign_key='country.id')


class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str


class TokenPayload(BaseModel):
    sub: str = None
    exp: int = None
