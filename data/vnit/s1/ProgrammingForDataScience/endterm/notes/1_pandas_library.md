# Module 5: Data Manipulation & Data Visualization - Pandas Library for Data Transformation

This module delves into the **Pandas library**, a cornerstone for data analysis and manipulation in Python. Built on top of **NumPy**, Pandas provides powerful and flexible data structures designed to make working with "relational" or "labeled" data both easy and intuitive.

## 5.1 Introduction to Pandas

Pandas is an open-source, fast, powerful, flexible, and easy-to-use data analysis and manipulation tool. It excels at handling tabular data, making it indispensable for tasks like data cleaning, transformation, analysis, and visualization.

### 5.1.1 Installation and Import

To begin using Pandas, it must first be installed in your Python environment.

* **Installation Command:**
    ```bash
    pip install pandas
    ```
    This command installs the Pandas library along with its necessary dependencies, such as NumPy, `python-dateutil`, `pytz`, and `tzdata`.

* **Common Aliases for Import:**
    It's standard practice to import Pandas and NumPy with common aliases to make your code more concise and readable.
    ```python
    import pandas as pd
    import numpy as np
    ```
    Here, `pd` is the conventional alias for Pandas, and `np` is for NumPy.

## 5.2 Core Pandas Data Structures

Pandas introduces two primary data structures: **Series** and **DataFrame**.

### 5.2.1 Pandas Series

A `Series` is a **one-dimensional labeled array** capable of holding any data type (integers, strings, floats, Python objects, etc.). It has an associated array of data labels called its `index`.

* **Characteristics:**
    * **1D (One-Dimensional):** Similar to a single column in a spreadsheet or a Python list.
    * **Homogeneous Data Types:** Typically holds data of a single type.
    * **Labeled Index:** Each element has a label (index) for easy access and alignment.

* **Creation of a Series:**
    1.  **From a List (with default integer index):**
        ```python
        import pandas as pd
        ser1 = pd.Series([33, 44, 55, 66, 22])
        print(ser1)
        # Output:
        # 0    33
        # 1    44
        # 2    55
        # 3    66
        # 4    22
        # dtype: int64
        ```
    2.  **From a List with a Custom Index:**
        You can assign custom labels to the index during creation.
        ```python
        st_marks = pd.Series([78, 56, 73, 83, 45], index=['S1', 'S2', 'S3', 'S4', 'S5'])
        print(st_marks)
        # Output:
        # S1    78
        # S2    56
        # S3    73
        # S4    83
        # S5    45
        # dtype: int64
        ```
    3.  **From a Dictionary:**
        When creating a Series from a dictionary, the dictionary's keys automatically become the Series's index, and the values become the data.
        ```python
        st_marks_dict = {'S1': 78, 'S2': 56, 'S3': 73, 'S4': 83, 'S5': 45}
        st_marks_seri = pd.Series(st_marks_dict)
        print(st_marks_seri)
        # Output:
        # S1    78
        # S2    56
        # S3    73
        # S4    83
        # S5    45
        # dtype: int64
        ```

* **Indexing and Slicing Series:**
    Elements in a Series can be accessed by their integer position or, more commonly, by their custom index labels.
    1.  **Accessing by Label:**
        ```python
        print(st_marks['S4'])
        # Output: 83
        ```
    2.  **Boolean Indexing (Filtering Data):**
        This method selects data based on a boolean condition applied to the Series values. It returns a new Series containing only the elements that satisfy the condition.
        ```python
        print(st_marks[st_marks > 75])
        # Output:
        # S1    78
        # S4    83
        # dtype: int64
        ```
        This filters `st_marks` to return only values greater than 75.

* **Converting Series to Dictionary and Vice Versa:**
    * **Series to Dictionary:** Use the `.to_dict()` method.
        ```python
        st_marks_dict_from_series = st_marks.to_dict()
        print(st_marks_dict_from_series)
        # Output: {'S1': 78, 'S2': 56, 'S3': 73, 'S4': 83, 'S5': 45}
        ```
    * **Dictionary to Series:** Pass the dictionary to the `pd.Series()` constructor. (Already shown in creation from dictionary example).

* **Series Attributes:**
    You can assign names to a Series and its index for better clarity.
    ```python
    st_marks_seri.name = "Student's Marks"
    st_marks_seri.index.name = "Students"
    print(st_marks_seri)
    # Output:
    # Students
    # S1    78
    # S2    56
    # S3    73
    # S4    83
    # S5    45
    # Name: Student's Marks, dtype: int64
    ```

