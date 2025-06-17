## VII. Joining Tables

In a relational database, data is often spread across multiple tables to reduce redundancy and improve organization. The `JOIN` operation allows you to combine rows from two or more tables based on a related column between them, enabling you to retrieve comprehensive information that spans across these tables.

**7. Joining Tables**

The `JOIN` clause is used in the `SELECT` statement to combine rows from different tables. The most common way to specify the relationship between the tables is using the `ON` clause, which defines the join condition (how rows from the tables should be matched).

* **`INNER JOIN`:**
    * Returns only the rows where there is a match in both tables based on the specified join condition. Rows that do not have a corresponding match in the other table are excluded from the result set.
    * Syntax:
      ```sql
      SELECT column1, column2, ...
      FROM Table1
      INNER JOIN Table2 ON Table1.MatchingColumn = Table2.MatchingColumn;
      ```
    * Example: Assuming you have a `SalesOrder` table with `Order ID` and a `Returns` table also with `Order ID`, this query would return only the orders that have a corresponding entry in the `Returns` table.
      ```sql
      SELECT SO.[Order ID], SO.[Customer Name], RT.Returned
      FROM SalesOrder SO
      INNER JOIN Returns RT ON SO.[Order ID] = RT.[Order ID];
      ```
      * `SO` and `RT` are table aliases used to make the query shorter and more readable.

* **`LEFT JOIN` (or `LEFT OUTER JOIN`):**
    * Returns all rows from the left table (the table specified first in the `FROM` clause) and the matching rows from the right table (the table specified after `LEFT JOIN`).
    * If there is no match in the right table for a row in the left table, `NULL` values are returned for the columns of the right table in the result set.
    * Syntax:
      ```sql
      SELECT column1, column2, ...
      FROM Table1
      LEFT JOIN Table2 ON Table1.MatchingColumn = Table2.MatchingColumn;
      ```
    * Example: This query would return all sales orders, and if a sales order has a corresponding return record in the `Returns` table, the `Returned` column from the `Returns` table would be included. If a sales order has no corresponding return, the `Returned` column would be `NULL`.
      ```sql
      SELECT SO.[Order ID], SO.[Customer Name], RT.Returned
      FROM SalesOrder SO
      LEFT JOIN Returns RT ON SO.[Order ID] = RT.[Order ID];
      ```

* **`RIGHT JOIN` (or `RIGHT OUTER JOIN`):**
    * Returns all rows from the right table (the table specified after `RIGHT JOIN`) and the matching rows from the left table (the table specified in the `FROM` clause).
    * If there is no match in the left table for a row in the right table, `NULL` values are returned for the columns of the left table.
    * Syntax:
      ```sql
      SELECT column1, column2, ...
      FROM Table1
      RIGHT JOIN Table2 ON Table1.MatchingColumn = Table2.MatchingColumn;
      ```
    * Example: This query would return all return records, and if a return record has a corresponding sales order in the `SalesOrder` table, the `Order ID` and `Customer Name` from the `SalesOrder` table would be included. If a return has no matching sales order, the `Order ID` and `Customer Name` columns would be `NULL`.
      ```sql
      SELECT SO.[Order ID], SO.[Customer Name], RT.Returned
      FROM SalesOrder SO
      RIGHT JOIN Returns RT ON SO.[Order ID] = RT.[Order ID];
      ```

