# 6. Analyze the average charges by smoker and non-smoker

avg_charges_smoker = df.groupby('smoker')['charges'].mean().round(2)

print(avg_charges_smoker)

#7. Analyze the Average charges by gender

avg_charges_gender = (
    df.groupby('sex')['charges']
      .mean()
      .round(2)
      .reset_index()
)

avg_charges_gender.columns = ['Gender', 'Average Charges']

print(avg_charges_gender)

#8. Analyze the average charges by region

df_clean = df.copy()
print(
    df_clean.groupby("region")["charges"]
      .agg(["count", "mean"])
      .round(2)
      .to_string()
)

#9. Analyze the average charges by the number of children

avg_charges_children = (
    df.groupby('children')['charges']
      .agg(['count', 'mean'])
      .round(2)
      .reset_index()
)

avg_charges_children.columns = ['Children', 'Total People', 'Average Charges']

print(avg_charges_children)

#10. Correlation Analysis
print(df_clean[["age", "bmi", "children", "charges"]].corr().round(3).to_string())

#11. Running tests for the true file path to analyze charges based on Body Mass Index or BMI
import os
import pandas as pd

home = os.path.expanduser("~")

possible_paths = [
    os.path.join(home, "Desktop", "insurance101.csv"),
    os.path.join(home, "OneDrive", "Desktop", "insurance101.csv"),
    os.path.join(home, "Downloads", "insurance101.csv"),
    os.path.join(home, "OneDrive", "Downloads", "insurance101.csv"),
]

for path in possible_paths:
    print(path, "->", os.path.exists(path))

#12. Analyze average BMI
import pandas as pd

file_path = r"C:\Users\jpmee\OneDrive\Desktop\insurance101.csv"   # replace with your true path

df = pd.read_csv(file_path)
df_clean = df.drop_duplicates().copy()

for col in ["sex", "smoker", "region"]:
    df_clean[col] = df_clean[col].str.strip().str.lower()

print("Clean shape:", df_clean.shape)
print(df_clean["bmi"].describe().round(2))

#13. Analyze charges based on BMI
import os
import pandas as pd

home = os.path.expanduser("~")

possible_paths = [
    os.path.join(home, "Desktop", "insurance101.csv"),
    os.path.join(home, "OneDrive", "Desktop", "insurance101.csv"),
    os.path.join(home, "Downloads", "insurance101.csv"),
    os.path.join(home, "OneDrive", "Downloads", "insurance101.csv"),
]

file_path = next((p for p in possible_paths if os.path.exists(p)), None)

if not file_path:
    raise FileNotFoundError("insurance101.csv not found")

df = pd.read_csv(file_path)
df_clean = df.drop_duplicates().copy()

for col in ["sex", "smoker", "region"]:
    df_clean[col] = df_clean[col].str.strip().str.lower()

# BMI groups
df_clean["bmi_category"] = pd.cut(
    df_clean["bmi"],
    bins=[0, 18.5, 25, 30, 100],
    labels=["Underweight", "Normal", "Overweight", "Obese"]
)

# Average charges by BMI category
bmi_analysis = (
    df_clean.groupby("bmi_category", observed=False)["charges"]
    .agg(["count", "mean", "min", "max"])
    .round(2)
)

print("\nAverage Charges Based on BMI")
print(bmi_analysis.to_string())

print("\nBMI and Charges Correlation:")
print(round(df_clean["bmi"].corr(df_clean["charges"]), 3))
