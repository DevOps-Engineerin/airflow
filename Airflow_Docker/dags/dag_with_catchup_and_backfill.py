from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'ganza_m',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}
#
with DAG(
    dag_id='ganza_dag_catchup_backfill_v18',
    default_args=default_args,
    start_date=datetime(2023, 8, 6),
    schedule_interval='@daily',
    catchup=False
) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command='echo "hello world, My Name is gmx the DJ, and I am 20 years old! from KGL"'
    )
    
