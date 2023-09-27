# Challange_DE
This Repo contains all the file related to Data Engineering question asked  


All files has been added i have used python to Fetch data from given API's (weather and User) same for the CSV file to store the database i have used SQLite3 database 
as it is a litewight database and very handy to use.


"""
Data Processing DAG
===================
This Apache Airflow DAG (Directed Acyclic Graph) performs data processing tasks, including fetching and saving user data from an API, writing sales data to an SQLite database, and retrieving weather data.

Tasks:
1. Fetch and Save User Data: This task sends a GET request to an API to retrieve user data, processes it, and saves it to an SQLite database.

2. Write Sales Data to SQLite: This task reads sales data from a CSV file and writes it to an SQLite database.

3. Get Weather Data: This task retrieves weather data for a specified city using an API and displays temperature and weather description.

Dependencies:
- 'fetch_and_save_user_data_task' depends on the start of the DAG.
- 'write_sales_data_task' depends on 'fetch_and_save_user_data_task.'
- 'get_weather_data_task' depends on 'write_sales_data_task.'

"""




