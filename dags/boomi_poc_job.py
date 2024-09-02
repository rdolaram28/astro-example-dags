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
    data='{"processId": "Main: SFDC to EDW Item Data"}',
    headers={"Content-Type": "application/json"},
    dag=dag,
)

trigger_boomi_process
