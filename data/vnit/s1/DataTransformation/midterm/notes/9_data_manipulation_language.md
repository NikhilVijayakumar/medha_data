## X. Data Manipulation Language (DML) in Detail

Data Manipulation Language (DML) commands are used to interact with the data stored within the database tables. This includes inserting new records, updating existing records, and deleting records.

**10. Data Manipulation Language (DML) in Detail**

* **`INSERT`:**
    Used to add new rows (records) into a table.

    * **Inserting all columns:** If you are providing values for all columns in the table, you can omit the column list in the `INSERT INTO` clause. However, the order of the values in the `VALUES` clause must exactly match the order of the columns in the table definition.
      ```sql
      -- Assuming the EMPLOYEE table has columns (EMPID, ENAME, DOJ, SAL, DEPTNAME)
      INSERT INTO EMPLOYEE
      VALUES ('E101', 'John Doe', '2025-04-24', 50000.00, 'Sales');
      ```

    * **Inserting specific columns:** It's generally safer and more readable to explicitly specify the columns you are inserting data into. This allows you to insert data into a subset of columns and in any order. Any columns not listed will either take their default value (if defined) or will be NULL if no default is specified and the column allows NULLs.
      ```sql
      INSERT INTO EMPLOYEE (ENAME, EMPID, SAL, DEPTNAME)
      VALUES ('Jane Smith', 'E102', 60000.00, 'Marketing');
      ```

    * **Inserting multiple rows:** You can insert multiple rows with a single `INSERT` statement by separating the value sets with commas.
      ```sql
      INSERT INTO EMPLOYEE (EMPID, ENAME, SAL, DEPTNAME)
      VALUES ('E103', 'Peter Jones', 55000.00, 'Sales'),
             ('E104', 'Mary Brown', 70000.00, 'Finance');
      ```

    * **Important Notes:**
        * "USING INSERT COMMAND WE CAN ONLY ADD NEW ROWS/RECORDS IN A TABLE". It does not modify existing data.
        * "INSERT CMD DOES NOT LOOK FOR DUPLICATE RECORDS/NO VALIDATIONS" by default. You need to define constraints (like `UNIQUE` or `PRIMARY KEY`) on the table to enforce uniqueness or other data integrity rules during insertion.

* **`UPDATE`:**
    Used to modify existing rows in a table. You typically use a `WHERE` clause to specify which rows should be updated. If no `WHERE` clause is provided, all rows in the table will be updated.

    * **Updating specific rows:** The `SET` clause specifies the columns to be updated and their new values.
      ```sql
      -- Example: Updating the salary of the employee with EMPID 'E101'
      UPDATE EMPLOYEE
      SET SAL = 52000.00
      WHERE EMPID = 'E101';

      -- Example: Updating the department and salary of employees in the 'Sales' department
      UPDATE EMPLOYEE
      SET DEPTNAME = 'Sales & Marketing', SAL = SAL * 1.10 -- Increase salary by 10%
      WHERE DEPTNAME = 'Sales';
      ```

    * **Updating all rows (without a `WHERE` clause - use with caution!):**
      ```sql
      -- Example: Increasing the salary of all employees by 5%
      UPDATE EMPLOYEE
      SET SAL = SAL * 1.05;
      ```

* **`DELETE`:**
    Used to remove existing rows from a table. Similar to `UPDATE`, you usually use a `WHERE` clause to specify which rows to delete. If no `WHERE` clause is provided, all rows in the table will be deleted, but the table structure will remain.

    * **Deleting specific rows:**
      ```sql
      -- Example: Deleting the employee with EMPID 'E104'
      DELETE FROM EMPLOYEE
      WHERE EMPID = 'E104';

      -- Example: Deleting all employees in the 'Finance' department
      DELETE FROM EMPLOYEE
      WHERE DEPTNAME = 'Finance';
      ```

    * **Deleting all rows from a table (keeping the table structure):**
      ```sql
      DELETE FROM EMPLOYEE;
      ```

    * **`TRUNCATE TABLE` (Alternative for deleting all rows):** SQL Server also provides the `TRUNCATE TABLE` command, which is a faster and less resource-intensive way to remove all rows from a table. However, it does not log individual row deletions and cannot be used if the table has foreign key constraints referencing it (unless those constraints are dropped first). Also, `TRUNCATE TABLE` resets any identity seed.
      ```sql
      TRUNCATE TABLE EMPLOYEE;
      ```

**Key Differences between `DELETE` and `TRUNCATE TABLE`:**

| Feature         | `DELETE`                      | `TRUNCATE TABLE`            |
|-----------------|-------------------------------|-----------------------------|
| Logging         | Logs each row deletion      | Minimal logging             |
| Transaction Log | Uses transaction log          | Uses less transaction log |
| Rollback        | Can be rolled back (within a transaction) | Cannot be rolled back       |
| Constraints     | Can be used with FKs        | May require dropping FKs  |
| Identity Seed   | Not reset                     | Resets to the initial seed  |
| Performance     | Slower for large tables     | Faster for large tables     |

Understanding these DML commands is fundamental for managing the data within your SQL Server databases. You'll use `INSERT` to add new information, `UPDATE` to keep existing information current, and `DELETE` to remove outdated or incorrect data. Always be cautious with `UPDATE` and `DELETE` statements, especially when not using a `WHERE` clause, as they can have a significant impact on your data. Transactions (as discussed in TCL) are crucial for ensuring data integrity when performing multiple DML operations.