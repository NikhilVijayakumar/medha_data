## Module 5: Advanced Queries for Large Databases (Continued)

### 5. User-Defined Functions (UDFs)

**Overview:**
User-Defined Functions (UDFs) are custom routines created by users to encapsulate specific logic or computations. They extend the functionality of SQL, promoting code reusability, modularity, and readability. UDFs are distinct from stored procedures primarily because they must return a value and can be used directly within SQL queries (e.g., in `SELECT` lists, `WHERE` clauses, or as part of expressions).

---

#### 5.1 Scalar Functions

**Definition:** A scalar function accepts parameters, performs an action (often a calculation or manipulation), and then returns a single, scalar data value (e.g., a number, string, or date).

* **Syntax for Creation:**
    ```sql
    CREATE FUNCTION FunctionName (@Parameter1 DataType, @Parameter2 DataType, ...)
    RETURNS ReturnDataType
    AS
    BEGIN
        -- Variable declarations
        DECLARE @LocalVariable DataType;

        -- SQL statements/logic
        SET @LocalVariable = @Parameter1 + SomeCalculation;

        -- Must return a single value
        RETURN @LocalVariable;
    END;
    GO -- Batch terminator
    ```
    * **Parameter Passing:** Parameters are declared within parentheses after the function name, similar to stored procedures, with their data types. They are used as input values within the function's logic.
    * **Variable Declaration:** Local variables, prefixed with `@`, are declared using `DECLARE` and assigned values using `SET`.
    * **`RETURNS` Clause:** Specifies the data type of the single value that the function will return.
    * **`RETURN` Statement:** Used to exit the function and provide the final scalar value.

* **Examples:**

    * **Basic Arithmetic (`FUN_01`, `FUN_02`):**
        ```sql
        -- FUN_01: Adds 100 to an input integer
        CREATE FUNCTION FUN_01(@X INT)
        RETURNS NUMERIC(10, 2)
        AS
        BEGIN
            DECLARE @Z NUMERIC(10, 2);
            SET @Z = @X + 100;
            RETURN @Z;
        END;
        GO

        -- FUN_02: Returns the input value (demonstrates basic structure)
        CREATE FUNCTION FUN_02(@X NUMERIC(10,2))
        RETURNS NUMERIC(10,2)
        AS
        BEGIN
            RETURN @X;
        END;
        GO
        ```
        * **Application with Table Columns:**
            ```sql
            SELECT SAL, DBO.FUN_02(SAL) AS OriginalSalary, DBO.FUN_01(SAL) AS SalaryPlus100
            FROM EMP;
            ```
            * **Explanation:** Scalar functions can be applied row-by-row to columns within a `SELECT` statement, transforming data for display or further calculation.

    * **Conditional Logic (`CHECK_POS_NEG_ZERO`):**
        ```sql
        CREATE FUNCTION CHECK_POS_NEG_ZERO(@Z INT)
        RETURNS VARCHAR(30)
        AS
        BEGIN
            DECLARE @X VARCHAR(50);
            IF @Z > 0
                SET @X = 'POS';
            ELSE IF @Z < 0
                SET @X = 'NEG';
            ELSE
                SET @X = 'ZERO';
            RETURN @X;
        END;
        GO
        ```
        * **Use Case:** Applied to `PROFIT` from `SalesOrder` or `SAL` from `EMP` to categorise values:
            ```sql
            SELECT PROFIT, DBO.CHECK_POS_NEG_ZERO(PROFIT) AS ProfitCategory
            FROM SalesOrder;
            ```
            * **Explanation:** Demonstrates embedding `IF...ELSE IF...ELSE` logic within a function to return a descriptive string based on numeric input.

    * **String Manipulation (`COUNT_WORDS`, `GETFIRSTNAME`):**
        ```sql
        -- COUNT_WORDS: Counts words in a string (simple heuristic)
        CREATE FUNCTION COUNT_WORDS(@X VARCHAR(200))
        RETURNS INT
        AS
        BEGIN
            RETURN(LEN(@X) - LEN(REPLACE(@X, ' ', '')) + 1);
        END;
        GO

        -- GETFIRSTNAME: Extracts the first name from a string
        CREATE FUNCTION GETFIRSTNAME(@X VARCHAR(200))
        RETURNS VARCHAR(200)
        AS
        BEGIN
            RETURN LEFT(@X, CHARINDEX(' ', @X, 1) -1); -- Subtract 1 to exclude the space
        END;
        GO
        ```
        * **Use Case:** Applied to `[CUSTOMER NAME]` from `SalesOrder`:
            ```sql
            SELECT [CUSTOMER NAME],
                   DBO.COUNT_WORDS([CUSTOMER NAME]) AS WordCount,
                   DBO.GETFIRSTNAME([CUSTOMER NAME]) AS CustomerFirstName
            FROM SalesOrder;
            ```
            * **Explanation:** `COUNT_WORDS` calculates words by counting spaces and adding one. `GETFIRSTNAME` uses `LEFT` and `CHARINDEX` to find the first word, illustrating practical text parsing within a UDF.

    * **Date/Time Manipulation (`GETAGE`):**
        ```sql
        CREATE FUNCTION GETAGE(@X DATE)
        RETURNS INT
        AS
        BEGIN
            RETURN DATEDIFF(YEAR, @X, GETDATE());
        END;
        GO
        ```
        * **Use Case:**
            ```sql
            SELECT DBO.GETAGE('1995-01-01') AS AgeInYears;
            ```
            * **Explanation:** Uses `DATEDIFF` to calculate the difference in years between a provided date of birth (`@X`) and the current system date (`GETDATE()`).

