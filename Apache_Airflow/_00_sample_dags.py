from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2022, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG('simple_dag', default_args=default_args, schedule_interval=timedelta(days=1))

t1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag)

t2 = BashOperator(
    task_id='sleep',
    bash_command='sleep 5',
    retries=3,
    dag=dag)

t1 >> t2
# ======================================================================================
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import BranchPythonOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2022, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG('branching_dag', default_args=default_args, schedule_interval=timedelta(days=1))

start_task = DummyOperator(task_id='start_task', dag=dag)


def get_branch(**context):
    if datetime.now().weekday() < 5:
        return 'weekday_task'
    else:
        return 'weekend_task'


branch_task = BranchPythonOperator(
    task_id='branch_task',
    provide_context=True,
    python_callable=get_branch,
    dag=dag)

weekday_task = BashOperator(
    task_id='weekday_task',
    bash_command='echo "This is a weekday task"',
    dag=dag)

weekend_task = BashOperator(
    task_id='weekend_task',
    bash_command='echo "This is a weekend task"',
    dag=dag)

end_task = DummyOperator(task_id='end_task', dag=dag)

start_task >> branch_task >> [weekday_task, weekend_task] >> end_task

# ===============================================================================

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2022, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG('dynamic_dag', default_args=default_args, schedule_interval=timedelta(days=1))


def create_dynamic_task(task_id):
    return BashOperator(
        task_id=task_id,
        bash_command='echo "This is a dynamic task: {}"'.format(task_id),
        dag=dag)


tasks = ['task1', 'task2', 'task3']

start_task = BashOperator(
    task_id='start_task',
    bash_command='echo "Starting dynamic tasks"',
    dag=dag)

for task in tasks:
    dynamic_task = PythonOperator(
        task_id='dynamic_task_{}'.format(task),
        python_callable=create_dynamic_task)


"""
DID POST GRADUATE  DIPLOMA IN ANIMAL WELFARE  2021
Did Post Graduate Diploma in Animal welfare 2021.
Attended for small animal Orthopedic Training session at Tirupati in August 2022.
Attended for small animal Ophthalmology Training session at Chennai.
Attended many Royal and ARS Clinical Webinars in online.
ATTENDED FOR SMALL ANIMAL ORTHOPEDIC TRAINING SESSION AT TIRUPATI IN AUGUST 2022.
ATTENDED FOR SAMLL ANIMAL OPHTHALMOLOGY TRAINING AT CHENNAI
ATTENDED ANY ROYAL  AND ARS CLINICAL WEBINARS IN ONLINE
EVALUATION OF NANOHYDROXYAPATITE CHITOSAN AND CEFTIOFUR BIOCOMPOSITE FILMS ON CUTANEOUS WOUND HEALING IN RATS
EVALUATION OF NANOHYDROXYAPATITE CHITOSAN AND CEFTIOFUR BIOCOMPOSITE FILMS ON CUTANEOUS WOUND HEALING IN RATS
dddddkjkjk
"""