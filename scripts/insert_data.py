import sqlite3
import random
from datetime import datetime, timedelta

# Connect to the SQLite database
conn = sqlite3.connect('ab_testing.db')
cursor = conn.cursor()

# Define how many rows you want to insert
num_rows = 100

# Function to generate random dates
def random_date(start_date, end_date):
    delta = end_date - start_date
    return start_date + timedelta(days=random.randint(0, delta.days))

# Generate random data and insert it into the table
for i in range(1, num_rows + 1):
    user_id = i
    group_name = random.choice(['A', 'B'])
    conversion = random.choice([0, 1])
    date = random_date(datetime(2024, 1, 1), datetime(2024, 1, 31)).strftime('%Y-%m-%d')

    cursor.execute("""
        INSERT INTO campaign_data (user_id, group_name, conversion, date)
        VALUES (?, ?, ?, ?)
    """, (user_id, group_name, conversion, date))

# Commit the changes and close the connection
conn.commit()
conn.close()

print(f"Inserted {num_rows} rows into campaign_data table.")

