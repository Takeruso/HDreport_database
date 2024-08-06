import mysql.connector
import psycopg2

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

def get_execution_plan(cursor, query):
    cursor.execute(f"EXPLAIN {query}")
    return cursor.fetchall()

queries = [
    "SELECT * FROM employees WHERE emp_no = 10001",
    "SELECT COUNT(*) FROM salaries WHERE salary > 50000"
]

execution_plans = {
    "MySQL": [],
    "MariaDB": [],
    "PostgreSQL": []
}

for query in queries:
    mysql_plan = get_execution_plan(mysql_cursor, query)
    mariadb_plan = get_execution_plan(mariadb_cursor, query)
    postgres_plan = get_execution_plan(postgres_cursor, query)
    
    execution_plans["MySQL"].append(mysql_plan)
    execution_plans["MariaDB"].append(mariadb_plan)
    execution_plans["PostgreSQL"].append(postgres_plan)

mysql_cursor.close()
mysql_conn.close()
mariadb_cursor.close()
mariadb_conn.close()
postgres_cursor.close()
postgres_conn.close()

for db, plans in execution_plans.items():
    print(f"{db} Execution Plans:")
    for query, plan in zip(queries, plans):
        print(f"  Query: {query} - Plan: {plan}")
