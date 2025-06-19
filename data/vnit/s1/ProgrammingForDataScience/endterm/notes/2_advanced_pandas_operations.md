# Module 5: Data Manipulation & Data Visualization - Advanced Pandas Operations

This section expands on the foundational Pandas concepts by exploring more advanced data manipulation techniques, including sophisticated missing data handling, various sorting and ranking methods, the power of Multi-Indexing, and diverse strategies for combining datasets.

## 5.1 Handling Missing Data (NaN Values)

Missing data is an inevitable part of real-world datasets. Pandas uses `NaN` (Not a Number), a special floating-point value from NumPy, to denote missing or undefined entries. Effectively handling these values is crucial for accurate analysis.

### 5.1.1 Identifying Missing Values

* **`isnull()`**: This method is used to detect missing or `NaN` values within a Pandas Series or DataFrame. It returns a boolean Series or DataFrame of the same shape, where `True` indicates a `NaN` value and `False` indicates a non-`NaN` value. This is fundamental for data cleaning and understanding incomplete datasets.

    **Example (Series):**
    ```python
    import pandas as pd
    import numpy as np

    data = pd.Series([1, 2, None, 3]) # None is converted to NaN
    print(data.isnull())
    # Output:
    # 0    False
    # 1    False
    # 2     True
    # 3    False
    # dtype: bool
    ```

    **Example (DataFrame):**
    ```python
    df = pd.DataFrame([[1, 2, 3], [np.nan, 5, 6], [np.nan, np.nan, np.nan]])
    print(df.isnull())
    # Output:
    #        0      1      2
    # 0  False  False  False
    # 1   True  False  False
    # 2   True   True   True
    ```

### 5.1.2 Dropping Missing Values

* **`dropna()`**: This method is used to remove rows or columns from a Series or DataFrame that contain missing (`NaN`) values.

    **Example (Series):**
    ```python
    print(data.dropna())
    # Output:
    # 0    1.0
    # 1    2.0
    # 3    3.0
    # dtype: float64
    ```

    **Example (DataFrame):**
    By default, `df.dropna()` removes any row containing at least one `NaN` value.
    ```python
    print(df.dropna())
    # Output:
    #    0  1  2
    # 0  1  2  3
    ```
    In this example, only the first row remains because the others contain `NaN` values. You can also specify `axis=1` to drop columns with `NaN` values, or `how='all'` to drop only rows/columns where *all* values are `NaN`.

### 5.1.3 Filling Missing Values

* **`fillna()`**: This method allows for replacing `NaN` values with specified data or using specific fill strategies (e.g., forward-fill, back-fill).

    **Example (Filling with a constant):**
    ```python
    print(data.fillna(0))
    # Output:
    # 0    1.0
    # 1    2.0
    # 2    0.0
    # 3    3.0
    # dtype: float64
    ```

* **Filling NaN values from another Series/DataFrame:**
    You can replace `NaN` values in one Series with corresponding values from another Series at the same index.

    1.  **Using `fillna()` with another Series:**
        ```python
        ser1 = pd.Series([1, np.nan, 3], index=['A', 'B', 'C'])
        ser2 = pd.Series([10, 20, 30], index=['A', 'B', 'C'])
        print(ser1.fillna(ser2))
        # Output:
        # A     1.0
        # B    20.0
        # C     3.0
        # dtype: float64
        ```
        This replaces `NaN` values in `ser1` with corresponding values from `ser2`.

    2.  **Using `numpy.where` (less direct for Pandas but useful for understanding logic):**
        ```python
        # This uses numpy.where to conditionally select values.
        # It's more verbose but illustrates the underlying conditional logic.
        import numpy as np
        print(pd.Series(np.where(ser1.notnull(), ser1, ser2), index=ser1.index))
        # Output:
        # A     1.0
        # B    20.0
        # C     3.0
        # dtype: float64
        ```

    3.  **`combine_first()`**: This Pandas method is specifically designed to combine two Series or DataFrames. It takes non-null values from the calling object first, then fills any remaining `NaN` values with corresponding values from the passed object. Where values are not `NaN` in the calling object, those values are retained.

        ```python
        print(ser1.combine_first(ser2))
        # Output:
        # A     1.0
        # B    20.0
        # C     3.0
        # dtype: float64
        ```
        This method is concise and idiomatic for this type of operation in Pandas.

