--3). Transform and Load New Table

INSERT INTO dbo.insurance101_clean (
    age,
    sex,
    bmi,
    children,
    smoker,
    region,
    charges
)
SELECT
    TRY_CAST(age AS INT),
    LOWER(LTRIM(RTRIM(sex))),
    TRY_CAST(bmi AS DECIMAL(10,2)),
    TRY_CAST(children AS INT),
    LOWER(LTRIM(RTRIM(smoker))),
    LOWER(LTRIM(RTRIM(region))),
    TRY_CAST(charges AS DECIMAL(12,2))
FROM dbo.customerinsurance_info;
GO



