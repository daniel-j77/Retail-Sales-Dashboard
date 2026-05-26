import pandas as pd

df=pd.read_csv("sales_raw.csv")

print("Before Cleaning")
print(df)

# Remove spaces
df["City"]=df["City"].str.strip()

# Standardize names
df["City"]=df["City"].str.title()

# Fill missing sales
df["Sales"]=df["Sales"].fillna(
df["Sales"].median()
)

# Fill missing profit
df["Profit"]=df["Profit"].fillna(
df["Profit"].median()
)

# Remove duplicates
df=df.drop_duplicates()

# Convert types
df["Sales"]=df["Sales"].astype(int)
df["Profit"]=df["Profit"].astype(int)

df.to_csv(
"sales_clean.csv",
index=False
)

print("\nCleaning Completed")