# Module 5: Data Manipulation & Data Visualization - Visualisation with Seaborn and Matplotlib

This section delves into the powerful world of data visualization in Python, primarily using the `matplotlib` and `seaborn` libraries. These tools enable us to transform raw data into insightful graphical representations, aiding in exploratory data analysis and communication of findings.

## 5.1 Core Visualization Libraries

The two primary Python libraries for plotting and statistical data visualization are:

* **Matplotlib:** A foundational plotting library, often imported as `import matplotlib.pyplot as plt`. It provides a comprehensive set of tools for creating static, animated, and interactive visualizations.
* **Seaborn:** A high-level statistical data visualization library built on top of Matplotlib. It simplifies the creation of more complex and aesthetically pleasing statistical graphics and is commonly imported as `import seaborn as sns`.

In addition, **NumPy (`np`)** provides numerical operations and **Pandas (`pd`)** offers data structures like DataFrames, which are fundamental for preparing data for visualization.

## 5.2 Basic Histograms with Matplotlib

Histograms are essential for visualizing the distribution of a single numerical dataset.

* **Creating a basic histogram:** You use the `plt.hist()` function. The typical input is a one-dimensional array or Series of numerical data.
    ```python
    import matplotlib.pyplot as plt
    import numpy as np

    dataset1 = np.random.randn(100) # Example data
    plt.hist(dataset1)
    plt.title('Basic Histogram')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()
    ```

* **Modifying appearance:**
    * **Number of bins:** The `bins` parameter controls the number of intervals into which the data range is divided, influencing granularity.
    * **Color:** The `color` parameter sets the color of the bars.
    * **Transparency:** The `alpha` parameter (values from 0 to 1) controls the transparency, crucial for overlapping plots.
    ```python
    dataset2 = np.random.randn(100) + 1 # Second example dataset
    plt.hist(dataset2, bins=20, color='green', alpha=0.5)
    plt.title('Customized Histogram')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()
    ```
    `plt.hist(dataset1, bins=20, alpha=0.5)` sets the number of bins to 20 for finer granularity and makes the bars partially transparent, which is useful for visualizing multiple distributions on the same plot.

### 5.2.1 Overlapping Histograms

To plot two datasets as overlapping histograms on the same plot, you call `plt.hist()` twice for each dataset on the same figure, ensuring you use the `alpha` parameter to make the overlapping regions visible.

```python
plt.hist(dataset1, bins=20, alpha=0.5, label='Dataset 1')
plt.hist(dataset2, bins=20, alpha=0.5, label='Dataset 2', color='red')
plt.title('Overlapping Histograms')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()
plt.show()
```

## 5.3 Seaborn's Distribution Plots and Relationships

Seaborn extends Matplotlib's capabilities, offering high-level functions for statistical graphics.

### 5.3.1 `sns.jointplot()`

* **Purpose:** `sns.jointplot()` is used to visualize the **bivariate distribution** (relationship between two variables) along with the **marginal distributions** (individual distributions) of each variable on the axes. This provides a holistic view, making it easier to understand both correlation and individual distributions simultaneously.
* **Inputs:** The primary inputs are `x` and `y` (the two continuous variables), and `data` (the DataFrame containing these variables).
* **`kind` parameter:** While the default is `'scatter'`, `jointplot` can generate other plot types within the main axes:
    * `'hex'`: Generates a hexagonal binning plot, useful for very large datasets where individual scatter points would overlap excessively. It shows density by coloring hexagons based on the number of observations within each bin.
    * `'kde'`: Shows a Kernel Density Estimate of the joint distribution.
    * `'reg'`: Displays a scatter plot with a linear regression line.

    ```python
    import seaborn as sns
    import pandas as pd

    # Example data
    df_joint = pd.DataFrame(np.random.randn(100, 2), columns=['d1', 'd2'])
    sns.jointplot(data=df_joint, x='d1', y='d2', kind='scatter')
    plt.suptitle('Joint Plot (Scatter Default)', y=1.02) # Adjust title position
    plt.show()

    sns.jointplot(data=df_joint, x='d1', y='d2', kind='hex')
    plt.suptitle('Joint Plot (Hex Binning)', y=1.02)
    plt.show()
    ```

### 5.3.2 `sns.rugplot()` and `sns.kdeplot()`

These functions help visualize univariate distributions.

* **`sns.rugplot()`:** Provides a direct visual representation of the density of observations by adding small, vertical lines (or "rug marks") along the x-axis at each data point. It complements histograms or KDE plots by showing the exact location of individual data points.

