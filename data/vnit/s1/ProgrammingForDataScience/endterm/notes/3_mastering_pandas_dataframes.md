# Module 5: Data Manipulation & Data Visualization - Mastering Pandas DataFrames

This section focuses on advanced functionalities of Pandas DataFrames, crucial for comprehensive data manipulation, cleaning, transformation, and basic analysis. It builds upon foundational Pandas concepts to tackle real-world data challenges.

## 5.1 DataFrame Restructuring

Reshaping DataFrames is often necessary to prepare data for specific analyses or to change its presentation.

### 5.1.1 `stack()` and `unstack()` Operations

These methods are powerful for transforming the shape of your DataFrame, pivoting between "wide" and "long" formats.

* **`stack()`**: This method "stacks" the columns into rows, effectively transforming a DataFrame from a wide format to a long format. It pivots a level of the (possibly multi-index) columns to the (possibly multi-index) row axis, resulting in a Series with a MultiIndex.
    * **Application:** Useful for reshaping data for analysis or display, especially when you want to treat column headers as a variable.

    **Example:**
    Consider a DataFrame `df` with `Section` as the index and `Student` as columns:
    ```python
    import pandas as pd
    import numpy as np

    # Example DataFrame to demonstrate stack
    data_wide = {1: [0, 4], 2: [1, 5], 3: [2, 6], 4: [3, 7]}
    df_wide = pd.DataFrame(data_wide, index=['AA', 'BB'], columns=pd.MultiIndex.from_product([['W', 'X', 'Y', 'Z']], names=['Student']))
    # Note: The provided example format for df was simplified in the quiz,
    # let's use a standard DataFrame for stack illustration.
    df_section_student = pd.DataFrame({
        'W': [0, 4],
        'X': [1, 5],
        'Y': [2, 6],
        'Z': [3, 7]
    }, index=['AA', 'BB'])
    df_section_student.index.name = 'Section'

    print("Original DataFrame (df_section_student):\n", df_section_student)

    st_df = df_section_student.stack()
    st_df.index.names = ['Section', 'Student'] # Assign names for clarity
    print("\nStacked Series (st_df):\n", st_df)
    # Output:
    # Original DataFrame (df_section_student):
    #          W  X  Y  Z
    # Section
    # AA       0  1  2  3
    # BB       4  5  6  7
    #
    # Stacked Series (st_df):
    # Section  Student
    # AA       W          0
    #          X          1
    #          Y          2
    #          Z          3
    # BB       W          4
    #          X          5
    #          Y          6
    #          Z          7
    # dtype: int64
    ```

* **`unstack()`**: This is the inverse operation of `stack()`. It "unstacks" a level of the (usually row) MultiIndex to form new columns, effectively transforming data from a "long" format to a "wide" format.
    * **Application:** Reverses the stacking process, making data more accessible and often more readable by spreading hierarchical index levels into columns.

    **Example:**
    ```python
    unstacked_df = st_df.unstack('Section') # Unstack the 'Section' level to columns
    print("\nUnstacked DataFrame (unstacked_df by 'Section'):\n", unstacked_df)
    # Output:
    # Student   AA  BB
    # W          0   4
    # X          1   5
    # Y          2   6
    # Z          3   7
    ```

### 5.1.2 Duplicating and Dropping Duplicates

Handling duplicate entries is a crucial step in data cleaning to ensure data integrity and avoid biased analysis.

* **`duplicated()`**: This method identifies duplicate rows in a DataFrame. It returns a boolean Series, where `True` indicates that the corresponding row is an exact duplicate of a previously observed row, and `False` indicates it is unique up to that point.

    **Example:**
    ```python
    df_dup = pd.DataFrame({'AA': ['Rohan']*2 + ['Shyam']*3, 'BB': [11, 11, 11, 44, 44]})
    print("Original DataFrame (df_dup):\n", df_dup)
    print("\nBoolean Series for duplicates:\n", df_dup.duplicated())
    # Output:
    # Original DataFrame (df_dup):
    #       AA  BB
    # 0  Rohan  11
    # 1  Rohan  11
    # 2  Shyam  11
    # 3  Shyam  44
    # 4  Shyam  44
    #
    # Boolean Series for duplicates:
    # 0    False
    # 1     True
    # 2    False
    # 3    False
    # 4     True
    # dtype: bool
    ```

