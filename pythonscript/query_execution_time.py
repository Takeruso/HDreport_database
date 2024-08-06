import time
import mysql.connector
import psycopg2

def measure_execution_time(cursor, query):
    start_time = time.time()
    cursor.execute(query)
    cursor.fetchall()  
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000 
    return execution_time

mysql_conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="employees"
)
mysql_cursor = mysql_conn.cursor()

postgres_conn = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="12345",
    database="employees"
)
postgres_cursor = postgres_conn.cursor()

mariadb_conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="employees",
    port=3307  
)
mariadb_cursor = mariadb_conn.cursor()

queries = [
    "SELECT * FROM employees WHERE emp_no = 10001",
    "SELECT COUNT(*) FROM salaries WHERE salary > 50000"
]

results = {
    "MySQL": [],
    "MariaDB": [],
    "PostgreSQL": []
}

for query in queries:
    mysql_time = measure_execution_time(mysql_cursor, query)
    mariadb_time = measure_execution_time(mariadb_cursor, query)
    postgres_time = measure_execution_time(postgres_cursor, query)
    
    results["MySQL"].append(mysql_time)
    results["MariaDB"].append(mariadb_time)
    results["PostgreSQL"].append(postgres_time)

mysql_cursor.close()
mysql_conn.close()
mariadb_cursor.close()
mariadb_conn.close()
postgres_cursor.close()
postgres_conn.close()

for db, times in results.items():
    print(f"{db} Execution Times (ms):")
    for query, time in zip(queries, times):
        print(f"  Query: {query} - Time: {time} ms")
