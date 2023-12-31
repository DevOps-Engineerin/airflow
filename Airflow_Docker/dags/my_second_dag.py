from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'ganza_m',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

def greet(ti):
    first_name = ti.xcom_pull(task_ids='get_name', key='first_name')
    last_name = ti.xcom_pull(task_ids='get_name', key='last_name')
    age = ti.xcom_pull(task_ids='get_age', key='age')
    print(f"hello world, My Name is {first_name} {last_name},"
          f"and I am {age} years old!")

def get_name(ti):  
    ti.xcom_push(key='first_name', value='gmx')
    ti.xcom_push(key='last_name', value='the DJ')
    
def get_age(ti): 
    ti.xcom_push(key='age', value=20)

with DAG(
    default_args=default_args,
    dag_id='ganza_dag_v13',
    description='this is my second dag that I write and the first with pythonoperator',
    start_date=datetime(2023, 9, 5),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet
        #op_kwargs={'age': 25}
    )
    
    task2 = PythonOperator(
        task_id='get_name',
        python_callable=get_name
    )
    
    task3 = PythonOperator(
        task_id='get_age',
        python_callable=get_age
    )
        
    [task2, task3] >> task1