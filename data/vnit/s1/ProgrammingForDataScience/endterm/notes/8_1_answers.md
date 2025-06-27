# Programming for Data Science End Term Exam Answers  

---

## **Q1: String Manipulation Tasks**  
### **Task 1.1: Reverse the string using slicing**  
```python
full_name = "John Doe"
reversed_name = full_name[::-1]
print("Reversed Name:", reversed_name)
```

### **Task 1.2: Print first name and last name separated by a tab**  
```python
first_name, last_name = full_name.split()
print(f"{first_name}\t{last_name}")
```

### **Task 1.3: Count characters in first and last names**  
```python
print(f"First Name Length: {len(first_name)}")
print(f"Last Name Length: {len(last_name)}")
```

### **Task 1.4: List of first letters of every word**  
```python
first_letters = [word[0] for word in full_name.split()]
print("First Letters:", first_letters)
```

### **Task 1.5–1.7: Write results to a text file and close it**  
```python
with open("results.txt", "w") as file:
    file.write(f"Reversed Name: {reversed_name}\n")
    file.write(f"{first_name}\t{last_name}\n")
    file.write(f"First Name Length: {len(first_name)}\n")
    file.write(f"Last Name Length: {len(last_name)}\n")
    file.write("First Letters: " + ", ".join(first_letters) + "\n")
    file.write("Roll Number: 123456\n")
```

---

## **Q2: Python Scripts with Loops, Functions, and Classes**  

### **Task 2.1: Multiply all numbers in a list**  
```python
def multiply_list(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

n = int(input("Enter number of elements: "))
numbers = [int(input(f"Enter element {i+1}: ")) for i in range(n)]
print("Product:", multiply_list(numbers))
```

### **Task 2.2: Remove duplicates from list A**  
```python
def get_unique_elements(lst):
    return list(set(lst))

unique_numbers = get_unique_elements(numbers)
print("Unique Elements:", unique_numbers)
```

### **Task 2.3: Square elements using lambda**  
```python
squared = list(map(lambda x: x**2, unique_numbers))
print("Squared Values:", squared)
```

### **Task 2.4: IndianRupees Class Implementation**  
```python
class IndianRupees:
    colors = ["Yellow", "Gray", "Magenta"]
    values = [200, 500, 2000]

    def __init__(self, color, value):
        self.color = color
        self.value = value

    def __str__(self):
        usd_value = round(self.value / 85, 2)
        return f"I have a {self.color} colored note of Rs {self.value} and it is equal to {usd_value} USD."

# Example usage:
note = IndianRupees("Gray", 500)
print(note)
```

---

## **Q3: Numpy, Pandas, and Plotting**  

### **Task 3.1: NumPy Operations**  
```python
import numpy as np

# Create random array
arr = np.random.randint(1, 10, size=(3, 4))
print("Original Array:\n", arr)

# Sum of all elements
total_sum = np.sum(arr)
print("Sum of All Elements:", total_sum)

# Mean of each column
column_means = np.mean(arr, axis=0)
print("Column Means:", column_means)

# Reshape array
reshaped_arr = arr.reshape(4, 3)
print("Reshaped Array:\n", reshaped_arr)
```

### **Task 3.2: Pandas DataFrame Operations**  
```python
import pandas as pd

# Create DataFrame
df = pd.DataFrame(reshaped_arr, index=['W', 'X', 'Y', 'Z'], columns=['A', 'B', 'C'])
print("DataFrame:\n", df)

# Add column D (row sums)
df['D'] = df.sum(axis=1)
print("DataFrame with Column D:\n", df)

# Replace values
df.replace([lambda x: 1 if x > 5 else (0 if x < 5 else x) for x in df.values], inplace=True)
print("Replaced Values DataFrame:\n", df)

# Columns containing 5
columns_with_5 = [col for col in df.columns if 5 in df[col].values]
print("Columns with 5:", columns_with_5)
```

### **Task 3.3: Line Plot**  
```python
import matplotlib.pyplot as plt

plt.plot(df['D'], marker='o', label='Row Sums')
plt.xlabel('Rows')
plt.ylabel('Sum of D')
plt.title('Row Sum Values')
plt.legend()
plt.show()
```

---

## **Q4: CSV Data Analysis with Pandas**  

### **Task 4.1–4.2: Load and Analyze Data**  
```python
import pandas as pd

# Load dataset
df = pd.read_csv("StudentMarks.csv")
print(df.info())
print(df.describe())
```

### **Task 4.3: Fill missing values with 0**  
```python
df.fillna(0, inplace=True)
```

### **Task 4.4: Add Total Marks Column (max 100)**  
```python
df['Total Marks'] = df.iloc[:, :-1].sum(axis=1).clip(upper=100)
```

### **Task 4.5: Compute Statistics**  
```python
avg_marks = df['Total Marks'].mean()
std_dev = round(df['Total Marks'].std(), 2)
max_marks = df['Total Marks'].max()
min_marks = df['Total Marks'].min()

print(f"Average Marks: {avg_marks}, Std Dev: {std_dev}, Max: {max_marks}, Min: {min_marks}")
```

### **Task 4.6: Add Pass/Fail Column**  
```python
df['Pass/Fail'] = df['Total Marks'].apply(lambda x: 'Pass' if x > 35 else 'Fail')
```

### **Task 4.7–4.8: Visualizations**  
```python
import seaborn as sns

# Count plot
sns.countplot(data=df, x='Pass/Fail', hue='Gender')
plt.title("Pass/Fail by Gender")
plt.show()

# Pie chart
pass_count = df[df['Pass/Fail'] == 'Pass'].shape[0]
fail_count = df[df['Pass/Fail'] == 'Fail'].shape[0]
labels = ['Pass', 'Fail']
sizes = [pass_count, fail_count]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Pass/Fail Distribution")
plt.show()
```

---

## **Q5: Data Analysis Process and Impact**  

### **Data Analysis Process**  
1. **Data Collection**: Gather data from sources (databases, APIs, surveys).  
2. **Data Cleaning**: Handle missing values, remove duplicates, correct errors.  
3. **Exploratory Data Analysis (EDA)**: Use visualizations/statistics to understand patterns.  
4. **Modeling**: Apply statistical or machine learning models for insights.  
5. **Interpretation**: Communicate findings through reports/visuals to stakeholders.  

### **Impact on Future Trends**  
- **Healthcare**: Predictive analytics improves disease detection and treatment personalization (e.g., IBM Watson Health).  
- **Finance**: AI-driven fraud detection systems reduce risks in real-time transactions.  
- **Climate Science**: Data analysis aids in modeling climate change and optimizing renewable energy use.  

### **Real-Life Example**  
Netflix uses data analysis to recommend content based on user behavior, increasing customer retention by 30% (case study: Netflix’s recommendation engine).  

--- 

**All the Best!** 🚀