## XI. Rules/Constraints

Constraints in SQL Server are rules that you can define on columns or tables to enforce data integrity and consistency. They help ensure that the data stored in your database adheres to specific business rules and prevents invalid data from being entered.

**11. Rules/Constraints**

* **`NOT NULL`:**
    Ensures that a column cannot contain NULL values. If you try to insert or update a row with a NULL value in a `NOT NULL` column, the operation will fail.

    * **Defining during table creation:**
      ```sql
      CREATE TABLE Products (
          ProductID INT PRIMARY KEY,
          ProductName VARCHAR(100) NOT NULL,
          Price DECIMAL(10, 2)
      );
      ```

    * **Adding to an existing column using `ALTER TABLE`:** You can only add a `NOT NULL` constraint to a column if it currently does not contain any NULL values.
      ```sql
      ALTER TABLE Products
      ALTER COLUMN Price DECIMAL(10, 2) NOT NULL;
      ```

    * **Removing using `ALTER TABLE`:**
      ```sql
      ALTER TABLE Products
      ALTER COLUMN Price DECIMAL(10, 2) NULL;
      ```

* **`UNIQUE`:**
    Ensures that all values in a column (or a set of columns) are distinct. Unlike primary keys, a unique constraint allows one NULL value (unless explicitly disallowed by a `NOT NULL` constraint).

    * **Defining during table creation:**
      ```sql
      CREATE TABLE Emails (
          UserID INT PRIMARY KEY,
          EmailAddress VARCHAR(100) UNIQUE
      );

      -- Unique constraint on multiple columns (composite unique key)
      CREATE TABLE Addresses (
          AddressID INT PRIMARY KEY,
          Street VARCHAR(100) NOT NULL,
          City VARCHAR(50) NOT NULL,
          PostalCode VARCHAR(10) NOT NULL,
          CONSTRAINT UQ_Address UNIQUE (Street, City, PostalCode)
      );
      ```

    * **Adding using `ALTER TABLE`:** You can name the constraint for easier management.
      ```sql
      ALTER TABLE Emails
      ADD CONSTRAINT UQ_Email UNIQUE (EmailAddress);
      ```

* **`CHECK`:**
    Defines a rule (a Boolean expression) that the values in a column must satisfy. If an insert or update operation violates the `CHECK` constraint, the operation will fail.

    * **Defining during table creation:**
      ```sql
      CREATE TABLE EMP_DATA (
          EmpID INT PRIMARY KEY,
          SAL NUMERIC(10, 2) CHECK (SAL >= 10000),
          Age INT CHECK (Age >= 18 AND Age <= 65)
      );
      ```

    * **Adding using `ALTER TABLE`:** You can name the constraint.
      ```sql
      ALTER TABLE EMP_DATA
      ADD CONSTRAINT CK_Salary CHECK (SAL >= 15000);

      ALTER TABLE EMP_DATA
      ADD CONSTRAINT CK_AgeRange CHECK (Age BETWEEN 21 AND 60);
      ```

    * **Removing using `ALTER TABLE`:** You need the constraint name to drop it.
      ```sql
      ALTER TABLE EMP_DATA
      DROP CONSTRAINT CK_Salary;
      ```

* **`DEFAULT`:**
    Specifies a default value for a column if no value is provided during an `INSERT` operation.

    * **Defining during table creation:**
      ```sql
      CREATE TABLE EMP_DATA_01 (
          EmpID INT PRIMARY KEY,
          CITY VARCHAR(20) DEFAULT 'PUNE',
          JoinDate DATE DEFAULT GETDATE()
      );
      ```

    * **Adding or modifying using `ALTER TABLE`:**
      ```sql
      ALTER TABLE EMP_DATA_01
      ADD CONSTRAINT DF_Country DEFAULT 'India' FOR Country;

      ALTER TABLE EMP_DATA_01
      ALTER COLUMN JoinDate SET DEFAULT '2025-05-01'; -- Syntax might vary slightly
      ```

    * **Removing a default constraint:**
      ```sql
      ALTER TABLE EMP_DATA_01
      ALTER COLUMN CITY DROP DEFAULT;
      ```

