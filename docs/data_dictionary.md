#  Data Dictionary – Insurance 101 Dataset

## * Overview

This data dictionary describes the structure, fields, and data types of the cleaned insurance dataset used in the ETL pipeline.

---

## * Table: `dbo.insurance101_clean`

| Column Name | Data Type     | Description                                                                 |
| ----------- | ------------- | --------------------------------------------------------------------------- |
| age         | INT           | Age of the primary beneficiary                                              |
| sex         | VARCHAR(20)   | Gender of the beneficiary (male/female)                                     |
| bmi         | DECIMAL(10,2) | Body Mass Index (BMI), a measure of body fat based on height and weight     |
| children    | INT           | Number of dependents covered by the insurance plan                          |
| smoker      | VARCHAR(10)   | Smoking status (yes/no)                                                     |
| region      | VARCHAR(20)   | Residential region in the U.S. (northeast, northwest, southeast, southwest) |
| charges     | DECIMAL(12,2) | Individual medical insurance cost billed by the provider                    |

---

## * Notes

* All text fields were standardized to lowercase during transformation
* Whitespace and formatting inconsistencies were removed
* Numeric fields were validated and converted to appropriate data types
* Duplicate records were removed to ensure data integrity

---

## * Data Source

* Original dataset: `insurance101.csv`
* Processed through ETL pipeline using Python, SQL Server, and Power BI

---

## * Usage

This dataset is used for:

* Data analysis and reporting
* SQL-based business insights
* Power BI dashboard visualizations
* Identifying key factors influencing insurance charges

