# **Practice Questions: SQL Server Programming Constructs**

Use the `UniversityDB` and its populated tables (`Students`, `Courses`, `Instructors`, `Enrollments`, `Departments`) to answer the following questions.

## **I. Conditional Logic (`IF`/`ELSE` Statements)**

1.  **`IF EXISTS` (in a Stored Procedure):**

      * Create a stored procedure named `CheckStudentExists` that takes a `StudentID` (INT) as input.
      * Inside the procedure, use `IF EXISTS` to check if a student with the given `StudentID` exists in the `Students` table.
      * If the student exists, `PRINT 'Student Found.'`.
      * If not, `PRINT 'Student Not Found.'`.
      * Test the procedure with `StudentID` 1 and `StudentID` 99.

2.  **`IF...ELSE` with `COUNT(*)` (in a Stored Procedure):**

      * Create a stored procedure named `GetDepartmentCourseCount` that takes a `DepartmentName` (VARCHAR(100)) as input.
      * Declare an integer variable to store the count of courses.
      * Use `COUNT(*)` to find how many courses belong to the specified department and store the result in the variable.
      * Use `IF...ELSE` to check:
          * If the count is greater than 0, `PRINT 'Department has [Count] courses.'` and then `SELECT * FROM Courses WHERE Department = @DepartmentName;`
          * If the count is 0, `PRINT 'Department has no courses.'`
      * Test the procedure with 'Computer Science and Engineering' and a non-existent department like 'Fine Arts'.

3.  **`IF...ELSE` for GPA Threshold (in a Stored Procedure):**

      * Create a stored procedure named `EvaluateStudentPerformance` that takes a `StudentID` (INT) as input.
      * Retrieve the `GPA` for the given student into a variable.
      * Use `IF...ELSE IF...ELSE` to evaluate the `GPA`:
          * If `GPA` is `NULL`, print 'GPA not available.'.
          * If `GPA` is `>= 3.5`, print '[StudentFullName] is an excellent student.'.
          * If `GPA` is `>= 3.0`, print '[StudentFullName] is a good student.'.
          * Else, print '[StudentFullName] needs to improve.'.
      * Test with different `StudentID`s (e.g., 2, 5, 9).

## **II. Loops (`WHILE` Condition)**

1.  **Basic Iteration for Data Generation/Manipulation:**

      * Create a stored procedure named `InsertDummyCourses`.
      * Use a `WHILE` loop to insert 5 new dummy courses into the `Courses` table. Start `CourseID` from 9001. Each course name can be 'Dummy Course [Number]' and `Credits` 3, `Department` 'Mathematics'.
      * **Crucial:** Include a condition to prevent an infinite loop.
      * After running, query the `Courses` table to see the new entries.

2.  **Iterating and Displaying Specific Information:**

      * Create a stored procedure named `DisplayStudentEnrollmentSummary`.
      * Use a `WHILE` loop to iterate through `StudentID`s from 1 to the maximum `StudentID` in your `Students` table.
      * Inside the loop, for each `StudentID`:
          * Declare variables to hold student `FirstName`, `LastName`, and `CourseName`.
          * Use a `SELECT` statement to retrieve the student's full name and the name of one of their enrolled courses (if any). If there are multiple, pick one, e.g., using `TOP 1` or just focus on the student's name if they have no enrollments.
          * `PRINT` a formatted string like "Student: [FirstName] [LastName] - Enrolled in: [CourseName]" or "Student: [FirstName] [LastName] - No enrollments."
      * **Hint:** You'll likely need a `LEFT JOIN` to `Enrollments` and `Courses` inside the loop's `SELECT` statement to get the course name.

## **III. Dynamic SQL**

1.  **Basic Dynamic `SELECT`:**

      * Create a stored procedure named `ExecuteDynamicSelect` that accepts a `TableName` (NVARCHAR(100)) as input.
      * Construct a dynamic SQL string to `SELECT *` from the given `TableName`.
      * Execute this dynamic SQL string using `EXECUTE SP_EXECUTESQL`.
      * Test by executing the procedure for 'Students' and 'Courses'.

2.  **Dynamic `UPDATE` with Parameterization:**

      * Create a stored procedure named `UpdateStudentEmail` that takes `StudentID` (INT) and `NewEmail` (NVARCHAR(100)) as input.
      * Construct a dynamic `UPDATE` statement for the `Students` table to set the `Email` for the given `StudentID`.
      * **Crucial:** Use `SP_EXECUTESQL` with parameters (`N'@param1 type, @param2 type'`, `@param1=value, @param2=value`) to prevent SQL injection.
      * Test by updating the email for `StudentID` 1 to 'john.doe.updated@example.com'. Verify the change.

