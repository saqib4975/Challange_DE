from airflow import DAG
# from airflow.operators.python import PythonOperator
from datetime import datetime
import requests
import pandas as pd
import sqlite3
# Default arguments for the DAG
default_args = {
    'owner': 'your_name',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

# Create the DAG object
dag = DAG(
    'data_processing_dag',
    default_args=default_args,
    description='A DAG for data processing tasks',
    schedule_interval=None,  # You can set a schedule interval if needed
    catchup=False,
)

def fetch_and_save_user_data():
    # Define the API endpoint URL
    url = "https://jsonplaceholder.typicode.com/users"
    headers = {"Content-Type": "application/json", "Accept-Encoding": "define"}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        response_data = response.json()
        
        user_data = []
        for user in response_data:
            user_info = {
                "id": user["id"],
                "name": user["name"],
                "username": user["username"],
                "email": user["email"],
                "lat": user["address"]["geo"]["lat"],
                "lng": user["address"]["geo"]["lng"],
            }
            user_data.append(user_info)
        
        df = pd.DataFrame(user_data)
        
        conn = sqlite3.connect("/path/to/user_data.db")
        df.to_sql("users", conn, if_exists="replace", index=False)
        conn.close()
        
        print("Data successfully saved to SQLite database (user_data.db).")
    else:
        print("Failed to retrieve data. Status code:", response.status_code)

fetch_and_save_user_data_task = PythonOperator(
    task_id='fetch_and_save_user_data_task',
    python_callable=fetch_and_save_user_data,
    dag=dag,
)

# You can define similar tasks for your other functions

# Task dependencies
# fetch_and_save_user_data_task >> other_task

if __name__ == "__main__":
    dag.cli()