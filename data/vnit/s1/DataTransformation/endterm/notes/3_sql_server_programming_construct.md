## Module 5: Advanced Queries for Large Databases (Continued)

### 4. SQL Server Programming Constructs

**Overview:**
SQL Server provides a rich set of programming constructs that extend the capabilities of standard SQL, allowing for the implementation of complex business logic, automated tasks, and flexible query generation. This section delves into conditional logic, looping mechanisms, dynamic SQL, and event-driven triggers.

---

#### 4.1 Conditional Logic (`IF`/`ELSE` Statements)

Conditional statements enable stored procedures and other SQL blocks to execute different sets of statements based on whether a specified condition is true or false.

* **`IF EXISTS`:**
    * **Purpose:** Checks for the existence of rows that match a specific condition. It's highly efficient when you only need to know if *any* record satisfies a criterion, not how many.
    * **Syntax:**
        ```sql
        IF EXISTS (SELECT * FROM YourTable WHERE YourCondition)
        BEGIN
            -- Statements to execute if records are found
        END
        ELSE
        BEGIN
            -- Statements to execute if no records are found
        END;
        ```
    * **Example (IF_01):**
        ```sql
        -- Procedure IF_01 (assuming @ENO is an input parameter)
        IF EXISTS (SELECT * FROM EMP WHERE EMPNO = @ENO)
            PRINT 'RECORDS FOUND'
        ELSE
            PRINT 'NO RECORDS';
        ```
        * **Explanation:** This snippet efficiently checks if an employee with the provided `EMPNO` (`@ENO`) exists. If at least one row is returned by the subquery, the `IF EXISTS` condition is true.

* **`IF...ELSE` with `COUNT(*)`:**
    * **Purpose:** Provides a general-purpose conditional branch based on a Boolean expression. When checking for record existence, it typically involves first calculating a count (`COUNT(*)`) and then evaluating if that count meets a certain criterion (e.g., `>0` or `=0`).
    * **Syntax:**
        ```sql
        IF (condition)
        BEGIN
            -- Statements to execute if condition is true
        END
        ELSE
        BEGIN
            -- Statements to execute if condition is false
        END;
        ```
    * **Example (IF_02 - Counting Employees in a Department):**
        ```sql
        -- Procedure IF_02 (assuming @DEPTN is an input parameter)
        DECLARE @CNT INT;
        SELECT @CNT = COUNT(*) FROM EMP WHERE DEPTNO = @DEPTN;

        IF @CNT > 0
            PRINT 'RECORDS PRESENT'
        ELSE
            PRINT 'NO RECORDS';
        ```
        * **Explanation:** This code first counts the number of employees in a given department and stores it in `@CNT`. The `IF` statement then checks if `@CNT` is greater than 0 to determine if records are present.

    * **Example (IF_03 - Conditional SELECT):**
        ```sql
        -- Procedure IF_03 (assuming @X is a count, @JOB is input parameter)
        IF @X = 0
            PRINT 'NO RECORDS'
        ELSE
        BEGIN
            PRINT 'RECORDS FOUND';
            SELECT * FROM EMP WHERE JOB = @JOB;
        END;
        ```
        * **Explanation:** This example demonstrates executing a `SELECT` statement only if records are found (i.e., `@X` is not 0), illustrating how conditional logic can control data retrieval.

* **Comparison: `IF EXISTS` vs. `IF...ELSE` with `COUNT(*)`**
    * `IF EXISTS` is generally preferred when you only need to know *if* records exist. It stops scanning as soon as it finds the first matching row, making it very efficient.
    * `IF...ELSE` with `COUNT(*)` is used when you need the actual *count* of records, or for more complex conditions beyond simple existence checks. If only existence is needed, `COUNT(*)` might be less efficient as it has to count all matching rows.

---

#### 4.2 Loops (`WHILE` Condition)

The `WHILE` loop is a control-flow statement that repeatedly executes a block of SQL statements as long as a specified Boolean condition remains true. It's useful for iterating through data, performing iterative calculations, or repetitive tasks.

* **Syntax:**
    ```sql
    WHILE (condition)
    BEGIN
        -- SQL statements to execute repeatedly
        -- Crucial: Include statement(s) to eventually make the condition false
    END;
    ```
