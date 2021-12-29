## 题目描述
编写一个 SQL 查询，获取 Employee 表中第 n 高的薪水（Salary）。
```
+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
```
例如上述 Employee 表，n = 2 时，应返回第二高的薪水 200。如果不存在第 n 高的薪水，那么查询应返回 null。
```
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+
```

### 解法1 去重 + 重新定义变量值
这题和上一题如出一辙。
思路还是一样，通过DISTINCT去重然后排序再用LIMIT找到相关行。

然而这题的难点在于，第N高的薪水，其实是排完序后表的下标第N-1行。
换言之，应该要用类似于`LIMIT N-1,1`这样的子句。

然而很遗憾，LIMIT后面不让接表达式，因此这里就需要提前定义一个值为N-1的变量。
然而MySQL的函数里变量定义还不是那么随意的，需要用@的方式进行地址申请。这么一来在LIMIT后面调用又要用@表达式。
所以这里采取一个比较巧妙的办法，就是重新定义变量N。
具体来说，就是在进行主要的处理前，先跑这么一行代码：
```sql
SET N:=N-1;
```
就万事大吉了。

最后答案：
```sql
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  SET N:=N-1;
  RETURN (
      # Write your MySQL query statement below.
      SELECT DISTINCT Salary FROM Employee ORDER BY Salary DESC LIMIT N,1
  );
END
```

### 解法2 Dense_rank
借鉴`LC.178`中的预设排名函数，也可以做这道题。
简单来说，首先这样一个SQL构成的表很好懂：
```sql
SELECT Salary, Dense_rank() OVER (ORDER BY Salary DESC) AS rnk FROM Employee
```
这就是给每个薪水做了一个有并列无间隔的排名。第N高的薪水其实就是这张表中那些`rnk=N`的记录中的Salary。
于是再`SELECT DISTINCT Salary FROM 这个表 WHERE rnk=N`即可。

最终答案：
```sql
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      SELECT DISTINCT Salary FROM
      (SELECT Salary, Dense_rank() OVER (ORDER BY Salary DESC) AS rnk FROM Employee) a
      WHERE rnk=N
  );
END
```