* **`sns.kdeplot()`:** Stands for **Kernel Density Estimate plot**. It generates a continuous, smoothed representation of the distribution of a dataset, rather than discrete bins like a histogram. It estimates the probability density function of a random variable.
    * **Cumulative distribution:** You can show the cumulative distribution function (CDF) by setting the `cumulative=True` parameter.

    ```python
    dataset3 = np.random.randn(50)
    plt.figure(figsize=(6, 4))
    sns.histplot(dataset3, bins=15, kde=True, color='skyblue', label='Histogram with KDE') # Combine hist and kde
    sns.rugplot(dataset3, color='red', height=0.05, label='Rug Plot')
    plt.title('Histogram, KDE, and Rug Plot')
    plt.legend()
    plt.show()

    plt.figure(figsize=(6, 4))
    sns.kdeplot(dataset3, cumulative=True, color='purple', label='Cumulative KDE')
    sns.kdeplot(dataset3, cumulative=False, color='green', linestyle='--', label='Standard KDE')
    plt.title('KDE Plot (Standard vs. Cumulative)')
    plt.legend()
    plt.show()
    ```

### 5.3.3 Box Plots and Violin Plots

Both are used to visualize the distribution of a quantitative variable across different categories.

* **Box Plots (`sns.boxplot()`):** Primarily display statistical information about the distribution:
    * Median (the line inside the box).
    * Interquartile Range (IQR - the box itself, from 25th to 75th percentile).
    * Whiskers (extend to a certain range of data, usually 1.5 times the IQR, or to the min/max if within that range).
    * Potential outliers (points beyond the whiskers).
    * The `whis` parameter can be used to control the extent of the whiskers; `whis=np.inf` extends whiskers to the minimum and maximum data points, showing all data within the range without traditional outlier exclusion.

* **Violin Plots (`sns.violinplot()`):** Extend the information provided by box plots by showing the full probability density of the data at different values (like a mirrored KDE plot). This allows you to see the shape of the distribution, including multimodality, skewness, and density variations, which a box plot would not reveal.
    * `bw_adjust`: Adjusts the bandwidth of the kernel density estimate, affecting the smoothness of the density curve.
    * `inner`: Specifies what to draw inside the violins (e.g., `'box'`, `'quartile'`, `'stick'` for individual data points).

    **When to choose:**
    * Choose a **box plot** for a concise summary, quick comparison of central tendency and spread, and clear outlier indication.
    * Choose a **violin plot** when you need to visualize the full distribution shape (e.g., multimodality, skewness) and density, providing a richer representation beyond just quartiles.

    ```python
    # Load example dataset
    tips = sns.load_dataset('tips')

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1) # Subplot 1 for Boxplot
    sns.boxplot(x='day', y='total_bill', data=tips, whis=np.inf)
    plt.title('Box Plot (whiskers to all data)')

    plt.subplot(1, 2, 2) # Subplot 2 for Violinplot
    sns.violinplot(x='day', y='total_bill', data=tips, inner='quartile', bw_adjust=0.5)
    plt.title('Violin Plot')
    plt.tight_layout()
    plt.show()
    ```

## 5.4 High-Level Seaborn Functions for Complex Visualizations

Seaborn offers figure-level functions (`relplot`, `displot`, `catplot`) that simplify creating plots across different subsets of a dataset using faceting.

### 5.4.1 Relational Plots (`sns.relplot()`)

* **Purpose:** `relplot` (relational plot) is designed to visualize **statistical relationships between quantitative variables**. It's a figure-level function that can generate scatter plots or line plots with great flexibility in showing different semantic mappings.
* **Parameters for encoding additional variables:**
    * `hue`: Maps a variable to the **color** of plot elements, differentiating categories or values.
    * `style`: Maps a variable to the **marker style** (e.g., shape) of plot elements.
    * `size`: Maps a variable to the **size** of plot elements.
    * `sizes`: Specifies the range of sizes to use when `size` is mapped to a quantitative variable (e.g., `sizes=(2, 100)`).

    ```python
    sns.relplot(data=tips, x='total_bill', y='tip',
                hue='sex',      # Color-codes points based on gender
                style='smoker', # Differentiates points by marker style based on smoker status
                size='size',    # Varies marker size based on dining party size
                sizes=(20, 400), # Set range of marker sizes
                col='time'      # Create separate columns for 'time'
               )
    plt.suptitle('Relational Plot (Total Bill vs Tip)', y=1.05)
    plt.show()
    ```

### 5.4.2 Distribution Plots (`sns.displot()`)

