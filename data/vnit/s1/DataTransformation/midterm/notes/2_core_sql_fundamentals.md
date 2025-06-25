## II. Core SQL Language Fundamentals

This section introduces the fundamental categories of SQL commands and provides an overview of their purpose within a database system.

**2. Categories of SQL Commands**

SQL commands are broadly categorized based on the type of operations they perform on a database. The four main categories are:

* **DDL (Data Definition Language):**
    * Used to define and manage the structure or schema of a database. DDL commands deal with creating, altering, and deleting database objects such as tables, indexes, views, and schemas themselves.
    * Think of DDL as the language for setting up the blueprint of your database.
    * **Key Commands:**
        * `CREATE`: Used to create new database objects (e.g., `CREATE TABLE`, `CREATE DATABASE`).
            ```sql
            -- Example: Creating a new table named 'Customers'
            CREATE TABLE Customers (
                CustomerID INT PRIMARY KEY,
                FirstName VARCHAR(50),
                LastName VARCHAR(50),
                City VARCHAR(50)
            );
            ```
        * `ALTER`: Used to modify the structure of existing database objects (e.g., `ALTER TABLE` to add/modify columns).
            ```sql
            -- Example: Adding a new column 'Email' to the 'Customers' table
            ALTER TABLE Customers
            ADD Email VARCHAR(100);
            ```
        * `DROP`: Used to delete existing database objects (e.g., `DROP TABLE`, `DROP DATABASE`). **Caution: This is a permanent operation and data will be lost.**
            ```sql
            -- Example: Deleting the 'Customers' table
            DROP TABLE Customers;
            ```

* **DML (Data Manipulation Language):**
    * Used to manipulate the data stored within the database tables. DML commands allow you to insert, update, and delete records (rows) in the tables.
    * Think of DML as the language for managing the actual data content.
    * **Key Commands:**
        * `INSERT`: Used to add new rows of data into a table.
            ```sql
            -- Example: Inserting a new customer record into the 'Customers' table
            INSERT INTO Customers (CustomerID, FirstName, LastName, City, Email)
            VALUES (1, 'Alice', 'Smith', 'New York', 'alice.smith@example.com');
            ```
        * `UPDATE`: Used to modify existing records in a table. You typically use a `WHERE` clause to specify which rows to update.
            ```sql
            -- Example: Updating the city of the customer with CustomerID 1
            UPDATE Customers
            SET City = 'Los Angeles'
            WHERE CustomerID = 1;
            ```
        * `DELETE`: Used to remove existing records from a table. Use a `WHERE` clause to specify which rows to delete. Without a `WHERE` clause, it will delete all rows.
            ```sql
            -- Example: Deleting the customer with CustomerID 1
            DELETE FROM Customers
            WHERE CustomerID = 1;

            -- Caution: The following will delete all rows from the 'Customers' table
            -- DELETE FROM Customers;
            ```

* **DQL (Data Query Language):**
    * Used to retrieve and view data stored in the database. The primary DQL command is `SELECT`.
    * Think of DQL as the language for asking questions about your data.
    * **Key Command:**
        * `SELECT`: Used to retrieve data from one or more tables based on specified criteria.
            ```sql
            -- Example: Selecting all columns and rows from the 'Customers' table
            SELECT *
            FROM Customers;

            -- Example: Selecting only the 'FirstName' and 'City' columns
            SELECT FirstName, City
            FROM Customers;

            -- Example: Selecting customers from 'New York'
            SELECT FirstName, LastName
            FROM Customers
            WHERE City = 'New York';
            ```

