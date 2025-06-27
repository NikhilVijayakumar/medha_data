# Pandas Details: Common Use Cases

Pandas is a powerful, flexible, and easy-to-use open-source data analysis and manipulation library for Python. It provides high-performance, easy-to-use data structures and data analysis tools, making it indispensable for tasks ranging from data cleaning and transformation to analysis and visualization.

**Common Import Convention:**

```python
import pandas as pd
import numpy as np # Often used alongside Pandas for numerical operations
```

### 1\. Core Data Structures: Series and DataFrame

Pandas introduces two primary data structures:

#### 1.1. Series

A **Series** is a one-dimensional labeled array capable of holding any data type (integers, strings, floats, Python objects, etc.). It's essentially a column or a row in a DataFrame.

**Creating a Series:**

```python
# From a list
s1 = pd.Series([1, 3, 5, np.nan, 6, 8])
print("Series from list:\n", s1)

# From a dictionary (keys become index)
s2 = pd.Series({'a': 10, 'b': 20, 'c': 30})
print("\nSeries from dictionary:\n", s2)

# With a custom index
s3 = pd.Series([10, 20, 30], index=['x', 'y', 'z'])
print("\nSeries with custom index:\n", s3)
```

#### 1.2. DataFrame

A **DataFrame** is a two-dimensional labeled data structure with columns of potentially different types. It's the most commonly used Pandas object, analogous to a spreadsheet, SQL table, or a dictionary of Series objects.

**Creating a DataFrame:**

```python
# From a dictionary of lists/arrays (common)
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 28],
    'City': ['New York', 'London', 'Paris', 'New York'],
    'Salary': [70000, 80000, 95000, 72000]
}
df1 = pd.DataFrame(data)
print("DataFrame from dictionary:\n", df1)

# From a NumPy array
dates = pd.date_range('20230101', periods=6)
df2 = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print("\nDataFrame from NumPy array with custom index and columns:\n", df2)

# From a list of dictionaries
data_list = [
    {'Name': 'Eve', 'Age': 22},
    {'Name': 'Frank', 'Age': 31, 'City': 'Berlin'}
]
df3 = pd.DataFrame(data_list)
print("\nDataFrame from list of dictionaries:\n", df3)
```

### 2\. Data Inspection and Basic Information

Understanding your data's structure and contents.

  * **`.head(n)`:** Returns the first `n` rows (default 5).
  * **`.tail(n)`:** Returns the last `n` rows (default 5).
  * **`.info()`:** Prints a concise summary of a DataFrame, including data types and non-null values.
  * **`.describe()`:** Generates descriptive statistics of the DataFrame's numerical columns (count, mean, std, min, max, quartiles).
  * **`.shape`:** Returns a tuple representing the dimensions (rows, columns) of the DataFrame.
  * **`.index`:** The row labels of the DataFrame.
  * **`.columns`:** The column labels of the DataFrame.
  * **`.dtypes`:** Returns a Series with the data type of each column.
  * **`.value_counts()` (Series method):** Returns a Series containing counts of unique values.

<!-- end list -->

```python
print("\n--- Data Inspection ---")
print("df1.head():\n", df1.head(2))
print("\ndf1.info():")
df1.info()
print("\ndf1.describe():\n", df1.describe())
print("\ndf1.shape:", df1.shape)
print("\ndf1.columns:", df1.columns)
print("\ndf1['City'].value_counts():\n", df1['City'].value_counts())
```

### 3\. Data Selection and Indexing

How to access specific rows, columns, or cells.

  * **Column Selection:** Using dictionary-like notation (`df['column_name']`) or attribute access (`df.column_name`).
  * **`.loc[]`:** Label-based indexing (select by row/column labels).
  * **`.iloc[]`:** Integer-location based indexing (select by row/column integer positions).
  * **Boolean Indexing:** Selecting data based on a boolean condition.

<!-- end list -->