* **Basic Iteration:**
    * **Example (WH_01 - Simple Increment):**
        ```sql
        DECLARE @X INT = 1;
        DECLARE @Y INT = 10;
        WHILE @X <= @Y
        BEGIN
            PRINT @X;
            SET @X = @X + 1; -- Increment @X to eventually terminate the loop
        END;
        ```
        * **Explanation:** This loop prints numbers from 1 to 10, incrementing `@X` by 1 in each iteration.

    * **Example (WH_02 - Increment by 2):**
        ```sql
        DECLARE @X INT = 1;
        DECLARE @Y INT = 10;
        WHILE @X <= @Y
        BEGIN
            PRINT @X;
            SET @X = @X + 2; -- Increment @X by 2
        END;
        ```
        * **Explanation:** This loop prints odd numbers (1, 3, 5, 7, 9) up to 10, demonstrating iteration with a custom step size.

* **Data Retrieval in Loops (Row-by-Row Processing):**
    While set-based operations (like `SELECT` with `WHERE`, `JOIN`, `GROUP BY`) are generally preferred in SQL for performance, `WHILE` loops can be used for row-by-row processing in specific scenarios, though often less efficient for large datasets.

    * **Example (WH_03 - Iterating and Displaying Rows):**
        ```sql
        -- Assuming SalesOrder$ table has a [Row ID] column
        -- (Similar to WH_04, but just selecting *)
        DECLARE @X INT = 1;
        DECLARE @Y INT;
        SELECT @Y = MAX([Row ID]) FROM SalesOrder$; -- Get max Row ID to set loop limit

        WHILE @X <= @Y
        BEGIN
            SELECT * FROM SalesOrder$ WHERE [Row ID] = @X;
            SET @X = @X + 1;
        END;
        ```
        * **Explanation:** This loop retrieves and displays each row from `SalesOrder$` table by iterating through `[Row ID]`.

    * **Example (WH_04 - Retrieving Specific Columns and Concatenating):**
        ```sql
        -- Assuming SalesOrder$ table has [Row ID], [ORDER ID], [Customer Name], SALES columns
        DECLARE @X INT = 1;
        DECLARE @Y INT;
        DECLARE @ORDERID NVARCHAR(50), @CUST_NAME NVARCHAR(100), @SLS NUMERIC(10, 2);

        SELECT @Y = MAX([Row ID]) FROM SalesOrder$;

        WHILE @X <= @Y
        BEGIN
            SELECT
                @ORDERID = [ORDER ID],
                @CUST_NAME = [Customer Name],
                @SLS = SALES
            FROM SalesOrder$
            WHERE [Row ID] = @X;

            PRINT CONCAT(@ORDERID, ' : ', @CUST_NAME, ' : ', @SLS);
            SET @X = @X + 1;
        END;
        ```
        * **Explanation:** This demonstrates fetching specific column values into variables within the loop and then using `CONCAT` to format and print them for each row.

* **Important Consideration:**
    * **Performance:** Loops in SQL (especially row-by-row processing) are generally less efficient than set-based operations for large datasets. Always prefer set-based operations (`JOIN`, `UPDATE` with `FROM`, `DELETE` with `WHERE`) over loops when possible. Loops are best reserved for specific tasks that cannot be easily achieved with set-based logic, or for control flow with a small, predefined number of iterations.

---

#### 4.3 Dynamic SQL

Dynamic SQL refers to SQL statements that are constructed as strings and then executed at runtime. This provides immense flexibility, especially when object names (tables, columns) or parts of the query (`WHERE` clause conditions) are not known until the code executes.

* **Constructing SQL String (DYN_01):**
    * **Purpose:** To demonstrate how a SQL query can be built as a string variable.
    * **Example (DYN_01):**
        ```sql
        -- Procedure DYN_01 (assuming @TABLE_NAME is an input parameter)
        DECLARE @SQL1 VARCHAR(200);
        SET @SQL1 = CONCAT('SELECT * FROM ', @TABLE_NAME);
        PRINT @SQL1;
        ```
        * **Explanation:** This example builds a simple `SELECT * FROM [table_name]` query string, where `[table_name]` is dynamically provided. It only prints the string, not executes it.

