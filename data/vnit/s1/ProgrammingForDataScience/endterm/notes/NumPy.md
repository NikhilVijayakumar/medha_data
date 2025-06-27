# NumPy (Numerical Python) Details

NumPy is the fundamental package for numerical computing with Python. It provides:

1.  **A powerful N-dimensional array object (ndarray):** This is the core data structure, allowing efficient storage and manipulation of large datasets.
2.  **Sophisticated (broadcasting) functions:** For performing operations on arrays of different shapes.
3.  **Tools for integrating C/C++ and Fortran code:** For speed-critical operations.
4.  **Useful linear algebra, Fourier transform, and random number capabilities:** Essential for scientific computing.

**Common Import Convention:**

```python
import numpy as np
```

### The NumPy `ndarray` (N-dimensional Array)

The `ndarray` is the central object in NumPy. It's a grid of values, all of the same type, and is indexed by a tuple of non-negative integers.

**Creating Arrays:**

```python
import numpy as np

# From a Python list
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr1)
print("Type:", type(arr1))
print("Shape:", arr1.shape) # (5,)

# From a nested Python list (creates a 2D array/matrix)
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:\n", arr2)
print("Shape:", arr2.shape) # (2, 3)

# Arrays with initial placeholders
arr_zeros = np.zeros((2, 3)) # 2 rows, 3 columns of zeros
print("\nZeros Array:\n", arr_zeros)

arr_ones = np.ones((3, 2)) # 3 rows, 2 columns of ones
print("\nOnes Array:\n", arr_ones)

arr_empty = np.empty((2, 2)) # Uninitialized (arbitrary) values
print("\nEmpty Array (values depend on memory):\n", arr_empty)

# Array with a range of numbers
arr_range = np.arange(10) # 0 to 9
print("\nArange Array:", arr_range)

arr_range_step = np.arange(0, 10, 2) # Start, Stop (exclusive), Step
print("Arange with Step:", arr_range_step)

# Random numbers
arr_random_uniform = np.random.rand(2, 3) # Uniform distribution [0, 1)
print("\nRandom Uniform Array:\n", arr_random_uniform)

arr_random_normal = np.random.randn(2, 3) # Standard normal (Gaussian) distribution (mean 0, variance 1)
print("\nRandom Normal Array (randn):\n", arr_random_normal)
```

### Common Calculation Methods

NumPy provides highly optimized functions for performing mathematical operations on arrays. These operations are often much faster than their pure Python counterparts due to their implementation in C.

Let's use an example array:

```python
data = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
matrix_data = np.array([[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]])
```

#### 1\. Minimum Value

  * **Method:** `np.min()` or `array.min()`
  * **Description:** Returns the minimum value in an array. For multi-dimensional arrays, you can specify an `axis` to find the minimum along rows or columns.

<!-- end list -->

```python
print(f"Minimum value in data: {np.min(data)}") # or data.min()
print(f"Minimum value in matrix_data: {matrix_data.min()}")
print(f"Minimum value along columns (axis=0) in matrix_data: {matrix_data.min(axis=0)}") # [1 2 3]
print(f"Minimum value along rows (axis=1) in matrix_data: {matrix_data.min(axis=1)}")    # [1 4 7]
```

#### 2\. Maximum Value

  * **Method:** `np.max()` or `array.max()`
  * **Description:** Returns the maximum value in an array. For multi-dimensional arrays, you can specify an `axis`.

<!-- end list -->

```python
print(f"Maximum value in data: {np.max(data)}") # or data.max()
print(f"Maximum value in matrix_data: {matrix_data.max()}")
print(f"Maximum value along columns (axis=0) in matrix_data: {matrix_data.max(axis=0)}") # [7 8 9]
print(f"Maximum value along rows (axis=1) in matrix_data: {matrix_data.max(axis=1)}")    # [3 6 9]
```

#### 3\. Mean Value

  * **Method:** `np.mean()` or `array.mean()`
  * **Description:** Computes the arithmetic mean of the array elements.

<!-- end list -->

