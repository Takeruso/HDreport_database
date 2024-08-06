import mysql.connector
import psycopg2
import time

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

def measure_execution_time(cursor, query):
    start_time = time.time()
    cursor.execute(query)
    cursor.fetchall()  # Fetch the data to ensure the query is fully executed
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
    return execution_time

def drop_index_if_exists(cursor, table_name, index_name):
    cursor.execute(f"SHOW INDEX FROM {table_name} WHERE Key_name='{index_name}'")
    result = cursor.fetchone()
    if result:
        cursor.execute(f"DROP INDEX {index_name} ON {table_name}")

queries = [
    "SELECT * FROM employees WHERE emp_no = 10001",
    "SELECT COUNT(*) FROM salaries WHERE salary > 50000"
]

results_before_index = {
    "MySQL": [],
    "MariaDB": [],
    "PostgreSQL": []
}

for query in queries:
    mysql_time = measure_execution_time(mysql_cursor, query)
    mariadb_time = measure_execution_time(mariadb_cursor, query)
    postgres_time = measure_execution_time(postgres_cursor, query)
    
    results_before_index["MySQL"].append(mysql_time)
    results_before_index["MariaDB"].append(mariadb_time)
    results_before_index["PostgreSQL"].append(postgres_time)

drop_index_if_exists(mysql_cursor, "employees", "idx_emp_no")
drop_index_if_exists(mysql_cursor, "salaries", "idx_salary")
drop_index_if_exists(mariadb_cursor, "employees", "idx_emp_no")
drop_index_if_exists(mariadb_cursor, "salaries", "idx_salary")
postgres_cursor.execute("DROP INDEX IF EXISTS idx_emp_no")
postgres_cursor.execute("DROP INDEX IF EXISTS idx_salary")

index_queries = [
    "CREATE INDEX idx_emp_no ON employees(emp_no)",
    "CREATE INDEX idx_salary ON salaries(salary)"
]

for index_query in index_queries:
    mysql_cursor.execute(index_query)
    mariadb_cursor.execute(index_query)
    postgres_cursor.execute(index_query)

results_after_index = {
    "MySQL": [],
    "MariaDB": [],
    "PostgreSQL": []
}

for query in queries:
    mysql_time = measure_execution_time(mysql_cursor, query)
    mariadb_time = measure_execution_time(mariadb_cursor, query)
    postgres_time = measure_execution_time(postgres_cursor, query)
    
    results_after_index["MySQL"].append(mysql_time)
    results_after_index["MariaDB"].append(mariadb_time)
    results_after_index["PostgreSQL"].append(postgres_time)

mysql_cursor.close()
mysql_conn.close()
mariadb_cursor.close()
mariadb_conn.close()
postgres_cursor.close()
postgres_conn.close()

print("Results before index:")
for db, times in results_before_index.items():
    print(f"{db} Execution Times (ms):")
    for query, time in zip(queries, times):
        print(f"  Query: {query} - Time: {time} ms")

print("\nResults after index:")
for db, times in results_after_index.items():
    print(f"{db} Execution Times (ms):")
    for query, time in zip(queries, times):
        print(f"  Query: {query} - Time: {time} ms")
