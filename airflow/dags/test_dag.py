from __future__ import print_function

import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

args = {
    "owner": "ryanyuan",
    "start_date": airflow.utils.dates.days_ago(1),
    "provide_context": True,
}

dag = DAG("hello_world_dag", schedule_interval="@once", default_args=args)


def print_hello(**kwargs):
    print("Hello")


say_hello = PythonOperator(task_id="print_hello",
                           dag=dag,
                           python_callable=print_hello)

say_world = BashOperator(
    task_id="print_world", dag=dag, bash_command='echo " world!"'
)

say_hello > say_world