* **Purpose:** `displot` is a figure-level function for visualizing the distribution of a single variable or the joint distribution of two variables. It can draw histograms, KDEs, and ECDF plots.
* **Parameters for exploring distributions:**
    * `col` / `row`: Creates separate plots arranged in columns or rows based on a categorical variable. This is useful for direct comparison of distributions across different categories.
        * `sns.displot(penguins, x='flipper_length_mm', col='sex')` creates separate plots arranged in columns, each column representing a different 'sex' category.
    * `hue`: Overlays distributions for different categories within a single plot, using different colors to distinguish them.
        * `sns.displot(penguins, x='flipper_length_mm', hue='species')` overlays the distributions for different 'species' within one plot.
    * `kind`: Specifies the type of plot (e.g., `'hist'`, `'kde'`, `'ecdf'`).
    * `fill`: When `True`, fills the area under the KDE curve.
    * `element`: Controls how the distribution is drawn for histograms (e.g., `'bars'`, `'step'`, `'poly'`).

    ```python
    # Load example dataset
    penguins = sns.load_dataset('penguins')

    # Distribution by column
    sns.displot(penguins, x='flipper_length_mm', col='sex', kind='hist', bins=20)
    plt.suptitle('Flipper Length Distribution by Sex (Separate Plots)', y=1.05)
    plt.show()

    # Distribution by hue
    sns.displot(penguins, x='flipper_length_mm', hue='species', kind='kde', fill=True)
    plt.suptitle('Flipper Length Distribution by Species (Overlaid KDE)', y=1.05)
    plt.show()

    # Histogram with step element
    sns.displot(penguins, x='flipper_length_mm', hue='species', element='step', bins=20)
    plt.suptitle('Flipper Length Histogram (Step Element)', y=1.05)
    plt.show()
    ```

### 5.4.3 Categorical Plots (`sns.catplot()`)

* **General Purpose:** `catplot` is a figure-level function for visualizing relationships where one or more variables are categorical. It can draw various types of categorical plots (e.g., `'box'`, `'violin'`, `'strip'`, `'swarm'`, `'bar'`, `'count'`, `'point'`).
* **Displaying relationships with box plots:** `kind='box'` is used to display the distribution of a quantitative variable across different categories using box plots.
* **Differentiating categories with `hue`:** The `hue` parameter differentiates subcategories within the plot by assigning different colors.

    ```python
    sns.catplot(data=tips, x='day', y='total_bill', kind='box', hue='sex')
    plt.suptitle('Total Bill Distribution by Day and Sex', y=1.05)
    plt.show()
    ```
    This plot reveals the median `total_bill`, spread (IQR), and outliers for each day, segmented by sex, allowing for comparison of spending habits.

## 5.5 Data Preprocessing for Visualization

Before creating complex visualizations, understanding the structure and completeness of a dataset is crucial.

### 5.5.1 Dataset Loading in Seaborn

* **`sns.load_dataset()`**: This function is used to load example datasets provided with the Seaborn library (e.g., `'tips'`, `'penguins'`). It retrieves the dataset and loads it directly into a Pandas DataFrame.
    ```python
    tips = sns.load_dataset('tips')
    penguins = sns.load_dataset('penguins')
    print("Tips dataset loaded. First 5 rows:\n", tips.head())
    print("\nPenguins dataset loaded. First 5 rows:\n", penguins.head())
    ```

### 5.5.2 Initial Data Inspection

* **`DataFrame.info()`:** Provides a concise summary of the DataFrame, including the number of entries, column names, non-null counts, data types (`dtype`), and memory usage. This is essential for understanding data completeness (presence of missing values) and column types.
    ```python
    tips.info()
    # Output (example, details vary):
    # <class 'pandas.core.frame.DataFrame'>
    # RangeIndex: 244 entries, 0 to 243
    # Data columns (total 7 columns):
    #  #   Column      Non-Null Count  Dtype
    # ---  ------      --------------  -----
    #  0   total_bill  244 non-null    float64
    #  1   tip         244 non-null    float64
    #  2   sex         244 non-null    category
    #  3   smoker      244 non-null    category
    #  4   day         244 non-null    category
    #  5   time        244 non-null    category
    #  6   size        244 non-null    int64
    # dtypes: category(4), float64(2), int64(1)
    # memory usage: 7.9 KB
    ```

* **`DataFrame.head()`:** Returns the first `n` rows (default 5) of the DataFrame. This allows for a quick visual inspection of the data's structure and actual values, helping to confirm that the data loaded correctly and appears as expected.
    ```python
    print(tips.head())
    # Output (example, details vary):
    #    total_bill   tip     sex smoker  day    time  size
    # 0       16.99  1.01  Female     No  Sun  Dinner     2
    # 1       10.34  1.66    Male     No  Sun  Dinner     3
    # 2       21.01  3.50    Male     No  Sun  Dinner     3
    # 3       23.68  3.31    Male     No  Sun  Dinner     2
    # 4       24.59  3.61  Female     No  Sun  Dinner     4
    ```
    This initial understanding of data types and null counts is crucial before attempting complex visualizations because:
    * Incorrect data types can lead to errors or misleading plots (e.g., plotting categorical data as numerical).
    * Missing values (NaNs) need to be handled (filled or dropped) as many plotting functions cannot directly process them or will produce incorrect results.
    * Understanding the range and nature of data helps in choosing appropriate plot types and aesthetic mappings.