* **TCL (Transaction Control Language):**
    * Used to manage transactions within a database. A transaction is a sequence of one or more SQL operations that are treated as a single logical unit of work. TCL commands are crucial for maintaining data integrity, especially when dealing with critical data modifications.
    * Think of TCL as the language for ensuring data consistency during a series of changes.
    * **Key Concepts:**
        * **Transaction:** A logical unit of work comprising one or more SQL statements. Transactions should ideally adhere to the ACID properties (Atomicity, Consistency, Isolation, Durability).
        * **Implicit vs. Explicit Transactions:** Some database systems have implicit transactions (each statement is treated as a transaction), while others require explicit initiation and termination of transactions.
    * **Key Commands:**
        * `COMMIT`: Saves all changes made within the current transaction permanently to the database.
            ```sql
            -- Example: Starting a transaction, performing an update, and then committing
            START TRANSACTION;
            UPDATE Accounts
            SET Balance = Balance - 100
            WHERE AccountID = 123;
            UPDATE Accounts
            SET Balance = Balance + 100
            WHERE AccountID = 456;
            COMMIT; -- Makes the balance changes permanent
            ```
        * `ROLLBACK`: Undoes all changes made within the current transaction since the last `COMMIT` or the beginning of the transaction. This is used to revert the database to a previous consistent state if an error occurs or if the transaction cannot be completed successfully.
            ```sql
            -- Example: Starting a transaction and then rolling back the changes
            START TRANSACTION;
            INSERT INTO Orders (CustomerID, OrderDate)
            VALUES (789, '2025-04-24');
            -- An error occurs here...
            ROLLBACK; -- Undoes the INSERT operation
            ```
        * `SAVEPOINT`: Creates a point within a transaction to which you can later roll back. This allows you to undo parts of a transaction without rolling back the entire thing.
            ```sql
            START TRANSACTION;
            INSERT INTO Products (ProductID, Name) VALUES (1001, 'New Widget');
            SAVEPOINT after_insert;
            UPDATE Inventory SET Quantity = Quantity + 10 WHERE ProductID = 1001;
            -- Another error occurs...
            ROLLBACK TO SAVEPOINT after_insert; -- Undoes the UPDATE but keeps the INSERT
            COMMIT;
            ```

ACID is an acronym that stands for **Atomicity, Consistency, Isolation, and Durability**. These four properties are fundamental principles in database management systems (DBMS) that guarantee reliable and accurate processing of database transactions. They ensure data integrity, even in the face of system failures, errors, or concurrent operations.

Here's a breakdown of each property:

1.  **Atomicity ("All or Nothing")**
    * **Concept:** An atomic transaction is treated as a single, indivisible unit of work. This means that either all operations within the transaction complete successfully, or none of them do. There is no "partially completed" transaction.
    * **Example:** Consider transferring money from Account A to Account B. This involves two operations: debiting Account A and crediting Account B. If the debit succeeds but the credit fails (e.g., due to a system crash), atomicity ensures that the entire transaction is rolled back. Account A will not be debited, and Account B will not be credited, leaving the database in its original consistent state.
    * **Benefit:** Prevents partial updates and ensures data consistency by avoiding situations where some changes are applied while others are not.

2.  **Consistency**
    * **Concept:** A transaction must bring the database from one valid, consistent state to another valid, consistent state. This means that all predefined rules, constraints (like data type checks, unique keys, foreign key relationships, etc.), and business logic must be maintained before and after the transaction.
    * **Example:** In a banking system, a consistency rule might be that an account balance cannot go below zero. If a transaction attempts to withdraw more money than is available, the transaction will be aborted to maintain this consistency rule.
    * **Benefit:** Guarantees data integrity and prevents the database from entering an invalid or corrupted state.

3.  **Isolation**
    * **Concept:** Concurrent execution of multiple transactions should appear as if they were executed sequentially. In other words, each transaction operates independently and is unaware of other ongoing transactions until they are committed.
    * **Example:** If two users try to book the last available seat on a flight simultaneously, isolation ensures that only one transaction succeeds in reserving the seat, and the other transaction will either fail or be made aware of the change. Without isolation, both users might think they booked the seat, leading to an overbooked situation.
    * **Benefit:** Prevents anomalies that can arise from concurrent access, such as dirty reads (reading uncommitted data), non-repeatable reads (reading the same data twice and getting different values within a single transaction), and phantom reads (new rows appearing in a result set during a transaction).

4.  **Durability**
    * **Concept:** Once a transaction has been successfully committed, its changes are permanently stored in the database and will survive even in the event of system failures (e.g., power outages, crashes, hardware malfunctions).
    * **Example:** After you complete an online purchase, the order details are saved to the database. Even if the e-commerce server crashes immediately after your purchase is confirmed, durability ensures that your order information is not lost and will be available when the system recovers.
    * **Benefit:** Guarantees that committed data is persistent and recoverable, providing reliability and ensuring that no data is lost after a successful transaction.

In summary, the ACID properties are crucial for building robust and reliable database systems, especially in applications where data accuracy and consistency are paramount, such as financial transactions, healthcare records, and inventory management.