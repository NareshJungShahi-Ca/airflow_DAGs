from datetime import datetime
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator

with DAG(
	dag_id="k8s_executor_test"
        start_date=datetime(2026, 1, 1),
        schedule=None,
        catchup=False,
) as dag:

   task_1 = BashOperator(
	task_id="print_hostname",
        bash_command="echo 'Running inside task pod'; hostname; sleep 30",
)