```python
print("\n--- Data Selection & Indexing ---")
# Select a single column
print("df1['Name']:\n", df1['Name'])

# Select multiple columns
print("\ndf1[['Name', 'Age']]:\n", df1[['Name', 'Age']])

# Select rows by label using .loc[]
print("\ndf1.loc[0]:\n", df1.loc[0])
print("\ndf1.loc[0:2, 'Name':'City']:\n", df1.loc[0:2, 'Name':'City']) # Rows 0,1,2 and columns Name,Age,City

# Select rows by integer position using .iloc[]
print("\ndf1.iloc[0]:\n", df1.iloc[0])
print("\ndf1.iloc[0:2, 0:3]:\n", df1.iloc[0:2, 0:3]) # Rows 0,1 and columns 0,1,2

# Boolean Indexing: Select rows where Age > 28
print("\nPeople older than 28:\n", df1[df1['Age'] > 28])

# Combined conditions
print("\nPeople from New York older than 25:\n", df1[(df1['City'] == 'New York') & (df1['Age'] > 25)])
```

### 4\. Handling Missing Data (NaN)

Missing data is common and Pandas provides robust tools to manage it.

  * **`np.nan`:** Represents missing data.
  * **`.isnull()` / `.isna()`:** Returns a boolean DataFrame indicating `NaN` values.
  * **`.notnull()`:** Returns a boolean DataFrame indicating non-`NaN` values.
  * **`.dropna(axis=0/1, how='any'/'all')`:** Removes rows or columns with `NaN` values.
  * **`.fillna(value, method='ffill'/'bfill')`:** Fills `NaN` values.

<!-- end list -->

```python
print("\n--- Handling Missing Data ---")
df_missing = pd.DataFrame({
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, np.nan, 8],
    'C': [9, 10, 11, 12]
})
print("Original DataFrame with NaNs:\n", df_missing)

print("\ndf_missing.isnull():\n", df_missing.isnull())

# Drop rows with any NaN
print("\nAfter dropping rows with any NaN:\n", df_missing.dropna())

# Drop columns with any NaN
print("\nAfter dropping columns with any NaN:\n", df_missing.dropna(axis=1))

# Fill NaN with a specific value
print("\nAfter filling NaN with 0:\n", df_missing.fillna(0))

# Fill NaN with the mean of the column
print("\nAfter filling NaN in 'A' with mean of 'A':\n",
      df_missing['A'].fillna(df_missing['A'].mean()))

# Forward fill (propagates last valid observation forward)
print("\nAfter forward fill:\n", df_missing.fillna(method='ffill'))

# Backward fill (propagates next valid observation backward)
print("\nAfter backward fill:\n", df_missing.fillna(method='bfill'))
```

### 5\. Data Cleaning and Transformation

Essential for preparing data for analysis.

  * **`.drop()`:** Remove specified rows or columns.
  * **`.rename()`:** Change labels of index or columns.
  * **`.replace()`:** Replace specific values.
  * **`.map()` (Series method):** Substitute each value in a Series with another value.
  * **`.apply()`:** Apply a function along an axis of the DataFrame or Series.
  * **`duplicated()` / `drop_duplicates()`:** Identify and remove duplicate rows.

<!-- end list -->

