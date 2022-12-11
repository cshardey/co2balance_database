from __future__ import annotations

import names
import pandas as pd


def clean_project_file(file_path, sheet_names):
    """
    Clean project file
    :return: project data: pd.DataFrame
    """
    data = pd.read_excel(file_path, sheet_name=sheet_names)
    if data is not None:
        # Initialize empty pd
        projects = pd.DataFrame()
        for sheet in data:
            project_data = data.get(sheet)[
                [
                    'start',
                    'end',
                    'Enumerator',
                    'House number',
                    'Confirm all fuels used by the household will be measured and included in the survey.',
                    'Do you consent to completing the survey?',
                    'Name of the Head of Household?',
                    'Name of survey respondent.',
                    'Phone number of survey respondent?',
                    'Region?',
                    'District?',
                    '_GPS?_latitude',
                    '_GPS?_longitude',
                    '_GPS?_altitude',
                    'How many types of stove does the household use?',
                    'Select all stoves used for cooking by the household:',
                    'Select all stoves used for cooking by the household:/Improved charcoal stove',
                    'Select all stoves used for cooking by the household:/Improved wood stove',
                    'Take a photo of the traditional 3 stone fire_URL',
                    'Take a photo of the ethanol/alcohol stove',
                    'Select all fuels used for cooking by the household:',
                    'Weigh the contents of the wood USE pile.',
                    'Any additional comments?',
                    'Village?',
                    'House number',
                    'Record the current weather.',
                    'District?',
                    'Sector?',
                    'Cell',
                ]
            ]

            # Rename columns
            project_data = project_data.rename(
                columns={
                    'start': 'start_date',
                    'end': 'end_date',
                    'Enumerator': 'enumerator',
                    'House number': 'house_number',
                    'Confirm all fuels used by the household will be measured and included in the survey.': 'confirm_all_fuels',
                    'Do you consent to completing the survey?': 'consent_to_survey',
                    'Name of the Head of Household?': 'head_of_household',
                    'Name of survey respondent.': 'surveyor',
                    'Phone number of survey respondent?': 'surveyor_phone_number',
                    'Region?': 'region',
                    '_GPS?_latitude': 'gps_latitude',
                    '_GPS?_longitude': 'gps_longitude',
                    '_GPS?_altitude': 'gps_altitude',
                    'How many types of stove does the household use?': 'number_of_stoves',
                    'Select all stoves used for cooking by the household:': 'stove_type',
                    'Select all stoves used for cooking by the household:/Improved charcoal stove': 'improved_charcoal_stove',
                    'Select all stoves used for cooking by the household:/Improved wood stove': 'improved_wood_stove',
                    'Take a photo of the traditional 3 stone fire_URL': 'photo_of_traditional_3_stone_fire',
                    'Take a photo of the ethanol/alcohol stove': 'photo_of_ethanol_alcohol_stove',
                    'Select all fuels used for cooking by the household:': 'fuel_type',
                    'Weigh the contents of the wood USE pile.': 'weight_of_wood_pile',
                    'Any additional comments?': 'comments',
                    'Village?': 'village',
                    'Record the current weather.': 'current_weather',
                    'District?': 'district',
                    'Sector?': 'sector',
                    'Cell': 'cell',
                },
            )

            # Convert Names to Title Case

            # Override all enumerator names with random names
            project_data['enumerator'] = project_data['enumerator'].apply(
                lambda x: names.get_full_name(),
            )
            project_data['head_of_household'] = project_data[
                'head_of_household'
            ].str.title()
            project_data['surveyor'] = project_data['surveyor'].str.title()
            project_data['region'] = project_data['region'].str.title()
            project_data['village'] = project_data['village'].str.title()
            # Join project data to a dataframe
            projects = projects.append(project_data, ignore_index=True)

            # project_data["project"] = project_data["project"].str.title()
        # convert to excel file
        projects.to_excel('../../app/data/project_data.xlsx', index=False)
        return projects

    # Read project data from project_data.json
