import psycopg2   # pyright: ignore[reportMissingModuleSource]
conn = psycopg2.connect(dbname="postgres", user="postgres", password="Q123Werc!4", host="localhost", port="5432", port="5433")

cursor = conn.cursor()
cursor.execute('''create table employees(Name text, ID int, Age int);''')
print("Table created successfully")

conn.commit()
conn.close()