---

## Glossary of Key Terms (Consolidated)

* **Matplotlib:** A comprehensive library for creating static, animated, and interactive visualizations in Python. Often imported as `plt`.
* **Seaborn:** A Python data visualization library based on Matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics. Often imported as `sns`.
* **NumPy (`np`):** A fundamental package for scientific computing with Python, providing support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.
* **Pandas (`pd`):** A software library written for the Python programming language for data manipulation and analysis. It offers data structures and operations for manipulating numerical tables and time series.
* **DataFrame:** A two-dimensional, size-mutable, and potentially heterogeneous tabular data structure with labeled axes (rows and columns), as used in Pandas.
* **`np.random.randn()`:** A NumPy function that returns samples from the "standard normal" distribution (mean 0, variance 1). Used to generate random data for plotting examples.
* **`plt.hist()`:** A Matplotlib function used to create a histogram, a graphical representation of the distribution of numerical data.
* **`bins` (histogram parameter):** Defines the number of intervals (bins) into which the range of data is divided, influencing the granularity of a histogram.
* **`alpha` (plot parameter):** Controls the transparency of plot elements, with values ranging from 0 (fully transparent) to 1 (fully opaque). Useful for overlapping plots.
* **`sns.jointplot()`:** A Seaborn function that plots bivariate (two-variable) distributions with marginal distributions for each variable along the axes. Default `kind` is `scatter`.
* **`kind` (plot parameter):** Specifies the type of plot to draw within a Seaborn function, e.g., `'scatter'`, `'hex'`, `'kde'`, `'reg'`.
* **`sns.rugplot()`:** A Seaborn function that draws a rug plot, marking the location of individual observations along an axis with small vertical ticks.
* **`sns.kdeplot()`:** A Seaborn function that generates a Kernel Density Estimate plot, a non-parametric way to estimate the probability density function of a random variable.
* **`cumulative` (kdeplot parameter):** When set to `True`, displays the cumulative distribution function (CDF) instead of the probability density function.
* **`sns.boxplot()`:** A Seaborn function that draws a box plot, summarizing the distribution of a quantitative variable by displaying its median, quartiles, and potential outliers.
* **`whis` (boxplot parameter):** Controls the extent of the whiskers in a box plot. `np.inf` extends whiskers to the min/max data points.
* **`sns.violinplot()`:** A Seaborn function that combines aspects of a box plot and a kernel density estimate. It shows the distribution of quantitative data across several categories.
* **`bw_adjust` (violinplot parameter):** Adjusts the bandwidth of the kernel density estimate in a violin plot, affecting the smoothness of the density curve.
* **`inner` (violinplot parameter):** Specifies what to draw inside the violins (e.g., `'box'`, `'quartile'`, `'stick'`, `None`).
* **`sns.load_dataset()`:** A Seaborn function used to load example datasets provided with the Seaborn library (e.g., `'tips'`, `'penguins'`).
* **`tips dataset`:** An example dataset commonly used in Seaborn, containing information about restaurant tips.
* **`penguins dataset`:** An example dataset commonly used in Seaborn, containing measurements and species information for penguins.
* **`tips.info()`:** A Pandas DataFrame method that prints a concise summary of a DataFrame, including data types and non-null values.
* **`tips.head()`:** A Pandas DataFrame method that returns the first `n` rows of the DataFrame, useful for a quick preview of the data.
* **`sns.relplot()`:** A Seaborn function for visualizing statistical relationships between variables. It creates relational plots with flexibility in showing different semantic mappings.
* **`hue` (plot parameter):** Maps a variable to the color of plot elements, differentiating categories or values.
* **`style` (relplot parameter):** Maps a variable to the marker style (e.g., shape) of plot elements.
* **`size` (relplot parameter):** Maps a variable to the size of plot elements.
* **`sizes` (relplot parameter):** Specifies the range of sizes to use when `size` is mapped to a quantitative variable.
* **`sns.displot()`:** A Seaborn function for visualizing the distribution of a single variable. It can draw histograms, KDEs, and ECDF plots.
* **`element` (displot parameter):** Controls how the distribution is drawn (e.g., `'bars'`, `'step'`, `'poly'`).
* **`col` (displot/catplot parameter):** Creates separate subplots arranged in columns based on a categorical variable.
* **`fill` (kdeplot/displot parameter):** When `True`, fills the area under the KDE curve.
* **`sns.catplot()`:** A Seaborn function for visualizing relationships between categorical and quantitative variables. It can draw various types of categorical plots (e.g., box, violin, strip, swarm).

---