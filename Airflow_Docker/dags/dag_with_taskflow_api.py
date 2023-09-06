from datetime import datetime, timedelta

from airflow.decorators import dag, task


default_args = {
    'owner': 'ganza_m',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

@dag(dag_id='ganza_dag_v14',
     default_args=default_args,
     start_date=datetime(2023, 9, 5),
     schedule_interval='@daily',
)

def hello_world_etl():
    
    @task()
    def get_name():
        return 'gmx'
    
    @task()
    def get_age():
        return 20
    
    @task()
    def greet(name, age):
        print(f"hello world, My Name is {name},"
              f"and I am {age} years old!") 
        
    #first_name = get_name()
    #last_name = get_name()
    name = get_name()
    age = get_age()
    greet(name=name, age=age) 
    
greet_dag = hello_world_etl()