## 题目描述
某网站包含两个表，Customers 表和 Orders 表。编写一个 SQL 查询，找出所有从不订购任何东西的客户。

Customers 表：
```
+----+-------+
| Id | Name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
```
Orders 表：
```
+----+------------+
| Id | CustomerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
```
例如给定上述表格，你的查询应返回：
```
+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+
```

### 解法 外联结
通过一个外联结可以统计出每个客户与属于其的订单，并包括那些没有订单的客户。
这么一来，只要再加一条where条件："订单为NULL的客户"就可以把目标客户筛选出来了。

注意上面这个条件得写成`is NULL`而不能是`= NULL`。

```sql
SELECT Name AS Customers FROM Customers
LEFT JOIN Orders ON Customers.Id=Orders.CustomerId
WHERE Orders.Id is NULL;
```