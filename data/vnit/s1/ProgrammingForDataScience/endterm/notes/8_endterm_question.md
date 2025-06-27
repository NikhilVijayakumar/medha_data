# Programming for Data Science End Term Exam  
**Course Code:** ECL – 536 | **Date:** 21/12/2024  
**Class:** M.Tech. in AAI, 1st Sem., Cohort-2 | **Time:** 10:00AM–01:00PM  
**Max. Marks:** 50 | **Session:** Winter 2024  

---

## Important Instructions  
1. All questions are compulsory.  
2. Clearly state the assumptions made while answering. Please, attempt the questions on your understanding.  

---

## Question 1 (CO1)  
Create a string containing your full name and write Python scripts to perform the following tasks:  

### Tasks  
- **Task 1.1:** Reverse the string using slicing.  
- **Task 1.2:** Print the first name and last name separated by a tab in a single line.  
- **Task 1.3:** Determine the number of characters in the first name and in the last name.  
- **Task 1.4:** Create a list of the first letters of every word in the string.  
- **Task 1.5:** Open and write results obtained in the above tasks onto a text file.  
- **Task 1.6:** Write your roll number in the next line of the same text file.  
- **Task 1.7:** Close the file.  

**Marks Distribution:** [1 + 1 + 1 + 2 + 2 + 2 + 1]  

---

## Question 2 (CO2)  
Write a Python script that incorporates `if` statements, `for` loops, and user input to perform the following tasks:  

### Tasks  
- **Task 2.1:** Create a list `A` of `n` numbers and write a Python function to multiply all the numbers in a list:  
  1. Take the integer input value of `n` by the user.  
  2. Take the input of all `n` numbers by the user.  
  3. Create a function that multiplies all the numbers of the list.  

- **Task 2.2:** Write a Python function to return a new list `B` with unique elements of the list `A`.  

- **Task 2.3:** Use a lambda expression to get the square of each element of the list `B`.  

- **Task 2.4:** Fill in the `IndianRupees` class to accept color (Yellow, Gray, Magenta) of the Indian note and their values in INR (200, 500, 2000) [let 1 USD = 85 INR], and return the following statement:  
  > “I have a Gray colored note of Rs 500 and it is equal to 5.88 USD.”  

```python
class IndianRupees:
    colors = []
    values = []

    def __init__(self):
        pass

    def __str__(self):
        pass
```

**Marks Distribution:** [2 + 2 + 2 + 4]  

---

## Question 3 (CO3, CO5)  
Write a Python script considering suitable examples to demonstrate the required operations. Import libraries `numpy` and `pandas`, and perform the following tasks:  

### Tasks  
- **Task 3.1:** Using NumPy:  
  1. Create a 2D array of shape (3, 4) with random integers ranging from 1 to 9.  
  2. Find the sum of all elements in the array.  
  3. Calculate the mean of each column.  
  4. Reshape the array into a shape of (4, 3).  

- **Task 3.2:** Using Pandas:  
  1. Create a DataFrame from the reshaped array. Assign column names as `A`, `B`, and `C`, and index as `W`, `X`, `Y`, and `Z`.  
  2. Create a new column `D` in the DataFrame containing each row’s sum values.  
  3. Replace all values greater than 5 with `1`, less than 5 with `0`, and keep `5` as it is.  
  4. Identify and display the columns that contain the term `5`.  

- **Task 3.3:** Write a Python script to get the line plot for the sum of values obtained in column `D` for each row. Ensure legends, labels, and title are displayed.  

**Marks Distribution:** [4 + 4 + 2]  

---

## Question 4 (CO4, CO5)  
Consider the following data in a CSV file named `StudentMarks.csv`:  

### Tasks  
- **Task 4.1:** Import all the required libraries.  
- **Task 4.2:** Load the dataset and show the information contained in the DataFrame (e.g., count, mean, max, etc.).  
- **Task 4.3:** Fill the missing values in marks with `0`.  
- **Task 4.4:** Create a new column for Total Marks (100) and add it to the DataFrame.  
- **Task 4.5:** Find the average marks of the class, standard deviation (up to 2 decimal places), maximum, and minimum marks obtained by the students.  
- **Task 4.6:** Create a new column for `Pass/Fail`, indicating student `Pass` if Total Marks is greater than 35; otherwise, `Fail`.  
- **Task 4.7:** Plot a count plot to show the comparison of the number of students Pass/Fail on Gender basis.  
- **Task 4.8:** Plot a pie chart to show the percentage of Pass/Fail students.  

**Marks Distribution:** [1 + 1 + 1 + 1 + 1 + 2 + 2 + 1]  

---

## Question 5 (CO3)  
Provide a detailed explanation of the data analysis process. Discuss how mastering data analysis skills can impact future trends in technology and innovation. Explain with a case-study or real-life examples.  

**Marks Distribution:** [5 + 5]  

---

**All the Best!** 🚀