* **`drop_duplicates()`**: This method removes duplicate rows from the DataFrame.
    * **Parameters:**
        * `keep`: Controls which duplicate rows are retained or dropped.
            * `'first'` (default): Keeps the first occurrence of each unique row and drops all subsequent duplicates.
            * `'last'`: Keeps the last occurrence and drops all preceding duplicates.
            * `False`: Drops all occurrences of duplicate rows, meaning if a row appears more than once, all instances of it are removed.
        * `subset`: A list of column names. If provided, duplicates are identified based only on the values in these specific columns, rather than all columns.

    **Example (Default - `keep='first'`):**
    ```python
    print("\nDataFrame after dropping duplicates (keep='first'):\n", df_dup.drop_duplicates())
    # Output:
    # DataFrame after dropping duplicates (keep='first'):
    #       AA  BB
    # 0  Rohan  11
    # 2  Shyam  11
    # 3  Shyam  44
    ```

    **Example (Column-specific duplication with `keep='last'`):**
    ```python
    print("\nDataFrame after dropping duplicates on 'AA' (keep='last'):\n", df_dup.drop_duplicates(subset='AA', keep='last'))
    # Output:
    # DataFrame after dropping duplicates on 'AA' (keep='last'):
    #       AA  BB
    # 1  Rohan  11
    # 4  Shyam  44
    ```

## 5.2 Data Manipulation and Transformation

Pandas offers versatile methods to modify and transform data within Series and DataFrames.

### 5.2.1 Mapping Data with `.map()`

* **Concept:** The `.map()` method is a Series method used to substitute values in a Series based on a dictionary, a Series, or a function. It's highly efficient for element-wise transformations.
* **Application:** Commonly used to add a new column to a DataFrame by mapping values from an existing column to a corresponding set of new values.

    **Example:**
    ```python
    df_students = pd.DataFrame({'Student': ['A', 'B', 'C'], 'Roll No.': [21, 24, 26]})
    Emarks = {'A': 78, 'B': 85, 'C': 64}

    df_students['Emarks'] = df_students['Student'].map(Emarks)
    print("DataFrame after mapping 'Emarks':\n", df_students)
    # Output:
    # DataFrame after mapping 'Emarks':
    #   Student  Roll No.  Emarks
    # 0       A        21      78
    # 1       B        24      85
    # 2       C        26      64
    ```

### 5.2.2 Replacing Values with `.replace()`

* **Concept:** The `.replace()` method is used to substitute specific values within a DataFrame or Series.
* **Parameters:** It's highly flexible, allowing you to replace single values, lists of values, or even patterns (using regular expressions) with new single values or lists of new values.

    **Example:**
    ```python
    df_replace = pd.DataFrame({'col1': [10, 20, 24, 30], 'col2': [26, 40, 50, 60]})
    print("Original DataFrame (df_replace):\n", df_replace)

    # Replacing single values
    df_replaced_single = df_replace.replace(24, 99)
    print("\nAfter replacing 24 with 99:\n", df_replaced_single)

    # Replacing lists of values with new lists of values
    df_replaced_list = df_replace.replace([24, 26], [32, 33])
    print("\nAfter replacing [24,26] with [32,33]:\n", df_replaced_list)
    # Output:
    # Original DataFrame (df_replace):
    #    col1  col2
    # 0    10    26
    # 1    20    40
    # 2    24    50
    # 3    30    60
    #
    # After replacing 24 with 99:
    #    col1  col2
    # 0    10    26
    # 1    20    40
    # 2    99    50
    # 3    30    60
    #
    # After replacing [24,26] with [32,33]:
    #    col1  col2
    # 0    10    33
    # 1    20    40
    # 2    32    50
    # 3    30    60
    ```
    **Difference from `.map()`:** `replace()` modifies existing values (or returns a new object with modifications), while `map()` creates a new Series by applying a function or dictionary element-wise to the calling Series. `replace()` is for direct value substitution; `map()` is for creating new derived data based on a mapping.

### 5.2.3 Renaming Indices and Columns with `.rename()`

* **Concept:** The `.rename()` method is used to modify the labels of rows (index) and columns in a DataFrame without altering the underlying data.
* **Parameters:** You provide mapping dictionaries for `index` and `columns` to perform targeted renaming.

    **Example:**
    ```python
    df_rename_ex = pd.DataFrame({'Student': ['A', 'B', 'C'], 'Emarks': [78, 85, 64]}, index=[0, 1, 2])
    print("Original DataFrame (df_rename_ex):\n", df_rename_ex)

    df_renamed = df_rename_ex.rename(index={1: 'X'}, columns={'Emarks': 'PDS_marks'})
    print("\nDataFrame after renaming:\n", df_renamed)
    # Output:
    # Original DataFrame (df_rename_ex):
    #   Student  Emarks
    # 0       A      78
    # 1       B      85
    # 2       C      64
    #
    # DataFrame after renaming:
    #   Student  PDS_marks
    # 0       A         78
    # X       B         85
    # 2       C         64
    ```

