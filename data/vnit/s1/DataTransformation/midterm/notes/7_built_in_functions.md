## VIII. Functions

SQL Server provides a wide range of built-in functions that allow you to perform various operations on data within your queries. These functions can be used to manipulate strings, work with dates and times, perform calculations, and more. This section focuses on Text Functions, Date Functions, and introduces Window Functions. Aggregate functions were covered in Section VI.

**8. Functions**

* **Aggregate Functions:** (Covered in Section VI)
    * `COUNT()`, `SUM()`, `AVG()`, `MAX()`, `MIN()`

* **Text Functions:**
    Used to manipulate and work with string data. Some common text functions in SQL Server include:

    * `LEN(string)`: Returns the length (number of characters) of the input string.
        ```sql
        SELECT LEN('Hello'); -- Result: 5
        SELECT [PRODUCT NAME], LEN([PRODUCT NAME]) AS ProductNameLength
        FROM SalesOrder;
        ```

    * `LEFT(string, length)`: Returns the leftmost `length` characters of the input string.
        ```sql
        SELECT LEFT('HelloWorld', 5); -- Result: 'Hello'
        SELECT [CUSTOMER NAME], LEFT([CUSTOMER NAME], 3) AS CustomerInitials
        FROM SalesOrder;
        ```

    * `RIGHT(string, length)`: Returns the rightmost `length` characters of the input string.
        ```sql
        SELECT RIGHT('HelloWorld', 5); -- Result: 'World'
        SELECT [ORDER ID], RIGHT([ORDER ID], 4) AS LastFourOrderID
        FROM SalesOrder;
        ```

    * `SUBSTRING(string, start, length)`: Extracts a substring of the specified `length` from the input `string`, starting at the `start` position (1-based index).
        ```sql
        SELECT SUBSTRING('HelloWorld', 6, 5); -- Result: 'World'
        SELECT [PRODUCT NAME], SUBSTRING([PRODUCT NAME], 1, 10) AS FirstTenChars
        FROM SalesOrder;
        ```

    * `CHARINDEX(substring, string)`: Returns the starting position of the first occurrence of `substring` within `string`. If the substring is not found, it returns 0.
        ```sql
        SELECT CHARINDEX('World', 'HelloWorld'); -- Result: 6
        SELECT [CUSTOMER NAME], CHARINDEX(' ', [CUSTOMER NAME]) AS SpacePosition
        FROM SalesOrder;
        ```

    * `CONCAT(string1, string2, ...)`: Concatenates two or more strings together. In some older versions of SQL Server, you might use the `+` operator for concatenation.
        ```sql
        SELECT CONCAT('Hello', ' ', 'World'); -- Result: 'Hello World'
        SELECT [CUSTOMER NAME], ' from ', City AS CustomerLocation
        FROM SalesOrder; -- Note: '+' might be used instead of CONCAT in some contexts
        ```

    * `TRIM(string)`: Removes leading and trailing spaces from a string. You can also specify characters to trim (e.g., `TRIM('x' FROM 'xxHelloxx')`).
        ```sql
        SELECT TRIM('   Hello   '); -- Result: 'Hello'
        SELECT TRIM(LEADING ' ' FROM '   Hello   '); -- Trim leading spaces
        SELECT TRIM(TRAILING ' ' FROM '   Hello   '); -- Trim trailing spaces
        ```

