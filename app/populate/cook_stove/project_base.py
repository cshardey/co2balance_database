from __future__ import annotations

import logging

import clean_project_file
import pandas as pd
from sqlalchemy import exc

import app.db.session
from app.db.session import engine

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')


class ProjectBase:
    def __init__(self, main_data):
        self.main_data = main_data

    # Read main excel data from CO2Balance
    # TODO: Data will be picked up from an ftpserver

    def create_enumerator(self):
        """
        Create an enumerator for the main data
        :return: enumerator
        """
        # Filter main data to only include the columns we need
        enumerator_data = self.main_data[['enumerator']]
        # check for duplicates and remove them
        enumerator_data = enumerator_data.drop_duplicates()

        # Convert the name  to a word case
        enumerator_data['enumerator'] = enumerator_data['enumerator'].str.title()
        # Rename the column enumerator to name
        enumerator_data = enumerator_data.rename(columns={'enumerator': 'name'})

        # Insert enumerator data into the database using pandas
        enumerator_data.to_sql(
            'enumerator',
            con=engine,
            if_exists='append',
            index=False,
            chunksize=10000,
        )

        logging.info('enumerator data inserted into database')

        self.insert_logger(len(enumerator_data), 'enumerator')

        return enumerate(self.main_data.iterrows())

    def insert_logger(self, length, tablename):
        # Log INFO of the number of rows inserted
        logging.info('{} {} data inserted into database' ''.format(length, tablename))

    def create_region(self):
        """
        Create region for the main data
        :return: enumerator
        """
        # Filter main data to only include the columns we need
        region_data = self.main_data[['region']]
        # check for duplicates and remove them
        region_data = region_data.drop_duplicates()
        # Rename the column enumerator to name
        region_data = region_data.rename(
            columns={'region': 'name'},
        )

        # Convert the name  to a word case
        region_data['name'] = region_data['name'].str.title()

        # Insert enumerator data into the database using pandas
        region_data.to_sql(
            'region',
            con=engine,
            if_exists='append',
            index=False,
            chunksize=10000,
        )

        logging.info('Region data inserted into database')

        self.insert_logger(len(region_data), 'region')

    def create_village(self):
        """
        Create a village for the main data
        :return: enumerator
        """
        # Filter main data to only include the columns we need
        village_data = self.main_data[['village', 'district', 'sector', 'region']]
        # check for duplicates and remove them
        village_data = village_data.drop_duplicates()

        # Check the region table for the region id
        village_data['region_id'] = village_data['region'].apply(
            lambda x: engine.execute(
                f"""
                SELECT id FROM region WHERE name = '{x}'
                """,
            ).fetchone()[0],
        )

        # Rename the column enumerator to name
        village_data = village_data.rename(
            columns={'village': 'name'},
        )
        # DROP the region column
        village_data = village_data.drop(columns=['region'])

        # Replace empty named villages with 'Unknown'
        village_data['name'] = village_data['name'].fillna('Unknown')

        #

        # Insert enumerator data into the database using pandas
        village_data.to_sql(
            'village',
            con=engine,
            if_exists='append',
            index=False,
            chunksize=10000,
        )

        logging.info('Village data inserted into database')

        self.insert_logger(len(village_data), 'village')

        return enumerate(self.main_data.iterrows())

    def insert_country(self):
        """
        Insert country data into the database
        :return: None
        """
        # Read country data from county.json into list
        country_data = pd.read_json('../../app/data/country.json')
        # Create a new column called code and set it to the  first header
        # Insert country data into the database using pandas
        country_data.to_sql(
            'country',
            con=engine,
            if_exists='append',
            index=False,
            chunksize=10000,
        )
        print('Country data inserted into database')

    def create_fuel_type(self):
        """
        Create fuel type for the main data
        :return: enumerator
        """
        # Filter main data to only include the columns we need
        fuel_type_data = self.main_data[
            ['fuel_type']
        ]
        # check for duplicates and remove them
        fuel_type_data = fuel_type_data.drop_duplicates()
        # Rename the column Select all fuels used for cooking by the household: to name
        fuel_type_data = fuel_type_data.rename(
            columns={'fuel_type': 'name'},
        )

        # Convert the name  to a word case
        fuel_type_data['name'] = fuel_type_data['name'].str.title()
        # Rename the column enumerator to name

        # Insert enumerator data into the database using pandas
        fuel_type_data.to_sql(
            'fuel_type',
            con=engine,
            if_exists='append',
            index=False,
            chunksize=10000,
        )

        logging.info('Fuel type data inserted into database')

        self.insert_logger(len(fuel_type_data), 'fuel_type')

        return enumerate(self.main_data.iterrows())

    def insert_project_surveyor(self):
        """
        Insert project data into the database
        :return: None
        """
        # Filter main data to only include the columns we need
        surveyor_data = self.main_data[
            [
                'surveyor',
                'surveyor_phone_number',
                'village',
            ]
        ]
        # check for duplicates and remove them
        surveyor_data = surveyor_data.drop_duplicates()
        # Remove duplicates
        surveyor_data = surveyor_data.drop_duplicates()
        # Rename the column enumerator to name
        surveyor_data = surveyor_data.rename(
            columns={
                'surveyor': 'name',
                'surveyor_phone_number': 'phone_number',
            },
        )
        surveyor_data['name'] = surveyor_data['name'].str.title()

        # Replace nan values in village with 'Unknown'
        surveyor_data['village'] = surveyor_data['village'].fillna('Unknown')
        # Get village id
        surveyor_data['village_id'] = surveyor_data['village'].apply(
            lambda x: engine.execute(
                f"SELECT id FROM village WHERE name = '{x}'",
            ).fetchone()[0],
        )

        # drop village column
        surveyor_data = surveyor_data.drop(columns=['village'])
        # Insert data into the database using pandas
        surveyor_data.to_sql(
            'surveyor',
            con=engine,
            if_exists='append',
            index=False,
            chunksize=10000,
        )

    def create_project(self):
        """
        Project scaffold from project_data.json
        :return: None
        """
        # Read project data from project_data.json
        project_data = pd.read_json('../../app/data/project_data.json')
        # Connect to country table and get the id of the country
        project_data['country_id'] = project_data['country'].apply(
            lambda x: engine.execute(
                f"""
                SELECT id FROM country WHERE name = '{x}'
                """,
            ).fetchone()[0],
        )
        # Drop the country column
        project_data = project_data.drop(columns=['country'])
        # Insert project data into the database using pandas
        project_data.to_sql(
            'project',
            con=engine,
            if_exists='append',
            index=False,
            chunksize=10000,
        )
        print('Project data inserted into database')

    def populate_base_data(self):
        """
        Populate base data into the database
        :return: None
    """
        try:
            # Insert country data into the database
            self.insert_country()
            # Insert project data into the database
            self.create_project()
            # Insert enumerator data into the database
            self.create_enumerator()
            # Insert region data into the database
            self.create_region()
            # Insert village data into the database
            self.create_village()
            # Insert fuel type data into the database
            self.create_fuel_type()
            # Insert project surveyor data into the database
            self.insert_project_surveyor()
        except exc.SQLAlchemyError as e:
            logging.error(e)
            raise e


cook_stove_data = clean_project_file.clean_project_file(
    file_path='../../app/data/co2balance.xlsx', sheet_names=['Day 1 Cleaned'],
)
kenya_cooked_stove_project = ProjectBase(cook_stove_data)
kenya_cooked_stove_project.populate_base_data()
