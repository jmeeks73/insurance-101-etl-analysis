# Insurance 101 ETL Data Analysis Project

## Project Overview

This project is a complete end-to-end ETL (Extract, Transform, Load) data analysis pipeline built using an insurance dataset. The project demonstrates how raw healthcare insurance data can be extracted, cleaned, transformed, analyzed, and visualized using Python, SQL Server, and Power BI.

The purpose of this project is to create a professional data analytics portfolio project that showcases:

- Data Extraction
- Data Cleaning
- Data Transformation
- SQL Analysis
- Data Visualization
- Predictive Modeling
- Business Insights

The final solution provides meaningful insights into factors affecting insurance charges such as:

- Smoking status
- Age
- BMI
- Number of children
- Gender
- Region

---

# Tools & Technologies

| Tool | Purpose |
|------|----------|
| Python | Data extraction and cleaning |
| Pandas | Data transformation |
| SQL Server | Data storage and SQL analysis |
| SQLAlchemy | ETL pipeline connection |
| Power BI | Dashboard visualizations |
| Scikit-Learn | Predictive modeling |
| Jupyter Notebook | Development environment |
| GitHub | Portfolio hosting |

---

# Project Architecture

```text
Raw CSV File
      ↓
Python Extraction
      ↓
Data Cleaning & Transformation
      ↓
SQL Server Database
      ↓
SQL Analysis Queries
      ↓
Power BI Dashboard
      ↓
Business Insights

insurance-101-etl-analysis/
│
├── data/
│   ├── raw/
│   │   └── insurance101.csv
│   │
│   └── cleaned/
│       └── insurance101_clean.csv
│
├── notebooks/
│   └── insurance_etl_analysis.ipynb
│
├── sql/
│   ├── create_database.sql
│   ├── create_tables.sql
│   ├── load_raw_data.sql
│   ├── clean_transform.sql
│   └── analysis_queries.sql
│
├── powerbi/
│   └── insurance_dashboard.pbix
│
├── images/
│   ├── dashboard_overview.png
│   ├── kpi_cards.png
│   └── charts.png
│
├── docs/
│   ├── etl_architecture.md
│   ├── data_dictionary.md
│   └── project_summary.md
│
├── requirements.txt
├── README.md
└── LICENSE

ETL Process
1. Extract
import pandas as pd

df = pd.read_csv("insurance101.csv")
print(df.head())

2. Transform

The dataset is cleaned by:

Removing duplicates
Standardizing text fields
Handling null values
Formatting numeric columns
Cleaning spaces and capitalization
df_clean = df.drop_duplicates()

df_clean['sex'] = df_clean['sex'].str.lower().str.strip()
df_clean['smoker'] = df_clean['smoker'].str.lower().str.strip()
df_clean['region'] = df_clean['region'].str.lower().str.strip()

3. Load

The cleaned dataset is loaded into SQL Server.

from sqlalchemy import create_engine

engine = create_engine(
    "mssql+pyodbc://localhost/Insurance101DB?driver=SQL+Server+Trusted+Connection=yes"
)

df_clean.to_sql(
    "insurance101_clean",
    con=engine,
    if_exists="replace",
    index=False
)

SQL Analysis

Example SQL queries used for analysis:

Average Charges by Smoking Status

SELECT
    smoker,
    COUNT(*) AS total_people,
    ROUND(AVG(charges), 2) AS avg_charges
FROM dbo.insurance101_clean
GROUP BY smoker
ORDER BY avg_charges DESC;

Top 10 Highest Insurance Charges

SELECT TOP (10)
    age,
    sex,
    bmi,
    smoker,
    region,
    FORMAT(charges, 'N2') AS charges
FROM dbo.insurance101_clean
ORDER BY charges DESC;

Power BI Dashboard

The Power BI dashboard includes:

KPI Cards
Average Charges Analysis
Charges by Gender
Charges by Region
Smoking Status Analysis
BMI Scatter Plot
Age vs Charges Visualization
Children vs Average Charges

Machine Learning Model

A regression model was created using Scikit-Learn to predict insurance charges.

| Metric   | Value      |
| -------- | ---------- |
| MAE      | 4,177      |
| MSE      | 35,478,020 |
| R² Score | 0.807      |

| Feature    | Impact                  |
| ---------- | ----------------------- |
| smoker_yes | Highest positive impact |
| bmi        | Strong positive impact  |
| age        | Positive impact         |
| children   | Moderate impact         |


Key Business Insights:
Smokers have significantly higher insurance charges.
Higher BMI is associated with increased medical costs.
Older individuals tend to have higher insurance expenses.
Regional differences impact average insurance charges.
Smoking status is the strongest predictor of insurance costs.

Business Solutions:
1. Recommendations For Smokers:
   Increase premium pricing for smokers
   Create smoking cessation wellness programs
   Offer discounts for non-smoking certification
   Develop preventive healthcare initiatives

2. Recommendatiions For Customers with High BMI:
   Introduce wellness and fitness incentives
   Promote nutrition and preventive care programs
   Offer premium reductions for healthy BMI improvement
   Predict high-risk populations earlier using analytics

3. Recommendations to lower healthcare cost for regional areas since the Southeast has the highest medical costs:
   Investigate regional healthcare pricing trends
   Adjust regional premium models
   Increase provider network negotiations
   Expand preventive care in high-cost regions

4. Recommendations for older customers:
   Build age-based risk scoring models
   Develop senior preventive healthcare programs
   Forecast long-term insurance liabilities
   Improve actuarial pricing strategies

Future Improvements:
Deploy ETL pipeline to AWS
Automate SQL loading process
Add real-time dashboards
Build predictive API
Add advanced machine learning models

Future Improvements
Deploy ETL pipeline to AWS
Automate SQL loading process
Add real-time dashboards
Build predictive API
Add advanced machine learning models

Author

John Meeks

GitHub Portfolio Project

License

This project is licensed under the MIT License.


## Suggested GitHub Repository Name

`insurance-101-etl-analysis`

## Suggested Commit Message

```text
Create professional README for Insurance 101 ETL analysis project
