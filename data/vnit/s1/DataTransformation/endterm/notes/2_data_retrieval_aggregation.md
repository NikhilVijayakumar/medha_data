## Module 4: Querying Databases Using Joins, Tables, and Variables (Continued)

### 2. Operators & Queries: Data Retrieval and Aggregation

**Overview:**
Efficient data retrieval and aggregation are fundamental skills in SQL. This section covers various techniques to extract meaningful insights from raw data, specifically focusing on identifying key dates and using subqueries for targeted filtering.

---

#### 2.1 Identifying First and Latest Order Dates by Customer

Retrieving the earliest and latest occurrences of an event (like an order) for each entity (like a customer) is a common analytical task. SQL offers highly efficient ways to achieve this.

**Method 1: Using Aggregate Functions (`MIN()`, `MAX()`) with `GROUP BY`**

This is the most straightforward and **highly efficient** method for aggregation. It groups rows that have the same value in a specified column (e.g., `[CUSTOMER NAME]`) and then applies an aggregate function to each group.

* **Retrieving First Order Date:**
    ```sql
    SELECT
        [CUSTOMER NAME],
        MIN([ORDER DATE]) AS FIRST_ORDER_PLACED
    FROM
        SalesOrder
    GROUP BY
        [CUSTOMER NAME]
    ORDER BY
        [CUSTOMER NAME];
    ```
    * **Explanation:** This query groups all sales orders by customer name. For each customer group, it finds the minimum (earliest) `[ORDER DATE]`, labeling it `FIRST_ORDER_PLACED`. The results are then ordered by customer name for readability.

* **Retrieving Latest Order Date:**
    ```sql
    SELECT
        [CUSTOMER NAME],
        MAX([ORDER DATE]) AS LASTEST_ORDER_PLACED
    FROM
        SalesOrder
    GROUP BY
        [CUSTOMER NAME]
    ORDER BY
        [CUSTOMER NAME];
    ```
    * **Explanation:** Similar to finding the first order, this query uses `MAX()` to find the maximum (latest) `[ORDER DATE]` for each customer group, labeled `LASTEST_ORDER_PLACED`.

**Method 2: Using Correlated Subqueries (Less Efficient for Aggregation)**

While powerful for certain scenarios, using correlated subqueries for simple aggregations like `MIN` or `MAX` across groups is generally **less efficient** than `GROUP BY` with aggregate functions, especially on large datasets. This is because the subquery executes once for *each row* of the outer query. However, it serves as a good example of how correlated subqueries function.

* **Retrieving First Order Date using Correlated Subquery:**
    ```sql
    SELECT DISTINCT
        B.[CUSTOMER NAME],
        (SELECT MIN(A.[Order Date])
         FROM SalesOrder A
         WHERE A.[Customer ID] = B.[CUSTOMER ID]) AS FIRST_ORDER_ID
    FROM
        SalesOrder B
    ORDER BY
        [Customer Name];
    ```
    * **Explanation:** For each distinct `[CUSTOMER NAME]` in the outer query (`B`), the subquery looks up the minimum `[Order Date]` from `SalesOrder A` *only for that specific customer's ID*. This demonstrates how the inner query depends on the outer query's current row value.

* **Retrieving Latest Order Date using Correlated Subquery:**
    ```sql
    SELECT DISTINCT
        B.[CUSTOMER NAME],
        (SELECT MAX(A.[Order Date]) AS LATEST_ORDER_ID
         FROM SalesOrder A
         WHERE A.[Customer ID] = B.[CUSTOMER ID]) AS LATEST_ORDER_ID
    FROM
        SalesOrder B
    ORDER BY
        [Customer Name];
    ```
    * **Explanation:** Similar to the `MIN` example, this correlated subquery retrieves the maximum `[Order Date]` for each customer from the outer query.

---

### 3. Subqueries (Continued)

**Overview:**
Subqueries (or inner queries) are queries nested inside another SQL query. They are used to return data that will be used by the outer query. They can be classified based on the number of rows they return (single-row, multi-row) and their dependency on the outer query (correlated).

#### 3.1 Nested Subqueries

A nested subquery is an inner `SELECT` statement that executes first and passes its result to the outer query for further processing. They are commonly used in `WHERE`, `HAVING`, or `FROM` clauses.

