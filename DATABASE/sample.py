import psycopg2

def table():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Q123Werc14",
        host="localhost",
        port="5433"
    )

    cursor = conn.cursor()
    cursor.execute("""create table employees(Name Text, ID Int, Age int);""")
    print("Table created successfully")

    conn.commit()
    conn.close()


# Adding data into table
# def data():
#     conn = psycopg2.connect(
#         dbname="postgres",
#         user="postgres",
#         password="Q123Werc14",
#         host="localhost",
#         port="5433"
#     )
#
#     cursor = conn.cursor()
#     cursor.execute("""insert into employees(Name,ID,Age) values ('Sam', 01, 30);""")
#     print("Data added successfully")
#
#     conn.commit()
#     conn.close()


# def extract():
#     conn = psycopg2.connect(
#         dbname="postgres",
#         user="postgres",
#         password="Q123Werc14",
#         host="localhost",
#         port="5433"
#     )
#
#     cursor = conn.cursor()
#     cursor.execute("""select * from employees;""")
#     show = cursor.fetchone()   # To get data from database
#     print(show[2])             # Extract data by using index
#
#     conn.commit()
#     conn.close()


print("--------Taking input from user to add data into database--------")

def data():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Q123Werc14",
        host="localhost",
        port="5433"
    )

    cursor = conn.cursor()

    name = input("Enter Name: ")
    id = int(input("Enter ID: "))
    age = int(input("Enter Age: "))

    query = """insert into employees(Name,ID,Age) values (%s, %s, %s);"""
    cursor.execute(query, (name, id, age))

    print("Data added successfully")

    conn.commit()
    conn.close()


data()