### 5.2.2 Pandas DataFrame

A `DataFrame` is a **two-dimensional tabular data structure** with labeled axes (rows and columns). It is the most commonly used Pandas object and can be thought of as a dictionary of Series objects sharing the same index, or analogous to a spreadsheet or SQL table.

* **Characteristics:**
    * **2D (Two-Dimensional):** Data is organized in rows and columns.
    * **Heterogeneous Data Types:** Columns can have different data types (e.g., one column of integers, another of strings).
    * **Labeled Axes:** Both rows (index) and columns have labels.

* **Creation of a DataFrame:**
    1.  **From a Dictionary of Lists (Common Method):**
        Each key in the dictionary becomes a column name, and its corresponding list becomes the column's data.
        ```python
        data = {'States': ['MP', 'UP', 'AP'], 'Companies': [120, 360, 232]}
        SF = pd.DataFrame(data)
        print(SF)
        # Output:
        #   States  Companies
        # 0     MP        120
        # 1     UP        360
        # 2     AP        232
        ```
    2.  **From NumPy Arrays (for numerical or random data):**
        This is useful for generating sample data or when working with existing NumPy arrays.
        ```python
        import numpy as np
        from numpy.random import randn

        # Example with random numbers
        dframe_random = pd.DataFrame(randn(25).reshape(5,5),
                                     index=['A','B','C','D','E'],
                                     columns=['c1','c2','c3','c4','c5'])
        print(dframe_random)
        # Output will vary due to random numbers, e.g.:
        #          c1        c2        c3        c4        c5
        # A -0.191599  0.941659 -0.669527  0.370724  1.139886
        # B  0.428514  0.957599 -1.610531 -0.063857 -0.222370
        # C -0.627796  0.473598  0.640974  0.222718 -0.053160
        # D  0.793856 -0.165249 -0.231221 -0.428612  0.038198
        # E -0.923164  0.742301 -0.832205  0.812239  0.706173

        # Example with structured numerical data using np.arange
        dframe_arange = pd.DataFrame(np.arange(25).reshape(5,5),
                                     index=['MP','UP','AP','MH','JK'],
                                     columns=['c1','c2','c3','c4','c5'])
        print(dframe_arange)
        # Output:
        #    c1  c2  c3  c4  c5
        # MP  0   1   2   3   4
        # UP  5   6   7   8   9
        # AP 10  11  12  13  14
        # MH 15  16  17  18  19
        # JK 20  21  22  23  24
        ```

* **Dropping Rows and Columns from a DataFrame:**
    The `.drop()` method is used to remove specified rows or columns.
    * **Dropping Rows:** Provide the index label(s) of the row(s) to remove. By default, `axis=0` (rows).
        ```python
        print("Original DataFrame SF:\n", SF)
        SF_after_row_drop = SF.drop(1) # Drops the row with index 1
        print("SF after dropping row 1:\n", SF_after_row_drop)
        # Output:
        # Original DataFrame SF:
        #    States  Companies
        # 0     MP        120
        # 1     UP        360
        # 2     AP        232
        # SF after dropping row 1:
        #   States  Companies
        # 0     MP        120
        # 2     AP        232
        ```
    * **Dropping Columns:** Provide the column name(s) and set `axis=1` (or `'columns'`).
        ```python
        SF_after_col_drop = SF.drop('States', axis=1) # Drops the 'States' column
        print("SF after dropping 'States' column:\n", SF_after_col_drop)
        # Output:
        # SF after dropping 'States' column:
        #    Companies
        # 0        120
        # 1        360
        # 2        232
        ```
    * **Important Note:** By default, `.drop()` returns a **new DataFrame** with the specified rows/columns removed, leaving the original DataFrame unchanged. To modify the DataFrame in place, use `inplace=True` (e.g., `SF.drop(1, inplace=True)`).

