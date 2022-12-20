from __future__ import annotations

from datetime import datetime
from itertools import groupby

from sqlalchemy.orm import Session

from app.models import country
from app.models import enumerator
from app.models import fuel
from app.models import project
from app.models import project_data
from app.models import surveyor
from app.models import village
from app.schema import base as schemas


class ProjectDataRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_date_range(
        self,
        start_date: datetime,
        end_date: datetime,
        project_name: str,
        comapny_name: str,
    ):
        """
        Get project data by  date range
        :param company_name: str (Company name from authentication)
        :param project_name: str ( Project name )
        :param end_date:
        :param start_date:
        :param project_data: schemas.ProjectData
        :return:
        """
        records = (
            self.db.query(
                project_data.ProjectData,
            )
            .filter(
                project.Project.name == project_name,
                project.Project.company == comapny_name,
                project_data.ProjectData.start_date >= start_date,
                project_data.ProjectData.end_date <= end_date,
            ).all()
        )
        data = []
        for record in records:
            data.append(
                {
                    'id': record.id,
                    'start_date': record.start_date.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
                    'end_date': record.end_date.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
                    'house_number': record.house_number,
                    'surveyor': record.surveyor.name,
                    'created_date': record.created_date.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
                    'current_weather': record.current_weather,
                    'comments': record.comments,
                    'meals_pp': record.meals_pp or 0,
                    'enumerator': record.enumerator.name,
                    'village': record.village.name,
                    'fuel_type': record.fuel_type.name,
                    'total_people': record.total_people or 0,
                    'weight_of_wood_pile': record.weight_of_wood_pile or 0,
                    'gps_longitude': record.gps_longitude,
                    'gps_latitude': record.gps_latitude,
                    'gps_altitude': record.gps_altitude,
                    'head_of_household': record.head_of_household,
                    'improved_wood_stove': record.improved_wood_stove,
                    'improved_charcoal_stove': record.improved_charcoal_stove,
                    'number_of_stoves': record.number_of_stoves,
                    'stove_type': record.stove_type,
                    'confirm_all_fuels': record.confirm_all_fuels,
                    'consent_to_survey': record.consent_to_survey,
                },
            )
        # group the by key village into a list of dict eg [{'village': 'village_name', 'project_data': [data]}]
        grouped_data = [
            {'village': k, 'project_data': list(v)}
            for k, v in groupby(data, key=lambda x: x['village'])
        ]

        return grouped_data

        # Group data by village
