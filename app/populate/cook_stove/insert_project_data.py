from __future__ import annotations

from app.db.session import engine
from app.db.session import logger


class InsertProjectData:
    def __init__(self, main_data):
        self.main_data = main_data

    def insert_project_datas(self):
        """
        Insert Project Data
        :return:district.1
        """
        # Get Enumerator  ID from the database
        self.main_data['enumerator_id'] = self.main_data['enumerator'].apply(
            lambda x: engine.execute(
                f"SELECT id FROM enumerator WHERE name = '{x}'",
            ).fetchone()[0],
        )
        logger.info('DB_OPERATIONS: Enumerator ID fetched from database')

        # Drop the Enumerator column
        self.main_data = self.main_data.drop(columns=['enumerator'])

        # Replace nan village vlaues with 'Unknown'
        self.main_data['village'] = self.main_data['village'].fillna('Unknown')
        # Get village_id from the database
        self.main_data['village_id'] = self.main_data['village'].apply(
            lambda x: engine.execute(
                f"SELECT id FROM village WHERE name = '{x}'",
            ).fetchone()[0],
        )
        # Drop the Village column
        self.main_data = self.main_data.drop(columns=['village'])
        # Get surveyor_id from the database
        self.main_data['surveyor_id'] = self.main_data['surveyor'].apply(
            lambda x: engine.execute(
                f"SELECT id FROM surveyor WHERE name = '{x}'",
            ).fetchone()[0],
        )

        logger.info('DB_OPERATIONS: Surveyor ID fetched from database')
        # Drop the Surveyor column
        self.main_data = self.main_data.drop(columns=['surveyor'])

        # Get Fuel Type ID from the database
        self.main_data['fuel_type_id'] = self.main_data['fuel_type'].apply(
            lambda x: engine.execute(
                f"SELECT id FROM fuel_type WHERE name = '{x}'",
            ).fetchone()[0],
        )
        # Drop the Fuel Type column
        self.main_data = self.main_data.drop(columns=['fuel_type'])

        self.main_data['project_id'] = 1

        # Drop columns that are not needed
        self.main_data = self.main_data.drop(
            columns=[
                'surveyor_phone_number', 'region', 'district', 'district.1', 'sector', 'cell', 'house_number.1',
                'photo_of_traditional_3_stone_fire', 'photo_of_ethanol_alcohol_stove',
            ],
        )

        # Insert data into the database using pandas
        self.main_data.to_sql(
            'project_data',
            con=engine,
            if_exists='append',
            index=False,
            chunksize=10000,
        )
        logger.info('Project Data inserted into database')
