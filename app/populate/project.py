from __future__ import annotations

import logging

import pandas as pd

from app.db.session import engine

# Read main excel data from CO2Balance
# TODO: Data will be picked up from an ftpserver


main_data = pd.read_excel('../../data/co2balance.xlsx', sheet_name='Day 1')


def create_enumerator():
    """
    Create an enumerator for the main data
    :return: enumerator
    """
    # Filter main data to only include the columns we need
    print(main_data.columns)
    enumerator_data = main_data[['Enumerator']]
    # check for duplicates and remove them
    enumerator_data = enumerator_data.drop_duplicates()

    # Convert the name  to a word case
    enumerator_data['Enumerator'] = enumerator_data['Enumerator'].str.title()
    # Rename the column Enumerator to name
    enumerator_data = enumerator_data.rename(columns={'Enumerator': 'name'})

    # Insert enumerator data into the database using pandas
    enumerator_data.to_sql(
        'enumerator',
        con=engine,
        if_exists='append',
        index=False,
        chunksize=10000,
    )

    print(enumerator_data.head())
    insert_logger(len(enumerator_data), 'enumerator')

    return enumerate(main_data.iterrows())


def insert_logger(length, tabalename):
    # Log INFO of the number of rows inserted
    logging.info('{} {} data inserted into database' ''.format(length, tabalename))


# Run the function
create_enumerator()
