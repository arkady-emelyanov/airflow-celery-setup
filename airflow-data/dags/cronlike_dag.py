from airflow import DAG
from airflow import utils
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

#
# @see: https://github.com/apache/incubator-airflow/blob/master/airflow/models.py#L1960
# for default_args and DAG args explanation.
#

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2016, 11, 22),
    'depends_on_past': False,
}

dag = DAG(
    dag_id='cronlike_dag',
    default_args=default_args,
    schedule_interval=timedelta(minutes=5),
    dagrun_timeout=timedelta(minutes=30),
    concurrency=1,
    max_active_runs=1,
    catchup=False)

t1 = BashOperator(
    task_id='print_current_date',
    bash_command='date',
    dag=dag)

t2 = BashOperator(
    task_id='print_os_version',
    bash_command='uname -r',
    dag=dag)

t2.set_upstream(t1)