* **Invocation:** Scalar functions are invoked in `SELECT` statements by prefixing the function name with the schema name (e.g., `DBO.FUN_01(50)`). This is a best practice to ensure proper function resolution.

* **Considerations:** While powerful, excessive use of scalar UDFs in complex queries, especially if they perform data access, can sometimes lead to performance issues due to iterative execution per row and context switching.

---

#### 5.2 Table-Valued Functions (TVFs)

**Definition:** A table-valued function returns a result set in the form of a table. This returned table can then be used in the `FROM` clause of a `SELECT` statement, much like a regular table or view.

* **Types of TVFs:**

    * **5.2.1 Inline Table-Valued Functions (iTVFs)**
        * **Definition:** These are the simplest form of TVFs. They do not have a `BEGIN...END` block and directly return the result of a single `SELECT` statement. They are essentially parameterized views.
        * **Syntax:**
            ```sql
            CREATE FUNCTION FunctionName (@Parameter1 DataType, ...)
            RETURNS TABLE
            AS
            RETURN
            (
                SELECT Column1, Column2
                FROM YourTable
                WHERE YourCondition;
            );
            GO
            ```
        * **Characteristics:**
            * No `BEGIN...END` block.
            * Return statement points directly to a `SELECT` query.
            * Often provide **significant performance benefits** as SQL Server can "inline" their definition into the calling query's execution plan, treating them similarly to views.
        * **Examples:**
            ```sql
            -- GETEMPDATA: Returns all data from EMP table
            CREATE FUNCTION GETEMPDATA()
            RETURNS TABLE
            RETURN (SELECT * FROM EMP);
            GO

            -- GETEMPDATA_SPEC_DEPT: Returns employees for a specific department
            CREATE FUNCTION GETEMPDATA_SPEC_DEPT(@X INT)
            RETURNS TABLE
            RETURN (SELECT * FROM EMP WHERE DEPTNO = @X);
            GO

            -- GET_TOP: Returns top N employees from EMP
            CREATE FUNCTION GET_TOP(@X INT)
            RETURNS TABLE
            RETURN (SELECT TOP (@X) * FROM EMP ORDER BY EMPNO); -- Added ORDER BY for consistent TOP results
            GO
            ```
        * **Invocation:**
            ```sql
            SELECT * FROM DBO.GETEMPDATA();
            SELECT * FROM DBO.GETEMPDATA_SPEC_DEPT(20);
            SELECT * FROM DBO.GET_TOP(5);
            ```
            * **Explanation:** They are used in the `FROM` clause like a table, optionally with parameters.

    * **5.2.2 Multi-Statement Table-Valued Functions (mTVFs)**
        * **Definition:** These TVFs allow for more complex logic within their body. They include a `BEGIN...END` block, require an explicit declaration of a table variable as their return type, and populate this table variable using `INSERT` statements (or other DML).
        * **Syntax:**
            ```sql
            CREATE FUNCTION FunctionName (@Parameter1 DataType, ...)
            RETURNS @TableName TABLE (
                Column1 DataType,
                Column2 DataType,
                -- ... define schema of the returned table
            )
            AS
            BEGIN
                -- Multiple SQL statements and logic
                INSERT INTO @TableName (Column1, Column2)
                SELECT DataCol1, DataCol2 FROM AnotherTable WHERE SomeCondition;

                -- More logic, e.g., updates to @TableName, loops, conditionals

                RETURN; -- No value specified, just signals end of function
            END;
            GO
            ```
        * **Characteristics:**
            * Uses `BEGIN...END` block.
            * Requires explicit declaration of a table variable in the `RETURNS` clause, defining the schema of the table to be returned.
            * Data is populated into the declared table variable using `INSERT` statements.
            * Can contain multiple statements, loops, conditional logic, and other complex operations.
            * Generally **less performant** than iTVFs because the optimizer cannot always inline their logic as effectively; they materialize the intermediate results into the table variable.
        * **Examples:**
            ```sql
            -- GET_EMP_DATA_01: Populates and returns EMPNO and ENAME
            CREATE FUNCTION GET_EMP_DATA_01()
            RETURNS @X TABLE(COL1 INT, COL2 VARCHAR(50))
            AS
            BEGIN
                INSERT INTO @X (COL1, COL2)
                SELECT EMPNO, ENAME FROM EMP;
                RETURN;
            END;
            GO

            -- GET_EMP_DATA_SPEC_DEPTNO: Filters and returns specific employee data
            CREATE FUNCTION GET_EMP_DATA_SPEC_DEPTNO(@Z INT)
            RETURNS @X TABLE(ENO INT, NAM VARCHAR(50), SL INT, DEP INT)
            AS
            BEGIN
                INSERT INTO @X (ENO, NAM, SL, DEP)
                SELECT EMPNO, ENAME, SAL, DEPTNO
                FROM EMP
                WHERE DEPTNO = @Z;
                RETURN;
            END;
            GO
            ```
        * **Invocation:**
            ```sql
            SELECT * FROM DBO.GET_EMP_DATA_01();
            SELECT * FROM DBO.GET_EMP_DATA_SPEC_DEPTNO(20);
            ```
        * **Use Cases:** Preferred over inline TVFs when:
            * The logic to build the result set is complex and requires multiple SQL statements.
            * Intermediate data manipulation or temporary storage is needed.
            * Error handling or other procedural logic is required within the function.

