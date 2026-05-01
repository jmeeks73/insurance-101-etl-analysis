# Portfolio Summary – Insurance 101 ETL Analysis

## * Project Overview

This project presents a complete end-to-end ETL (Extract, Transform, Load) data pipeline built on an insurance dataset. It focuses on transforming raw data into a clean, structured format and delivering actionable business insights through SQL-based analysis and interactive Power BI visualizations.


---

## * Objective

The primary objective of this project was to:

* Design a clean and reliable dataset from raw insurance data
* Conduct data transformation using Python and SQL Server
* Identify key factors affecting insurance charges
* Provide an interactive Power BI dashboard for insights

---

## * Tools & Technologies

* **Python (Pandas)** – Data extraction and cleaning
* **SQL Server (T-SQL)** – Data transformation and analysis
* **SQLAlchemy** – ETL pipeline integration
* **Power BI** – Data visualization and dashboard creation
* **Jupyter Notebook** – Development environment
* **GitHub** – Version control and documentation

---

## * ETL Process

### 1. Extract

* Loaded raw data from CSV file (`insurance101.csv`)
* Validated dataset structure and row count (~1337 records)

### 2. Transform

* Cleaned missing and inconsistent values
* Standardized text fields (sex, smoker, region)
* Converted data types (age, bmi, charges)
* Removed duplicates

### 3. Load

* Loaded cleaned data into SQL Server table: `dbo.insurance101_clean`
* Verified row count and data integrity

---

## * Key Analysis Performed

* Average insurance charges by:

  * Smoking status
  * Gender
  * Region
  * Number of children
* Correlation between BMI, age, and charges
* Identification of high-cost risk groups

---

## * Key Insights

* Smokers have significantly higher insurance charges
* BMI and age positively correlate with higher costs
* Regional differences impact insurance pricing
* Families with more children show moderate cost increases

---

## * Power BI Dashboard Features

* KPI Cards (Average Charges, Total Records)
* Bar Charts (Charges by Gender & Region)
* Donut Chart (Charges by Gender)
* Scatter Plot (BMI vs Charges)
* Interactive Filters (Smoker, Region)

---

## * Results

* Clean dataset with consistent formatting and correct data types
* Accurate average charges (~$13,200–$13,300)
* Fully functional ETL pipeline
* Professional dashboard for business insights

---

## * Business Value

This project demonstrates the ability to:

* Build scalable ETL pipelines
* Clean and transform raw data into usable formats
* Perform data-driven analysis
* Present insights visually for decision-making

---

## * Future Enhancements

* Deploy ETL pipeline in AWS (S3, RDS, Glue)
* Automate data refresh processes
* Implement machine learning model for charge prediction

---

## * Author

John Meeks
Aspiring Data Analyst | ETL Developer | Python & SQL Enthusiast

