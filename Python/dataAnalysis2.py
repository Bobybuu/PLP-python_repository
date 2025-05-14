import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "sales_data.csv"
df = pd.read_csv(file_path)


total_revenue = df["Revenue ($)"].sum()

best_selling_product = df.groupby("Product")["Quantity Sold"].sum().idxmax()

top_sales_day = df.groupby("Date")["Revenue ($)"].sum().idxmax()

summary = f"""
Sales Summary:
--------------
Total Revenue: ${total_revenue:,.2f}
Best-Selling Product: {best_selling_product}
Day with Highest Sales: {top_sales_day}
"""
with open("sales_summary.txt", "w") as f:
    f.write(summary)

print(summary)

daily_revenue = df.groupby("Date")["Revenue ($)"].sum().reset_index()

# Plotting
plt.figure(figsize=(10, 6))
sns.lineplot(data=daily_revenue, x="Date", y="Revenue ($)", marker="o", color="blue")
plt.title("Daily Revenue Trends")
plt.xlabel("Date")
plt.ylabel("Revenue ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("daily_revenue_trend.png")
plt.show()