* **Filtering Employees by Department:**
    ```sql
    SELECT *
    FROM EMP
    WHERE DEPTNO IN (SELECT DEPTNO FROM EMP WHERE ENAME IN ('SCOTT'));
    ```
    * **Explanation:** This query demonstrates a multi-row, non-correlated subquery.
        1.  The inner subquery `(SELECT DEPTNO FROM EMP WHERE ENAME IN ('SCOTT'))` first identifies the `DEPTNO`(s) associated with the employee 'SCOTT'.
        2.  The outer query then uses the `IN` operator to retrieve all records from the `EMP` table where the `DEPTNO` matches any of the department numbers returned by the subquery. This effectively finds all employees in the same department(s) as 'SCOTT'.

* **Additional Point: Subqueries in `FROM` Clause (Derived Tables/Inline Views)**
    Subqueries can also be used in the `FROM` clause. The result set of such a subquery is treated as a temporary, inline table, often called a "derived table" or "inline view."

    * **Example:**
        ```sql
        SELECT
            d.DeptName,
            e.EmployeeCount
        FROM
            Departments d
        JOIN
            (SELECT DEPTNO, COUNT(*) AS EmployeeCount FROM EMP GROUP BY DEPTNO) e
        ON d.DeptNo = e.DEPTNO;
        ```
    * **Explanation:** This example first calculates the `EmployeeCount` per department in the subquery (the derived table `e`) and then joins this result with the `Departments` table. This is very useful for pre-aggregating data before joining or for complex filtering.

---

## Module 5: Advanced Queries for Large Databases

### 2. Stored Procedures

**Overview:**
Stored procedures are powerful, pre-compiled blocks of one or more SQL statements or a set of instructions designed to perform a specific task. They are stored within the database and can be executed multiple times, offering significant benefits in terms of reusability, performance, and security.

---

#### 2.1 Definition and Purpose

* **Definition:** A stored procedure is a program that contains a set of SQL statements and logic (e.g., control flow, variable declarations) designed to perform a specific task. It's akin to a function or subroutine in other programming languages.
* **Purpose:**
    * **Reusability:** Write once, use many times. Avoids redundant coding of complex logic.
    * **Performance:** Stored procedures are typically compiled and optimized when first created or executed, leading to faster execution times for subsequent calls compared to repeatedly sending raw SQL queries.
    * **Security:** Users can be granted permissions to execute a stored procedure without needing direct permissions on the underlying tables. This enhances security and restricts access to sensitive data or operations.
    * **Reduced Network Traffic:** Instead of sending multiple SQL statements over the network, only the stored procedure name and its parameters are sent.
    * **Maintainability:** Centralized logic makes it easier to update and maintain business rules.

#### 2.2 Syntax for Creation

The basic syntax for creating a stored procedure is as follows:

```sql
CREATE PROCEDURE ProcedureName
AS
BEGIN
    -- SQL Statement(s) or block of instructions
    STATEMENT1;
    STATEMENT2;
    -- ...
END;
```
* **`CREATE PROCEDURE`**: The command to create a new stored procedure.
* **`ProcedureName`**: A unique name for your stored procedure.
* **`AS BEGIN ... END`**: Defines the body of the stored procedure, containing the SQL statements to be executed.

#### 2.3 Examples of Stored Procedures

* **Retrieving All Employee Records (Basic):**
    ```sql
    CREATE PROCEDURE GetAllEmpRecords
    AS
    BEGIN
        SELECT * FROM EMP;
    END;
    ```
    * **Execution:**
        ```sql
        EXEC GetAllEmpRecords;
        ```
    * **Explanation:** This simple procedure encapsulates a `SELECT` statement, making it reusable to fetch all employee data with a single command.

* **Retrieving Records from Multiple Tables:**
    ```sql
    CREATE PROCEDURE GetAllRecords
    AS
    BEGIN
        SELECT * FROM EMP;
        SELECT * FROM SalesOrder;
        SELECT * FROM Returns;
    END;
    ```
    * **Execution:**
        ```sql
        EXEC GetAllRecords;
        ```
    * **Explanation:** Stored procedures can contain multiple SQL statements, returning multiple result sets to the calling application.

