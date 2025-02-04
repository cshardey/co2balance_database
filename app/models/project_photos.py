from __future__ import annotations

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer

from app.db.base_class import Base


class ProjectPhotos(Base):
    photo_id = Column(Integer, ForeignKey('photos.photo_id'),
                      primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey('project.id'), primary_key=True, index=True)