```python
print(f"Mean value of data: {np.mean(data)}") # or data.mean()
print(f"Mean value of matrix_data: {matrix_data.mean()}")
print(f"Mean value along columns (axis=0) in matrix_data: {matrix_data.mean(axis=0)}")
print(f"Mean value along rows (axis=1) in matrix_data: {matrix_data.mean(axis=1)}")
```

#### 4\. Median Value

  * **Method:** `np.median()`
  * **Description:** Computes the median of the array elements. The median is the middle value in a sorted list of numbers.

<!-- end list -->

```python
print(f"Median value of data: {np.median(data)}")
print(f"Median value of matrix_data: {np.median(matrix_data)}")
print(f"Median value along columns (axis=0) in matrix_data: {np.median(matrix_data, axis=0)}")
print(f"Median value along rows (axis=1) in matrix_data: {np.median(matrix_data, axis=1)}")
```

#### 5\. Standard Deviation

  * **Method:** `np.std()` or `array.std()`
  * **Description:** Computes the standard deviation of the array elements. It measures the amount of variation or dispersion of a set of values.
  * **To 2 decimal points:** Use f-strings with `:.2f`.

<!-- end list -->

```python
std_dev_data = np.std(data)
print(f"Standard Deviation of data: {std_dev_data:.2f}")

std_dev_matrix = np.std(matrix_data)
print(f"Standard Deviation of matrix_data: {std_dev_matrix:.2f}")

std_dev_cols = np.std(matrix_data, axis=0)
print(f"Standard Deviation along columns (axis=0) in matrix_data: {std_dev_cols}")

std_dev_rows = np.std(matrix_data, axis=1)
print(f"Standard Deviation along rows (axis=1) in matrix_data: {std_dev_rows}")
```

#### 6\. Variance

  * **Method:** `np.var()` or `array.var()`
  * **Description:** Computes the variance of the array elements. Variance is the average of the squared differences from the mean. It is the square of the standard deviation.
  * **To 2 decimal points:** Use f-strings with `:.2f`.

<!-- end list -->

```python
variance_data = np.var(data)
print(f"Variance of data: {variance_data:.2f}")

variance_matrix = np.var(matrix_data)
print(f"Variance of matrix_data: {variance_matrix:.2f}")

variance_cols = np.var(matrix_data, axis=0)
print(f"Variance along columns (axis=0) in matrix_data: {variance_cols}")

variance_rows = np.var(matrix_data, axis=1)
print(f"Variance along rows (axis=1) in matrix_data: {variance_rows}")
```

### Matrix Operations (Linear Algebra)

NumPy is incredibly powerful for linear algebra operations.

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix Multiplication (Dot Product)
C = np.dot(A, B) # or A @ B (Python 3.5+)
print("\nMatrix Multiplication (A @ B):\n", C)

# Transpose
A_t = A.T
print("\nTranspose of A:\n", A_t)

# Determinant
det_A = np.linalg.det(A)
print(f"\nDeterminant of A: {det_A}")

# Inverse
try:
    inv_A = np.linalg.inv(A)
    print("\nInverse of A:\n", inv_A)
    print("A dot A_inv (should be identity matrix):\n", A @ inv_A)
except np.linalg.LinAlgError as e:
    print(f"\nCould not calculate inverse of A: {e}")

# Eigenvalues and Eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
print(f"\nEigenvalues of A: {eigenvalues}")
print(f"Eigenvectors of A:\n {eigenvectors}")
```

### Normalization

Normalization (or standardization) is a common preprocessing step in data science to scale numerical data. Two common types are Min-Max Normalization and Z-score Standardization.

#### 1\. Min-Max Normalization

Scales values to a range (e.g., \[0, 1]).
Formula: $X\_{normalized} = (X - X\_{min}) / (X\_{max} - X\_{min})$

```python
data_to_normalize = np.array([10, 20, 30, 40, 50])

min_val = np.min(data_to_normalize)
max_val = np.max(data_to_normalize)

normalized_data = (data_to_normalize - min_val) / (max_val - min_val)
print(f"\nOriginal data for normalization: {data_to_normalize}")
print(f"Min-Max Normalized data: {normalized_data}")
```

#### 2\. Z-score Standardization

Scales values to have a mean of 0 and a standard deviation of 1.
Formula: $X\_{standardized} = (X - \\mu) / \\sigma$ (where $\\mu$ is mean, $\\sigma$ is standard deviation)

```python
mean_val = np.mean(data_to_normalize)
std_dev_val = np.std(data_to_normalize)