**Real-world scenario for missing data handling:**
Imagine a dataset of customer orders where `delivery_date` might be missing for pending orders, and `payment_status` might be `NaN` for abandoned carts.
* You might use `isnull()` to count how many orders are pending delivery or have unknown payment status.
* You could use `dropna(subset=['payment_status'])` to analyze only completed transactions.
* For pending orders, you might use `fillna({'delivery_date': 'Pending', 'payment_status': 'Unknown'})` to make these values explicit strings for reporting purposes, instead of `NaN`.
* If you have a backup dataset of payment records, `orders_df['payment_status'].combine_first(backup_payments_series)` could be used to fill in missing payment statuses from the backup.

## 5.2 Sorting and Ranking Data

Pandas provides flexible methods for ordering and ranking data within Series and DataFrames, essential for data exploration and preparation.

### 5.2.1 Sorting by Index

* **`sort_index()`**: This method sorts a Series or DataFrame based on its index labels. By default, it sorts in ascending order.
    ```python
    ser1_unsorted_index = pd.Series([11, 22, 33], index=['A', 'C', 'B'])
    print(ser1_unsorted_index.sort_index())
    # Output:
    # A    11
    # B    33
    # C    22
    # dtype: int64
    ```
    For DataFrames, `sort_index()` can sort by row index (`axis=0`, default) or column index (`axis=1`).

### 5.2.2 Sorting by Values

* **`sort_values()`**: This method sorts a Series or DataFrame based on the actual values in its data. For DataFrames, you need to specify the column(s) by which to sort using the `by` parameter. By default, it sorts in ascending order.
    ```python
    print(ser1_unsorted_index.sort_values())
    # Output:
    # A    11
    # C    22
    # B    33
    # dtype: int64
    ```

### 5.2.3 Ranking Values

* **`rank()`**: This Series method assigns numerical ranks to values. It's particularly useful for understanding the relative position of values within a dataset. The `method` argument determines how ties (duplicate values) are handled.

    * **`method='dense'`**: Duplicate values are assigned the same rank, and the next rank assigned is the next consecutive integer, without skipping any ranks. For example, if two values are tied for the 2nd rank, the next unique value will receive rank 3.
        ```python
        ser_for_rank = pd.Series([11, 22, 22, 44, 55])
        print(ser_for_rank.rank(method='dense').astype(int))
        # Output:
        # 0    1
        # 1    2
        # 2    2
        # 3    3
        # 4    4
        # dtype: int64
        ```
        Other `method` options include `'average'` (default, assigns average rank to ties), `'min'` (assigns lowest rank in ties), `'max'` (assigns highest rank in ties), and `'first'` (assigns rank based on order of appearance).

## 5.3 Multi-Indexing (Hierarchical Indexing)

MultiIndex (or Hierarchical Index) allows for **multiple levels of indexing** on an axis (rows or columns), enabling you to work with higher-dimensional data in a lower-dimensional structure like a Series or DataFrame. This is particularly beneficial for organizing complex datasets.

### 5.3.1 Creating a Multi-Indexed Series

A Series can be created with a list of arrays (or a list of lists) for its index, where each inner list represents a level of the hierarchy.

```python
ser3 = pd.Series([12, 78, 23, 22, 45, 38], index=[['A', 'A', 'A', 'B', 'B', 'B'], [1, 2, 3, 1, 2, 3]])
print(ser3.index)
# Output:
# MultiIndex([('A', 1), ('A', 2), ('A', 3), ('B', 1), ('B', 2), ('B', 3)],)
```

### 5.3.2 Selecting Data with Multi-Index

Data can be selected using slicing across the index levels.
```python
print(ser3[:, 2]) # Selects all values where the second level of the index is 2
# Output:
# A    78
# B    45
# dtype: int64
```
For more advanced selection with MultiIndex, `.loc` is often used, providing tuple-based indexing.

### 5.3.3 Converting Multi-level Series to DataFrame (`unstack()`)

The `unstack()` method is a powerful tool that pivots the innermost index level to become column labels, effectively transforming a Multi-Indexed Series into a DataFrame or reshaping a Multi-Indexed DataFrame. This makes the data more accessible and often more readable by spreading out hierarchical index levels into columns.

```python
dataframe_from_ser3 = ser3.unstack()
print(dataframe_from_ser3)
# Output:
#    1   2   3
# A  12  78  23
# B  22  45  38
```
Applying `unstack()` again will further pivot the DataFrame, potentially leading back to a Series or reshaping it further.