* **`PRIMARY KEY`:**
    Uniquely identifies each row in a table. A primary key constraint enforces both `NOT NULL` and `UNIQUE` constraints on the specified column(s). A table can have only one primary key.

    * **Defining during table creation (single column):**
      ```sql
      CREATE TABLE Employees (
          EmployeeID INT PRIMARY KEY,
          FirstName VARCHAR(50),
          LastName VARCHAR(50)
      );
      ```

    * **Defining during table creation (composite primary key - multiple columns):**
      ```sql
      CREATE TABLE OrderDetails (
          OrderID INT,
          ProductID INT,
          Quantity INT NOT NULL,
          PRIMARY KEY (OrderID, ProductID) -- Combination must be unique
      );
      ```

    * **Adding using `ALTER TABLE`:** The column(s) you designate as the primary key must not contain NULL values.
      ```sql
      ALTER TABLE Employees
      ADD CONSTRAINT PK_EmployeeID PRIMARY KEY (EmployeeID);

      ALTER TABLE OrderDetails
      ADD CONSTRAINT PK_OrderDetail PRIMARY KEY (OrderID, ProductID);
      ```

* **`FOREIGN KEY`:**
    Establishes a link between two tables. A foreign key in one table (the child or referencing table) refers to the primary key in another table (the parent or referenced table). It enforces referential integrity, ensuring that relationships between tables are valid and preventing actions that would break those relationships (e.g., deleting a parent record if child records still exist).

    * **Defining during table creation:**
      ```sql
      CREATE TABLE Orders (
          OrderID INT PRIMARY KEY,
          CustomerID INT,
          OrderDate DATE,
          CONSTRAINT FK_Customer FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
      );
      ```

    * **Adding using `ALTER TABLE`:** The data in the foreign key column must match existing values in the referenced primary key column (or be NULL if the foreign key allows NULLs).
      ```sql
      ALTER TABLE Orders
      ADD CONSTRAINT FK_Customer FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID);
      ```

* **`COMPOSITE KEY`:**
    A primary key (or sometimes a unique key) that consists of two or more columns. The combination of values in these columns must be unique to identify each row uniquely. The `PRIMARY KEY (Column1, Column2, ...)` syntax during table creation or using `ALTER TABLE ADD CONSTRAINT PRIMARY KEY (Column1, Column2, ...)` defines a composite primary key.

    * **Example (revisited from `PRIMARY KEY`):**
      ```sql
      CREATE TABLE OrderDetails (
          OrderID INT,
          ProductID INT,
          Quantity INT NOT NULL,
          CONSTRAINT CK_IDNO_CONT PRIMARY KEY(OrderID, ProductID)
      );
      ```

* **`IDENTITY`:**
    A column property (not strictly a constraint in the same way as `PRIMARY KEY` or `UNIQUE`) that automatically generates sequential numeric values when new rows are inserted into a table. It's often used to create primary key values.

    * **Syntax during table creation:**
      ```sql
      CREATE TABLE Items (
          ItemID INT IDENTITY(1, 1) PRIMARY KEY, -- Starts at 1, increments by 1
          ItemName VARCHAR(50)
      );

      CREATE TABLE Tasks (
          TaskID INT IDENTITY(100, 5) PRIMARY KEY, -- Starts at 100, increments by 5
          TaskDescription VARCHAR(200)
      );
      ```

    * You cannot directly add or modify an `IDENTITY` property using `ALTER TABLE` in the same way as constraints. You might need to create a new column with the `IDENTITY` property and then potentially drop the old column.

Understanding and implementing constraints is crucial for building robust and reliable databases that maintain the integrity and accuracy of your data. Choosing the right constraints depends on the specific requirements and relationships within your data model.