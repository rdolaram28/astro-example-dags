from airflow import DAG
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
}

dag = DAG(
    'trigger_boomi_process_non_api',
    default_args=default_args,
    description='A simple DAG to trigger Boomi process',
    schedule_interval=None,
)

trigger_boomi_process_non_api = SimpleHttpOperator(
    task_id='trigger_boomi_process',
    http_conn_id='boomi_poc_non_api',
    endpoint='/executeProcess',
    method='POST',
    data='{"processId": "82a51cb5-ec36-42d6-a003-3c0c00573f47",
"atomId": "fd4a0b19-e6ce-4ace-9e34-de484c83141b"}',
    headers={"Content-Type": "application/json"},
    dag=dag,
)

trigger_boomi_process_non_api

