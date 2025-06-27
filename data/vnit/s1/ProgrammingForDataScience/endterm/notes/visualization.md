# Common Visualizations with Matplotlib and Pandas

### 1\. Line Plot

  * **Description:** Displays data points connected by straight line segments. Ideal for showing trends over time or ordered categories.
  * **When to Use:**
      * **Time Series Data:** To show how a variable changes over a continuous period (e.g., stock prices, temperature over days).
      * **Trends:** To visualize the progression or trend of a continuous variable.
      * **Comparison:** To compare trends of multiple variables on the same plot.
  * **Pandas Method:** `.plot.line()` or `df.plot()` (default for time series or single Series).

<!-- end list -->

```python
# Sample Data: Time series of stock prices
dates = pd.date_range('2024-01-01', periods=100, freq='D')
np.random.seed(42)
stock_prices = pd.Series(np.random.randn(100).cumsum() + 100, index=dates)

plt.figure(figsize=(10, 6))
stock_prices.plot(title='Daily Stock Price Trend', xlabel='Date', ylabel='Price')
plt.grid(True)
plt.show()

# Multiple lines
df_trends = pd.DataFrame({
    'Product A': np.random.randn(100).cumsum() + 50,
    'Product B': np.random.randn(100).cumsum() + 60
}, index=dates)

plt.figure(figsize=(10, 6))
df_trends.plot(title='Product Sales Trends', xlabel='Date', ylabel='Sales Units')
plt.grid(True)
plt.legend(title='Product')
plt.show()
```

### 2\. Bar Plot (Bar Chart)

  * **Description:** Uses rectangular bars to represent the magnitude of different categories. The length of each bar is proportional to the value it represents.
  * **When to Use:**
      * **Categorical Data Comparison:** To compare quantities of different discrete categories (e.g., sales by region, votes per candidate).
      * **Frequency Distribution:** To show the frequency of items in different categories.
      * **Ranking:** To quickly see which categories are highest or lowest.
  * **Pandas Method:** `.plot.bar()` (vertical bars) or `.plot.barh()` (horizontal bars).

<!-- end list -->

```python
# Sample Data: Sales by Region
sales_data = pd.DataFrame({
    'Region': ['North', 'South', 'East', 'West'],
    'Sales': [15000, 22000, 18000, 12000]
})

plt.figure(figsize=(8, 5))
sales_data.plot.bar(x='Region', y='Sales', title='Total Sales by Region', legend=False)
plt.ylabel('Sales ($)')
plt.xlabel('Region')
plt.xticks(rotation=0) # Keep labels horizontal
plt.tight_layout()
plt.show()

# Horizontal Bar Plot
plt.figure(figsize=(8, 5))
sales_data.plot.barh(x='Region', y='Sales', title='Total Sales by Region (Horizontal)', legend=False)
plt.xlabel('Sales ($)')
plt.ylabel('Region')
plt.tight_layout()
plt.show()

# Using value_counts() for frequency distribution
gender_data = pd.Series(['Male', 'Female', 'Male', 'Female', 'Male', 'Other', 'Female'])
gender_counts = gender_data.value_counts()

plt.figure(figsize=(7, 4))
gender_counts.plot.bar(title='Gender Distribution', rot=0) # rot=0 keeps x-labels horizontal
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()
```

### 3\. Histogram

  * **Description:** Displays the distribution of a numerical dataset. It groups numbers into "bins" and counts how many observations fall into each bin.
  * **When to Use:**
      * **Distribution of a Single Numerical Variable:** To understand the shape, spread, and central tendency of continuous data (e.g., distribution of ages, heights, test scores).
      * **Detecting Outliers:** Can help identify unusual data points far from the main distribution.
      * **Assessing Normality:** To see if data approximates a normal distribution.
  * **Pandas Method:** `.plot.hist()`

<!-- end list -->

```python
# Sample Data: Random data for distribution
np.random.seed(42)
data_for_hist = np.random.normal(loc=70, scale=10, size=1000) # Mean 70, Std Dev 10

plt.figure(figsize=(9, 6))
pd.Series(data_for_hist).plot.hist(bins=30, edgecolor='black', alpha=0.7,
                                   title='Distribution of Student Scores', xlabel='Score', ylabel='Frequency')
plt.show()

# Histogram with multiple columns
df_grades = pd.DataFrame({
    'Math': np.random.normal(loc=75, scale=8, size=200),
    'Science': np.random.normal(loc=70, scale=12, size=200)
})

plt.figure(figsize=(10, 6))
df_grades.plot.hist(bins=20, alpha=0.6, title='Distribution of Math and Science Grades')
plt.xlabel('Grade')
plt.ylabel('Frequency')
plt.legend()
plt.show()
```

### 4\. Scatter Plot

  * **Description:** Displays individual data points on a two-dimensional graph. Each point represents the values of two variables for a single observation.
  * **When to Use:**
      * **Relationship Between Two Numerical Variables:** To explore the correlation or relationship between two continuous variables (e.g., height vs. weight, advertising spend vs. sales).
      * **Identifying Clusters or Outliers:** Can reveal groups of data points or unusual observations.
  * **Pandas Method:** `.plot.scatter(x, y)`

<!-- end list -->

