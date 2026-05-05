# Extract Github Python Scripts

#1. Extract the data
import pandas as pd

df = pd.read_csv(r"C:\Users\jpmee\OneDrive\Desktop\insurance101.csv")
print(df.head())
print(df.shape)
print(df.columns)
