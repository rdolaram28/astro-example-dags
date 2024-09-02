from airflow import DAG
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
}

dag = DAG(
    'boomi_process_trigger',
    default_args=default_args,
    description='A simple DAG to trigger Boomi process',
    schedule_interval=None,
)

trigger_boomi_process = SimpleHttpOperator(
    task_id='trigger_boomi_process',
    http_conn_id='boomi_http_con_poc',
    endpoint='/getItems',
    method='POST',
    data='{"processId": "92a9614c-44a1-41e6-a2b5-d503aa8177dd"}',
    headers={"Content-Type": "application/json"},
    dag=dag,
)

trigger_boomi_process
