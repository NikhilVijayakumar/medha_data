## III. Data Query Language (DQL) - SELECT Statement

The `SELECT` statement is the cornerstone of DQL (Data Query Language) and is used to retrieve data from one or more tables in a database. It's a highly versatile command with numerous clauses that allow you to specify exactly what data you want to see and how you want it presented.

**4. Data Query Language (DQL) - SELECT Statement**

* **Basic Syntax:**

    ```sql
    SELECT column1, column2, ...
    FROM TableName;
    ```

    * `SELECT column1, column2, ...`: Specifies the columns you want to retrieve. You can list one or more column names separated by commas.
    * `FROM TableName`: Specifies the table from which you want to retrieve the data.

    * **Selecting All Columns:** To select all columns in a table, you can use the asterisk (`*`) wildcard.

        ```sql
        SELECT *
        FROM YourTableName;
        ```

* **Column Names with Spaces or Hyphens:**

    If a column name contains spaces or hyphens (or other special characters), you need to enclose it in square brackets `[]` in SQL Server.

    ```sql
    SELECT [ORDER ID], [CUSTOMER NAME]
    FROM SalesOrder;
    ```

* **`WHERE` Clause:**

    The `WHERE` clause is used to filter the rows returned by the `SELECT` statement based on specified conditions. Only rows that meet the condition(s) in the `WHERE` clause will be included in the result set.

    ```sql
    SELECT column1, column2
    FROM TableName
    WHERE condition;
    ```

    * **Comparison Operators:** You can use various comparison operators in the `WHERE` clause:
        * `=`: Equal to
        * `>`: Greater than
        * `<`: Less than
        * `>=`: Greater than or equal to
        * `<=`: Less than or equal to
        * `<>` or `!=`: Not equal to

        ```sql
        -- Example: Selecting all columns from the 'SalesOrder' table where the 'REGION' is 'SOUTH'
        SELECT *
        FROM SalesOrder
        WHERE REGION = 'SOUTH';

        -- Example: Selecting all columns where 'SALES' are greater than or equal to 10000
        SELECT *
        FROM SalesOrder
        WHERE SALES >= 10000;
        ```

    * **Combining Conditions with `AND` and `OR`:** You can combine multiple conditions using the logical operators `AND` and `OR`.
        * `AND`: Both conditions must be true for a row to be included.
        * `OR`: At least one of the conditions must be true for a row to be included.

        ```sql
        -- Example: Selecting orders from the 'SOUTH' region AND with 'SALES' greater than 5000
        SELECT *
        FROM SalesOrder
        WHERE REGION = 'SOUTH' AND SALES > 5000;

        -- Example: Selecting orders from either the 'SOUTH' OR the 'WEST' region
        SELECT *
        FROM SalesOrder
        WHERE REGION = 'SOUTH' OR REGION = 'WEST';
        ```

    * **`IN` and `NOT IN` Operators:** Used to check if a value matches any value within a list of specified values.

        ```sql
        -- Example: Selecting orders where the 'Category' is either 'OFFICE SUPPLIES' or 'FURNITURE'
        SELECT *
        FROM SalesOrder
        WHERE Category IN ('OFFICE SUPPLIES', 'FURNITURE');

        -- Example: Selecting orders where the 'CITY' is NOT 'LOS ANGELES'
        SELECT *
        FROM SalesOrder
        WHERE CITY NOT IN ('LOS ANGELES');
        ```

    * **`BETWEEN` and `NOT BETWEEN` Operators:** Used to filter values within a specified range (inclusive).

        ```sql
        -- Example: Selecting orders where 'SALES' are between 0 and 5000 (inclusive)
        SELECT *
        FROM SalesOrder
        WHERE SALES BETWEEN 0 AND 5000;

        -- Example: Selecting orders where 'SALES' are NOT between 2000 and 5000
        SELECT *
        FROM SalesOrder
        WHERE SALES NOT BETWEEN 2000 AND 5000;
        ```

    * **`LIKE` and `NOT LIKE` Operators (for Pattern Matching):** Used to search for patterns in string columns.

        * `%` (Percent sign): Matches any sequence of zero or more characters.
        * `_` (Underscore): Matches any single character (not explicitly covered in the initial excerpts but is a standard `LIKE` operator).

        ```sql
        -- Example: Selecting customers whose 'CUSTOMER NAME' starts with 'A'
        SELECT *
        FROM SalesOrder
        WHERE [CUSTOMER NAME] LIKE 'A%';

        -- Example: Selecting products where the 'Sub-Category' contains the word 'PAPER'
        SELECT *
        FROM SalesOrder
        WHERE [Sub-Category] LIKE '%PAPER%';

        -- Example (using underscore): Selecting names that start with 'J' and have 'n' as the third letter (e.g., 'Jon', 'Jan')
        SELECT *
        FROM Customers
        WHERE FirstName LIKE 'J_n%';
        ```

    * **`IS NULL` and `IS NOT NULL` Operators (for Null Values):** Used to check for the presence or absence of NULL values in a column. NULL represents a missing or unknown value.

        ```sql
        -- Example: Selecting orders where the 'Category' is NULL
        SELECT *
        FROM SalesOrder
        WHERE Category IS NULL;

        -- Example: Selecting orders where the 'Category' is not NULL
        SELECT *
        FROM SalesOrder
        WHERE Category IS NOT NULL;
        ```

The `SELECT` statement with the `WHERE` clause provides powerful capabilities for retrieving specific subsets of data from your tables based on various conditions and patterns. Mastering the different operators and how to combine them is crucial for effective data querying in SQL Server.