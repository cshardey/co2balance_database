from __future__ import annotations

import logging

import pandas as pd

from app.db.session import engine

# Read main excel data from CO2Balance
# TODO: Data will be picked up from an ftpserver

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

main_data = pd.read_excel('../../data/co2balance.xlsx', sheet_name='Day 1')


def create_enumerator():
    """
    Create an enumerator for the main data
    :return: enumerator
    """
    # Filter main data to only include the columns we need
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

    logging.info('Enumerator data inserted into database')

    insert_logger(len(enumerator_data), 'enumerator')

    return enumerate(main_data.iterrows())


def insert_logger(length, tabalename):
    # Log INFO of the number of rows inserted
    logging.info('{} {} data inserted into database' ''.format(length, tabalename))


# Run the function
create_enumerator()


def create_village():
    """
    Create a village for the main data
    :return: enumerator
    """
    # Filter main data to only include the columns we need
    village_data = main_data[['Village?', 'District?', 'Sector?']]
    # check for duplicates and remove them
    village_data = village_data.drop_duplicates()

    # Convert the name  to a word case
    village_data['Village?'] = village_data['Village?'].str.title()
    # Rename the column Enumerator to name
    village_data = village_data.rename(
        columns={'Village?': 'name', 'District?': 'district', 'Sector?': 'sector'},
    )

    # Replace empty named villages with 'Unknown'
    village_data['name'] = village_data['name'].fillna('Unknown')

    # Insert enumerator data into the database using pandas
    village_data.to_sql(
        'village',
        con=engine,
        if_exists='append',
        index=False,
        chunksize=10000,
    )

    logging.info('Village data inserted into database')

    insert_logger(len(village_data), 'village')

    return enumerate(main_data.iterrows())


create_village()
