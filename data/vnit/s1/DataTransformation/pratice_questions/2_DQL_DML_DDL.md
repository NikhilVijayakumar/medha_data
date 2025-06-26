It's great you're diving deep into SQL Server for your exam\! This comprehensive request covers a lot of ground, and I'll do my best to provide you with a solid foundation for practice.

Instead of just giving you questions, I'll provide you with a structured learning path:

1.  **Schema Definition (DDL):** I'll give you `CREATE TABLE` statements for a few tables, along with various constraints.
2.  **Sample Data (DML - INSERT):** I'll provide `INSERT` statements with enough data for you to practice all your DQL and Join concepts.
3.  **Practice Questions (DQL, DML, TCL, DDL - Alter/Drop):** I'll then give you a series of questions that guide you through applying each concept you mentioned.
4.  **Explanation of Semi/Anti Joins and Minus:** Since `MINUS` isn't a direct SQL Server keyword, I'll explain how to achieve its functionality.

-----



-----

### 3\. Practice Questions

Now, let's get to the practice questions. I'll categorize them by the concepts you want to cover.

**Before you start:** Execute all the `CREATE TABLE` and `INSERT` statements in your SQL Server environment.

-----

#### DQL - Basic `SELECT` and Conditional Operators (`=`, `<`, `>`, `<=`, `>=`, `!=`)

1.  Select all columns from the `Students` table.
2.  Retrieve the `FirstName` and `LastName` of all students.
3.  Find all students whose `GPA` is exactly `3.50`.
4.  List students whose `DateOfBirth` is before January 1, 2001.
5.  Show students who enrolled on or after September 1, 2021.
6.  Find all courses with more than 3 `Credits`.
7.  Display instructors who were hired before 2015.
8.  Select all enrollments where the `Grade` is not 'A'.

-----

#### DQL - Logical Operators (`AND`, `OR`, `NOT`)

1.  Find students whose `GPA` is greater than `3.00` AND `EnrollmentDate` is in the year 2020.
2.  List courses that are either in the 'Computer Science and Engineering' department OR have 3 `Credits`.
3.  Select students whose `FirstName` is 'John' OR `LastName` is 'Smith'.
4.  Find instructors who are NOT in the 'Computer Science and Engineering' department.
5.  Retrieve students whose `GPA` is between `3.00` and `3.50` (inclusive). (Hint: You can use `AND` here, or `BETWEEN`).

-----

#### DQL - Range (`BETWEEN`, `NOT BETWEEN`)

1.  Select students whose `DateOfBirth` is between January 1, 2000, and December 31, 2001.
2.  Find courses with `Credits` not between 3 and 4.
3.  List enrollments that occurred between '2023-09-01' and '2023-09-10'.

-----

#### DQL - Pattern Matching (`LIKE`, `NOT LIKE`, `%`, `_`)

1.  Find students whose `FirstName` starts with 'A'.
2.  Select courses whose `CourseName` contains the word 'Database'.
3.  List instructors whose `LastName` ends with 's'.
4.  Find students whose `Email` address has 'example' as the domain.
5.  Select departments whose `DeptName` has 'Engineering' as the second word (e.g., "Mechanical Engineering"). (Hint: Use `_` for single characters).
6.  Find instructors whose `LastName` does not start with 'S'.

-----

#### DQL - List (`IN`, `NOT IN`)

1.  Select students whose `StudentID` is 1, 3, or 5.
2.  Find courses that are in the 'Computer Science and Engineering' OR 'Mathematics' departments.
3.  List enrollments where the `Grade` is 'C', 'D', or 'F'.
4.  Show instructors who are NOT in the 'Computer Science and Engineering' department AND NOT in the 'Electrical Engineering' department.
5.  Retrieve students who have not enrolled in CourseID 1001 or 1002.

-----

#### DQL - Aggregate Functions (`SUM`, `COUNT`, `AVG`, `MIN`, `MAX`)

1.  Count the total number of students.
2.  Find the average `GPA` of all students.
3.  Get the minimum and maximum `Credits` for all courses.
4.  Count the number of enrollments.
5.  What is the highest `GPA` among students who enrolled in 2020?
6.  How many courses are in the 'Computer Science and Engineering' department?
7.  What is the earliest `HireDate` among instructors?

-----

#### DQL - Sorting (`ORDER BY`)

