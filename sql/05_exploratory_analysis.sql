--5) Exploratory Analysis

-- 1. Overall summary
SELECT
    COUNT(*)               AS total_people,
    ROUND(AVG(charges), 2) AS avg_charges,
    ROUND(MIN(charges), 2) AS min_charges,
    ROUND(MAX(charges), 2) AS max_charges
FROM dbo.insurance101_clean;
GO

-- 2. Charges by smoker
SELECT
    smoker,
    COUNT(*)               AS total_people,
    ROUND(AVG(charges), 2) AS avg_charges
FROM dbo.insurance101_clean
GROUP BY smoker
ORDER BY avg_charges DESC;
GO

-- 3. Charges by gender
SELECT
    sex,
    COUNT(*)               AS total_people,
    ROUND(AVG(charges), 2) AS avg_charges
FROM dbo.insurance101_clean
GROUP BY sex
ORDER BY avg_charges DESC;
GO

-- 4. Charges by region

SELECT
    region,
    COUNT(*)               AS total_people,
    ROUND(AVG(charges), 2) AS avg_charges
FROM dbo.insurance101_clean
GROUP BY region
ORDER BY avg_charges DESC;
GO

-- 5. Charges by children
SELECT
    children,
    COUNT(*)               AS total_people,
    ROUND(AVG(charges), 2) AS avg_charges
FROM dbo.insurance101_clean
GROUP BY children
ORDER BY children;
GO

-- 6. Charges by age

SELECT
    age,
    COUNT(*)               AS total_people,
    ROUND(AVG(charges), 2) AS avg_charges
FROM dbo.insurance101_clean
GROUP BY age
ORDER BY age;
GO

-- 7. Top 10 highest charges

SELECT TOP (10)
    age,
    sex,
    bmi,
    children,
    smoker,
    region,
    charges
FROM dbo.insurance101_clean
ORDER BY charges DESC;
GO