standardized_data = (data_to_normalize - mean_val) / std_dev_val
print(f"Z-score Standardized data: {standardized_data}")
```

### Other Common Use Cases

#### Reshaping Arrays

Changing the dimensions of an array without changing its data.

  * **Method:** `.reshape()`

<!-- end list -->

```python
arr_1d = np.arange(12) # [ 0  1  2  3  4  5  6  7  8  9 10 11]
print(f"\nOriginal 1D array:\n{arr_1d}")

arr_2d = arr_1d.reshape(3, 4) # 3 rows, 4 columns
print(f"\nReshaped to 3x4:\n{arr_2d}")

arr_3d = arr_1d.reshape(2, 2, 3) # 2 "slices", 2 rows, 3 columns
print(f"\nReshaped to 2x2x3:\n{arr_3d}")

# Using -1 to infer a dimension
arr_inferred = arr_1d.reshape(4, -1) # 4 rows, NumPy calculates columns
print(f"\nReshaped with inferred dimension (4x-1):\n{arr_inferred}")
```

#### Element-wise Operations

Arithmetic operations on NumPy arrays are performed element-wise.

```python
arr_a = np.array([1, 2, 3])
arr_b = np.array([4, 5, 6])

print(f"\narr_a + arr_b: {arr_a + arr_b}")
print(f"arr_a * arr_b: {arr_a * arr_b}")
print(f"arr_a / arr_b: {arr_a / arr_b}")
print(f"arr_a ** 2: {arr_a ** 2}") # Element-wise exponentiation
```

#### Broadcasting

NumPy's ability to operate on arrays of different shapes during arithmetic operations.

```python
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
scalar = 10

# Scalar added to all elements
print(f"\nMatrix + Scalar:\n{matrix + scalar}")

vector = np.array([10, 20, 30])

# Vector added to each row (or column if reshaped for column-wise operation)
# This is equivalent to adding [10, 20, 30] to [1,2,3], then to [4,5,6], etc.
print(f"\nMatrix + Vector (row-wise broadcasting):\n{matrix + vector}")

# To add column-wise, reshape the vector
column_vector = np.array([[10], [20], [30]])
print(f"\nMatrix + Column Vector (column-wise broadcasting):\n{matrix + column_vector}")
```

#### Slicing and Indexing

Similar to Python lists, but more powerful for multi-dimensional arrays.

```python
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print(f"\nOriginal matrix:\n{matrix}")

# Accessing a single element (row, column)
print(f"Element at [0, 0]: {matrix[0, 0]}") # 1

# Slicing rows
print(f"First row: {matrix[0, :]}") # or matrix[0]
print(f"First two rows:\n{matrix[:2, :]}")

# Slicing columns
print(f"First column: {matrix[:, 0]}")
print(f"Last two columns:\n{matrix[:, 1:]}")

# Sub-matrix
print(f"Sub-matrix (rows 0-1, cols 1-2):\n{matrix[:2, 1:]}")

# Boolean Indexing
print(f"\nElements greater than 5:\n{matrix[matrix > 5]}") # Returns a 1D array of values
```

#### Universal Functions (ufuncs)

NumPy provides "universal functions" (`ufuncs`) that operate element-wise on `ndarray`s. These are highly optimized for speed.

```python
arr = np.array([-1, 0, 1, 2, -3])

print(f"\nAbsolute values: {np.abs(arr)}")
print(f"Square root (element-wise): {np.sqrt(np.array([4, 9, 16]))}")
print(f"Exponential (e^x): {np.exp(arr)}")
print(f"Logarithm (natural): {np.log(np.array([1, 2, 3]))}")
print(f"Sine: {np.sin(arr)}")
```

This comprehensive overview of NumPy, covering array creation, common calculations, matrix operations, normalization, and other essential functionalities, should provide a solid foundation before diving deeper into Pandas. Understanding these core concepts in NumPy will make the data manipulation in Pandas much more intuitive.