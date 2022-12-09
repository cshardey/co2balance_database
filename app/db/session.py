from __future__ import annotations

import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.base_class import Base
from app.models.enumerator import Enumerator
from app.models.village import Village
from app.models.project_data import ProjectData
from app.models.project import Project
from app.models.surveyor import Surveyor
from app.models.country import Country
from app.models.fuel import FuelType
from app.models.photos import Photos
from app.models.project_photos import ProjectPhotos
from app.models.region import Region

load_dotenv()
try:
    engine = create_engine(os.getenv('DATABASE_URL'))
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    print('Database created and tables initialized')
except Exception as e:
    print("Error: Database Initialization failed see error --> ", e)
