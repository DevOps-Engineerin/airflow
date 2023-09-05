from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'ganza_m',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

def greet(name, ti):
    name = ti.xcom_pull(task_ids='get_name')
    print(f"hello world from pythonoperator, My Name is {name},"
          f"and I am {age} years old!")

def get_name():  
    return 'ganza' 

with DAG(
    default_args=default_args,
    dag_id='ganza_dag_v9',
    description='this is my second dag that I write and the first with pythonoperator',
    start_date=datetime(2023, 9, 5),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet,
        op_kwargs={'age': 25}
    )
    
    task2 = PythonOperator(
        task_id='get_name',
        python_callable=get_name
    )
    
    task2 >> task1