* **Indexing and Selection in DataFrames:**
    DataFrames offer powerful methods for selecting subsets of data.
    1.  **Selecting Multiple Columns:**
        ```python
        print(dframe_arange[['c2', 'c5']])
        # Output:
        #     c2  c5
        # MP   1   4
        # UP   6   9
        # AP  11  14
        # MH  16  19
        # JK  21  24
        ```
    2.  **Boolean Indexing for Rows (Filtering):**
        Selects rows where a condition applied to a column is True.
        ```python
        print(dframe_arange[dframe_arange['c3'] > 10])
        # Output:
        #     c1  c2  c3  c4  c5
        # AP  10  11  12  13  14
        # MH  15  16  17  18  19
        # JK  20  21  22  23  24
        ```
    3.  **Combining Boolean Indexing with Column Selection:**
        ```python
        print(dframe_arange[dframe_arange['c3'] > 10]['c3'])
        # Output:
        # AP    12
        # MH    17
        # JK    22
        # Name: c3, dtype: int64
        ```
    4.  **Selecting Rows by Index Label:**
        * Using boolean condition on index:
            ```python
            print(dframe_arange[dframe_arange.index == 'AP'])
            # Output:
            #    c1  c2  c3  c4  c5
            # AP 10  11  12  13  14
            ```
        * Using `.loc[]` (label-based indexer): This is the preferred and more efficient way for label-based selection.
            ```python
            print(dframe_arange.loc['AP'])
            # Output:
            # c1    10
            # c2    11
            # c3    12
            # c4    13
            # c5    14
            # Name: AP, dtype: int64
            ```
    5.  **Integer-Location Based Indexing (`.iloc[]`):**
        Selects data by integer position, similar to NumPy array indexing.
        ```python
        print(dframe_arange.iloc[2]) # Selects the row at integer position 2 (AP)
        # Output:
        # c1    10
        # c2    11
        # c3    12
        # c4    13
        # c5    14
        # Name: AP, dtype: int64
        ```
    6.  **Applying a Boolean Condition to the Entire DataFrame:**
        This returns a DataFrame of boolean values indicating where the condition is met.
        ```python
        print(dframe_arange > 10)
        # Output:
        #       c1     c2     c3     c4     c5
        # MP  False  False  False  False  False
        # UP  False  False  False  False  False
        # AP  False   True   True   True   True
        # MH   True   True   True   True   True
        # JK   True   True   True   True   True
        ```

## 5.3 Handling Missing Data (NaN Values)

Missing data is a common challenge in data science. Pandas uses `NaN` (Not a Number), a special floating-point value from NumPy, to represent missing or undefined data.

* **Significance of NaN:**
    When creating a Series or DataFrame from a dictionary and providing an index that includes labels not found in the source data, Pandas assigns `NaN` to those new index positions. This explicitly indicates missing data.
    ```python
    students = ['S1', 'S2', 'G3', 'S5', 'J6']
    st_marks_dict = {'S1': 78, 'S2': 56, 'S3': 73, 'S4': 83, 'S5': 45}
    st_marks_with_nan = pd.Series(st_marks_dict, index=students)
    print(st_marks_with_nan)
    # Output:
    # S1    78.0
    # S2    56.0
    # G3     NaN
    # S5    45.0
    # J6     NaN
    # dtype: float64
    ```
    Notice how `G3` and `J6` are assigned `NaN`. Also, the `dtype` becomes `float64` because `NaN` is a float.

* **Identifying NaN Values:**
    1.  **`.isnull()`:** A Series/DataFrame method that returns a boolean Series/DataFrame, with `True` where the corresponding element is `NaN` and `False` otherwise.
        ```python
        print(st_marks_with_nan.isnull())
        # Output:
        # S1    False
        # S2    False
        # G3     True
        # S5    False
        # J6     True
        # dtype: bool
        ```
    2.  **`pd.notnull()`:** A top-level Pandas function (or Series/DataFrame method) that does the opposite, returning `True` for non-null values and `False` for `NaN` values.
        ```python
        print(pd.notnull(st_marks_with_nan))
        # Output:
        # S1     True
        # S2     True
        # G3    False
        # S5     True
        # J6    False
        # dtype: bool
        ```

## 5.4 Arithmetic Operations in Pandas

Pandas supports element-wise arithmetic operations between Series and DataFrames. A key feature is **data alignment based on labels**.

* **Arithmetic Operations between Series:**
    When performing operations like addition, Pandas attempts to align data based on their indices. If indices don't align, `NaN` is introduced in the result for those unaligned positions.
    ```python
    st_marks1 = pd.Series([78, 56, 73], index=['S1', 'S2', 'S3'])
    st_marks2 = pd.Series([10, 20, 30], index=['S2', 'S3', 'S4'])

    result_sum = st_marks1 + st_marks2
    print(result_sum)
    # Output:
    # S1     NaN
    # S2    66.0
    # S3    103.0
    # S4     NaN
    # dtype: float64
    ```
    Notice `S1` and `S4` become `NaN` because they only exist in one of the Series.

