## V. Sorting and Limiting Results

After retrieving data using the `SELECT` statement, you often need to sort the results in a specific order or limit the number of rows returned. SQL provides the `ORDER BY` and `LIMIT` (though syntax can vary) clauses for these purposes, as well as `DISTINCT` to retrieve unique values.

**5. Sorting and Limiting Results**

* **`ORDER BY` Clause:**

    The `ORDER BY` clause is used to sort the rows in the result set based on one or more columns. You can specify whether to sort in ascending (A-Z, 1-9) or descending (Z-A, 9-1) order.

    ```sql
    SELECT column1, column2
    FROM TableName
    WHERE condition
    ORDER BY column_to_sort ASC | DESC;
    ```

    * `ORDER BY column_to_sort`: Specifies the column by which to sort the results.
    * `ASC`: Sorts in ascending order (default if not specified).
    * `DESC`: Sorts in descending order.

    ```sql
    -- Example: Selecting all columns from 'SalesOrder' and sorting the results by 'PROFIT' in descending order (highest profit first)
    SELECT *
    FROM SalesOrder
    ORDER BY PROFIT DESC;

    -- Example: Selecting 'CUSTOMER NAME' and 'SALES' and sorting first by 'REGION' (ascending) and then by 'SALES' (descending) within each region
    SELECT [CUSTOMER NAME], REGION, SALES
    FROM SalesOrder
    ORDER BY REGION ASC, SALES DESC;

    -- The ORDER BY clause is typically placed after the WHERE clause (if used).
    SELECT *
    FROM SalesOrder
    WHERE REGION = 'CENTRAL'
    ORDER BY SALES ASC;
    ```

* **`LIMIT` Clause (Syntax Variation):**

    The `LIMIT` clause is used to restrict the number of rows returned by a query. The syntax for `LIMIT` can vary significantly across different SQL dialects.

    * **MySQL, PostgreSQL, SQLite:**

        ```sql
        SELECT column1, column2
        FROM TableName
        LIMIT number_of_rows;

        -- To specify an offset (start from a certain row):
        SELECT column1, column2
        FROM TableName
        LIMIT number_of_rows OFFSET starting_row_number;
        ```

        ```sql
        -- Example (MySQL/PostgreSQL/SQLite): Selecting the top 5 most profitable orders
        SELECT *
        FROM SalesOrder
        ORDER BY PROFIT DESC
        LIMIT 5;

        -- Example (MySQL/PostgreSQL/SQLite): Selecting 5 orders starting from the 6th row (offset 5)
        SELECT *
        FROM SalesOrder
        ORDER BY [ORDER ID] ASC
        LIMIT 5 OFFSET 5;
        ```

    * **SQL Server (using `TOP`):** SQL Server uses the `TOP` keyword to limit the number of rows.

        ```sql
        SELECT TOP (number_of_rows) column1, column2
        FROM TableName
        ORDER BY column_to_sort;

        -- You can also use WITH TIES to include rows that have the same value in the ORDER BY column as the last row returned.
        SELECT TOP (number_of_rows) WITH TIES column1, column2
        FROM TableName
        ORDER BY column_to_sort;
        ```

        ```sql
        -- Example (SQL Server): Selecting the top 5 most profitable orders
        SELECT TOP (5) *
        FROM SalesOrder
        ORDER BY PROFIT DESC;

        -- Example (SQL Server): Selecting the top 3 products by sales, including ties
        SELECT TOP (3) WITH TIES [PRODUCT NAME], SALES
        FROM SalesOrder
        ORDER BY SALES DESC;
        ```

* **`DISTINCT` Clause:**

    The `DISTINCT` clause is used to retrieve only unique rows from the result set, eliminating duplicate values in the specified column(s).

    ```sql
    SELECT DISTINCT column1, column2, ...
    FROM TableName
    WHERE condition
    ORDER BY column;
    ```

    * `DISTINCT` applies to all the columns listed in the `SELECT` statement. If you select multiple columns, a row is considered distinct only if the combination of values in all those columns is unique.

    ```sql
    -- Example: Selecting all the unique cities from the 'Customers' table
    SELECT DISTINCT City
    FROM Customers;

    -- Example: Selecting unique combinations of 'REGION' and 'CATEGORY'
    SELECT DISTINCT REGION, Category
    FROM SalesOrder;

    -- You can also use ORDER BY with DISTINCT
    SELECT DISTINCT City
    FROM Customers
    ORDER BY City ASC;
    ```

Understanding how to sort and limit your query results is essential for presenting data in a meaningful way and for optimizing query performance when dealing with large datasets. Remember the specific syntax for the `LIMIT` functionality might differ based on the SQL Server version or other database systems you might be working with. In SQL Server, `TOP` is the standard way to achieve this.