---

#### 5.3 General UDF Concepts & Management

* **`GO` Command:** Not a Transact-SQL statement itself, but a batch terminator used by SQL Server utilities (like SSMS). It signals the end of a batch of T-SQL statements, telling the server to compile and execute the preceding code. This is crucial when creating objects like functions, procedures, or triggers, as they often need to be the only statement in a batch or executed after previous DDL.
* **`DBO` Schema:** Functions (and other database objects) are often prefixed with `DBO.` (Database Owner) when called. This refers to the default schema for objects created by users who are members of the `db_owner` fixed database role. It's good practice to always specify the schema to avoid ambiguity and ensure correct object resolution.
* **Function Alteration/Renaming:**
    * **`ALTER FUNCTION`:** Used to modify an existing function's definition without dropping and recreating it. This preserves permissions and dependencies. (Implied, though not directly shown in syntax).
    * **`SP_RENAME`:** A system stored procedure used to change the name of a user-defined object in the current database, including functions.
        ```sql
        EXEC sp_rename 'DBO.OLD_FUN_NAME', 'NEW_FUN_NAME';
        ```
        * **Caution:** Renaming objects, especially those with dependencies, requires careful consideration. `sp_rename` only renames the object; it does not update references to that object in other queries, views, or stored procedures.

---

### 6. Indexing

**Overview:**
Indexing is a critical performance optimization technique in relational databases. An index is a database object that provides a fast way to look up data in a table based on the values in one or more columns, much like an index in a book.

---

#### 6.1 Purpose of Indexes

* **Faster Data Retrieval:** The primary purpose of an index is to significantly speed up data retrieval operations (e.g., `SELECT` statements, especially those with `WHERE`, `JOIN`, or `ORDER BY` clauses) by providing a quick lookup mechanism.
* **Reduced I/O Operations:** By pointing directly to the data's physical location, indexes minimize the amount of data that needs to be read from disk, thus reducing costly input/output (I/O) operations.
* **Improved Query Performance:** Overall, indexes are crucial for optimizing complex queries, joins, and sorting operations on large datasets.

* **`SET STATISTICS IO ON`:**
    * **Purpose:** This T-SQL command is invaluable for performance tuning. When enabled, it displays detailed information about the number of logical and physical reads performed by a query in the messages tab of query tools like SSMS.
    * **Usefulness:** By comparing the I/O statistics of a query before and after creating an index, developers can empirically demonstrate the performance benefits of indexing. Reduced logical/physical reads indicate more efficient data access.

