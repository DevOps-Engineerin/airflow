from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args ={
    'owner': 'ganza_m',
    'retries': 5,
    'retry_delay':timedelta(minutes=2)
}

with DAG(
    dag_id='ganza_dag_v3',
    default_args=default_args,
    description='this is my first dag that we write',
    start_date=datetime(2023, 8, 30),
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id = 'first_task',
        bash_command="echo hello world, this is the first task"
    )
    
    task2 = BashOperator(
        task_id ='second_task',
        bash_command="echo hello, this is a second task2 and it will run after task1 has runned"
    )
    
    task3 = BashOperator(
        task_id = 'third_task',
        bash_command="echo hello, task3 here runnig after task2"
    )
    
    task1.set_downstream(task2)
    task1.set_downstream(task3)
