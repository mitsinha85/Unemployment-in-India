import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sahi file paths
file1_path = r"D:\Unemployment in India\Unemployment in India.csv"
file2_path = r"D:\Unemployment in India\Unemployment_Rate_upto_11_2020.csv"

# Load datasets
df1 = pd.read_csv(file1_path)
df2 = pd.read_csv(file2_path)

# Clean column names
df1.columns = df1.columns.str.strip()
df2.columns = df2.columns.str.strip()

# Convert 'Date' to datetime format
df1['Date'] = pd.to_datetime(df1['Date'], dayfirst=True, errors='coerce')
df2['Date'] = pd.to_datetime(df2['Date'], dayfirst=True, errors='coerce')

# Drop unnecessary columns
df2.drop(columns=['Region.1'], inplace=True, errors='ignore')

# Merge datasets
df = pd.concat([df1, df2], ignore_index=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Check missing values
print("Missing Values:\n", df.isnull().sum())

# Fill missing values using forward fill
df.ffill(inplace=True)

# Unemployment Rate Over Time
plt.figure(figsize=(12,6))
sns.lineplot(data=df, x="Date", y="Estimated Unemployment Rate (%)", marker="o", color="b")
plt.title("Unemployment Rate Over Time", fontsize=14)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Unemployment Rate (%)", fontsize=12)
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# State-wise Unemployment Rate
plt.figure(figsize=(14,6))
sns.barplot(data=df, x="Region", y="Estimated Unemployment Rate (%)", hue="Region", dodge=False, legend=False, palette="viridis")
plt.title("Unemployment Rate by Region", fontsize=14)
plt.xlabel("Region", fontsize=12)
plt.ylabel("Unemployment Rate (%)", fontsize=12)
plt.xticks(rotation=90)
plt.show()

# COVID-19 Impact Analysis
pre_covid = df[df['Date'] < "2020-03-01"]
post_covid = df[df['Date'] >= "2020-03-01"]

print("Pre-COVID Unemployment Rate:", pre_covid["Estimated Unemployment Rate (%)"].mean())
print("Post-COVID Unemployment Rate:", post_covid["Estimated Unemployment Rate (%)"].mean())

# Visualization of COVID-19 Impact
plt.figure(figsize=(8,5))
sns.boxplot(data=[pre_covid["Estimated Unemployment Rate (%)"], post_covid["Estimated Unemployment Rate (%)"]], palette=["blue"])
plt.xticks([0, 1], ["Pre-COVID", "Post-COVID"])
plt.title("Unemployment Rate Before and After COVID-19")
plt.ylabel("Unemployment Rate (%)")
plt.show()

# ----------------------------
# Author: [AMIT KUMAR SINHA]
# Date: [06-03-2025]
# Project: Unemployment Analysis
# ----------------------------
