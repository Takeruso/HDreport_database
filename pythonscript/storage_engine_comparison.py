import time
import mysql.connector
import psycopg2

mysql_conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="employees"
)
mysql_cursor = mysql_conn.cursor()

mariadb_conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="employees",
    port=3307  
)
mariadb_cursor = mariadb_conn.cursor()

postgres_conn = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="12345",
    database="employees"
)
postgres_cursor = postgres_conn.cursor()

mysql_cursor.execute("CREATE TABLE IF NOT EXISTS test_innodb (id INT PRIMARY KEY, data VARCHAR(100)) ENGINE=InnoDB")
mysql_cursor.execute("CREATE TABLE IF NOT EXISTS test_myisam (id INT PRIMARY KEY, data VARCHAR(100)) ENGINE=MyISAM")
mariadb_cursor.execute("CREATE TABLE IF NOT EXISTS test_innodb (id INT PRIMARY KEY, data VARCHAR(100)) ENGINE=InnoDB")
mariadb_cursor.execute("CREATE TABLE IF NOT EXISTS test_myisam (id INT PRIMARY KEY, data VARCHAR(100)) ENGINE=MyISAM")

def measure_insert_time(cursor, table_name, start_id):
    start_time = time.time()
    for i in range(10000):  
        cursor.execute(f"INSERT INTO {table_name} (id, data) VALUES (%s, %s)", (start_id + i, 'test'))
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000  
    return execution_time

innodb_time_mysql = measure_insert_time(mysql_cursor, 'test_innodb', 1)
myisam_time_mysql = measure_insert_time(mysql_cursor, 'test_myisam', 20001)  
innodb_time_mariadb = measure_insert_time(mariadb_cursor, 'test_innodb', 1)
myisam_time_mariadb = measure_insert_time(mariadb_cursor, 'test_myisam', 20001)  


print(f"MySQL InnoDB Insert Time: {innodb_time_mysql} ms")
print(f"MySQL MyISAM Insert Time: {myisam_time_mysql} ms")
print(f"MariaDB InnoDB Insert Time: {innodb_time_mariadb} ms")
print(f"MariaDB MyISAM Insert Time: {myisam_time_mariadb} ms")

mysql_cursor.execute("DROP TABLE test_innodb")
mysql_cursor.execute("DROP TABLE test_myisam")
mariadb_cursor.execute("DROP TABLE test_innodb")
mariadb_cursor.execute("DROP TABLE test_myisam")

mysql_cursor.close()
mysql_conn.close()
mariadb_cursor.close()
mariadb_conn.close()
postgres_cursor.close()
postgres_conn.close()
