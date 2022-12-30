import os
import unittest

import pandas as pd
from sqlalchemy import inspect

from app import db
from app.db.base_class import Base
from app.populate.cook_stove import clean_project_file


class TestPipeline(unittest.TestCase):
    def test_db_init(self):
        """
        Test that the database is initialised
        :return:
        """
        db.session.init_db()
        inspector = inspect(db.session.engine)
        tables = inspector.get_table_names()
        self.assertEqual(len(tables), len(Base.metadata.tables))

    def test_extract_project_data(self):
        """
        Test that the data extraction in pipeline works
        """
        current_working_dir = os.getcwd()
        clean_project_file.extract_project_data(file_path=f"{current_working_dir}/data_test_co2balance.xlsx",
                                                sheet_names=["Sheet1"])
        path = f"{current_working_dir}/project_data.xlsx"
        self.assertTrue(os.path.exists(path))

    def test_header_cleaning(self):
        """
        Test that the data cleaning  for the header in pipeline works
        """
        ds = clean_project_file.clean_project_file(file_path=f"{os.getcwd()}/data_test_co2balance.xlsx",
                                                   sheet_names=["Sheet1"])
        data = pd.read_excel(ds, sheet_name="Sheet1")

        # Get all headers name and check if they are lower case
        headers = data.columns
        self.assertTrue(all([header.islower() for header in headers]))

    def test_name_cleaning(self):
        """
        Test that the data cleaning  for the name in pipeline works
        """
        ds = clean_project_file.clean_project_file(file_path=f"{os.getcwd()}/data_test_co2balance.xlsx",
                                                   sheet_names=["Sheet1"])
        data = pd.read_excel(ds, sheet_name="Sheet1")
        # Get enumerator column and check if they are sentence case
        enumerator = data["enumerator"]
        region = data["region"]
        surveyor = data["surveyor"]
        # Check if enumerator, region and surveyor are sentence case
        self.assertTrue(all([name.istitle() for name in enumerator]))
        self.assertTrue(all([name.istitle() for name in region]))
        self.assertTrue(all([name.istitle() for name in surveyor]))


if __name__ == '__main__':
    unittest.main()
