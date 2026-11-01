import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    r"C:\Users\harzs\Downloads\archive\Sample - Superstore.csv",
    encoding="latin1"
)

df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

print("DATASET LOADED SUCCESSFULLY")
print("Dataset Shape:", df.shape)

print("\nDATA CLEANING")
print("Missing Values:", df.isnull().sum().sum())
print("Duplicate Rows:", df.duplicated().sum())

print("\nBUSINESS SUMMARY")
print("Total Sales:", df['Sales'].sum())
print("Total Profit:", df['Profit'].sum())
print("Total Quantity:", df['Quantity'].sum())
print("Average Discount:", df['Discount'].mean())
print("\nCATEGORY WISE SALES")
print(df.groupby('Category')['Sales'].sum())
print("\nCATEGORY WISE PROFIT")
print(df.groupby('Category')['Profit'].sum())
df.groupby('Region')['Sales'].sum().plot(kind='bar', title='Region Wise Sales')
plt.tight_layout()
plt.savefig('region_sales.png')
plt.show()