### 5.3.4 Creating a Multi-Indexed DataFrame

Similar to Series, DataFrames can have multi-level row and column indices.

```python
df2 = pd.DataFrame(np.arange(16).reshape(4, 4),
                   index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                   columns=[['x', 'x', 'y', 'z'], ['c1', 'c2', 'c3', 'c4']])
print(df2)
# Output:
#       x       y   z
#      c1 c2    c3 c4
# a 1   0  1     2  3
#   2   4  5     6  7
# b 1   8  9    10 11
#   2  12 13    14 15
```

### 5.3.5 Renaming MultiIndex Levels

Index and column levels can be assigned meaningful names using the `.index.names` and `.columns.names` attributes, respectively. This improves readability and understanding of the data structure.

```python
df2.index.names = ['ind1', 'ind2']
df2.columns.names = ['col1', 'col2']
print(df2)
# Output:
# col1    x       y   z
# col2   c1 c2    c3 c4
# ind1 ind2
# a    1    0  1     2  3
#      2    4  5     6  7
# b    1    8  9    10 11
#      2   12 13    14 15
```

### 5.3.6 Swapping MultiIndex Levels (`swaplevel()`)

The `swaplevel()` method is used to interchange the levels of a MultiIndex on either an axis (rows or columns) of a DataFrame. This is useful for reordering the presentation of data or preparing for subsequent operations that rely on a specific index level order.

* **Swapping Column Levels:**
    ```python
    print(df2.swaplevel('col2', 'col1', axis=1)) # Swaps 'col1' and 'col2' levels in columns
    # Output:
    # col2   c1 c2    c3 c4
    # col1    x       y   z
    # ind1 ind2
    # a    1    0  1     2  3
    #      2    4  5     6  7
    # b    1    8  9    10 11
    #      2   12 13    14 15
    ```

* **Swapping Row Levels:**
    ```python
    print(df2.swaplevel('ind1', 'ind2', axis=0)) # Swaps 'ind1' and 'ind2' levels in rows
    # Output:
    # col1    x       y   z
    # col2   c1 c2    c3 c4
    # ind2 ind1
    # 1    a    0  1     2  3
    # 2    a    4  5     6  7
    # 1    b    8  9    10 11
    # 2    b   12 13    14 15
    ```

### 5.3.7 Sorting by MultiIndex Level

`sort_index(level=X)` sorts the DataFrame by a specific index level `X`. The `ascending=False` argument reverses the sort order.

```python
# Assuming df2 is the multi-indexed DataFrame from above
print(df2.sort_index(level='ind2', ascending=False))
# Output:
# col1    x       y   z
# col2   c1 c2    c3 c4
# ind1 ind2
# a    2    4  5     6  7
# b    2   12 13    14 15
# a    1    0  1     2  3
# b    1    8  9    10 11
```

## 5.4 Combining DataFrames and Series

Pandas offers robust methods for combining Series and DataFrames, crucial for integrating data from various sources.

### 5.4.1 Merging DataFrames (`pd.merge()`)

The `pd.merge()` function is a general function for combining DataFrames based on common columns (keys) or indices, similar to SQL joins. The `how` parameter specifies the type of join (`'inner'`, `'outer'`, `'left'`, `'right'`).

* **Merging on Common Key Columns:**
    ```python
    df3 = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                        'A': ['A0', 'A1', 'A2', 'A3']})
    df4 = pd.DataFrame({'key': ['K0', 'K1', 'K4', 'K5'],
                        'B': ['B0', 'B1', 'B2', 'B3']})

    print("df3:\n", df3)
    print("\ndf4:\n", df4)

    # Right Merge: Includes all keys from the right DataFrame (df4),
    # and matching keys from the left DataFrame (df3).
    # If a key from df4 has no match in df3, columns from df3 will contain NaN.
    right_merged_df = pd.merge(df3, df4, on='key', how='right')
    print("\nRight Merge (how='right'):\n", right_merged_df)
    # Output:
    # df3:
    #   key   A
    # 0  K0  A0
    # 1  K1  A1
    # 2  K2  A2
    # 3  K3  A3
    #
    # df4:
    #   key   B
    # 0  K0  B0
    # 1  K1  B1
    # 2  K4  B2
    # 3  K5  B3
    #
    # Right Merge (how='right'):
    #   key    A   B
    # 0  K0   A0  B0
    # 1  K1   A1  B1
    # 2  K4  NaN  B2
    # 3  K5  NaN  B3
    ```

