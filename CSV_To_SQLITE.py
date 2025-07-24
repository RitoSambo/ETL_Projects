import pandas as pd
import sqlite3
import os

#EXTRACT 
csv_file = 'netflix_titles.csv'

if not os.path.exists(csv_file):
    raise FileNotFoundError(f"{csv_file} not found in the current directory.")

df = pd.read_csv(csv_file)
print(f"Original data shape: {df.shape}")

#USER CHOICE
print(" What type of content do you want to load into the database?")
print("1. Movies only")
print("2. TV Shows only")
print("3. Both (All)")

choice = input("Enter your choice (1/2/3): ")

if choice == '1':
    df = df[df['type'].str.lower() == 'movie']
    print("You chose: Movies only")
elif choice == '2':
    df = df[df['type'].str.lower() == 'tv show']
    print(" You chose: TV Shows only")
elif choice == '3':
    print(" You chose: All records (Movies + TV Shows)")
else:
    print(" Invalid choice. Loading all records by default.")

print(f"Filtered data shape: {df.shape}")

#TRANSFORM 
df.drop_duplicates(inplace=True)
df.fillna("Unknown", inplace=True)

# LOAD
db_file = 'netflix.db'
conn = sqlite3.connect(db_file)

# Save to SQLite 
df.to_sql('netflix_titles', conn, if_exists='replace', index=False)

# Confirm
print("Data successfully loaded into SQLite database: netflix.db")
conn.close()