```python
print("\n--- Data Cleaning & Transformation ---")
# Dropping columns
df_cleaned = df1.drop(columns=['City'])
print("df1 after dropping 'City' column:\n", df_cleaned)

# Renaming columns
df_renamed = df1.rename(columns={'Name': 'Full Name', 'Age': 'Years Old'})
print("\ndf1 after renaming columns:\n", df_renamed)

# Replacing values
df_replaced = df1.replace('New York', 'NYC')
print("\ndf1 after replacing 'New York' with 'NYC':\n", df_replaced)

# Using .map() for categorical mapping
gender_map = {'Male': 'M', 'Female': 'F'}
df_gender = pd.DataFrame({'Gender': ['Male', 'Female', 'Male', 'Female']})
df_gender['Gender_Code'] = df_gender['Gender'].map(gender_map)
print("\nDataFrame with mapped gender codes:\n", df_gender)

# Using .apply()
df1['Salary_USD'] = df1['Salary'].apply(lambda x: x / 83) # Assuming 1 USD = 83 INR
print("\ndf1 with Salary in USD (using apply):\n", df1)

# Duplicates
df_dups = pd.DataFrame({'A': [1, 2, 2, 3], 'B': ['x', 'y', 'y', 'z']})
print("\nDataFrame with duplicates:\n", df_dups)
print("Duplicated rows:\n", df_dups.duplicated())
print("After dropping duplicates:\n", df_dups.drop_duplicates())
print("After dropping duplicates based on 'A':\n", df_dups.drop_duplicates(subset=['A']))
```

### 6\. Combining DataFrames (Merge, Join, Concat)

Connecting multiple DataFrames.

  * **`pd.merge()`:** Combine DataFrames based on common columns or indices (SQL-like joins).
      * `how`: `'inner'`, `'outer'`, `'left'`, `'right'`.
      * `on`: Column(s) to merge on.
      * `left_on`/`right_on`: Different column names for keys.
      * `left_index`/`right_index`: Use index as merge key.
  * **`.join()` (DataFrame method):** Combine DataFrames based on their indices. Often more concise for index-based merges.
  * **`pd.concat()`:** Stack or append Series or DataFrames along an axis.

<!-- end list -->

```python
print("\n--- Combining DataFrames ---")
df_orders = pd.DataFrame({
    'CustomerID': [1, 2, 3, 4],
    'OrderID': ['A1', 'A2', 'A3', 'A4']
})
df_customers = pd.DataFrame({
    'CustomerID': [1, 2, 5],
    'Name': ['Alice', 'Bob', 'Eve']
})

# pd.merge() - Inner merge (default)
merged_df_inner = pd.merge(df_orders, df_customers, on='CustomerID')
print("Inner Merge:\n", merged_df_inner)

# Left merge (keep all from left)
merged_df_left = pd.merge(df_orders, df_customers, on='CustomerID', how='left')
print("\nLeft Merge:\n", merged_df_left)

# pd.concat() - Stacking rows (axis=0)
s_new = pd.Series([9, 10, 11])
concatenated_s = pd.concat([s1, s_new])
print("\nConcatenated Series:\n", concatenated_s)

df_more_data = pd.DataFrame({
    'Name': ['Grace', 'Henry'],
    'Age': [40, 29],
    'City': ['Tokyo', 'London'],
    'Salary': [100000, 75000]
})
concatenated_df_rows = pd.concat([df1, df_more_data], ignore_index=True)
print("\nConcatenated DataFrames (rows):\n", concatenated_df_rows)

# Concatenating columns (axis=1) - make sure indices align or handle carefully
df_contact = pd.DataFrame({
    'Email': ['alice@example.com', 'bob@example.com', 'charlie@example.com', 'david@example.com']
}, index=df1.index) # Align index for correct column wise concatenation

concatenated_df_cols = pd.concat([df1, df_contact], axis=1)
print("\nConcatenated DataFrames (columns):\n", concatenated_df_cols)

# Using keys for MultiIndex during concat
concatenated_with_keys = pd.concat([df1, df_more_data], keys=['Original', 'New'], ignore_index=False)
print("\nConcatenated with MultiIndex keys:\n", concatenated_with_keys)
print(concatenated_with_keys.loc['New']) # Access data from 'New' source
```

### 7\. Grouping and Aggregation (`groupby()`)

The `groupby()` method is one of the most powerful features in Pandas for performing "split-apply-combine" operations.