* **Date Functions:**
    Used to work with date and time data types. Some common date functions in SQL Server include:

    * `DATEPART(interval, date)`: Extracts a specific part of a date (e.g., year, month, day, week, hour, minute, second).
        ```sql
        SELECT DATEPART(year, GETDATE());   -- Returns the current year
        SELECT DATEPART(month, [ORDER DATE]) AS OrderMonth
        FROM SalesOrder;
        ```

    * `DATENAME(interval, date)`: Returns the name of a specific part of a date as a string (e.g., 'Year', 'January', 'Monday').
        ```sql
        SELECT DATENAME(month, GETDATE());  -- Returns the current month name
        SELECT DATENAME(weekday, [ORDER DATE]) AS OrderDayName
        FROM SalesOrder;
        ```

    * `DATEDIFF(interval, start_date, end_date)`: Calculates the difference between two dates based on the specified `interval` (e.g., year, month, day). The result is an integer.
        ```sql
        SELECT DATEDIFF(day, '2025-01-01', GETDATE()); -- Returns the number of days between the two dates
        SELECT DATEDIFF(year, MIN([ORDER DATE]), MAX([ORDER DATE])) AS YearsOfData
        FROM SalesOrder;
        ```

    * `DATEADD(interval, number, date)`: Adds a specified `number` of `interval`s to a `date`.
        ```sql
        SELECT DATEADD(day, 7, GETDATE());  -- Returns the date 7 days from now
        SELECT DATEADD(month, 3, [ORDER DATE]) AS OrderPlusThreeMonths
        FROM SalesOrder;
        ```

    * `EOMONTH(date, number_of_months)`: Returns the last day of the month that is the specified `number_of_months` after or before the input `date`. If `number_of_months` is 0, it returns the last day of the month for the given `date`.
        ```sql
        SELECT EOMONTH(GETDATE(), 0);   -- Returns the last day of the current month
        SELECT EOMONTH([ORDER DATE], 1) AS EndOfNextMonth
        FROM SalesOrder;
        ```

    * `GETDATE()`: Returns the current database system date and time.
        ```sql
        SELECT GETDATE();
        ```

    * `SYSDATETIMEOFFSET()`: Returns the current database system date and time with the time zone offset.
        ```sql
        SELECT SYSDATETIMEOFFSET();
        ```

    * `SWITCHOFFSET(datetimeoffset, time_zone)`: Changes the time zone offset of a `datetimeoffset` value to the specified `time_zone`.
        ```sql
        SELECT SWITCHOFFSET(SYSDATETIMEOFFSET(), '+05:30'); -- Convert to IST
        ```

* **Window Functions:**
    Perform calculations across a set of table rows that are related to the current row. Unlike aggregate functions, window functions do not collapse rows into a single output row. They provide a way to perform calculations like ranking, running totals, and moving averages within a result set.

    * **Syntax Overview:**
      ```sql
      SELECT column1, column2,
             window_function(column) OVER (
                 [PARTITION BY partition_column(s)]
                 ORDER BY sort_column(s) [ASC|DESC]
             ) AS window_function_result
      FROM TableName;
      ```

    * **Common Window Functions:**
        * `RANK() OVER (ORDER BY column)`: Assigns a rank to each row within the partition of a result set based on the `ORDER BY` clause. Rows with equal values receive the same rank, and subsequent ranks are skipped.
        * `DENSE_RANK() OVER (ORDER BY column)`: Similar to `RANK()`, but it assigns consecutive ranks without gaps, even if there are ties.
        * `ROW_NUMBER() OVER (ORDER BY column)`: Assigns a unique sequential integer to each row within the partition based on the `ORDER BY` clause.
        * `PARTITION BY`: Divides the rows of the query into partitions (groups) to which the window function is applied independently. If not specified, the function is applied to all rows of the query.

    * **Examples:**
        ```sql
        -- Example: Ranking products within each category based on their sales
        SELECT Category, [PRODUCT NAME], SALES,
               RANK() OVER (PARTITION BY Category ORDER BY SALES DESC) AS SalesRankInCategory
        FROM SalesOrder;

        -- Example: Assigning a dense rank to customers based on their total number of orders
        WITH CustomerOrderCount AS (
            SELECT [CUSTOMER NAME], COUNT([ORDER ID]) AS TotalOrders
            FROM SalesOrder
            GROUP BY [CUSTOMER NAME]
        )
        SELECT [CUSTOMER NAME], TotalOrders,
               DENSE_RANK() OVER (ORDER BY TotalOrders DESC) AS CustomerRankByOrders
        FROM CustomerOrderCount;

        -- Example: Assigning a unique row number to each sales order
        SELECT [ORDER ID], [ORDER DATE],
               ROW_NUMBER() OVER (ORDER BY [ORDER DATE] ASC) AS OrderNumber
        FROM SalesOrder;
        ```

This section provides an introduction to some of the essential built-in functions available in SQL Server for manipulating text and date data, as well as an overview of the powerful concept of window functions for advanced data analysis within queries. Exploring the full range of available functions in SQL Server's documentation will further enhance your ability to work with and transform data.