# **DDL - Database and Table Creation Question**

**Scenario:**

You are tasked with setting up a new database system for a university. The system needs to manage information about students, courses, instructors, and their enrollments. It's crucial to ensure data integrity and establish clear relationships between these entities.

**Question:**

Design and write the SQL Server `CREATE` statements to set up the `UniversityDB` database and the following tables with the specified columns and constraints:

1.  **`Departments` Table:**
    * `DeptID`: A 3-character unique identifier for the department (e.g., 'CSE', 'MEC'). This should be the primary key.
    * `DeptName`: The full name of the department (e.g., 'Computer Science and Engineering'). This must be unique and cannot be empty.
    * `HeadOfDepartment`: An integer representing the `InstructorID` of the department head. This should initially allow NULLs, but later be linked to the `Instructors` table.

2.  **`Instructors` Table:**
    * `InstructorID`: A unique integer identifier for the instructor. This should be the primary key.
    * `FirstName`: The instructor's first name. Cannot be empty.
    * `LastName`: The instructor's last name. Cannot be empty.
    * `Department`: The department the instructor belongs to. This should reference the `DeptName` from the `Departments` table. Allow NULLs initially, but ensure referential integrity if a department is specified.
    * `HireDate`: The date the instructor was hired. Default to the current date if not specified.

3.  **`Students` Table:**
    * `StudentID`: A unique integer identifier for the student. This should be the primary key.
    * `FirstName`: The student's first name. Cannot be empty.
    * `LastName`: The student's last name. Cannot be empty.
    * `DateOfBirth`: The student's date of birth.
    * `Email`: The student's email address. Must be unique.
    * `EnrollmentDate`: The date the student enrolled. Default to the current date.
    * `GPA`: The student's Grade Point Average. Must be a decimal number between 0.00 and 4.00 (inclusive).

4.  **`Courses` Table:**
    * `CourseID`: A unique integer identifier for the course. This should be the primary key.
    * `CourseName`: The full name of the course. Must be unique and cannot be empty.
    * `Credits`: The number of credits for the course. Must be an integer between 1 and 6 (inclusive).
    * `Department`: The department offering the course. This should reference the `DeptName` from the `Departments` table.

5.  **`Enrollments` Table:**
    * `EnrollmentID`: An auto-incrementing integer primary key for each enrollment record, starting from 1.
    * `StudentID`: The ID of the student enrolled. Must reference `StudentID` from the `Students` table. If a student record is deleted, their enrollments should also be deleted (`ON DELETE CASCADE`).
    * `CourseID`: The ID of the course enrolled in. Must reference `CourseID` from the `Courses` table.
    * `InstructorID`: The ID of the instructor for this specific enrollment. Must reference `InstructorID` from the `Instructors` table. Allow NULLs.
    * `EnrollmentDate`: The date of enrollment for this specific course. Default to the current date.
    * `Grade`: The grade received by the student (e.g., 'A', 'B', 'C', 'D', 'F').
    * **Composite Key/Unique Constraint:** Ensure that a student can only enroll in a specific course once.

**Instructions:**

1.  Write the `CREATE DATABASE` statement for `UniversityDB`.
2.  Write the `USE UniversityDB` statement to select your database.
3.  Write the `CREATE TABLE` statements for each of the five tables, incorporating all specified column definitions, primary keys, foreign keys (with `ON DELETE CASCADE` where specified), unique constraints, `NOT NULL` constraints, `CHECK` constraints, and `DEFAULT` values.
4.  If any foreign key relationships require `ALTER TABLE` statements after initial table creation (e.g., linking `HeadOfDepartment` in `Departments` to `Instructors`), include those as well.

---
