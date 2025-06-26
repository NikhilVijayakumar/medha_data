# **Practice Questions: Subqueries & Stored Procedures**

Use the `UniversityDB` and its populated tables (`Students`, `Courses`, `Instructors`, `Enrollments`, `Departments`) to answer the following questions.

## **I. Subqueries**

**A. Non-Correlated Subqueries (often used with `IN`, `NOT IN`, `=`, `<`, `>`, etc.)**

1.  **Filtering with `IN`:**
    * Find the `FirstName` and `LastName` of all students who are enrolled in a course offered by the 'Computer Science and Engineering' department.
    * List the `CourseName` for all courses that have at least one enrollment with a `Grade` of 'A'.

2.  **Filtering with Comparison Operators (`=`, `>`)**
    * Find the `CourseName` of the course with the maximum number of `Credits`.
    * Select all students whose `GPA` is higher than the average `GPA` of all students.

3.  **Using `NOT IN`:**
    * Find the `FirstName` and `LastName` of students who have *not* enrolled in `CourseID` 1001.
    * List the `CourseName` for courses that have *no* enrollments with a `Grade` of 'F'.

**B. Correlated Subqueries (often used with `EXISTS`, `NOT EXISTS`, or for per-row calculations)**

1.  **Using `EXISTS`:**
    * Select the `FirstName`, `LastName`, and `Email` of students who are currently enrolled in *any* course. (This is a "semi-join" equivalent).
    * Find the `CourseName` and `Department` of courses that have at least one enrollment with an `InstructorID` of 101.

2.  **Using `NOT EXISTS`:**
    * Find the `FirstName` and `LastName` of students who have *no* enrollments recorded in the `Enrollments` table. (This is an "anti-join" equivalent).
    * List the `CourseName` for courses that have *no* students enrolled (i.e., no entries in the `Enrollments` table for that course).

3.  **Correlated Subquery for per-row calculation:**
    * For each student, display their `FirstName`, `LastName`, and the total number of courses they are currently enrolled in. (Hint: Use a subquery in the `SELECT` clause that counts enrollments for the *current* student).
    * For each department, list the `Department Name` and the count of instructors working in that specific department.

**C. Subqueries in the `FROM` Clause (Derived Tables / Inline Views)**

1.  **Basic Derived Table:**
    * Create a derived table that lists `StudentID` and the `TotalCoursesEnrolled` for each student. Then, select all students from this derived table who have enrolled in more than 2 courses.
    * Find the `Department Name` and the `AverageCredits` of courses in that department. Use a derived table to calculate the `AverageCredits` per department first, then join it with the `Departments` table.

2.  **Using Derived Table with Ranking:**
    * Find the student with the highest `GPA` in each `EnrollmentYear`. (Hint: Use `ROW_NUMBER()` or `RANK()` inside a derived table, then select the top rank).

## **II. Stored Procedures**

**A. Basic Stored Procedures (No Parameters)**

1.  **Create and Execute:**
    * Create a stored procedure named `GetAllStudents` that returns all columns and rows from the `Students` table.
    * Execute `GetAllStudents`.
2.  **Multiple Select Statements:**
    * Create a stored procedure named `GetUniversityOverview` that returns:
        * All records from the `Students` table.
        * All records from the `Courses` table.
        * All records from the `Instructors` table.
    * Execute `GetUniversityOverview`.
3.  **Simple Calculation/Variable:**
    * Create a stored procedure named `GetTotalCoursesCount` that declares an integer variable, assigns the total count of courses to it, and then prints a message like "Total number of courses: [Count]".
    * Execute `GetTotalCoursesCount`.

**B. Parameterized Stored Procedures**

1.  **Filtering by ID:**
    * Create a stored procedure named `GetStudentDetails` that accepts a `StudentID` (INT) as an input parameter and returns all details for that specific student.
    * Execute `GetStudentDetails` for `StudentID` 5.
2.  **Filtering by String/Date:**
    * Create a stored procedure named `GetCoursesByDepartment` that accepts a `DepartmentName` (VARCHAR(100)) as an input parameter and returns all courses belonging to that department.
    * Execute `GetCoursesByDepartment` for 'Electrical Engineering'.
    * Create a stored procedure named `GetEnrollmentsAfterDate` that accepts an `EnrollmentDateThreshold` (DATE) as an input parameter and returns all enrollments that occurred on or after that date.
    * Execute `GetEnrollmentsAfterDate` for '2023-09-10'.
3.  **Conditional Logic/More Complex Filtering:**
    * Create a stored procedure named `GetStudentsByGPA` that accepts a `MinGPA` (DECIMAL(3,2)) and an optional `MaxGPA` (DECIMAL(3,2)) as input parameters.
        * If only `MinGPA` is provided, return students with `GPA` greater than or equal to `MinGPA`.
        * If both `MinGPA` and `MaxGPA` are provided, return students with `GPA` between `MinGPA` and `MaxGPA` (inclusive).
    * Execute `GetStudentsByGPA` with `MinGPA` 3.5.
    * Execute `GetStudentsByGPA` with `MinGPA` 3.0 and `MaxGPA` 3.7.

**C. Modifying and Deleting Stored Procedures**

1.  **`ALTER PROCEDURE`:**
    * Modify the `GetStudentDetails` stored procedure (created earlier) to also include the `CourseName` of all courses the student is enrolled in. (You'll need a `JOIN` inside the procedure).
    * Execute the modified `GetStudentDetails` for `StudentID` 1.
2.  **`DROP PROCEDURE`:**
    * Drop the `GetUniversityOverview` stored procedure.
    * Verify that it has been dropped (e.g., by trying to execute it or checking `sys.procedures`).

---