## 5.3 Data Cleaning and Outlier Handling

Data cleaning involves dealing with imperfections in data, such as missing values and outliers, to ensure the reliability of analysis.

### 5.3.1 Identifying and Handling Missing Values (NaN)

* **Concept:** `NaN` (Not a Number) serves as a placeholder for missing data.
* **Detection:** Use `.isna()` (alias for `.isnull()`) to create a boolean mask, and then use `.shape[0]` (for rows) or `.size` (for total elements) to count missing values.
    * Example: `data[data.iloc[:, -1].isna()].shape[0]` counts rows where the last column has `NaN`.

* **Imputation (`fillna()`):** Replacing missing values with a specified value (e.g., 0, mean, median, mode).
    * **Example:** `data[colm] = data[colm].fillna(0)` replaces all `NaN` values in `colm` (e.g., 'Total MT') with 0.
    * **Conditional Filling (Dynamic IDs):** For `Student Id` where `NaN` values are replaced with dynamically generated IDs:
        ```python
        # Assuming 'data' DataFrame and 'Student Id' column exists with NaNs
        # (This is a simplified representation of the logic from the notes)
        sample_data = pd.DataFrame({'Student Id': [101, np.nan, 103, np.nan]})
        print("Original 'Student Id' column:\n", sample_data['Student Id'])

        sample_data['Student Id'] = sample_data['Student Id'].fillna(sample_data.apply(lambda row: f'NewID{int(row.name)+1}', axis=1))
        print("\n'Student Id' after dynamic fill:\n", sample_data['Student Id'])
        # Output:
        # Original 'Student Id' column:
        # 0    101.0
        # 1      NaN
        # 2    103.0
        # 3      NaN
        # Name: Student Id, dtype: float64
        #
        # 'Student Id' after dynamic fill:
        # 0        101.0
        # 1    NewID2
        # 2        103.0
        # 3    NewID4
        # Name: Student Id, dtype: object
        ```
* **Dropping Missing Values (`dropna()`):** (Briefly understood, covered in previous section).

### 5.3.2 Outlier Detection and Treatment

* **Concept:** An outlier is a data point that significantly differs from other observations, often indicating variability or error.
* **Detection:**
    * **Descriptive Statistics (`.describe()`):** Provides summary statistics (min, max, mean, std) that can hint at extreme values.
    * **Conditional Indexing:** Using statistical thresholds (e.g., values exceeding a certain number of standard deviations from the mean).
        * Example: `np.abs(column) > 3` identifies values whose absolute magnitude exceeds 3 (assuming standard normal distribution, 3 standard deviations is a common threshold).

    **Example (Outlier Detection):**
    ```python
    # Generate a DataFrame with random numbers, likely to have some outliers
    df_outliers = pd.DataFrame(np.random.randn(10, 5) * 5) # Multiply by 5 to increase spread
    print("Original DataFrame (first 5 rows):\n", df_outliers.head())
    print("\nDescriptive statistics of original data:\n", df_outliers.describe())

    # Identify outliers in a specific column (e.g., column 0) where absolute value > 3
    print("\nOutliers in column 0 (abs value > 3):\n", df_outliers[df_outliers[0].abs() > 3])
    ```

* **Treatment (`.clip()`):** This method is used to cap values within a specified range, effectively handling outliers by setting them to a maximum or minimum boundary. Values below the lower bound are set to the lower bound, and values above the upper bound are set to the upper bound.
    * **Benefit:** Reduces the impact of extreme values without removing entire data points, which can be beneficial if the outlier itself contains valid information.

    **Example (Outlier Treatment with `clip()`):**
    ```python
    df_clipped = df_outliers.clip(lower=-3, upper=3)
    print("\nDataFrame after clipping (first 5 rows):\n", df_clipped.head())
    print("\nDescriptive statistics of clipped data:\n", df_clipped.describe())
    # Observe that min and max values in the describe output will now be bounded by -3 and 3.
    ```

## 5.4 Data Analysis and Aggregation

### 5.4.1 Descriptive Statistics

* **Concept:** Generating summary statistics for DataFrame columns provides quick insights into the distribution and central tendencies of the data.
* **`.describe()`:** This DataFrame method generates descriptive statistics for numerical columns, including `count`, `mean`, `std` (standard deviation), `min`, `max`, and quartiles (25%, 50% - median, 75%).
    * **Interpretation:** Allows for quick assessment of data spread, central tendency, and potential outliers.

    **Example:** (See output of `df_outliers.describe()` and `df_clipped.describe()` in the outlier section above).