```python
# Sample Data: Relationship between advertising spend and sales
advertising_data = pd.DataFrame({
    'Ad_Spend': np.random.uniform(500, 5000, 50),
    'Sales': np.random.uniform(50, 500, 50) + np.linspace(0, 100, 50) # Adding a slight positive trend
})

plt.figure(figsize=(9, 6))
advertising_data.plot.scatter(x='Ad_Spend', y='Sales', title='Ad Spend vs. Sales', alpha=0.7, s=50) # s is marker size
plt.xlabel('Advertising Spend ($)')
plt.ylabel('Sales ($)')
plt.grid(True)
plt.show()

# Scatter plot with a third variable represented by color (using Matplotlib directly)
df_people = pd.DataFrame({
    'Height': np.random.normal(170, 10, 100),
    'Weight': np.random.normal(70, 15, 100),
    'Gender': np.random.choice(['Male', 'Female'], 100)
})

# Map gender to colors
colors = df_people['Gender'].map({'Male': 'blue', 'Female': 'red'})

plt.figure(figsize=(9, 6))
plt.scatter(df_people['Height'], df_people['Weight'], c=colors, alpha=0.7, s=50)
plt.title('Height vs. Weight by Gender')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.grid(True)
# Create a custom legend
from matplotlib.lines import Line2D
legend_elements = [Line2D([0], [0], marker='o', color='w', label='Male', markerfacecolor='blue', markersize=10),
                   Line2D([0], [0], marker='o', color='w', label='Female', markerfacecolor='red', markersize=10)]
plt.legend(handles=legend_elements, title='Gender')
plt.show()
```

### 5\. Box Plot (Box-and-Whisker Plot)

  * **Description:** Displays the distribution of numerical data and skewness through quartiles (25th, 50th/median, 75th percentiles) and outliers.
      * The box represents the interquartile range (IQR), from Q1 to Q3.
      * A line inside the box marks the median (Q2).
      * "Whiskers" extend from the box to show the range of the data, usually up to 1.5 times the IQR from the quartiles.
      * Points outside the whiskers are considered outliers.
  * **When to Use:**
      * **Distribution Summary:** To quickly visualize the central tendency, spread, and skewness of a numerical variable.
      * **Comparing Distributions Across Categories:** To compare the distribution of a numerical variable across different categories.
      * **Outlier Detection:** Excellent for identifying potential outliers.
  * **Pandas Method:** `.plot.box()`

<!-- end list -->

```python
# Sample Data: Test scores for different subjects
df_scores = pd.DataFrame({
    'Math': np.random.normal(70, 10, 100),
    'English': np.random.normal(75, 8, 100),
    'History': np.random.normal(65, 12, 100)
})

plt.figure(figsize=(10, 6))
df_scores.plot.box(title='Distribution of Scores by Subject', patch_artist=True) # patch_artist fills boxes
plt.ylabel('Score')
plt.xlabel('Subject')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Box plot for a single series
data_for_box = np.random.normal(loc=100, scale=15, size=200)
data_for_box[50] = 160 # introduce an outlier
data_for_box[100] = 30 # introduce another outlier

plt.figure(figsize=(6, 8))
pd.Series(data_for_box).plot.box(title='Distribution with Outliers', sym='r+') # sym='r+' to show outliers as red plus signs
plt.ylabel('Value')
plt.show()
```

### 6\. Pie Chart

  * **Description:** A circular statistical graphic divided into slices to illustrate numerical proportion. The arc length of each slice is proportional to the quantity it represents.
  * **When to Use:**
      * **Proportions of a Whole (Few Categories):** To show the relative contribution of each category to a total, especially when there are only a few categories (ideally 2-5).
      * **Composition:** To display the composition of something (e.g., market share, budget allocation).
  * **When NOT to Use:**
      * Many categories (becomes cluttered and hard to read).
      * Comparing exact values between categories (bar charts are better for this).
  * **Pandas Method:** `.plot.pie()`

<!-- end list -->

```python
# Sample Data: Market Share
market_share = pd.Series({'Apple': 45, 'Samsung': 30, 'Xiaomi': 15, 'Others': 10})

plt.figure(figsize=(8, 8))
market_share.plot.pie(autopct='%1.1f%%', startangle=90, explode=(0.05, 0, 0, 0),
                      title='Smartphone Market Share', ylabel='') # ylabel='' removes y-axis label
plt.show()
```

### 7\. Area Plot

  * **Description:** A line chart with the area between the line and the axis filled with color. Useful for showing the magnitude of change over time and for highlighting trends and contributions of different categories to a whole.
  * **When to Use:**
      * **Cumulative or Stacked Trends:** To show how proportions or quantities change over time for several categories, where the areas stack up to represent a total.
      * **Magnitude of Change:** When the magnitude of values is important in addition to trends.
  * **Pandas Method:** `.plot.area()`

<!-- end list -->

```python
# Sample Data: Quarterly sales breakdown by product
data = {
    'Q1': [100, 120, 80],
    'Q2': [110, 130, 90],
    'Q3': [105, 125, 85],
    'Q4': [120, 140, 95]
}
df_quarterly_sales = pd.DataFrame(data, index=['Product A', 'Product B', 'Product C']).T # Transpose to have quarters as index

plt.figure(figsize=(10, 6))
df_quarterly_sales.plot.area(title='Quarterly Sales by Product', alpha=0.7)
plt.xlabel('Quarter')
plt.ylabel('Sales Units')
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.show()
```

-----

### Tips for Effective Visualization

  * **Choose the Right Plot Type:** Select a visualization that best represents your data and the message you want to convey.
  * **Labels and Titles:** Always include clear titles, x-axis labels, and y-axis labels.
  * **Legends:** Use legends when plotting multiple series to differentiate them.
  * **Clarity and Simplicity:** Avoid clutter. Remove unnecessary elements.
  * **Color Choice:** Use colors effectively to differentiate categories or highlight important data points. Be mindful of colorblindness.
  * **Figure Size:** Adjust `figsize` (`plt.figure(figsize=(width, height))`) for better readability, especially for presentations.
  * **`plt.tight_layout()`:** Often helps automatically adjust plot parameters for a tight layout.
  * **`plt.show()`:** Essential to display the plot.
