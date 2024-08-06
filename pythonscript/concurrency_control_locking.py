import threading
import time
import mysql.connector
import psycopg2

mysql_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '12345',
    'database': 'employees'
}

postgres_config = {
    'host': 'localhost',
    'user': 'postgres',
    'password': '12345',
    'database': 'employees'
}

mariadb_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '12345',
    'database': 'employees',
    'port': 3307 
}

def execute_concurrent_queries_mysql(query, results, index):
    start_time = time.time()
    conn = mysql.connector.connect(**mysql_config)
    cursor = conn.cursor(buffered=True)
    cursor.execute(query)
    cursor.fetchall()  
    cursor.close()
    conn.close()
    end_time = time.time()
    results[index] = end_time - start_time

def execute_concurrent_queries_mariadb(query, results, index):
    start_time = time.time()
    conn = mysql.connector.connect(**mariadb_config)
    cursor = conn.cursor(buffered=True)
    cursor.execute(query)
    cursor.fetchall()  
    cursor.close()
    conn.close()
    end_time = time.time()
    results[index] = end_time - start_time

def execute_concurrent_queries_postgres(query, results, index):
    start_time = time.time()
    conn = psycopg2.connect(**postgres_config)
    cursor = conn.cursor()
    cursor.execute(query)
    cursor.fetchall() 
    cursor.close()
    conn.close()
    end_time = time.time()
    results[index] = end_time - start_time

# D
query = "SELECT * FROM employees WHERE emp_no < 10010"


results_mysql = [0] * 10
results_mariadb = [0] * 10
results_postgres = [0] * 10


threads = []
for i in range(10):  
    t1 = threading.Thread(target=execute_concurrent_queries_mysql, args=(query, results_mysql, i))
    t2 = threading.Thread(target=execute_concurrent_queries_mariadb, args=(query, results_mariadb, i))
    t3 = threading.Thread(target=execute_concurrent_queries_postgres, args=(query, results_postgres, i))
    threads.extend([t1, t2, t3])

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print("MySQL execution times (s):", results_mysql)
print("MariaDB execution times (s):", results_mariadb)
print("PostgreSQL execution times (s):", results_postgres)
