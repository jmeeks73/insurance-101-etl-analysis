# 🧠 ETL Architecture

## 📌 Project Overview

This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline using an insurance dataset.

The objective is to:

* Extract raw data from a CSV file
* Transform and clean the data using Python and SQL Server
* Load the cleaned data into a structured database
* Visualize insights using Power BI

---

## 🔄 Data Flow

```text
Raw CSV → Python Cleaning → SQL Server → Power BI Dashboard
```

---

## ⚙️ Tools Used

* Python (pandas)
* SQL Server (T-SQL)
* Power BI
* GitHub

---

## 🧩 ETL Process

### 1. Extract

* Source file: `insurance101.csv`
* Stored in: `data/raw/`
* Loaded using Python (`pandas.read_csv`)

---

### 2. Transform

#### Python Cleaning

* Remove duplicate rows
* Check and handle missing values
* Standardize column names
* Validate dataset structure

#### SQL Cleaning

* Trim whitespace (`LTRIM`, `RTRIM`)
* Convert text to lowercase (`LOWER`)
* Convert data types (`CAST`)
* Remove duplicate records

---

### 3. Load

* Database: `Insurance101DB`
* Table: `dbo.insurance101_clean`
* Cleaned CSV stored in: `data/cleaned/`

---

### 4. Visualization

* Tool: Power BI
* Connected to SQL Server
* Built interactive dashboard

---

## 📊 Final Output

The final dashboard includes:

* KPI: Average insurance charges (~$13,279)
* Bar chart: Charges by smoker status
* Pie chart: Gender distribution
* Scatter plot: BMI vs Charges

---

## 📎 Related Documentation

* [Data Dictionary](data_dictionary.md)
* [Data Cleaning](data_cleaning.md)
* [Analysis](analysis.md)
* [Dashboard](dashboard.md)