* **Performing Calculations and Using Variables:**
    Stored procedures support variable declaration and basic programming constructs.
    ```sql
    CREATE PROCEDURE ADD_NUM
    AS
    BEGIN
        DECLARE @X INT, @Y INT; -- Declare integer variables
        SET @X = 10;            -- Assign values to variables
        SET @Y = 30;
        PRINT @X + @Y;          -- Print the sum
    END;
    ```
    * **Execution:**
        ```sql
        EXEC ADD_NUM; -- This would output '40'
        ```
    * **Explanation:** This demonstrates how to declare variables (`DECLARE`), assign values (`SET`), and perform arithmetic operations within a stored procedure. `PRINT` is used for outputting messages (useful for debugging or simple results).

#### 2.4 Parameterized Stored Procedures

A key feature of stored procedures is their ability to accept input parameters, making them highly flexible and dynamic.

* **Adding Two Numbers with Parameters:**
    ```sql
    CREATE PROCEDURE ADD_NUM_01 (@X INT, @Y INT)
    AS
    BEGIN
        PRINT @X + @Y;
    END;
    ```
    * **Execution:**
        ```sql
        EXEC ADD_NUM_01 20, 30; -- This would print '50'
        ```
    * **Explanation:** Parameters (`@X INT`, `@Y INT`) are defined in the `CREATE PROCEDURE` statement. When executing, values are passed for these parameters, which are then used within the procedure's logic.

* **Filtering Employee Records by Department Number:**
    ```sql
    CREATE PROCEDURE PR_01 (@DEPTNO INT)
    AS
    BEGIN
        SELECT * FROM EMP WHERE DEPTNO = @DEPTNO;
    END;
    ```
    * **Execution:**
        ```sql
        EXEC PR_01 20; -- Retrieves all employees from department 20
        ```
    * **Explanation:** This procedure takes a department number as input and returns only the employees belonging to that department, demonstrating how parameters can control query results.

#### 2.5 Modifying and Deleting Stored Procedures

* **Modifying (`ALTER PROCEDURE`):**
    To change an existing stored procedure's definition, use `ALTER PROCEDURE`. This is preferred over `DROP` and `CREATE` as it preserves existing permissions and dependencies.
    ```sql
    ALTER PROCEDURE PR_02 (@ENAME VARCHAR(20))
    AS
    BEGIN
        SELECT * FROM EMP WHERE ENAME = @ENAME;
    END;
    ```
    * **Execution (after alteration):**
        ```sql
        EXEC PR_02 'SCOTT'; -- Retrieves employee 'SCOTT'
        ```
    * **Explanation:** This demonstrates changing the `PR_02` procedure to accept an employee name parameter instead of a department number.

* **Deleting (`DROP PROCEDURE`):**
    To permanently remove a stored procedure from the database, use `DROP PROCEDURE`.
    ```sql
    DROP PROCEDURE GetAllEmpRecords;
    ```
    * **Explanation:** This command removes the specified stored procedure. Be cautious as this action is irreversible.

---

### 3. Other Advanced Concepts (Brief Introduction)

The following concepts are crucial for developing robust and high-performing database solutions and are typically covered in advanced SQL curricula. They are often used in conjunction with stored procedures and functions.

* **Error Handling:** Mechanisms (e.g., `TRY...CATCH` blocks in T-SQL) to manage and respond to errors during SQL execution, preventing application crashes and ensuring data integrity. (Covered in Module 5 Overview)
* **Triggers:** Special stored procedures that automatically execute (or "fire") in response to certain events on a table (e.g., `INSERT`, `UPDATE`, `DELETE`).
* **User-Defined Functions (UDFs):** Custom functions created by users to encapsulate reusable logic. Unlike stored procedures, UDFs can be used directly within SQL queries (e.g., in `SELECT` lists, `WHERE` clauses) and must return a value. (Covered in Module 5 Overview)
    * **Scalar Functions:** Return a single data value.
    * **Inline Table-Valued Functions (iTVFs):** Return a table data type. They are often highly optimized.
    * **Multi-Statement Table-Valued Functions (mTVFs):** Also return a table, but allow for more complex logic inside the function body.
* **Indexes:** Database objects that improve the speed of data retrieval operations on a database table. They work much like an index in a book. (Covered in Module 3 and Module 5 Overviews)

---

**Next Steps:**

I've integrated the notes on data retrieval, subqueries, and stored procedures. Please share your next set of notes when you're ready, and I'll continue building out the documentation!