* **Arithmetic Operations between DataFrames:**
    Similar to Series, DataFrames align data based on both **row and column labels**.
    ```python
    dframe1 = pd.DataFrame(np.arange(9).reshape(3,3), index=['A','B','C'], columns=['col1','col2','col3'])
    dframe2 = pd.DataFrame(np.arange(16).reshape(4,4), index=['A','B','C','D'], columns=['col1','col2','col3','col4'])

    print("dframe1:\n", dframe1)
    print("\ndframe2:\n", dframe2)

    sum_df = dframe1 + dframe2
    print("\nSum (dframe1 + dframe2):\n", sum_df)
    # Output (Illustrates NaN for misaligned labels):
    # dframe1:
    #    col1  col2  col3
    # A     0     1     2
    # B     3     4     5
    # C     6     7     8
    #
    # dframe2:
    #    col1  col2  col3  col4
    # A     0     1     2     3
    # B     4     5     6     7
    # C     8     9    10    11
    # D    12    13    14    15
    #
    # Sum (dframe1 + dframe2):
    #    col1  col2  col3  col4
    # A   0.0   2.0   4.0   NaN
    # B   7.0   9.0  11.0   NaN
    # C  14.0  16.0  18.0   NaN
    # D   NaN   NaN   NaN   NaN
    ```

* **Handling Misaligned Indices with `fill_value`:**
    The `fill_value` argument is an optional parameter used with methods like `.add()` (and `reindex()`) to specify a default value that will be used instead of `NaN` for any labels introduced in the new index that were not present in the original object.
    ```python
    # Using .add() with fill_value
    sum_with_fill = dframe1.add(dframe2, fill_value=0)
    print("\nSum with fill_value=0:\n", sum_with_fill)
    # Output (NaNs are replaced by 0 before addition):
    #    col1  col2  col3  col4
    # A   0.0   2.0   4.0   3.0
    # B   7.0   9.0  11.0   7.0
    # C  14.0  16.0  18.0  11.0
    # D  12.0  13.0  14.0  15.0
    ```
    Here, `NaN` values from `dframe1` (for `col4` and row `D`) and `dframe2` (for no `D` row and no `col4` in dframe1) are treated as 0 during the addition.

## 5.5 Reindexing Data Structures

The `.reindex()` method is a powerful tool to conform a Series or DataFrame to a new index. It can be used to reorder existing data, or to introduce `NaN` values for new labels.

* **Reindexing a Series:**
    ```python
    st_marks = pd.Series([78,56,73,83,45], index = ['S1','S2','S3','S4','S5'])
    new_students_index = ['S1','S2','S3','S4','S5','S6','S7']

    st_marks_reindexed = st_marks.reindex(new_students_index)
    print("Reindexed Series with default NaN:\n", st_marks_reindexed)
    # Output:
    # S1    78.0
    # S2    56.0
    # S3    73.0
    # S4    83.0
    # S5    45.0
    # S6     NaN
    # S7     NaN
    # dtype: float64
    ```
    As seen, `S6` and `S7` are introduced with `NaN` values because they were not present in the original `st_marks` Series.

* **Reindexing with `fill_value`:**
    To avoid `NaN` for newly introduced labels during reindexing, use the `fill_value` argument.
    ```python
    st_marks_reindexed_filled = st_marks.reindex(new_students_index, fill_value=0)
    print("Reindexed Series with fill_value=0:\n", st_marks_reindexed_filled)
    # Output:
    # S1    78
    # S2    56
    # S3    73
    # S4    83
    # S5    45
    # S6     0
    # S7     0
    # dtype: int64
    ```

## 5.6 Integration with NumPy

Pandas is built on top of NumPy, and leverages its highly optimized array operations.

* **Standard Practice:** `import numpy as np` is almost always paired with `import pandas as pd`.
* **Creating DataFrames from NumPy Arrays:** As shown in DataFrame creation examples, `np.random.randn()` for random data and `np.arange()` for sequences are commonly used to create numerical arrays that are then converted into DataFrames.
* **Underlying Data Types:** When you index a Series and retrieve a value, its underlying type often reflects NumPy's types (e.g., `np.int64(83)`).
* **Reshaping Arrays:** `numpy.reshape()` is frequently used to convert a 1D array into a 2D array suitable for DataFrame creation.

