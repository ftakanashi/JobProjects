# Write your MySQL query statement below
SELECT(
    SELECT DISTINCT Salary FROM Employee
    ORDER BY Salary DESC LIMIT 1,1
) AS SecondHighestSalary;