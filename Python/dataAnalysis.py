import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Task 1: Load and Explore the Dataset
try:
    # Load the sales dataset from CSV file
    df = pd.read_csv('sales_data.csv')
    print(" Dataset loaded successfully.")
except FileNotFoundError:
    print(" Error: The file 'sales_data.csv' was not found.")
    exit()

# Display the first few rows to inspect the data
print("\n First 5 rows of the dataset:")
print(df.head())

# Explore the structure of the dataset
print("\n Dataset info (Data types and missing values):")
print(df.info())

# Check for missing values
print("\n Checking for missing values:")
print(df.isnull().sum())

# Clean the dataset (If any missing values exist, drop them)
df.dropna(inplace=True)  # Drop rows with missing values (if any)

# Task 2: Basic Data Analysis

# Compute basic statistics for numerical columns (Quantity Sold, Revenue)
print("\n Descriptive statistics:")
print(df.describe())

# Group by Product and calculate the total quantity sold and total revenue
product_group = df.groupby('Product').agg({'Quantity Sold': 'sum', 'Revenue ($)': 'sum'}).reset_index()

# Display grouped data
print("\n Grouped data by Product (Total Quantity Sold and Revenue):")
print(product_group)


# Set plot style
sns.set(style="whitegrid")

# 1. Line Chart: Trends in Revenue over time (Date)
plt.figure(figsize=(10, 6))
df['Date'] = pd.to_datetime(df['Date'])  # Convert Date to datetime format
daily_revenue = df.groupby('Date')['Revenue ($)'].sum().reset_index()

plt.plot(daily_revenue['Date'], daily_revenue['Revenue ($)'], marker="o", color="blue", label="Revenue")
plt.title("Line Chart: Revenue Trends Over Time")
plt.xlabel("Date")
plt.ylabel("Revenue ($)")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig("line_chart.png")
plt.show()

# 2. Bar Chart: Total Revenue per Product
plt.figure(figsize=(8, 5))
sns.barplot(x='Product', y='Revenue ($)', data=product_group, palette="viridis")
plt.title("Bar Chart: Total Revenue per Product")
plt.xlabel("Product")
plt.ylabel("Total Revenue ($)")
plt.tight_layout()
plt.savefig("bar_chart.png")
plt.show()

# 3. Histogram: Distribution of Quantity Sold
plt.figure(figsize=(8, 5))
plt.hist(df['Quantity Sold'], bins=10, color="skyblue", edgecolor="black")
plt.title("Histogram: Distribution of Quantity Sold")
plt.xlabel("Quantity Sold")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("histogram.png")
plt.show()

# 4. Scatter Plot: Quantity Sold vs Revenue ($)
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="Quantity Sold", y="Revenue ($)", hue="Product", palette="deep")
plt.title("Scatter Plot: Quantity Sold vs Revenue ($)")
plt.xlabel("Quantity Sold")
plt.ylabel("Revenue ($)")
plt.legend(title="Product")
plt.tight_layout()
plt.savefig("scatter_plot.png")
plt.show()