### 5.4.2 Grouping Data with `groupby()`

* **Concept:** The `groupby()` method is fundamental for splitting data into groups based on some criteria (one or more columns) and then applying a function (e.g., aggregation, transformation, filtration) to each group.
* **Aggregation:** Performing aggregate functions (e.g., `mean()`, `sum()`, `size()`, `count()`, `min()`, `max()`) on grouped data.

    **Example 1: Single-level Grouping (`mean()`):**
    ```python
    df_animal_speed = pd.DataFrame({'Animal': ['Falcon', 'Falcon', 'Parrot', 'Parrot'],
                                    'Max_speed': [400, 350, 30, 20]})
    print("Original Animal Speed DataFrame:\n", df_animal_speed)

    grouped_mean = df_animal_speed.groupby(['Animal']).mean()
    print("\nMean Max_speed by Animal:\n", grouped_mean)
    # Output:
    # Original Animal Speed DataFrame:
    #    Animal  Max_speed
    # 0  Falcon        400
    # 1  Falcon        350
    # 2  Parrot         30
    # 3  Parrot         20
    #
    # Mean Max_speed by Animal:
    #           Max_speed
    # Animal
    # Falcon        375.0
    # Parrot         25.0
    ```

* **Multi-level Grouping (`.size()`):** Grouping by multiple columns to count occurrences within each combination.
    ```python
    # Hypothetical 'Marks.csv' data structure for demonstration
    data_marks = pd.DataFrame({
        'Q1': [5, 10, 5, 8, 10, 5],
        'Q2': [15, 9, 15, 12, 9, 15],
        'Total MT': [20, 19, 20, 20, 19, 20] # Assuming some total marks, potentially with NaNs
    })
    print("Original Marks Data (first 5 rows):\n", data_marks.head())

    # Count occurrences across 'Total MT' and 'Q2' combinations
    grouped_counts = data_marks.groupby(['Total MT', 'Q2']).size()
    print("\nCounts by 'Total MT' and 'Q2':\n", grouped_counts)
    # Output:
    # Original Marks Data (first 5 rows):
    #    Q1  Q2  Total MT
    # 0   5  15        20
    # 1  10   9        19
    # 2   5  15        20
    # 3   8  12        20
    # 4  10   9        19
    #
    # Counts by 'Total MT' and 'Q2':
    # Total MT  Q2
    # 19        9     2
    # 20        12    1
    #           15    3
    # dtype: int64
    ```

### 5.4.3 Custom Functions and Data Transformation

* **Concept:** Applying user-defined functions to DataFrame columns allows for complex, conditional data transformations.
* **Application:** Creating new categorical columns based on numerical ranges (e.g., assigning grades based on total marks).

    **Example: Grade Mapping:**
    ```python
    # Using 'data_marks' from the groupby example
    grades = {20: 'A', 19: 'B', 15: 'C', 10: 'D', 0: 'E'}

    def grade_mapping(marks):
        for thmarks, grd in grades.items():
            if marks >= thmarks:
                return grd
        return 'F' # Default if no condition met (e.g., negative marks)

    data_marks['Grades'] = data_marks['Total MT'].map(grade_mapping)
    print("\nDataFrame with 'Grades' column:\n", data_marks)
    # Output:
    # DataFrame with 'Grades' column:
    #    Q1  Q2  Total MT Grades
    # 0   5  15        20      A
    # 1  10   9        19      B
    # 2   5  15        20      A
    # 3   8  12        20      A
    # 4  10   9        19      B
    # 5   5  15        20      A
    ```

## 5.5 Data Loading, Saving, and Basic Visualization

### 5.5.1 Loading Data from CSV

* **`pd.read_csv()`**: Reads data from a Comma Separated Values (CSV) file into a DataFrame.

    ```python
    # Assuming a file named 'sample_data.csv' exists with comma-separated values
    # Example content of 'sample_data.csv':
    # Q1,Q2,Total MT,Grades
    # 5,15,20,A
    # 10,9,19,B
    # ...
    # df_loaded = pd.read_csv('sample_data.csv')
    # print("Loaded DataFrame:\n", df_loaded.head())
    ```

### 5.5.2 Saving Data to CSV

* **`to_csv()`**: Writes a DataFrame to a CSV file.
* **Parameters:**
    * `index=False`: Prevents writing the DataFrame index as a column in the CSV file, which is often desired when the index is not meaningful data itself.

    ```python
    # data_marks.to_csv('Grades.csv', index=False)
    # print("DataFrame saved to Grades.csv")
    ```

