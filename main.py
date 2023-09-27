import requests
import pandas as pd
import sqlite3

def fetch_and_save_user_data():
    # Define the API endpoint URL
    url = "https://jsonplaceholder.typicode.com/users"

    # Define headers for the request
    headers = {"Content-Type": "application/json", "Accept-Encoding": "define"}

    # Send a GET request to the API endpoint with the specified headers
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        response_data = response.json()

        # Extract and create a DataFrame with the specified fields
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

        # Create a DataFrame from the extracted data
        df = pd.DataFrame(user_data)

        # Create a SQLite database connection
        conn = sqlite3.connect("user_data.db")

        # Write the DataFrame to the SQLite database
        df.to_sql("users", conn, if_exists="replace", index=False)

        # Close the database connection
        conn.close()

        print("Data successfully saved to SQLite database (user_data.db).")
    else:
        print("Failed to retrieve data. Status code:", response.status_code)


fetch_and_save_user_data()
