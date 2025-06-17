## VI. Aggregate Functions and `GROUP BY` Clause

Aggregate functions perform calculations on a set of rows and return a single summary value. The `GROUP BY` clause is used to group rows with the same values in one or more columns, allowing you to apply aggregate functions to each group. The `HAVING` clause then filters these grouped results.

**6. Aggregate Functions and `GROUP BY` Clause**

* **Aggregate Functions:**

    These functions operate on a set of rows and return a single value. Common aggregate functions in SQL Server include:

    * `COUNT()`: Returns the number of rows in a group or the number of non-NULL values in a specified column.
        ```sql
        -- Example: Counting the total number of orders in the 'SalesOrder' table
        SELECT COUNT(*) AS TotalOrders
        FROM SalesOrder;

        -- Example: Counting the number of orders in the 'SalesOrder' table for the 'SOUTH' region
        SELECT COUNT([ORDER ID]) AS SouthRegionOrders
        FROM SalesOrder
        WHERE REGION = 'SOUTH';

        -- Example: Counting the number of non-NULL values in the 'Category' column
        SELECT COUNT(Category) AS CategoriesFilled
        FROM SalesOrder;
        ```

    * `SUM()`: Returns the sum of the values in a specified numeric column.
        ```sql
        -- Example: Calculating the total 'SALES' from the 'SalesOrder' table
        SELECT SUM(SALES) AS TotalSales
        FROM SalesOrder;

        -- Example: Calculating the total 'PROFIT' for the 'WEST' region
        SELECT SUM(PROFIT) AS WestRegionProfit
        FROM SalesOrder
        WHERE REGION = 'WEST';
        ```

    * `AVG()`: Returns the average of the values in a specified numeric column. NULL values are typically ignored in the calculation.
        ```sql
        -- Example: Calculating the average 'SALES'
        SELECT AVG(SALES) AS AverageSales
        FROM SalesOrder;

        -- Example: Calculating the average 'DISCOUNT' for 'OFFICE SUPPLIES'
        SELECT AVG(DISCOUNT) AS AvgOfficeSuppliesDiscount
        FROM SalesOrder
        WHERE Category = 'OFFICE SUPPLIES';
        ```

    * `MAX()`: Returns the maximum value in a specified column. Can be used with numeric, string, and date/time data types.
        ```sql
        -- Example: Finding the highest 'SALES' amount
        SELECT MAX(SALES) AS MaxSales
        FROM SalesOrder;

        -- Example: Finding the latest 'ORDER DATE'
        SELECT MAX([ORDER DATE]) AS LatestOrderDate
        FROM SalesOrder;
        ```

    * `MIN()`: Returns the minimum value in a specified column. Similar to `MAX()`, it can be used with various data types.
        ```sql
        -- Example: Finding the lowest 'SALES' amount
        SELECT MIN(SALES) AS MinSales
        FROM SalesOrder;

        -- Example: Finding the earliest 'ORDER DATE'
        SELECT MIN([ORDER DATE]) AS EarliestOrderDate
        FROM SalesOrder;
        ```

* **`GROUP BY` Clause:**

    The `GROUP BY` clause groups rows that have the same values in one or more specified columns into summary rows. Aggregate functions are then applied to these groups to calculate summary information for each group.

    ```sql
    SELECT column1, column2, aggregate_function(column3)
    FROM TableName
    WHERE condition
    GROUP BY column1, column2
    ORDER BY column1, column2;
    ```

    * The `GROUP BY` clause is typically placed after the `WHERE` clause (if used) and before the `ORDER BY` clause.
    * Any non-aggregated columns in the `SELECT` list must also be included in the `GROUP BY` clause.

    ```sql
    -- Example: Counting the number of orders in each 'REGION'
    SELECT REGION, COUNT([ORDER ID]) AS OrdersCount
    FROM SalesOrder
    GROUP BY REGION;

    -- Example: Calculating the total 'SALES' for each 'CATEGORY'
    SELECT Category, SUM(SALES) AS TotalSales
    FROM SalesOrder
    GROUP BY Category;

    -- Example: Finding the average 'PROFIT' for each 'REGION' and 'SEGMENT' combination
    SELECT REGION, Segment, AVG(PROFIT) AS AverageProfit
    FROM SalesOrder
    GROUP BY REGION, Segment
    ORDER BY REGION, Segment;
    ```

* **`HAVING` Clause:**

    The `HAVING` clause is used to filter the groups created by the `GROUP BY` clause based on specified conditions applied to the aggregated results. It's similar to the `WHERE` clause, but it operates on groups rather than individual rows.

    ```sql
    SELECT column1, aggregate_function(column2)
    FROM TableName
    WHERE condition
    GROUP BY column1
    HAVING group_condition
    ORDER BY column1;
    ```

    * The `HAVING` clause is placed after the `GROUP BY` clause.
    * You can use aggregate functions in the `HAVING` clause's condition.

    ```sql
    -- Example: Selecting 'REGION's where the total 'SALES' are greater than 600000
    SELECT REGION, SUM(SALES) AS TotalSales
    FROM SalesOrder
    GROUP BY REGION
    HAVING SUM(SALES) > 600000;

    -- Example: Finding 'CATEGORY's with more than 1000 orders
    SELECT Category, COUNT([ORDER ID]) AS OrdersCount
    FROM SalesOrder
    GROUP BY Category
    HAVING COUNT([ORDER ID]) > 1000
    ORDER BY OrdersCount DESC;

    -- Alias names created for aggregates in the SELECT list can be used in the ORDER BY clause but not directly in GROUP BY or HAVING (though some SQL Server versions might allow it in certain contexts, it's generally safer to use the aggregate expression).
    SELECT REGION, SUM(SALES) AS TotalSales
    FROM SalesOrder
    GROUP BY REGION
    HAVING SUM(SALES) > 500000
    ORDER BY TotalSales DESC;
    ```

* **`ROLLUP`:**

    `ROLLUP` is an extension of the `GROUP BY` clause used to generate subtotals and grand totals for the grouped columns. It allows you to see aggregations at different levels of granularity.

    ```sql
    SELECT REGION, STATE, SUM(Sales) AS TotalSales
    FROM SalesOrder
    GROUP BY ROLLUP(Region, State)
    ORDER BY Region, State;
    ```

    The `ROLLUP(Region, State)` would generate:
    * Total sales for each `REGION` and `STATE` combination.
    * Subtotals for each `REGION` (where `STATE` is NULL).
    * A grand total for all regions (where both `REGION` and `STATE` are NULL).

    `ORDER BY` should be used carefully with `ROLLUP` to ensure the desired presentation of subtotals and grand totals.

Understanding aggregate functions and the `GROUP BY` and `HAVING` clauses is crucial for summarizing and analyzing data in SQL Server, allowing you to gain insights from collections of rows. `ROLLUP` provides an additional powerful tool for creating multi-level aggregations.