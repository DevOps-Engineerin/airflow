from datetime import datetime, timedelta

from airflow.decorators import dag, task


default_args = {
    'owner': 'ganza_m',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

@dag(dag_id='ganza_dag_v16',
     default_args=default_args,
     start_date=datetime(2023, 9, 6),
     schedule_interval='@daily',
)

def hello_world_etl():
    
    @task(multiple_outputs=True)
    def get_name():
        return {
                'first_name': 'gmx',
                'last_name': 'the DJ'
                }
    
    @task()
    def get_age():
        return 20
    
    @task()
    def greet(first_name, last_name, age):
        print(f"hello world, My Name is {first_name} {last_name},"
              f"and I am {age} years old!") 
        
    name_dict = get_name()
    #last_name = get_name()
    name = get_name()
    age = get_age()
    greet(first_name=name_dict['first_name'], last_name=name_dict['last_name'], age=age) 
    
greet_dag = hello_world_etl()