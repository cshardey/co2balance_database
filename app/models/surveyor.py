from __future__ import annotations

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.sql import func

from app.db.base_class import Base


class Surveyor(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(256), nullable=False)
    phone_number = Column(String(256), nullable=True)
    address = Column(Text)
    village_id = Column(Integer, ForeignKey('village.id'))
    created_date = Column(DateTime(timezone=True), server_default=func.now())
