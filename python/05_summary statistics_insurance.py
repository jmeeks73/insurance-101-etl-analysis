#5. Summary Statistics
summary = df_clean.describe(include="all").transpose().round(2)
print(summary.to_string())
