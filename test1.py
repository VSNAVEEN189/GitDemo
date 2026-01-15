import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="demo123",
    host="localhost",
    port="5433"
)

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE employees (
        Name TEXT,
        ID INT,
        Age INT
    );
''')

print("Table created successfully")

conn.commit()
conn.close()
