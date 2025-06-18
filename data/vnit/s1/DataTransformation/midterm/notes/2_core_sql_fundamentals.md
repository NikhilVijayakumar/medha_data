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

Understanding these categories of SQL commands is essential for interacting effectively with relational databases. You'll use DDL to structure your database, DML to manage the data within it, DQL to retrieve information, and TCL to ensure the integrity of your data changes.
