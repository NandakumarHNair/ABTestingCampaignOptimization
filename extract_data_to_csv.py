import sqlite3
import pandas as pd

# Step 1: Connect to the SQLite database
conn = sqlite3.connect('ab_testing.db')

# Step 2: Write a SQL query to extract all data from campaign_data
query = "SELECT * FROM campaign_data"

# Step 3: Load the data into a pandas DataFrame
df = pd.read_sql_query(query, conn)

# Step 4: Save the DataFrame to a CSV file
df.to_csv('data/marketing_data.csv', index=False)

# Step 5: Close the database connection
conn.close()

print("Data extracted and saved to 'data/marketing_data.csv'.")