## 5.7 Comparison of Data Filtering Techniques

Both the `.drop()` method and boolean indexing are used to manipulate data, but they serve different primary purposes for filtering or removing data.

* **`.drop()` Method:**
    * **Purpose:** Primarily for **removing data permanently** (or returning a new object with data removed) based on explicit index labels (for rows) or column labels (for columns).
    * **Effectiveness:** Most effective when you know the exact rows or columns you want to eliminate.
    * **Use Case:** Removing irrelevant columns (e.g., `ID` columns after joining), or specific problematic rows identified by their index.
    * **Example:** `df.drop(['col_to_remove', 'another_col'], axis=1)`, `df.drop([0, 5, 8])`

* **Boolean Indexing:**
    * **Purpose:** Primarily for **selecting data based on conditions**, which effectively filters the data without necessarily "dropping" it from the original object. It returns a *view* or *copy* of the data that matches the criteria.
    * **Effectiveness:** Most effective for dynamic filtering based on data values.
    * **Use Case:** Selecting all customers who made purchases over a certain amount, filtering out data points that fall outside a specific range, or selecting rows with specific string patterns.
    * **Example:** `df[df['sales'] > 1000]`, `df[df['city'] == 'New York']`

* **Key Differences:**
    * `drop()` removes by **label/position**. Boolean indexing filters by **value/condition**.
    * `drop()` is often about removing *known* unwanted parts. Boolean indexing is about *selecting* desired parts based on their content.

## Glossary of Key Terms (Consolidated)

* **Pandas:** A fast, powerful, flexible, and easy-to-use open-source data analysis and manipulation library for Python, built on top of the NumPy library.
* **NumPy:** A fundamental package for scientific computing with Python, providing support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.
* **Series:** A one-dimensional labeled array capable of holding any data type. It is one of the primary data structures in Pandas.
* **DataFrame:** A two-dimensional labeled data structure with columns of potentially different types. It is the most commonly used Pandas object, analogous to a spreadsheet or SQL table.
* **Index:** The labels (either numeric or custom) associated with rows in a Series or DataFrame, used for data selection and alignment.
* **`pip install pandas`:** A command-line instruction used to install the Pandas library in a Python environment.
* **`import pandas as pd`:** The standard convention for importing the Pandas library into a Python script or notebook, aliasing it as `pd`.
* **`import numpy as np`:** The standard convention for importing the NumPy library, aliasing it as `np`.
* **Boolean Indexing:** A method of selecting data from a Series or DataFrame based on a boolean condition, where `True` values in the boolean Series/DataFrame indicate rows/columns to be selected.
* **`.to_dict()`:** A Pandas method used to convert a Series or DataFrame into a Python dictionary.
* **NaN (Not a Number):** A special floating-point value in Pandas and NumPy representing missing or undefined data.
* **`.isnull()`:** A Series or DataFrame method that returns a boolean Series/DataFrame indicating where values are `NaN`.
* **`.notnull()`:** A Series or DataFrame method (or a top-level Pandas function `pd.notnull()`) that returns a boolean Series/DataFrame indicating where values are not `NaN`.
* **`.drop()`:** A Series or DataFrame method used to remove specified rows or columns. The `axis` parameter determines whether rows (`axis=0`) or columns (`axis=1`) are dropped.
* **`.reindex()`:** A Series or DataFrame method used to conform an object to a new index. It can introduce `NaN` values for labels not present in the original object.
* **`fill_value`:** An optional parameter used with methods like `reindex()` or during arithmetic operations to specify a value to substitute for missing data (`NaN`) when aligning objects.
* **`randn()`:** A NumPy function from `numpy.random` that generates random numbers following a standard normal (Gaussian) distribution.
* **`.reshape()`:** A NumPy array method used to change the shape (dimensions) of an array without changing its data.
* **`.loc[]`:** A label-based indexer for selecting data by row and column labels in a DataFrame.
* **`.iloc[]`:** An integer-location based indexer for selecting data by integer position in a DataFrame.
* **`axis`:** A parameter used in many Pandas functions to specify whether an operation should be performed row-wise (`axis=0`) or column-wise (`axis=1`).

-