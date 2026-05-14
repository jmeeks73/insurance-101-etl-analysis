--2). Create New Table

CREATE TABLE dbo.insurance101_clean (
    age       INT,
    sex       VARCHAR(20),
    bmi       DECIMAL(10,2),
    children  INT,
    smoker    VARCHAR(10),
    region    VARCHAR(30),
    charges   DECIMAL(12,2)
);
GO