* **Executing Dynamic SQL (`SP_EXECUTESQL`):**
    * **Purpose:** The standard and recommended way to execute dynamically constructed SQL strings in SQL Server.
    * **Benefits of `SP_EXECUTESQL`:**
        * **Security (SQL Injection Prevention):** Allows for parameterization of queries, which is crucial for preventing SQL injection attacks. Instead of concatenating user input directly into the SQL string, parameters are passed separately.
        * **Performance (Execution Plan Reuse):** SQL Server can cache and reuse execution plans for `SP_EXECUTESQL` queries more effectively when parameters are used, leading to better performance.
        * **Clarity:** Often leads to cleaner code when dealing with complex dynamic queries.
    * **Example (DYN_02 - Basic Execution):**
        ```sql
        -- Procedure DYN_02 (assuming @TABLE_NAME is an input parameter)
        DECLARE @SQL1 NVARCHAR(200); -- Use NVARCHAR for dynamic SQL for Unicode support
        SET @SQL1 = CONCAT('SELECT * FROM ', @TABLE_NAME);
        EXECUTE SP_EXECUTESQL @SQL1;
        ```
        * **Explanation:** This executes the `SELECT *` query constructed dynamically, allowing the database to be queried based on a table name provided at runtime.

    * **Example (DYN_03 - Potential for Output Parameters):**
        ```sql
        -- Procedure DYN_03 (intended for output parameter, incomplete in snippet)
        DECLARE @SQL1 NVARCHAR(200);
        DECLARE @CNT INT; -- Variable to capture output

        SET @SQL1 = CONCAT('SELECT @RecordCount = COUNT(*) FROM ', @TABLE_NAME);

        -- This part needs to be completed for output parameters:
        -- EXECUTE SP_EXECUTESQL @SQL1, N'@RecordCount INT OUTPUT', @RecordCount = @CNT OUTPUT;
        -- PRINT @CNT;
        ```
        * **Explanation:** This snippet hints at `SP_EXECUTESQL`'s ability to handle output parameters, which is essential for capturing results from dynamic queries (e.g., a `COUNT(*)` or an ID generated by an `INSERT`).

* **Security Concerns:**
    * **SQL Injection:** Without proper parameterization (`SP_EXECUTESQL` with parameters), direct concatenation of user input into dynamic SQL strings is highly vulnerable to SQL injection attacks. Always use parameters when executing dynamic SQL based on user-supplied values.
    * **Permissions:** Ensure that the user executing the dynamic SQL has only the necessary permissions on the underlying objects, not excessive privileges that could be exploited.

---

#### 4.4 Triggers

Triggers are a special type of stored procedure that execute automatically (or "fire") in response to specific Data Manipulation Language (DML) events (INSERT, UPDATE, DELETE) on a specified table or view. They are crucial for enforcing complex business rules, maintaining data integrity, and creating audit trails.

* **Key Characteristics:**
    * **Automatic Execution:** Triggers do not need to be explicitly called. They are implicitly executed by the SQL Server engine when their associated DML event occurs on the designated table.
    * **Event-Driven:** Linked to DML events (`FOR INSERT`, `FOR UPDATE`, `FOR DELETE`).
    * **Associated with a Table/View:** Defined for a specific table or view.

* **Special Logical Tables (`inserted` and `deleted`):**
    Within the body of a DML trigger, two special logical (pseudo) tables are available:
    * **`inserted` Table:**
        * Contains the new data rows after an `INSERT` or `UPDATE` operation.
        * For `INSERT` triggers, `inserted` holds the rows that were just added.
        * For `UPDATE` triggers, `inserted` holds the new values of the updated rows.
    * **`deleted` Table:**
        * Contains the old data rows before a `DELETE` or `UPDATE` operation.
        * For `DELETE` triggers, `deleted` holds the rows that were just removed.
        * For `UPDATE` triggers, `deleted` holds the original (old) values of the updated rows.
    * **Purpose:** These tables are vital for:
        * Comparing old and new data during an `UPDATE`.
        * Logging changes (auditing).
        * Enforcing complex business rules that depend on the state of data before or after a modification.

