from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


defaylt_args = {
    'owner': 'ganza_m',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    default_args=defaylt_args,
    dag_id='ganza_dag_cron_expression_v19',
    start_date=datetime(2023, 9, 6),
    schedule_interval='0 0 * * Tue-Fri', # this is a cron expression that will run the dag at midnight every day
    ) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command='echo "hello world, and this a dag with cron expression "'
    )
    
    task1