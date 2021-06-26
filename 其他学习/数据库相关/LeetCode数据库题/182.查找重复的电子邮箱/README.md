## 题目描述
编写一个 SQL 查询，查找 Person 表中所有重复的电子邮箱。

示例：
```
+----+---------+
| Id | Email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
```
根据以上输入，你的查询应返回以下结果：
```
+---------+
| Email   |
+---------+
| a@b.com |
+---------+
```
- 说明：所有电子邮箱都是小写字母。

### 解法 子查询（临时表
重复的地址，换句话说就是计数值大于1的那些记录。
说到计数，就想到了Count配合group by了。
所以可以先写出这么一条：
```sql
SELECT Email, Count(*) AS cnt FROM Person GROUP BY Email;
```
可上面的SQL没有什么地方可以让我们再插入一个针对cnt的判断条件子句了。

于是将其结果视作一个"临时表"，将其作为子查询使用。
这么一来就可以很简单地写出外层的SQL了：
```sql
SELECT Email FROM
(SELECT Email, Count(*) AS cnt FROM Person GROUP BY Email)
WHERE cnt > 1;
```