1.  List all students, ordered by `LastName` in ascending order.
2.  Show courses, ordered by `Credits` in descending order, and then by `CourseName` in ascending order.
3.  Retrieve enrollments, ordered by `EnrollmentDate` in ascending order, and then by `Grade` in descending order.
4.  Select the top 3 students with the highest `GPA`.

-----

#### DQL - Limiting Results (`TOP`)

1.  Get the `FirstName` and `LastName` of the top 5 students.
2.  Find the top 2 courses with the most credits.
3.  Select the top 1 enrollment by `Grade` (assuming 'A' is highest).

-----

#### DQL - Grouping (`GROUP BY`, `HAVING`)

1.  Count the number of students per `EnrollmentDate`.
2.  Find the average `GPA` for students grouped by their `EnrollmentDate`.
3.  Display the number of courses per `Department`, but only for departments that have more than 2 courses.
4.  List the `Department` and the `COUNT` of instructors, showing only departments with at least 2 instructors.
5.  For each `CourseID`, find the average `Grade` (you'll need to convert grades to numeric values for this, or just count them per grade). *Self-correction: Calculating average grade for `CHAR` is tricky. Let's rephrase:* For each `CourseID`, count the number of students who received an 'A' grade.
6.  Find the `StudentID` and the `COUNT` of courses they are enrolled in, for students enrolled in more than 2 courses.

-----

#### DQL - Joins (`INNER`, `LEFT`, `RIGHT`, `FULL`, `CROSS`, `SELF`, `SEMI/ANTI`)

**Note on Semi/Anti Joins:** SQL Server doesn't have direct `SEMI` or `ANTI` join keywords. You achieve this functionality using `EXISTS`/`NOT EXISTS` or `IN`/`NOT IN` with subqueries.

1.  **INNER JOIN:** List all students and the courses they are enrolled in.
2.  **INNER JOIN (Three Tables):** Show student `FirstName`, `LastName`, `CourseName`, and `Grade` for all enrollments.
3.  **LEFT JOIN:** Display all students and any courses they are enrolled in. Include students who are not enrolled in any courses.
4.  **RIGHT JOIN:** List all courses and any students enrolled in them. Include courses that have no enrollments.
5.  **FULL OUTER JOIN:** Show all students and all courses, matching where enrollments exist, and showing nulls where there's no match in either table.
6.  **CROSS JOIN:** Generate all possible combinations of students and courses. (Be careful with the number of results\!)
7.  **SELF JOIN:** Find pairs of students who enrolled on the same `EnrollmentDate`.
8.  **SEMI JOIN (using `EXISTS`):** Find students who have enrolled in at least one course. (Equivalent to `INNER JOIN` on `StudentID` then `DISTINCT`, but `EXISTS` is often more efficient for just checking existence).
      * *Question:* Select the `FirstName` and `LastName` of students who are enrolled in *any* course.
9.  **ANTI JOIN (using `NOT EXISTS`):** Find students who have *not* enrolled in any course.
      * *Question:* Select the `FirstName` and `LastName` of students who are *not* enrolled in any course.
10. **SEMI JOIN (using `IN`):** Find instructors who are teaching at least one course.
      * *Question:* Select the `FirstName` and `LastName` of instructors who are assigned to teach an enrollment.
11. **ANTI JOIN (using `NOT IN`):** Find instructors who are not currently assigned to teach any enrollment.
      * *Question:* Select the `FirstName` and `LastName` of instructors who are *not* assigned to teach any enrollment.

-----

#### DQL - Set Operations (`UNION`, `INTERSECT`, `EXCEPT`)

**Note on `MINUS`:** SQL Server uses `EXCEPT` for the functionality of `MINUS`.

1.  **UNION:** Combine the `FirstName` and `LastName` of all students and instructors into a single list.
2.  **UNION ALL:** Same as above, but allow duplicate names.
3.  **INTERSECT:** Find the names (First and Last) that appear in both the `Students` table and the `Instructors` table (unlikely with this data, but for concept).
4.  **EXCEPT (MINUS):** Find students who have not received a grade of 'A' in any course. (Hint: Select all students, then `EXCEPT` students who have an 'A').
      * *Question:* List the `StudentID` of students who have enrolled in a course but have *not* achieved a 'B' grade in any course. (This will be a bit more complex, involving `EXCEPT` on `StudentID`s).
      * *Alternative `EXCEPT` Question:* Select `CourseID`s that have enrollments but are not taught by InstructorID 101.

-----

#### DML - `UPDATE`, `DELETE`

1.  **UPDATE:** Change the `Email` of 'John Doe' to 'john.doe.new@example.com'.
2.  **UPDATE:** Increase the `GPA` of all students who enrolled in 2021 by 0.1 (ensure `GPA` stays within 0.00-4.00 range using `CHECK` constraint).
3.  **UPDATE:** Set the `Department` of Instructor 'Ivy Queen' to 'Computer Science and Engineering'.
4.  **DELETE:** Delete the student with `StudentID` 9 (Frank Moore). Observe the `ON DELETE CASCADE` effect on enrollments.
5.  **DELETE:** Delete all courses that have 3 `Credits`.

-----

#### TCL - `COMMIT`, `ROLLBACK`, `SAVEPOINT`

1.  **Transaction 1 (COMMIT):**

      * Start a transaction.
      * Insert a new student: `(12, 'Zara', 'Khan', '2003-01-01', 'zara.khan@example.com', GETDATE(), 3.50)`.
      * Commit the transaction.
      * Verify the insertion.

2.  **Transaction 2 (ROLLBACK):**

      * Start a transaction.
      * Update the `GPA` of all students to `2.00`.
      * Rollback the transaction.
      * Verify that the `GPA` values are unchanged.

3.  **Transaction 3 (SAVEPOINT):**

      * Start a transaction.
      * Insert a new course: `(6001, 'Advanced SQL', 3, 'Computer Science and Engineering')`.
      * Create a `SAVEPOINT` named `BeforeDelete`.
      * Delete all enrollments where the `Grade` is 'F'.
      * Rollback to `BeforeDelete`.
      * Verify that the new course is still there, but the 'F' grade enrollments are back. (This might be tricky, as `DELETE` might not be reverted by `ROLLBACK TO SAVEPOINT` if the transaction is not committed. `ROLLBACK` will revert all changes since `BEGIN TRAN`).

    *Self-correction for `SAVEPOINT` clarity:*
    When you `ROLLBACK TO SAVEPOINT`, it undoes changes *after* the `SAVEPOINT` but does not end the transaction.
    Let's refine the `SAVEPOINT` example:

      * Start a transaction.
      * Insert a new student: `(13, 'Leo', 'Singh', '2004-05-10', 'leo.singh@example.com', GETDATE(), 3.00)`.
      * Create a `SAVEPOINT` named `S1`.
      * Insert a new enrollment for `Leo Singh` into `CourseID 1001` with `Grade 'B'`.
      * `ROLLBACK TRANSACTION S1;`
      * Verify that the enrollment for Leo Singh is gone, but Leo Singh himself is still in the `Students` table (because the `SAVEPOINT` was after his insertion).
      * `COMMIT TRANSACTION;`

-----

#### DDL - `ALTER TABLE`, `DROP TABLE`

1.  **ALTER TABLE (Add Column):** Add a `PhoneNumber` column (VARCHAR(20)) to the `Students` table.
2.  **ALTER TABLE (Modify Column):** Change the `Credits` column in the `Courses` table to allow `DECIMAL(3,1)`. (Be careful, if you have existing integer data, it might truncate or error).
3.  **ALTER TABLE (Drop Column):** Remove the `GPA` column from the `Students` table.
4.  **ALTER TABLE (Add Constraint):** Add a `CHECK` constraint to the `Instructors` table ensuring `HireDate` is not in the future.
5.  **ALTER TABLE (Drop Constraint):** Drop the `UQ_Student_Course` constraint from the `Enrollments` table.
6.  **DROP TABLE:** Drop the `Departments` table. (Note: This will fail if there are foreign key dependencies. You might need to drop dependent foreign keys first or use `CASCADE`).

-----

**Important Notes for your Exam:**

  * **Syntax:** Pay close attention to SQL Server syntax (e.g., `TOP` instead of `LIMIT`).
  * **Data Types:** Understand when to use `VARCHAR`, `INT`, `DATE`, `DECIMAL`, etc.
  * **Constraints:** Remember the purpose of each constraint (`PRIMARY KEY`, `FOREIGN KEY`, `NOT NULL`, `UNIQUE`, `CHECK`, `DEFAULT`).
  * **Joins:** Visualize how data is combined with different join types. Drawing Venn diagrams can be helpful.
  * **Aggregate Functions & `GROUP BY`/`HAVING`:** Understand that aggregate functions operate on groups, and `HAVING` filters those groups.
  * **Transactions:** Grasp the ACID properties and how `COMMIT`, `ROLLBACK`, and `SAVEPOINT` help maintain data integrity.

