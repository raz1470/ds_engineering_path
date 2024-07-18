Contents
==
- [Contents](#contents)
- [Airflow](#airflow)
- [Airflow DAG example](#airflow-dag-example)

<!--intro-start-->
# Airflow
Airflow is an open-source orchestration tool used to programmatically author, schedule, and monitor workflows.

Key concepts:

- **DAGs** - A Python script that defines the workflow structure, where each node represents a task and the edges represent dependencies between tasks.
- **Operators** - Operators define individual tasks within a DAG. Airflow provides many built-in operators for common tasks such as BashOperator (to execute bash commands) and PythonOperator (to execute Python functions).
- **Schedulers** - Airflow's scheduler continuously monitors all DAGs and tasks, and triggers the execution of tasks based on their dependencies and defined schedule.
- **Executors** - Executors determine how tasks are executed.
- **Web interface** - Airflow provides a web-based UI for monitoring and managing DAGs and tasks.

# Airflow DAG example
Below you can see an example of an DAG:

```
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

# Define default arguments for the DAG
default_args = {
    'owner': 'data_scientist',
    'depends_on_past': False,
    'start_date': datetime(2024, 4, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Instantiate the DAG
dag = DAG(
    'simple_dag',
    default_args=default_args,
    description='A simple DAG with two tasks',
    schedule_interval=timedelta(days=1),
)

# Define the first task
def print_hello():
    print("Hello, Airflow!")

task_hello = PythonOperator(
    task_id='print_hello',
    python_callable=print_hello,
    dag=dag,
)

# Define the second task
def print_goodbye():
    print("Goodbye, Airflow!")

task_goodbye = PythonOperator(
    task_id='print_goodbye',
    python_callable=print_goodbye,
    dag=dag,
)

# Define task dependencies
task_hello >> task_goodbye
```

<!--intro-end-->