### 5.5.3 Basic Data Visualization

* **`matplotlib.pyplot` (plt)**: A Python plotting library that provides a MATLAB-like plotting interface, widely used for creating static visualizations.
* **Bar Plots:** Useful for displaying the distribution of categorical data (e.g., grade distribution).
* **Customizing Plots:** Setting labels, titles, and figure size for better readability.

    **Example: Grade Distribution Bar Plot:**
    ```python
    import matplotlib.pyplot as plt

    # Using 'data_marks' DataFrame with 'Grades' column
    grade_counts = data_marks['Grades'].value_counts()
    print("Grade Counts:\n", grade_counts)

    # Ensure grades are plotted in a specific order (A, B, C, D, E)
    grade_order = ['A', 'B', 'C', 'D', 'E']
    # Reindex to include all possible grades in order, even if counts are 0
    grade_counts = grade_counts.reindex(grade_order, fill_value=0)
    print("\nGrade Counts (reindexed):\n", grade_counts)

    plt.figure(figsize=(4, 3)) # Adjust figure size for better display
    plt.bar(grade_counts.index, grade_counts.values, color='skyblue')
    plt.xlabel('Grades')
    plt.ylabel('No. of students')
    plt.title('Grade Distribution')
    plt.grid(axis='y', linestyle='--', alpha=0.7) # Add grid for readability
    plt.tight_layout() # Adjust layout to prevent labels from overlapping
    plt.show()
    ```

---

## Glossary of Key Terms (Consolidated)

* **DataFrame:** A two-dimensional, size-mutable, tabular data structure with labeled axes (rows and columns). It is the primary data structure in the Pandas library.
* **Series:** A one-dimensional labeled array capable of holding any data type. It is essentially a column or row in a DataFrame.
* **NumPy (`np`):** A fundamental package for numerical computing in Python, providing support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.
* **Pandas (`pd`):** An open-source Python library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.
* **`stack()`:** A DataFrame method that "stacks" columns into rows, producing a Series with a MultiIndex. Transforms data from a "wide" to a "long" format.
* **`unstack()`:** A DataFrame method that "unstacks" a level of the MultiIndex (rows) to form new columns. Transforms data from a "long" to a "wide" format.
* **`duplicated()`:** A DataFrame or Series method that returns a boolean Series indicating whether each row/entry is a duplicate of a previous one.
* **`drop_duplicates()`:** A DataFrame method used to remove duplicate rows based on all columns or a specified subset of columns.
* **`map()`:** A Series method used for substituting each value in a Series with another value, often from a dictionary or another Series.
* **`replace()`:** A DataFrame or Series method used to replace specific values in a dataset. It can replace single values, lists of values, or regular expressions.
* **`rename()`:** A DataFrame method used to change the labels of the index (rows) or columns.
* **Outlier:** A data point that differs significantly from other observations. It lies an abnormal distance from other values in a random sample from a population.
* **`np.random.randn()`:** A NumPy function that returns a sample (or samples) from the "standard normal" distribution (mean 0, variance 1).
* **`describe()`:** A DataFrame method that generates descriptive statistics of the DataFrame columns, including count, mean, standard deviation, min, max, and quartiles.
* **`np.abs()`:** A NumPy function that computes the absolute value of each element in an array.
* **`clip()`:** A DataFrame or Series method used to clip (limit) values to a specified minimum and maximum threshold. Values outside this range are set to the boundary values.
* **NaN (Not a Number):** A floating-point value used to represent undefined or unrepresentable numerical results, commonly used in Pandas to denote missing values.
* **`fillna()`:** A DataFrame or Series method used to replace `NaN` (missing) values with a specified value or method.
* **`isna()`:** A DataFrame or Series method that returns a boolean DataFrame/Series indicating which elements are `NaN` (missing values).
* **`groupby()`:** A DataFrame method that splits the DataFrame into groups based on one or more columns, allowing for aggregate operations to be performed on these groups.
* **`value_counts()`:** A Series method that returns a Series containing counts of unique values.
* **`reindex()`:** A Series/DataFrame method that conforms the object to a new index with optional filling logic for missing data. In the context of `value_counts()`, it can be used to order the counts according to a predefined sequence.
* **`matplotlib.pyplot` (`plt`):** A Python plotting library that provides a MATLAB-like plotting interface, widely used for creating static visualizations in Python.
* **Bar Plot:** A chart that presents categorical data with rectangular bars whose heights or lengths are proportional to the values that they represent.
* **`pd.read_csv()`:** Reads data from a CSV file into a DataFrame.
* **`to_csv()`:** Writes a DataFrame to a CSV file.

---