* **Examples of Triggers:**

    * **`FOR UPDATE` Trigger (TRIG_01 - Simple Message):**
        ```sql
        CREATE TRIGGER TRIG_01
        ON EMP
        FOR UPDATE
        AS
        BEGIN
            PRINT 'THIS IS A TRIGGER PROGRAM';
        END;
        GO -- Batch terminator
        ```
        * **Explanation:** This trigger fires every time an `UPDATE` statement is executed on the `EMP` table. It simply prints a message, useful for confirming trigger execution during development.

    * **`FOR DELETE` Trigger with `deleted` Table (TRIG_02 - Viewing Deleted Data):**
        ```sql
        CREATE TRIGGER TRIG_02
        ON EMP
        FOR DELETE
        AS
        BEGIN
            SELECT * FROM deleted; -- Shows the rows that were just deleted
            PRINT 'tRIG_02 EXECUTED';
        END;
        GO
        ```
        * **Explanation:** When rows are deleted from `EMP`, this trigger automatically executes. It selects all columns from the `deleted` pseudo-table, showing exactly which rows were removed. This is useful for debugging or initial auditing.

    * **Auditing with Triggers (Creating `AUDIT_LOG` Table):**
        Before demonstrating auditing, an `AUDIT_LOG` table is typically created to store historical changes.
        ```sql
        CREATE TABLE AUDIT_LOG (
            LogID INT IDENTITY(1,1) PRIMARY KEY,
            EMPNO INT,
            SAL NUMERIC(10, 2),
            ChangeDate DATETIME
        );
        GO
        ```
        * **Explanation:** This table will capture key details (employee number, salary, and the timestamp) of changes made to the `EMP` table.

    * **`FOR INSERT` Trigger for Auditing (TRIG_03 - Logging New Records):**
        ```sql
        CREATE TRIGGER TRIG_03
        ON EMP
        FOR INSERT
        AS
        BEGIN
            INSERT INTO AUDIT_LOG (EMPNO, SAL, ChangeDate)
            SELECT EMPNO, SAL, GETDATE() -- GETDATE() returns current system date/time
            FROM inserted;              -- Data from the newly inserted rows
        END;
        GO
        ```
        * **Explanation:** This trigger fires after an `INSERT` on `EMP`. It takes the `EMPNO` and `SAL` from the `inserted` pseudo-table (which contains the newly added rows) and logs them, along with the current timestamp, into the `AUDIT_LOG` table.

    * **`FOR DELETE` Trigger for Auditing (TRIG_04 - Logging Deleted Records):**
        ```sql
        CREATE TRIGGER TRIG_04
        ON EMP
        FOR DELETE
        AS
        BEGIN
            INSERT INTO AUDIT_LOG (EMPNO, SAL, ChangeDate)
            SELECT EMPNO, SAL, GETDATE()
            FROM deleted;               -- Data from the rows that were deleted
        END;
        GO
        ```
        * **Explanation:** This trigger fires after a `DELETE` on `EMP`. It records the `EMPNO` and `SAL` of the rows that were deleted (from the `deleted` pseudo-table) into the `AUDIT_LOG`, providing a historical record of deletions.

* **Important Considerations:**
    * **Performance:** Triggers execute within the transaction of the DML statement. If a trigger performs complex operations or affects many rows, it can impact the performance of the original DML operation.
    * **Nesting:** Triggers can trigger other triggers (nesting). While this can be powerful, it can also lead to complex debugging issues. SQL Server has a configurable limit for trigger nesting.
    * **Order of Execution:** When multiple triggers exist for the same event on a table, their order of execution might be important and can be managed.
    * **Error Handling:** It's critical to include robust error handling within triggers to prevent them from failing and rolling back the original DML operation.
    * **Alternatives:** While powerful, sometimes simpler constraints (e.g., `CHECK`, `FOREIGN KEY`) or application-level logic are more appropriate than triggers for certain business rules.

---

#### 4.5 User-Defined Functions (UDFs) - Brief Introduction

User-Defined Functions (UDFs) are custom functions created by users to encapsulate reusable logic. Unlike stored procedures, UDFs must return a value and can be used directly within SQL queries (e.g., in `SELECT` lists, `WHERE` clauses, `HAVING` clauses, or as part of expressions).

* **Types Mentioned:**
    * **Inline Table-Valued Functions (iTVFs):** Return a table data type. They are essentially parameterized views and are often highly optimized for performance as SQL Server can inline their definition into the calling query's execution plan.
    * **Multi-Statement Table-Valued Functions (mTVFs):** Also return a table data type, but they can contain multiple T-SQL statements and more complex logic within their body. They are generally less performant than iTVFs.
    * **Scalar Functions:** Return a single data value (e.g., `INT`, `VARCHAR`).

* **Note:** While your notes mention these types, concrete examples were not provided in the source material. These will be elaborated upon if further notes on UDFs become available.

---

This covers the programming constructs section thoroughly. Please share your next set of notes when you are ready!