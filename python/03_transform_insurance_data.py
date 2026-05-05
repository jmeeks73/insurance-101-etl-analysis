# Transformation of Data Scripts
#3. Transform the data
df_clean = df.drop_duplicates().copy()

for col in ["sex", "smoker", "region"]:
    df_clean[col] = df_clean[col].astype(str).str.strip().str.lower()

print(df_clean.shape)
print(df_clean.isnull().sum())
print(df_clean.duplicated().sum())
df_clean.head(10)
