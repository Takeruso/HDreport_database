import mysql.connector
import psycopg2

mysql_conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="employees"
)

postgres_conn = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="12345",
    database="employees"
)

mysql_cursor = mysql_conn.cursor()
postgres_cursor = postgres_conn.cursor()

tables = ["departments", "employees", "dept_emp", "dept_manager", "salaries", "titles"]

for table in tables:
    print(f"Migrating {table}...")

    mysql_cursor.execute(f"SELECT * FROM {table}")
    rows = mysql_cursor.fetchall()

    placeholders = ', '.join(['%s'] * len(rows[0]))
    columns = ', '.join([desc[0] for desc in mysql_cursor.description])
    insert_query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"

    postgres_cursor.executemany(insert_query, rows)
    postgres_conn.commit()
    print(f"{table} migrated successfully!")

mysql_cursor.close()
mysql_conn.close()
postgres_cursor.close()
postgres_conn.close()
print("Data migration completed successfully!")
