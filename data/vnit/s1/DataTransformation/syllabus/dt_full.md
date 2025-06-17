# Module Documentation: Introduction to Querying Language and RDBMS

---

## Module 1: Introduction to Querying Language and RDBMS

### Overview
- **Introduction to Structured Query Language (SQL)**  
  - Purpose, syntax, and role in managing relational databases.

- **Types of Databases**  
  - Relational vs. Non-relational databases (NoSQL), use cases, and differences.

- **Client-Server vs. File Server Databases**  
  - Key distinctions: scalability, security, performance, and architecture.

- **Understanding SQL Server Management Studio (SSMS)**  
  - Tools for database management, query execution, and administration.

- **SQL Table Basics**  
  - Creating tables, defining columns, and understanding relationships.

- **Data Types and Functions in SQL**  
  - Numeric, string, date/time data types; built-in functions for manipulation.

- **Transaction-SQL (T-SQL)**  
  - Extending SQL with procedural programming capabilities.

- **Authentication for Windows**  
  - Integration of Windows credentials with database systems.

- **Data Control Language (DCL)**  
  - Commands like `GRANT`, `REVOKE`, and `DENY` for managing access rights.

- **SQL Keywords Identification**  
  - Recognizing reserved keywords in SQL queries and their roles.

---

## Module 2: Database Normalization and Entity-Relationship Model

### Overview
- **Entity-Relationship (E-R) Model**  
  - Concepts of entities, attributes, and relationships.

- **Entities and Entity Sets**  
  - Definition of entities and how they are grouped into sets.

- **Attributes and Their Types**  
  - Single-valued vs. multi-valued attributes; derived and composite attributes.

- **Relationship Sets and Degree**  
  - How entities relate to each other; one-to-one, one-to-many, many-to-many relationships.

- **Mapping Cardinalities**  
  - Constraints on the number of entity instances that can participate in a relationship.

- **E-R Notation Symbols**  
  - Standard symbols for representing entities, attributes, and relationships (e.g., diamonds, rectangles).

- **Database Normalization**  
  - Principles of normalization to reduce redundancy and improve data integrity.

- **Functional Dependencies**  
  - Key concepts underpinning normalization: candidate keys, primary keys.

- **Normalization Forms**  
  - First Normal Form (1NF), Second Normal Form (2NF), Third Normal Form (3NF),  
    Boyce-Codd Normal Form (BCNF), Fourth Normal Form (4NF), Fifth Normal Form (5NF).

---

## Module 3: Operators for Querying Databases

### Overview
- **Relational Database Fundamentals**  
  - Tables, rows, columns, and keys as foundational concepts.

- **Operators in SQL**  
  - Logical operators (`AND`, `OR`, `NOT`) and relational operators (`=`, `<`, `>`, etc.).

- **Constraints and Domains**  
  - Primary key, foreign key, unique constraints; domain definitions for data validation.

- **Indexes**  
  - Types (clustered, non-clustered) and their role in query performance optimization.

- **Stored Procedures**  
  - Precompiled SQL code blocks for reusable operations.

- **Primary, Foreign, and Unique Keys**  
  - Enforcing referential integrity and uniqueness constraints.

- **Group Functions**  
  - Aggregation functions like `COUNT`, `SUM`, `AVG`, `MAX`, `MIN` with `GROUP BY`.

---

## Module 4: Querying Databases Using Joins, Tables, and Variables

### Overview
- **Advanced SQL Table Concepts**  
  - Temporary tables, table variables, and their use cases.

- **SQL Functions**  
  - Scalar functions (e.g., `UPPER`, `LOWER`), aggregate functions (e.g., `SUM`, `AVG`).

- **Operators & Queries**  
  - Advanced query techniques using logical and relational operators.

- **Join Types**  
  - Inner, outer, cross, and self joins for combining data from multiple tables.

- **Set Operators**  
  - `UNION`, `INTERSECT`, `EXCEPT` for merging query results with rules and constraints.

- **Subqueries**  
  - Nested queries in `SELECT`, `INSERT`, `UPDATE`, `DELETE` statements.  
    - Types: Scalar, inline table-valued, multi-statement table-valued.

- **SQL Subquery Rules**  
  - Scope, performance considerations, and usage with operators like `WHERE`, `HAVING`.

- **Set Clause in Subqueries**  
  - Modifying query results using subquery outputs in `SET` statements.

- **Temporary Table Creation**  
  - Local vs. global temporary tables for intermediate data storage.

---

## Module 5: Advanced Queries for Large Databases

### Overview
- **SQL Views**  
  - Creating, altering, renaming, and dropping views; benefits of using views.

- **Stored Procedures**  
  - Key advantages (reusability, security) and working with parameters.

- **User-Defined Functions (UDFs)**  
  - Scalar, inline table-valued, and multi-statement table-valued functions.

- **Error Handling**  
  - Implementing `TRY...CATCH` blocks for robust query execution.

- **Ranking Functions**  
  - `RANK`, `DENSE_RANK`, `ROW_NUMBER` for sorting and grouping data.

- **Indexes for Performance**  
  - Clustered vs. non-clustered indexes; guidelines for efficient index creation.

- **Covering Queries**  
  - Leveraging indexes to avoid table scans in large datasets.

- **Common Table Expressions (CTEs)**  
  - Recursive CTEs and hierarchical data querying.

- **Python as a Front End**  
  - Integration of Python with SQL for data analysis and automation.

- **NoSQL Querying**  
  - Introduction to querying NoSQL databases (e.g., MongoDB, Cassandra) vs. relational models.

- **Handling Large Datasets**  
  - Optimization techniques for scalability, performance, and memory management.
