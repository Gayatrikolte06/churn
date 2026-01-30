import pandas as pd

df = pd.read_csv("D:/churn prediction/data/Teleco-Customer-churn.csv")

print(df.head())

print("dataset info")
print(df.info(),"\n")

#check for missing values
print("missing values in each column")
print(df.isnull().sum(),"\n")

print("descriptive statistics")
print(df.describe())

#target variable distribution
#Check target variable distribution
if 'Churn' in df.columns:
    print("\n===== Target Variable Distribution (Churn) =====")
    print(df['Churn'].value_counts())
else:
    print("\nChurn column not found!")

categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
print("\n Unique values in categorical column")
for col in categorical_cols:
    print(f"{col}:{df[col].unique()}")

numeric_cols=df.select_dtypes(include=['int64','float64']).columns
print("\n===== Skewnessof numeric fetaures =====")
print(df[numeric_cols].skew())