from __future__ import annotations

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String

from app.db.base_class import Base


class Photos(Base):
    photo_id = Column(Integer, primary_key=True, index=True)
    photo_url = Column(String(256), nullable=False)
    type = Column(String(256), nullable=False)
