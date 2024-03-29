## 题目描述
编写一个 SQL 查询，获取 Employee 表中第二高的薪水（Salary） 。
```
+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
```
例如上述 Employee 表，SQL查询应该返回 200 作为第二高的薪水。如果不存在第二高的薪水，那么查询应返回 null。
```
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
```

### 解法 子查询
看似用下面这个就行了。
```sql
SELECT Salary FROM Employee ORDER BY Salary DESC LIMIT 1,1;
```

但是这条SQL存在几个问题。
首先，如果大家的工资一样高，那么就不存在第二高工资，所以在Salary之前应该加上DISTINCT。或者也可以借用GROUP BY来进行去重操作，如：
`SELECT Salary FROM Employee GROUP BY Salary ORDER BY Salary DESC LIMIT 1,1;`

其次，当表中数据不足两条时，显然这条SQL返回的是空结果，即0行结果。
但是题目要求在这种情况下要返回NULL。
此时可以将本SQL写成一个独立的子查询。这个子查询建立在临时表上。
临时表是空表时，子查询会返回NULL，于是就实现了将空结果转换成NULL的过程
