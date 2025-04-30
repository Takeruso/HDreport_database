# RDBMS Performance Comparison – MySQL, MariaDB, PostgreSQL

📘 **Course**: COS20015 - Database Concepts (Swinburne University of Technology, Sarawak Campus)  
👥 **Authors**: Takeru (102784225), Pang Jee Nee (102771146), Jessabel (102766540)  
🧪 **Tech used**: Docker, WSL, Sysbench, Python, SQL  

> 📄 **Disclaimer**:  
> This report was produced as part of a group assignment for COS20015 – Database Concepts at Swinburne University of Technology (Sarawak Campus) in Semester 1, 2023.  
> It is published here strictly for educational and portfolio purposes.  
> The intellectual content belongs to the authors listed above.  
> Redistribution, modification, or commercial use of this material is not permitted without permission.  
> No official content or materials provided by Swinburne (e.g., assignment briefs, marking rubrics) are included.

While the project was a team effort, I (Takeru) led the experimental design and execution, including Docker/WSL setup, benchmarking with Sysbench and Python, and writing most of the technical analysis and discussion in the final report.  
Although my SQL knowledge was limited at the time, I actively used AI tools to overcome technical gaps and complete the benchmarks and report.

---

## 📂 Contents

- Experimental setup (WSL + Docker + Sysbench)  
- Query execution time & indexing impact  
- Concurrency benchmarking  
- Storage engine comparison  
- Query optimization plan analysis  

---

## 📝 Summary of the Report

This report investigates the performance of three widely used relational database systems — **MySQL**, **MariaDB**, and **PostgreSQL** — under various workloads using Docker containers. The benchmarks were conducted via Python and Sysbench tools, focusing on:

- **Raw query execution time** (e.g., SELECT on indexed vs non-indexed columns)  
- **Indexing impact on read performance**  
- **Concurrency performance under 10-thread workloads**  
- **Differences in execution plans and optimizers**  
- **Insert performance comparison across storage engines (InnoDB, MyISAM)**  

Key findings include:

- **MariaDB** generally showed fast performance for simple indexed reads.  
- **PostgreSQL** demonstrated superior concurrency handling and consistent performance under stress.  
- **Indexing significantly improved performance** across all systems, though PostgreSQL’s cost model offered better optimization in certain cases.  
- **Storage engine selection** (e.g., MyISAM vs InnoDB) had a noticeable effect on insert latency.

---

## 📸 Screenshots of Benchmark Results

### 🖼️ Query Execution Time & Index Impact

![Query Execution Benchmark](screenshot/compare_result1.png)  
> Execution time (ms) for SELECT queries before and after indexing across MySQL, MariaDB, and PostgreSQL.

---

### 🖼️ Query Plan Analysis & Insert Time

![Execution Plans & Insert Time](screenshot/compare_result2.png)  
> Comparison of execution plans and INSERT performance across different storage engines and databases.

---

### 🖼️ Sysbench - MariaDB (Read/Write)

![MariaDB Sysbench](screenshot/mariadb_result_day2.png)  
> MariaDB processed 58,357 transactions in 60s with average latency of ~10.28ms using 10 threads.

---

### 🖼️ Sysbench - MySQL (Read/Write)

![MySQL Sysbench](screenshot/mysql_result_day2.png)  
> MySQL handled 20,845 transactions in 60s with average latency of ~28.78ms under 10 concurrent threads.

---

### 🖼️ Sysbench - PostgreSQL (Read/Write)

![PostgreSQL Sysbench](screenshot/postgresql_result_day2.png)  
> PostgreSQL achieved 20,963 transactions with the lowest average latency (~4.77ms) among all three DBs.

---

## 📄 Report

The full report is available in [`report/Comparison of.pdf`](../report/Comparison%20of.pdf)

---

## 📜 License

Educational Use Only

This repository is provided solely for educational and portfolio purposes. All content is owned by the respective authors. You may not copy, redistribute, or use this material for commercial or academic cheating purposes.
