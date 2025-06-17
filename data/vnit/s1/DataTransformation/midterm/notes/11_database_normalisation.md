## XII. Database Normalisation

Database normalisation is the process of organizing data in a database to reduce data redundancy and improve data integrity. It involves dividing larger tables into smaller, more manageable tables and defining relationships between them. The goal is to eliminate data anomalies (insertion, update, deletion) and make the database more efficient and easier to maintain.

**12. Database Normalisation**

* **Goals of Normalisation:**
    * **Reduce Data Redundancy:** Minimizing the duplication of data across multiple tables, which saves storage space and reduces the chance of inconsistencies.
    * **Eliminate Anomalies:** Preventing issues that can arise when inserting, updating, or deleting data due to redundancy:
        * **Insertion Anomaly:** Difficulty in inserting a new record because some required information is not yet available.
        * **Update Anomaly:** Needing to update the same piece of information in multiple rows if it's stored redundantly.
        * **Deletion Anomaly:** Unintentionally losing related information when deleting a record.
    * **Improve Query Performance:** Well-normalised databases can sometimes lead to more efficient queries by reducing the amount of data that needs to be scanned.
    * **Ensure Data Consistency and Integrity:** Making sure that data is accurate and consistent across the database by enforcing relationships and reducing redundancy.

* **Normal Forms (NF):**
    Normalisation is typically achieved by adhering to a series of normal forms. Each normal form builds upon the previous one. The most commonly discussed normal forms are 1NF, 2NF, and 3NF. Boyce-Codd Normal Form (BCNF) is a stricter version of 3NF. Higher normal forms (4NF, 5NF) address more specific types of data dependencies but are less frequently encountered in typical database design.

    * **1st Normal Form (1NF):**
        A table is in 1NF if it meets the following criteria:
        * **Atomic Values:** Each column in a row contains a single, indivisible value. No multi-valued columns or repeating groups are allowed.
        * **Same Data Type:** All values in a column must be of the same data type.
        * **Unique Column Names:** All columns in a table must have unique names.
        * **Order Doesn't Matter:** The order of rows or columns does not affect the meaning of the data.
        * **Primary Key:** Each record must be uniquely identifiable, typically by having a primary key.

        * **Example of Violation (Not in 1NF):**
          ```
          OrderID | ProductNames        | Quantities |
          --------|---------------------|------------|
          101     | {Laptop, Mouse}     | {1, 2}     |
          102     | Keyboard            | 1          |
          ```
        * **Transformation to 1NF:** Create separate rows for each product in an order.
          ```
          OrderID | ProductName | Quantity |
          --------|-------------|----------|
          101     | Laptop      | 1        |
          101     | Mouse       | 2        |
          102     | Keyboard    | 1        |
          ```

    * **2nd Normal Form (2NF):**
        A table is in 2NF if it meets the following criteria:
        * It is already in 1NF.
        * There is no partial dependency: all non-key attributes must be fully dependent on the entire primary key. This is only relevant if the primary key is composite (consists of two or more columns). If the primary key is a single column, a 1NF table is automatically in 2NF.

        * **Example of Violation (Not in 2NF):**
          Consider a table `OrderItems` with a composite primary key `(OrderID, ProductID)`:
          ```
          OrderID | ProductID | ProductName | Price | Discount |
          --------|-----------|-------------|-------|----------|
          101     | P1        | Laptop      | 1200  | 0.10     |
          101     | P2        | Mouse       | 25    | 0.05     |
          102     | P1        | Laptop      | 1200  | 0.10     |
          ```
          Here, `ProductName` and `Price` are only dependent on `ProductID` (part of the primary key), not on `OrderID`. `Discount` might depend on the combination of `OrderID` and `ProductID`.

        * **Transformation to 2NF:** Split into two tables: `OrderItems` and `Products`.
          ```
          -- OrderItems Table (Primary Key: OrderID, ProductID)
          OrderID | ProductID | Discount |
          --------|-----------|----------|
          101     | P1        | 0.10     |
          101     | P2        | 0.05     |
          102     | P1        | 0.10     |

          -- Products Table (Primary Key: ProductID)
          ProductID | ProductName | Price |
          ----------|-------------|-------|
          P1        | Laptop      | 1200  |
          P2        | Mouse       | 25    |
          ```

    * **3rd Normal Form (3NF):**
        A table is in 3NF if it meets the following criteria:
        * It is already in 2NF.
        * There is no transitive dependency: no non-key attribute should be dependent on another non-key attribute. All non-key attributes must be directly dependent on the primary key.

        * **Example of Violation (Not in 3NF):**
          Consider an `Employees` table:
          ```
          EmployeeID | EmployeeName | DepartmentID | DepartmentName |
          ------------|--------------|--------------|----------------|
          1           | Alice        | D1           | Sales          |
          2           | Bob          | D2           | Marketing      |
          3           | Charlie      | D1           | Sales          |
          ```
          Here, `DepartmentName` is dependent on `DepartmentID` (a non-key attribute), not directly on `EmployeeID` (the primary key).

        * **Transformation to 3NF:** Split into two tables: `Employees` and `Departments`.
          ```
          -- Employees Table (Primary Key: EmployeeID, Foreign Key: DepartmentID)
          EmployeeID | EmployeeName | DepartmentID |
          ------------|--------------|--------------|
          1           | Alice        | D1           |
          2           | Bob          | D2           |
          3           | Charlie      | D1           |

          -- Departments Table (Primary Key: DepartmentID)
          DepartmentID | DepartmentName |
          -------------|----------------|
          D1           | Sales          |
          D2           | Marketing      |
          ```

    * **Boyce-Codd Normal Form (BCNF):**
        A stricter form of 3NF. A table is in BCNF if every determinant (any attribute or set of attributes that determines another attribute) is a candidate key (a minimal superkey, meaning it can uniquely identify a row). In most cases, if a table is in 3NF and every determinant is a candidate key, it is also in BCNF. BCNF is more concerned with situations where there are multiple candidate keys.

    * **4th Normal Form (4NF) and 5th Normal Form (5NF):**
        These deal with more complex types of dependencies (multi-valued dependencies in 4NF and join dependencies in 5NF) and are typically considered in more advanced database design scenarios.

* **De-Normalisation:**
    The process of intentionally adding redundancy back into a database design (e.g., by combining tables) to improve performance for specific read-heavy applications. De-normalisation can speed up data retrieval by reducing the need for complex joins, but it can also reintroduce the risk of data anomalies and increase storage requirements. It should be done judiciously and with a clear understanding of the trade-offs.

Understanding normalisation principles is crucial for designing efficient, maintainable, and reliable relational databases. By systematically applying the normal forms, you can structure your data in a way that minimizes redundancy and promotes data integrity. However, the level of normalisation to apply can sometimes be a trade-off between data integrity and query performance, leading to carefully considered de-normalisation in specific cases.