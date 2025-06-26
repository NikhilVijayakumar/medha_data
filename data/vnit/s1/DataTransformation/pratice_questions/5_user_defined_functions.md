# **Practice Questions: User-Defined Functions (UDFs) & Indexing**

Use the `UniversityDB` and its populated tables (`Students`, `Courses`, `Instructors`, `Enrollments`, `Departments`) to answer the following questions.

## **I. User-Defined Functions (UDFs)**

**A. Scalar Functions**

1.  **Student Full Name Function:**
    * Create a scalar function named `GetStudentFullName` that takes `FirstName` (VARCHAR(50)) and `LastName` (VARCHAR(50)) as input.
    * The function should concatenate these two names with a space in between and return the full name as a `VARCHAR(101)`.
    * Use this function in a `SELECT` statement to display the `StudentID` and the full name for all students from the `Students` table.

2.  **Enrollment Grade Category:**
    * Create a scalar function named `GetGradeCategory` that takes a `Grade` (CHAR(1)) as input.
    * The function should return a `VARCHAR(20)` category based on the grade:
        * 'Excellent' for 'A'
        * 'Good' for 'B'
        * 'Satisfactory' for 'C'
        * 'Needs Improvement' for 'D'
        * 'Failed' for 'F'
        * 'Unknown' for any other value.
    * Use this function in a `SELECT` statement to display `EnrollmentID`, `Grade`, and the `GradeCategory` for all enrollments.

3.  **Instructor Tenure (Years):**
    * Create a scalar function named `CalculateInstructorTenure` that takes `HireDate` (DATE) as input.
    * The function should return an `INT` representing the number of full years the instructor has been employed (based on `GETDATE()`).
    * Use this function in a `SELECT` statement to display `InstructorID`, `FirstName`, `LastName`, and their `TenureInYears`.

4.  **Course Credit Descriptor:**
    * Create a scalar function named `GetCourseCreditDescriptor` that takes `Credits` (INT) as input.
    * Return a `VARCHAR(50)` describing the credit load:
        * 'Full Load Course' if Credits >= 4
        * 'Standard Course' if Credits = 3
        * 'Light Load Course' if Credits < 3
    * Use this function to select `CourseName`, `Credits`, and `CreditDescriptor` for all courses.

**B. Table-Valued Functions (TVFs)**

1.  **Inline Table-Valued Function (iTVF) - Students by Year:**
    * Create an inline table-valued function named `GetStudentsEnrolledInYear` that takes `EnrollmentYear` (INT) as input.
    * The function should return a table containing `StudentID`, `FirstName`, `LastName`, and `EnrollmentDate` for all students who enrolled in the specified year.
    * Call this function to get all students enrolled in 2020.
    * Join the result of this function with the `Enrollments` table to see which courses these students enrolled in.

2.  **Inline Table-Valued Function (iTVF) - Courses by Department:**
    * Create an inline table-valued function named `GetCoursesByDept` that takes `DepartmentName` (VARCHAR(100)) as input.
    * The function should return all columns for courses belonging to that department.
    * Call this function to get courses from the 'Mechanical Engineering' department.

3.  **Multi-Statement Table-Valued Function (mTVF) - Enrollment Summary per Student:**
    * Create a multi-statement table-valued function named `GetStudentEnrollmentSummary` that takes `StudentID` (INT) as input.
    * The function should return a table with the following columns:
        * `CourseName` (VARCHAR(100))
        * `InstructorFullName` (VARCHAR(101) - combine first and last name)
        * `EnrollmentGrade` (CHAR(1))
    * Populate this table variable by joining `Enrollments`, `Courses`, and `Instructors` tables based on the input `StudentID`.
    * Call this function for `StudentID` 1.

## **II. Indexing**

**A. Understanding Index Impact (SET STATISTICS IO ON)**

1.  **Before Index:**
    * Turn on `SET STATISTICS IO ON;`.
    * Execute the following query: `SELECT * FROM Students WHERE LastName LIKE 'S%';`
    * Note the "Logical reads" and "Physical reads" in the Messages tab.

2.  **Create Non-Clustered Index:**
    * Create a non-clustered index named `IX_Students_LastName` on the `LastName` column of the `Students` table.
    * `CREATE NONCLUSTERED INDEX IX_Students_LastName ON Students(LastName ASC);`

3.  **After Index:**
    * Execute the same query again: `SELECT * FROM Students WHERE LastName LIKE 'S%';`
    * Compare the "Logical reads" and "Physical reads" to the previous execution. Explain the difference you observe. (Expect a decrease in reads).

**B. Clustered vs. Non-Clustered Indexes**

1.  **Identifying Existing Clustered Index:**
    * Use `sys.indexes` to find out if the `Students` table already has a clustered index. What column is it on? (It should be on `StudentID` because it's the `PRIMARY KEY`).

2.  **Attempting to Create a Second Clustered Index (and understanding why it fails):**
    * Try to create a clustered index on the `FirstName` column of the `Students` table.
    * What error message do you receive? Explain why this error occurs.
    * **DO NOT commit this change if it succeeds, as it will physically reorder your table.** (It won't succeed due to the existing primary key clustered index).

3.  **Creating a Non-Clustered Index on a Commonly Filtered Column:**
    * Create a non-clustered index named `IX_Courses_Credits_Department` on the `Credits` column (ASC) and `Department` column (ASC) of the `Courses` table.
    * Explain why this index might be beneficial for queries filtering courses by `Credits` and `Department`.

**C. Viewing Indexes and Tables**

1.  **List All Indexes on `Students` Table:**
    * Write a query using `sys.indexes` and `sys.tables` to list all indexes currently defined on the `Students` table. Include `IndexName`, `IndexType`, and whether it's `is_unique`.

2.  **List All Tables in `UniversityDB`:**
    * Write a simple query to list all user tables in your current `UniversityDB` database.

**D. Index Management (Bonus - Conceptual/Syntax only for Exam)**

1.  **`ALTER FUNCTION` (Conceptual):**
    * Suppose you wanted to modify the `GetGradeCategory` function to also recognize 'E' as 'Needs Improvement'. Describe conceptually how you would use `ALTER FUNCTION` to achieve this. (No code needed, just the idea).

2.  **`SP_RENAME` (Conceptual):**
    * You decide that `GetStudentFullName` is too long and want to rename it to `GetFullStudentName`. Explain the SQL command you would use. What is an important caution to remember after renaming?

---
