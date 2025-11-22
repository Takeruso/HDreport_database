# RDBMS Performance Comparison – MySQL, MariaDB, PostgreSQL

This repository documents a benchmarking project comparing the performance of three widely used relational database systems — **MySQL**, **MariaDB**, and **PostgreSQL** — under a variety of read/write workloads using Docker containers on WSL. The benchmarks were conducted using Python scripts and Sysbench to automate query execution and concurrency testing.

---

## 📂 Contents

- Docker-based experimental setup (WSL + Sysbench)
- Query execution time (with/without indexing)
- Concurrency performance benchmarking
- Insert performance across storage engines (InnoDB, MyISAM)
- Execution plan (EXPLAIN) analysis

---

## 📝 Project Summary

This benchmarking project aimed to explore how common factors such as **indexing**, **storage engine type**, and **concurrent workload levels** influence the performance of relational databases.

### Scope of Testing:
- **SELECT and COUNT queries** on large tables (1M rows) with and without indexing.
- **INSERT throughput** across different storage engines (InnoDB, MyISAM).
- **Concurrency simulation** using 10 threads over a 60-second Sysbench OLTP workload.
- **Execution plan analysis** using EXPLAIN outputs from each database engine.

### Key Findings:

- 🔹 **MariaDB** performed best in simple indexed SELECT queries.
- 🔹 **PostgreSQL** excelled in high-concurrency conditions and aggregate queries, showing consistent low-latency performance.
- 🔹 **MySQL** delivered average results, heavily dependent on the storage engine used.
- 🔹 Indexing improved performance across all engines, especially for COUNT-based queries.
- 🔹 Storage engine selection (e.g., MyISAM vs InnoDB) significantly affected INSERT performance and latency.

---

## 📸 Benchmark Screenshots

### 🔹 Query Execution Time & Index Impact

![Query Execution Benchmark](screenshot/compare_result1.png)  
> SELECT performance before and after indexing across MySQL, MariaDB, and PostgreSQL.

---

### 🔹 Query Plan Analysis & Insert Time

![Execution Plans & Insert Time](screenshot/compare_result2.png)  
> Execution plan differences and INSERT speed comparison across storage engines.

---

### 🔹 Sysbench - MariaDB

![MariaDB Sysbench](screenshot/mariadb_result_day2.png)  
> MariaDB: ~58,357 transactions in 60s, average latency ~10.28ms (10 threads).

---

### 🔹 Sysbench - MySQL

![MySQL Sysbench](screenshot/mysql_result_day2.png)  
> MySQL: ~20,845 transactions in 60s, average latency ~28.78ms (10 threads).

---

### 🔹 Sysbench - PostgreSQL

![PostgreSQL Sysbench](screenshot/postgresql_resutlt_day2.png)  
> PostgreSQL: ~20,963 transactions, average latency ~4.77ms — lowest among all three engines.

---

## 🗂️ Data Used

- 📁 **MySQL Employees Sample Dataset**  
  A publicly available dataset from MySQL containing synthetic employee records.  
  [https://dev.mysql.com/doc/employee/en/](https://dev.mysql.com/doc/employee/en/)

- 🔧 **Sysbench OLTP Benchmark Data**  
  Automatically generated test data using Sysbench’s built-in OLTP read/write script  
  with a table size of 1,000,000 rows and 10 concurrent threads.

- 📊 **Custom Benchmark Results**  
  All latency, throughput, and execution plan data were collected during live tests using Python scripts and shell automation.

---

## 📜 Disclaimer

This project serves as a personal portfolio piece demonstrating database performance benchmarking methodologies. 
While based on past academic concepts, the implementation and analysis are reconstructed for educational purposes. 
Please do not use this code for active university assignments.