```python
print("\n--- Grouping and Aggregation ---")
# Group by 'City' and calculate the mean age and sum salary for each city
grouped_city = df1.groupby('City').agg({
    'Age': 'mean',
    'Salary': 'sum'
})
print("Grouped by City (mean age, sum salary):\n", grouped_city)

# Group by 'City' and count number of people
print("\nCount of people per City:\n", df1.groupby('City')['Name'].count())

# Multiple aggregations
grouped_multi_agg = df1.groupby('City')['Salary'].agg(['mean', 'min', 'max', 'np.std'])
print("\nMultiple aggregations on Salary per City:\n", grouped_multi_agg)
```

### 8\. Sorting Data

  * **`.sort_values(by, axis=0, ascending=True)`:** Sorts by the values in one or more columns.
  * **`.sort_index(axis=0/1, ascending=True)`:** Sorts by the index labels.

<!-- end list -->

```python
print("\n--- Sorting Data ---")
# Sort by 'Age' column in ascending order
df_sorted_age = df1.sort_values(by='Age')
print("DataFrame sorted by Age:\n", df_sorted_age)

# Sort by 'City' then by 'Salary' in descending order
df_sorted_multi = df1.sort_values(by=['City', 'Salary'], ascending=[True, False])
print("\nDataFrame sorted by City (asc) then Salary (desc):\n", df_sorted_multi)

# Sort by index
df_reindexed = df1.reindex(index=[3, 1, 0, 2])
print("\nDataFrame reindexed:\n", df_reindexed)
print("DataFrame sorted by index:\n", df_reindexed.sort_index())
```

### 9\. Reshaping Data (Stack/Unstack, Pivot Tables)

Transforming the layout of your data.

  * **`.stack()`:** "Stacks" columns into rows, producing a Series with a MultiIndex.
  * **`.unstack()`:** "Unstacks" a level of the MultiIndex (rows) to form new columns.
  * **`pivot_table()`:** Creates a spreadsheet-style pivot table as a DataFrame.

<!-- end list -->

```python
print("\n--- Reshaping Data ---")
data_long = pd.DataFrame({
    'Year': [2020, 2020, 2021, 2021],
    'City': ['A', 'B', 'A', 'B'],
    'Sales': [100, 150, 120, 180],
    'Profit': [10, 15, 12, 18]
})
print("Original 'Long' DataFrame:\n", data_long)

# Create a pivot table
pivot_table = data_long.pivot_table(index='Year', columns='City', values='Sales')
print("\nPivot Table (Sales by Year and City):\n", pivot_table)

# Stack/Unstack Example
multi_index_df = data_long.set_index(['Year', 'City'])
stacked_series = multi_index_df['Sales'].stack()
print("\nMultiIndex DataFrame (partial):\n", multi_index_df)
print("\nStacked Series (columns to index levels):\n", stacked_series)

unstacked_df = stacked_series.unstack()
print("\nUnstacked DataFrame (index level to columns):\n", unstacked_df)
```

### 10\. MultiIndex (Hierarchical Indexing)

Allows for multiple levels of indexing on a single axis (rows or columns), enabling the representation of higher-dimensional data.

  * **`index.names` / `columns.names`:** Attributes to set/retrieve MultiIndex level names.
  * **`.swaplevel()`:** Interchange two levels of a MultiIndex.

<!-- end list -->

```python
print("\n--- MultiIndex ---")
arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
          ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
multi_index = pd.MultiIndex.from_arrays(arrays, names=['first', 'second'])

s_multi = pd.Series(np.random.randn(8), index=multi_index)
print("Series with MultiIndex:\n", s_multi)

# Accessing data with MultiIndex
print("\nElements where first level is 'bar':\n", s_multi['bar'])
print("\nElement at ('baz', 'two'):\n", s_multi['baz', 'two'])

# Setting names for index levels
df_multi_cols = pd.DataFrame(np.random.randn(3, 8), index=['A', 'B', 'C'], columns=multi_index)
df_multi_cols.columns.names = ['Major', 'Minor']
print("\nDataFrame with MultiIndex Columns:\n", df_multi_cols)

# Swapping levels
swapped_df = df_multi_cols.swaplevel(0, 1, axis=1) # Swap Major and Minor levels
print("\nDataFrame with swapped column levels:\n", swapped_df)
```