* **`FULL JOIN` (or `FULL OUTER JOIN`):**
    * Returns all rows from both the left table and the right table.
    * If there is a match between the tables based on the join condition, the corresponding columns from both tables are included in the result.
    * If there is no match in the left table for a row in the right table, `NULL` values are returned for the columns of the left table. Similarly, if there is no match in the right table for a row in the left table, `NULL` values are returned for the columns of the right table.
    * Syntax:
      ```sql
      SELECT column1, column2, ...
      FROM Table1
      FULL JOIN Table2 ON Table1.MatchingColumn = Table2.MatchingColumn;
      ```
    * Example: This query would return all sales orders and all return records. Where an `Order ID` exists in both tables, the corresponding information from both would be shown. For orders with no return, the return columns would be `NULL`, and for returns with no matching order (if that's possible in the database design), the order columns would be `NULL`.
      ```sql
      SELECT SO.[Order ID], SO.[Customer Name], RT.Returned
      FROM SalesOrder SO
      FULL JOIN Returns RT ON SO.[Order ID] = RT.[Order ID];
      ```

* **`CROSS JOIN`:**
    * Returns the Cartesian product of the two tables. This means every row from the first table is combined with every row from the second table. It typically does not have an `ON` clause.
    * Syntax:
      ```sql
      SELECT column1, column2, ...
      FROM Table1
      CROSS JOIN Table2;
      ```
    * Example: If `SalesOrder` has 100 rows and `Returns` has 10 rows, a `CROSS JOIN` would result in 100 * 10 = 1000 rows. This type of join is less common but can be useful for specific scenarios like generating all possible combinations.

* **`SELF JOIN`:**
    * Used to join a table to itself. This is useful when you need to compare different rows within the same table, often based on a hierarchical relationship or some other related column.
    * Requires using aliases for the table to differentiate between the two instances of the table being joined.
    * Example: If you have an `Employees` table with `EmployeeID` and `ManagerID` (referencing another `EmployeeID`), you can use a self-join to find each employee and their manager's name.
      ```sql
      SELECT e.EmployeeName AS Employee, m.EmployeeName AS Manager
      FROM Employees e
      INNER JOIN Employees m ON e.ManagerID = m.EmployeeID;
      ```

* **`SEMI JOIN`:**
    * Returns rows from the left table where a condition is met in the right table, but it only returns the columns from the left table and does not duplicate rows even if there are multiple matches in the right table.
    * Often implemented using `WHERE EXISTS` or `WHERE column IN (SELECT ...)`.
    * Example: Selecting all sales orders that have at least one corresponding return record.
      ```sql
      SELECT SO.[Order ID], SO.[Customer Name]
      FROM SalesOrder SO
      WHERE EXISTS (SELECT 1 FROM Returns RT WHERE SO.[Order ID] = RT.[Order ID]);
      ```

* **`ANTI JOIN`:**
    * Returns rows from the left table where a condition is *not* met in the right table. It's used to find rows in one table that do not have a corresponding entry in another table.
    * Often implemented using `WHERE NOT EXISTS` or `WHERE column NOT IN (SELECT ...)`.
    * Example: Selecting all sales orders that do not have any corresponding return records.
      ```sql
      SELECT SO.[Order ID], SO.[Customer Name]
      FROM SalesOrder SO
      WHERE NOT EXISTS (SELECT 1 FROM Returns RT WHERE SO.[Order ID] = RT.[Order ID]);
      ```

* **`UNION`:**
    * Combines the result sets of two or more `SELECT` statements into a single result set.
    * Removes duplicate rows from the final result.
    * Requires that all `SELECT` statements have the same number of columns with compatible data types in the same order.
    * Example: Combining a list of active customers and a list of recently archived customers.
      ```sql
      SELECT CustomerID, Name, City FROM ActiveCustomers
      UNION
      SELECT CustomerID, Name, City FROM ArchivedCustomers;
      ```

* **`UNION ALL`:**
    * Similar to `UNION`, but it does not remove duplicate rows from the combined result set.
    * Syntax and requirements for the `SELECT` statements are the same as `UNION`.
    * Example: Combining all customer records, including duplicates if any exist in both active and archived tables.
      ```sql
      SELECT CustomerID, Name, City FROM ActiveCustomers
      UNION ALL
      SELECT CustomerID, Name, City FROM ArchivedCustomers;
      ```

* **`INTERSECT`:**
    * Returns only the rows that are present in the result sets of both (or all) `SELECT` statements being combined.
    * Requires that all `SELECT` statements have the same number of columns with compatible data types in the same order.
    * Example: Finding customers who have both placed an order and submitted a return.
      ```sql
      SELECT CustomerID FROM Orders
      INTERSECT
      SELECT CustomerID FROM Returns;
      ```

* **`EXCEPT` (or `MINUS`):**
    * Returns the rows from the first result set that are not present in the second result set.
    * Requires that all `SELECT` statements have the same number of columns with compatible data types in the same order.
    * The keyword might be `MINUS` in some SQL dialects (e.g., Oracle).
    * Example: Finding customers who have placed an order but have not submitted any returns.
      ```sql
      SELECT CustomerID FROM Orders
      EXCEPT
      SELECT CustomerID FROM Returns;
      ```

Understanding the different types of joins and set operators is crucial for querying data that is spread across multiple tables in a relational database, allowing you to combine and compare data in various powerful ways. The choice of join type depends on the specific relationships between the tables and the information you need to retrieve.