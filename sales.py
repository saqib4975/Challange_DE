import pandas as pd
import sqlite3

def write_sales_data_to_sqlite():
    # Read the sales data from a CSV file
    sales_data = pd.read_csv("sales_data.csv")

    # Create a connection to the SQLite database (user_data.db)
    conn = sqlite3.connect("user_data.db")

    # Write the sales data to the SQLite database in a new table named Sales_data
    sales_data.to_sql("Sales_data", conn, if_exists="replace", index=False)

    # Close the database connection
    conn.close()

    print("Sales data successfully saved to SQLite database (user_data.db).")

if __name__ == "__main__":
    write_sales_data_to_sqlite()
