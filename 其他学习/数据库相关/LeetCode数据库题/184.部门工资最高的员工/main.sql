SELECT Department.Name As Department, Employee.Name as Employee, Employee.Salary
FROM Department, Employee
WHERE Employee.DepartmentId = Department.Id AND
(Employee.DepartmentId, Employee.Salary) IN  /* 这里就是多元元组的IN */
(SELECT DepartmentId, MAX(Salary) FROM Employee GROUP BY DepartmentId);