* **Merging on Index:**
    You can merge on the index of one or both DataFrames using `left_index=True` and/or `right_index=True`.
    ```python
    df5 = pd.DataFrame({'key': ['K0', 'K1', 'K2'], 'A': ['A0', 'A1', 'A2']})
    df6 = pd.DataFrame({'B': ['B0', 'B1', 'B2']}, index=['K0', 'K1', 'K2']) # df6 has 'K0','K1','K2' as index

    print("df5:\n", df5)
    print("\ndf6:\n", df6)

    # Merge df5 using its 'key' column and df6 using its index
    merged_on_index = pd.merge(df5, df6, left_on='key', right_index=True)
    print("\nMerge (left_on='key', right_index=True):\n", merged_on_index)
    # Output:
    # df5:
    #   key   A
    # 0  K0  A0
    # 1  K1  A1
    # 2  K2  A2
    #
    # df6:
    #      B
    # K0  B0
    # K1  B1
    # K2  B2
    #
    # Merge (left_on='key', right_index=True):
    #   key   A   B
    # 0  K0  A0  B0
    # 1  K1  A1  B1
    # 2  K2  A2  B2
    ```
    `pd.merge()` is more general than `DataFrame.join()` and is usually preferred for complex join operations.

### 5.4.2 Joining DataFrames (`DataFrame.join()`)

The `DataFrame.join()` method is similar to `merge()` but is primarily designed for combining DataFrames on their indices. It offers a more concise syntax for certain merge operations.

```python
# Using df5 and df6 from the merge example above
joined_df = df5.set_index('key').join(df6) # Set 'key' as index for df5 to join on index
print("Joined DataFrame (df5.set_index('key').join(df6)):\n", joined_df)
# Output:
#       A   B
# key
# K0   A0  B0
# K1   A1  B1
# K2   A2  B2
```
`df5.join(df6)` directly would attempt to join `df5` and `df6` on their respective current (default integer) indices. If the indices don't align perfectly, `NaN` values will be introduced.

### 5.4.3 Concatenating Data (`pd.concat()`)

`pd.concat()` is used to concatenate (stack or append) Series or DataFrames along a particular axis.

* **Concatenating NumPy Arrays (underlying concept):**
    ```python
    arr1 = np.arange(6).reshape(3,2)
    print(np.concatenate([arr1, arr1], axis=1)) # Appends arr1 to itself column-wise
    # Output:
    # [[0 1 0 1]
    #  [2 3 2 3]
    #  [4 5 4 5]]
    ```

* **Concatenating Series:**
    1.  **Column-wise (creating a DataFrame):**
        ```python
        ser_a = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
        ser_b = pd.Series([4, 5, 6], index=['c', 'd', 'e'])
        print(pd.concat([ser_a, ser_b], axis=1)) # Concatenates two Series as columns
        # Output:
        #      0    1
        # a  1.0  NaN
        # b  2.0  NaN
        # c  3.0  4.0
        # d  NaN  5.0
        # e  NaN  6.0
        ```
        `NaN` values appear where indices don't align.

    2.  **Row-wise (stacking vertically) with `keys` for MultiIndex:**
        The `keys` argument allows for the creation of a MultiIndex on the concatenation axis, typically used to identify the source of each concatenated object.
        ```python
        print(pd.concat([ser_a, ser_b], axis=0, keys=['SeriesA', 'SeriesB']))
        # Output:
        # SeriesA  a    1
        #          b    2
        #          c    3
        # SeriesB  c    4
        #          d    5
        #          e    6
        # dtype: int64
        ```

* **Concatenating DataFrames:**
    By default, `pd.concat([df1, df2])` stacks DataFrames vertically (along `axis=0`). Columns that are not common to both DataFrames will be filled with `NaN`.
    ```python
    df7 = pd.DataFrame({'A': ['A0', 'A1'], 'B': ['B0', 'B1']}, index=[0, 1])
    df8 = pd.DataFrame({'C': ['C2', 'C3'], 'D': ['D2', 'D3']}, index=[2, 3])
    print(pd.concat([df7, df8]))
    # Output:
    #      A    B    C    D
    # 0   A0   B0  NaN  NaN
    # 1   A1   B1  NaN  NaN
    # 2  NaN  NaN   C2   D2
    # 3  NaN  NaN   C3   D3
    ```
    If you concatenate along `axis=1`, it joins them side-by-side, aligning on the index.