### 11\. Input/Output

Reading data from and writing data to various formats.

  * **`pd.read_csv()`:** Reads data from a CSV file.
  * **`df.to_csv()`:** Writes a DataFrame to a CSV file.
  * `pd.read_excel()` / `df.to_excel()`
  * `pd.read_sql()` / `df.to_sql()`
  * `pd.read_json()` / `df.to_json()`
  * And many more...

<!-- end list -->

```python
print("\n--- Input/Output ---")
# Example: Create a dummy CSV file
dummy_df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
dummy_df.to_csv('dummy_data.csv', index=False) # index=False prevents writing the DataFrame index as a column
print("Dummy CSV file 'dummy_data.csv' created.")

# Read from CSV
df_from_csv = pd.read_csv('dummy_data.csv')
print("\nDataFrame read from 'dummy_data.csv':\n", df_from_csv)
```

### 12\. Outlier Detection and Handling (using NumPy methods)

While Pandas doesn't have a specific `outlier()` method, it integrates seamlessly with NumPy for numerical operations like outlier detection.

  * **Outlier:** A data point that differs significantly from other observations.
  * **`np.abs()`:** NumPy function for absolute value.
  * **`.clip()`:** Pandas method to limit values to a specified range.

<!-- end list -->

```python
print("\n--- Outlier Detection & Handling ---")
np.random.seed(42) # for reproducibility
data_with_outliers = pd.Series(np.random.randn(100) * 10 + 50) # mean 50, std 10
data_with_outliers.iloc[10] = 150 # Introduce an outlier
data_with_outliers.iloc[20] = -50 # Introduce another outlier

print("Original data (first 5 values):\n", data_with_outliers.head())
print("Original data (values around outliers):\n", data_with_outliers.iloc[[9,10,11,19,20,21]])


# Method 1: Z-score for outlier detection (threshold typically 2 or 3 standard deviations)
mean = data_with_outliers.mean()
std = data_with_outliers.std()
z_scores = np.abs((data_with_outliers - mean) / std)
outliers_mask = z_scores > 3 # Identify points more than 3 std dev away

print("\nOutliers detected (Z-score > 3):\n", data_with_outliers[outliers_mask])

# Handling Outliers: Capping/Clipping
# Cap values that are more than 3 standard deviations away
lower_bound = mean - 3 * std
upper_bound = mean + 3 * std

data_capped = data_with_outliers.clip(lower=lower_bound, upper=upper_bound)
print("\nData after capping outliers (first 5 values):\n", data_capped.head())
print("Data after capping outliers (values around original outliers):\n", data_capped.iloc[[9,10,11,19,20,21]])

# Handling Outliers: Replacing with NaN and then filling
data_replaced_nan = data_with_outliers.copy()
data_replaced_nan[outliers_mask] = np.nan
print("\nData after replacing outliers with NaN (first 5 values):\n", data_replaced_nan.head())
print("Data after replacing outliers with NaN (values around original outliers):\n", data_replaced_nan.iloc[[9,10,11,19,20,21]])

# Then fill NaNs, e.g., with median
data_filled_median = data_replaced_nan.fillna(data_replaced_nan.median())
print("\nData after filling NaNs with median (first 5 values):\n", data_filled_median.head())
print("Data after filling NaNs with median (values around original outliers):\n", data_filled_median.iloc[[9,10,11,19,20,21]])
```

This guide covers the most common and fundamental use cases of Pandas, providing a strong foundation for data analysis tasks. Remember, the best way to learn is by doing, so practice these operations with your own datasets\!