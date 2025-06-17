## IX. Data Definition Language (DDL) in Detail

Data Definition Language (DDL) commands are used to define and manage the structure of a database schema. This includes creating, altering, and deleting database objects such as tables.

**9. Data Definition Language (DDL) in Detail**

* **`CREATE TABLE`:**
    Used to create new tables in the database. You need to specify the table name and define its columns, including their names, data types, and any constraints.

    * **Syntax:**
      ```sql
      CREATE TABLE TableName (
          ColumnName1 DataType1 [Constraint1] [Constraint2] ...,
          ColumnName2 DataType2 [Constraint] ...,
          ...
          [CONSTRAINT ConstraintName PRIMARY KEY (ColumnName(s))],
          [CONSTRAINT ConstraintName FOREIGN KEY (ForeignKeyColumn(s)) REFERENCES ParentTable(PrimaryKeyColumn(s))]
      );
      ```

    * **Example:** Creating an `EMPLOYEE` table with various columns and data types.
      ```sql
      CREATE TABLE EMPLOYEE (
          EMPID CHAR(5) PRIMARY KEY, -- Primary Key constraint defined inline
          ENAME VARCHAR(50) NOT NULL,
          DOJ DATE,
          SAL NUMERIC(10, 2) CHECK (SAL >= 0), -- CHECK constraint defined inline
          DEPTNAME VARCHAR(30) DEFAULT 'Unknown' -- DEFAULT constraint defined inline
      );
      ```

    * **`dbo` Prefix:** In SQL Server, the `dbo` prefix (e.g., `dbo.EMPLOYEE`) stands for "Database Owner" and is the default schema for user-created objects. When you create a table without specifying a schema, it is automatically created under the `dbo` schema.

* **`SP_HELP TableName`:**
    `sp_help` is a system stored procedure in SQL Server that provides detailed information about a database object, such as a table. When you execute `sp_help YourTableName`, it will return a result set describing the table's columns (name, type, length, nullability), constraints (primary key, foreign keys, etc.), and other properties.

    ```sql
    EXEC sp_help EMPLOYEE;
    ```

* **`ALTER TABLE`:**
    Used to modify the structure of an existing table. You can use `ALTER TABLE` to add, drop, or modify columns, as well as add or drop constraints.

    * **`ADD COLUMN`:** Adds one or more new columns to the table. The new column is typically added at the end of the table.
      ```sql
      ALTER TABLE EMPLOYEE
      ADD Email VARCHAR(100);
      ```

    * **`DROP COLUMN`:** Removes one or more existing columns from the table. **Caution: This will also delete any data stored in those columns.**
      ```sql
      ALTER TABLE EMPLOYEE
      DROP COLUMN Email;
      ```

    * **`ALTER COLUMN`:** Modifies the definition of an existing column, such as its data type, length, or nullability. However, you might encounter errors if the existing data is incompatible with the new definition.
      ```sql
      -- Example: Increasing the length of the ENAME column
      ALTER TABLE EMPLOYEE
      ALTER COLUMN ENAME VARCHAR(100);

      -- Example: Setting the DOJ column to NOT NULL (only if there are no NULL values in it)
      ALTER TABLE EMPLOYEE
      ALTER COLUMN DOJ DATE NOT NULL;

      -- Example: Allowing NULL values in the DOJ column
      ALTER TABLE EMPLOYEE
      ALTER COLUMN DOJ DATE NULL;
      ```

    * **`ADD CONSTRAINT`:** Adds a new constraint to the table (e.g., `PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE`, `CHECK`).
      ```sql
      -- Example: Adding a UNIQUE constraint to the ENAME column
      ALTER TABLE EMPLOYEE
      ADD CONSTRAINT UQ_ENAME UNIQUE (ENAME);

      -- Example: Adding a FOREIGN KEY constraint
      ALTER TABLE EMPLOYEE
      ADD CONSTRAINT FK_DEPT
      FOREIGN KEY (DEPTNAME) REFERENCES DEPARTMENT(DEPTNAME);
      ```

    * **`DROP CONSTRAINT`:** Removes an existing constraint from the table. You need to know the name of the constraint to drop it. You can find constraint names using `sp_help TableName`.
      ```sql
      ALTER TABLE EMPLOYEE
      DROP CONSTRAINT UQ_ENAME;

      ALTER TABLE EMPLOYEE
      DROP CONSTRAINT FK_DEPT;
      ```

* **`SP_RENAME`:**
    A system stored procedure used to rename various database objects, including tables and columns.

    * **Renaming a Column:**
      ```sql
      SP_RENAME 'EMPLOYEE.ENAME', 'EmployeeName', 'COLUMN';
      -- Note the 'COLUMN' parameter specifies that you are renaming a column.
      ```

    * **Renaming a Table:**
      ```sql
      SP_RENAME 'EMPLOYEE', 'Employees';
      -- When renaming a table, you typically don't need to specify 'OBJECT' as it's the default.
      ```

* **`DROP TABLE`:**
    Used to remove an entire table and all its data from the database. **This is a permanent operation, and the data cannot be easily recovered.**

    ```sql
    DROP TABLE Employees;
    ```

**Important Note on DDL Commands:** As mentioned in the excerpts, "ANY DDL COMMANDS EXECUTED CANNOT BE UNDONE" in the same way that DML changes within a transaction can be rolled back (unless you have specific database recovery mechanisms in place). Therefore, it's crucial to be careful when executing DDL commands, especially in production environments. Always plan and test schema changes thoroughly.