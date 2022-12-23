import pandas as pd
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import app
from app.populate.cook_stove.clean_project_file import clean_project_file as Transform
from app.populate.cook_stove.clean_project_file import extract_project_data
from app.populate.cook_stove.project_base import ProjectBase
from app.populate.cook_stove.insert_project_data import InsertProjectData

args = {
    'owner': 'CO2balance',
    'start_date': days_ago(1)
}
dag = DAG(
    dag_id='co2balance',
    default_args=args,
    schedule_interval=None,
    description='Data Pipeline for CO2balance',
    tags=['CookStove']
)


def extract_data(**kwargs):
    fn = extract_project_data(file_path='/opt/airflow/dags/app/data/co2balance.xlsx', sheet_names=['Day 1 Cleaned'])
    kwargs['ti'].xcom_push(key='extracted_data_file', value=fn)


def transform_data(**kwargs):
    ti = kwargs['ti']
    extracted_data_file = ti.xcom_pull(key='extracted_data_file', task_ids='ExtractData')
    fn = Transform(file_path=extracted_data_file, sheet_names=['Sheet1'])
    kwargs['ti'].xcom_push(key='transformed_data_file', value=fn)


def load_project_base(**kwargs):
    ti = kwargs['ti']
    transformed_data_file = ti.xcom_pull(key='transformed_data_file', task_ids='TransformData')
    main_data = pd.read_excel(transformed_data_file, sheet_name='Sheet1')
    kenya_cooked_stove_project = ProjectBase(main_data, "/opt/airflow/dags/app/data")
    kenya_cooked_stove_project.populate_base_data()


def load_project_data(**kwargs):
    ti = kwargs['ti']
    transformed_data_file = ti.xcom_pull(key='transformed_data_file', task_ids='TransformData')
    main_data = pd.read_excel(transformed_data_file, sheet_name='Sheet1')
    insert_data = InsertProjectData(main_data)
    insert_data.insert_project_datas()




with dag:
    initialise_db = PythonOperator(
        task_id='InitialiseDB',
        python_callable=app.db.session.init_db,
    )

with dag:
    extract_data = PythonOperator(
        task_id='ExtractData',
        python_callable=extract_data,

    )

with dag:
    transform_data_dag = PythonOperator(
        task_id='TransformData',
        python_callable=transform_data,
    )

with dag:
    load_project_base_dag = PythonOperator(
        task_id='LoadProjectBase',
        python_callable=load_project_base,
    )


with dag:
    load_project_data_dag = PythonOperator(
        task_id='LoadProjectData',
        python_callable=load_project_data,
    )


initialise_db >> extract_data >> transform_data_dag >> load_project_base_dag >> load_project_data_dag
