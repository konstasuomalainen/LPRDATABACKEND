import pandas as pd
import sqlite3

# List of Excel files for different years (Replace these with your actual file paths)
excel_files = [
    'LappeenrantaOstoLaskuData2020.xlsx',
    'LappeenrantaOstoLaskuData2021.xlsx',
    'LappeenrantaOstoLaskuData2022.xlsx',
    'LappeenrantaOstoLaskuData2023.xlsx'
]

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# Create table in SQLite if it doesn't already exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS data (
   "Index" INTEGER PRIMARY KEY,  -- Make Index a primary key
    "Kuntanro" TEXT,
    "Kunnan nimi" TEXT,         
    "Tositepäivä" DATE,
    "Tositenro" TEXT,
    "Toimittajanro" TEXT,
    "Y-tunnus" TEXT,
    "Toimittaja" TEXT,
    "Tiliryhmän nro" TEXT,
    "Tiliryhmä" TEXT,
    "Lask.tili" TEXT,
    "Tili" TEXT,
    "Summa" REAL,
    "Toimiala nro" TEXT,
    "Toimiala" TEXT,
    "Vastuualue nro" TEXT,
    "Vastuualue" TEXT,
    "Kustannuspaikka" TEXT,
    "Year" INTEGER
)
''')

# Initialize a variable to track the next available ID
next_id = cursor.execute("SELECT MAX(\"Index\") FROM data").fetchone()[0] or 0

# Loop through each Excel file and append its data to the database
for excel_file in excel_files:
    print(f"Processing {excel_file}...")
    
    # Extract the year from the filename (assuming the year is the last 4 digits before .xlsx)
    year = int(excel_file[-9:-5])  # Extracts 2020, 2021, etc.
    
    # Read the Excel file into a DataFrame
    df = pd.read_excel(excel_file)
    
    # Add a "Year" column to the DataFrame
    df['Year'] = year
    
    # Resetting the index to create unique IDs for the new entries
    df.reset_index(drop=True, inplace=True)
    
    # Create a new ID column and increment the next_id
    df["Index"] = range(next_id + 1, next_id + 1 + len(df))
    
    # Update the next_id for the next batch
    next_id += len(df)
    
    # Save the DataFrame to the SQLite database
    df.to_sql('data', conn, if_exists='append', index=False)

# Commit the changes
conn.commit()

# Check the number of records in the table
cursor.execute("SELECT COUNT(*) FROM data")
record_count = cursor.fetchone()
print(f"Number of records in the database: {record_count[0]}")

# Close the connection
conn.close()






