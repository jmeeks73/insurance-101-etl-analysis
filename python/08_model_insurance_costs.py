#18. Prediction model performance based on top coeffiecents. 
import os
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# 1. Find and load file
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

# 2. Clean data
df = df.drop_duplicates().copy()

for col in ["sex", "smoker", "region"]:
    df[col] = df[col].str.strip().str.lower()

# 3. Convert text columns to numbers
df_model = pd.get_dummies(df, columns=["sex", "smoker", "region"], drop_first=True)

# 4. Define X and y
X = df_model.drop("charges", axis=1)
y = df_model["charges"]

# 5. Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 6. Train model
model = LinearRegression()
model.fit(X_train, y_train)

# 7. Predict
y_pred = model.predict(X_test)

# 8. Evaluate
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Model Performance")
print(f"MAE: {mae:,.2f}")
print(f"MSE: {mse:,.2f}")
print(f"R²: {r2:.3f}")
coefficients = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_
}).sort_values("Coefficient", ascending=False)

print("\nTop coefficients:")
print(coefficients.head(10).to_string(index=False))
