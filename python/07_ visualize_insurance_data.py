#14. Add bar chart to base average charges based on BMI on weight categories
import matplotlib.pyplot as plt

bmi_analysis["mean"].plot(kind="bar")
plt.title("Average Charges by BMI Category")
plt.xlabel("BMI Category")
plt.ylabel("Average Charges")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

#15. Bar chart based on average charges based on smoking status
import os
import pandas as pd
import matplotlib.pyplot as plt

# Find the file
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

# Load and clean
df = pd.read_csv(file_path)
df_clean = df.drop_duplicates().copy()

for col in ["sex", "smoker", "region"]:
    df_clean[col] = df_clean[col].str.strip().str.lower()

# Average charges by smoker
smoker_avg = (
    df_clean.groupby("smoker")["charges"]
    .mean()
    .round(2)
)

print(smoker_avg)

# Create chart
smoker_avg.plot(kind="bar")
plt.title("Average Charges by Smoking Status")
plt.xlabel("Smoking Status")
plt.ylabel("Average Charges")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

#16. Pie chart on average charges based on gender
import os
import pandas as pd
import matplotlib.pyplot as plt

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

gender_avg = df_clean.groupby("sex")["charges"].mean().round(2)
gender_avg.index = gender_avg.index.str.title()

labels = [f"{gender}: ${value:,.2f}" for gender, value in gender_avg.items()]

plt.figure(figsize=(6, 6))
plt.pie(
    gender_avg,
    labels=labels,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Average Charges by Gender")
plt.tight_layout()
plt.show()

#17. Scatter chart on average charges based on ages
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Find the file
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

x = df_clean["age"]
y = df_clean["charges"]

plt.figure(figsize=(8, 6))
plt.scatter(x, y)

# trend line
m, b = np.polyfit(x, y, 1)
plt.plot(x, m * x + b)

plt.title("Scatter Plot of Age vs Charges")
plt.xlabel("Age")
plt.ylabel("Charges")
plt.tight_layout()
plt.show()