**Comparison of `pd.merge()` vs. `pd.concat()`:**

* **`pd.merge()`:**
    * **Purpose:** Combines DataFrames based on **shared values** in one or more columns (keys) or indices. It's about finding relationships between data points in different tables.
    * **Analogy:** Database joins (INNER, OUTER, LEFT, RIGHT).
    * **Scenario:** Combining a customer information table with an order history table based on a `customer_ID` column.

* **`pd.concat()`:**
    * **Purpose:** Stacks or appends Series/DataFrames **along an axis**. It's about combining objects that have similar structures (same columns for row-wise concat, same rows for column-wise concat).
    * **Analogy:** Stacking Lego blocks.
    * **Scenario:** Appending monthly sales reports (each with the same columns but different rows), or combining multiple sensor readings (same index but different data columns).

## Glossary of Key Terms (Consolidated)

* **Pandas:** An open-source data analysis and manipulation library for Python.
* **Series:** A one-dimensional labeled array-like object in Pandas, capable of holding any data type.
* **DataFrame:** A two-dimensional labeled data structure in Pandas with columns of potentially different types, analogous to a spreadsheet or SQL table.
* **NaN (Not a Number):** A special floating-point value representing undefined or unrepresentable numerical results, commonly used in Pandas to denote missing data.
* **`isnull()`:** A Pandas method used to detect missing values (`NaN`) in a Series or DataFrame, returning a boolean object of the same shape.
* **`dropna()`:** A Pandas method used to remove rows or columns from a Series or DataFrame that contain missing (`NaN`) values.
* **`fillna()`:** A Series or DataFrame method used to fill missing (`NaN`) values with a specified value or using a specific method (e.g., forward-fill, back-fill).
* **`combine_first()`:** A Series or DataFrame method that fills `NaN` values in the calling object with corresponding values from another Series or DataFrame. Where values are not `NaN` in the calling object, those values are retained.
* **`sort_index()`:** A Series or DataFrame method that sorts the object by its index labels.
* **`sort_values()`:** A Series or DataFrame method that sorts the object by the values in its data.
* **`rank()`:** A Series method that computes numerical data ranks (e.g., 1st, 2nd, ...) for each element. The `method` argument (`dense`, `average`, `min`, `max`, `first`) determines how ties are handled.
* **MultiIndex (Hierarchical Index):** A Pandas index object that allows for multiple levels of indexing on a single axis (rows or columns), enabling the representation of higher-dimensional data.
* **`unstack()`:** A Series or DataFrame method that pivots the innermost index level to become column labels, effectively reshaping the data.
* **`index.names`:** An attribute used to set or retrieve the names of the levels in a MultiIndex for a DataFrame's rows.
* **`columns.names`:** An attribute used to set or retrieve the names of the levels in a MultiIndex for a DataFrame's columns.
* **`swaplevel()`:** A DataFrame method used to interchange two levels of a MultiIndex on either the row (`axis=0`) or column (`axis=1`) axis.
* **`pd.merge()`:** A Pandas function for combining DataFrames based on common columns or indices, similar to SQL joins. The `how` argument (`'inner'`, `'outer'`, `'left'`, `'right'`) specifies the type of merge.
* **`left_on` / `right_on`:** Arguments in `pd.merge()` that specify the column(s) from the left/right DataFrame to use as keys for merging.
* **`left_index` / `right_index`:** Arguments in `pd.merge()` that, when set to `True`, indicate that the index of the left/right DataFrame should be used as the merge key.
* **`DataFrame.join()`:** A DataFrame method used to combine DataFrames, typically based on their indices, offering a more concise syntax for certain merge operations.
* **`pd.concat()`:** A Pandas function used to concatenate (stack or append) Series or DataFrames along a particular axis (`axis=0` for rows, `axis=1` for columns).
* **`axis`:** A parameter in Pandas functions that specifies whether an operation should be applied along rows (`axis=0` or `'index'`) or columns (`axis=1` or `'columns'`).
* **`keys`:** An argument in `pd.concat()` that allows for the creation of a MultiIndex on the concatenation axis, typically used to identify the source of each concatenated object.

---

This document provides a comprehensive overview of advanced Pandas data manipulation, directly correlating with the relevant parts of your "Python for Data Science" syllabus, particularly Module 5. It includes explanations, examples, and distinctions between similar functionalities.

Feel free to provide any other notes you'd like me to process!