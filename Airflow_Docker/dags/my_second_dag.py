from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'ganza_m',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

def greet():
    print("hello world from pythonoperator")
    

with DAG(
    default_args=default_args,
    dag_id='ganza_dag_v6',
    description='this is my second dag that I write and the first with pythonoperator',
    start_date=datetime(2023, 9, 5),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet
    )
    
    task1