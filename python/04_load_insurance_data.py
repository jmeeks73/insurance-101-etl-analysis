#4. Load the data
# 4. Load / Save Cleaned Data
import os

os.makedirs("data/cleaned", exist_ok=True)

df_clean.to_csv("data/cleaned/insurance101_clean.csv", index=False)

print("Cleaned data loaded/saved successfully ✅")
print("Saved to: data/cleaned/insurance101_clean.csv")