* **Conceptual Index Structure:**
    An index conceptually creates a sorted list of indexed column values (the "key") along with pointers (addresses) to the actual data rows where those values are stored.
    ```
    -- Conceptual Index Table Structure:
    -- IndexKey | DataAddress1 | DataAddress2 | ...
    -- 10       | ADD1         | ADDR2        | ADDR3
    -- 20       | ADD4         | ADD5         | ADD6
    -- 30       | ADD7         | ADDR8        | ADD9
    ```
    * **Explanation:** When a query searches for `IndexKey = 20`, the database quickly finds `20` in the sorted index and then uses the associated addresses (`ADD4`, `ADD5`, `ADD6`) to directly retrieve the relevant data rows, bypassing a full table scan.

#### 6.2 Types of Indexes

* **6.2.1 Clustered Index**
    * **Definition:** A clustered index determines the **physical storage order** of the data rows in a table or view based on its key values. The data rows themselves are stored in the same order as the index.
    * **Uniqueness:** A table can have **only one clustered index**. This is because the data can only be physically sorted in one way on disk.
    * **Syntax:**
        ```sql
        CREATE CLUSTERED INDEX IndexName ON TableName(ColumnName [ASC/DESC]);
        ```
    * **Application/Suitability:**
        * Typically applied on `PRIMARY KEY` columns because primary keys inherently enforce uniqueness and are frequently used for lookups and joins, making them ideal for physical ordering.
        * Best for columns that are:
            * Unique or have very few duplicates.
            * Accessed frequently for range scans (e.g., `WHERE DateColumn BETWEEN 'X' AND 'Y'`).
            * Used in `ORDER BY` clauses.
        * **Example:**
            ```sql
            CREATE CLUSTERED INDEX INDX_03 ON EMP(EMPNO);
            ```
            * **Explanation:** This would physically sort the `EMP` table's data rows by `EMPNO`.

* **6.2.2 Non-Clustered Index**
    * **Definition:** A non-clustered index does **not affect the physical order** of data rows. Instead, it creates a separate, independent structure (a B-tree) that contains the indexed key values and "row locators" (pointers) to the actual data rows in the table.
    * **Multiplicity:** A table can have **multiple non-clustered indexes** (up to 999 in SQL Server).
    * **Syntax:**
        ```sql
        CREATE NONCLUSTERED INDEX IndexName ON TableName(ColumnName [ASC/DESC]);
        ```
    * **Application/Suitability:**
        * Applied on columns that are frequently used in `WHERE` clauses, `JOIN` conditions, or `ORDER BY` clauses but are not suitable for the clustered index.
        * Good for columns with high selectivity (many distinct values).
        * Can be used to cover queries (see "Covering Queries" in Module 5 Overview), where all columns needed by the query are present in the index itself, avoiding a lookup to the actual data.
        * **Example:**
            ```sql
            CREATE NONCLUSTERED INDEX INDX_02 ON EMP(DEPTNO);
            ```
            * **Explanation:** This creates a separate index structure sorted by `DEPTNO`. When a query filters by `DEPTNO`, the database uses this index to quickly find the pointers to the relevant data rows, without disturbing the physical order of the `EMP` table.

---

#### 6.3 Viewing Indexes

SQL Server provides system catalog views that allow users to inspect metadata about existing database objects, including indexes and tables. This is invaluable for database administration, auditing, and performance tuning.

* **`SYS.indexes`:** This system view provides information about all indexes in the database.
* **`SYS.tables`:** This system view provides information about all tables in the database.

* **Querying for Index Information:**
    ```sql
    SELECT
        T.name AS TableName,
        I.name AS IndexName,
        I.type_desc AS IndexType, -- e.g., 'CLUSTERED', 'NONCLUSTERED'
        I.is_unique,
        I.has_filter,
        I.fill_factor
    FROM
        SYS.indexes I
    INNER JOIN
        SYS.tables T ON I.object_id = T.object_id
    WHERE
        I.object_id = OBJECT_ID('EMP'); -- Use OBJECT_ID to get object_id dynamically for a table name
    -- Alternatively, if you know the object_id:
    -- WHERE I.object_id = 66099276;
    ```
    * **Explanation:** This query joins `SYS.indexes` and `SYS.tables` on their shared `object_id` to link indexes to their respective tables. It provides detailed information such as the index name, its type (clustered or non-clustered), and other properties. Using `OBJECT_ID('TableName')` is more robust than hardcoding `object_id` values.

* **Listing All Tables:**
    ```sql
    SELECT * FROM SYS.tables;
    ```
    * **Explanation:** This simple query lists all tables within the current database, showing their names, `object_id`, `schema_id`, and other metadata.

---

This completes the documentation for UDFs and Indexing. Let me know when you're ready for the next set of notes!