3.  **Dynamic `COUNT` with Output Parameter:**

      * Create a stored procedure named `GetDynamicRowCount` that takes a `TableName` (NVARCHAR(100)) as input and has an `OUTPUT` parameter `TotalRows` (INT).
      * Construct a dynamic SQL string to `SELECT COUNT(*)` from the given `TableName` into `@TotalRows`.
      * Execute this dynamic SQL using `SP_EXECUTESQL`, correctly passing the output parameter.
      * Outside the procedure, declare a variable, execute `GetDynamicRowCount`, and then `PRINT` the result.
      * Test for 'Students' and 'Enrollments'.

## **IV. Triggers**

**A. Setup for Trigger Questions:**

  * **Create an `AuditLog` Table:**
    ```sql
    CREATE TABLE AuditLog (
        LogID INT IDENTITY(1,1) PRIMARY KEY,
        TableName VARCHAR(50) NOT NULL,
        OperationType VARCHAR(10) NOT NULL, -- 'INSERT', 'UPDATE', 'DELETE'
        RecordID INT, -- Store PK of the changed record if applicable
        OldValue VARCHAR(MAX), -- Store relevant old data (e.g., old email, old GPA)
        NewValue VARCHAR(MAX), -- Store relevant new data
        ChangeDate DATETIME DEFAULT GETDATE(),
        ChangedBy VARCHAR(100) DEFAULT SUSER_SNAME() -- SQL Server username
    );
    GO
    ```

**B. Trigger Creation & Testing:**

1.  **`FOR INSERT` Trigger on `Students`:**

      * Create a trigger named `TR_Students_AfterInsert` on the `Students` table, `FOR INSERT`.
      * This trigger should insert a record into the `AuditLog` table for each new student inserted.
      * Log `TableName`='Students', `OperationType`='INSERT', `RecordID`=`StudentID`, `NewValue` (can concatenate `FirstName` and `LastName`), `OldValue`='N/A'.
      * **Test:** Insert a new student: `INSERT INTO Students (StudentID, FirstName, LastName, DateOfBirth, Email, GPA) VALUES (100, 'Test', 'Student', '2003-01-01', 'test.student@example.com', 3.2);`
      * Verify the entry in `AuditLog`.

2.  **`FOR UPDATE` Trigger on `Students` (for GPA changes):**

      * Create a trigger named `TR_Students_AfterUpdate_GPA` on the `Students` table, `FOR UPDATE`.
      * This trigger should fire *only if* the `GPA` column is updated (`IF UPDATE(GPA)`).
      * If `GPA` is updated, insert a record into `AuditLog`.
      * Log `TableName`='Students', `OperationType`='UPDATE', `RecordID`=`StudentID`.
      * `OldValue`: `CAST(d.GPA AS VARCHAR(10))` (from `deleted` table).
      * `NewValue`: `CAST(i.GPA AS VARCHAR(10))` (from `inserted` table).
      * **Test:** Update the `GPA` for an existing student: `UPDATE Students SET GPA = 3.65 WHERE StudentID = 1;`
      * Verify the entry in `AuditLog`. Try updating another column (e.g., `FirstName`) and confirm the trigger does *not* log.

3.  **`FOR DELETE` Trigger on `Students`:**

      * Create a trigger named `TR_Students_AfterDelete` on the `Students` table, `FOR DELETE`.
      * This trigger should insert a record into `AuditLog` for each student deleted.
      * Log `TableName`='Students', `OperationType`='DELETE', `RecordID`=`StudentID` (from `deleted` table), `OldValue` (concatenated name), `NewValue`='N/A'.
      * **Test:** Delete a student: `DELETE FROM Students WHERE StudentID = 6;`
      * Verify the entry in `AuditLog`.

4.  **Displaying `inserted` and `deleted` (Simple Trigger):**

      * Create a temporary trigger named `TR_Enrollment_Debug` on the `Enrollments` table, `FOR UPDATE`.
      * Inside this trigger, simply `SELECT * FROM inserted;` and `SELECT * FROM deleted;`.
      * **Test:** Update a grade in `Enrollments`: `UPDATE Enrollments SET Grade = 'B' WHERE StudentID = 3 AND CourseID = 1001;`
      * Observe the output showing the old and new row values.
      * **Cleanup:** `DROP TRIGGER TR_Enrollment_Debug;` after testing.

-----
