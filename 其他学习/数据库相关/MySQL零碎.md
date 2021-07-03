>参考1：https://github.com/Snailclimb/JavaGuide/blob/master/docs/database/MySQL.md
>
>参考2: https://mp.weixin.qq.com/s/IiJYHoAxqTnqW0LfRAh2BQ
>
>索引：https://zhuanlan.zhihu.com/p/352181863
>
>参考（2021/06/26追加）：https://www.nowcoder.com/discuss/637486

# MySQL的存储引擎有哪些，区别是什么
MySQL支持很多存储引擎。主要比较InnoDB和MyISAM。
可以在终端中键入`show engines;`查看。

比较两者，InnoDB的优势在于：
- 不仅支持表锁，还支持行锁
- 支持事务
- 支持外键
- 根据事务日志，可以对数据进行恢复
- 使用聚簇索引
劣势在于
- 不能进行全文本搜索

# 常用的MySQL数据类型有哪些
- 整数：INT, BIGINT分别标识32、64位整数
- 浮点数：FLOAT，DOUBLE，DECIMAL。其中DECIMAL基于字符串处理，能存储更加精确的小数。
三者都可以指定位长如`DECIMAL(a,b)`表示总共用a位表示浮点数，其中b位保存小数部分。

- 字符串：CHAR, VARCHAR。VARCHAR可变长，更灵活但更耗费空间
- 日期：DATE，DATETIME等

# MySQL收到请求后的处理流程
![](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9wNi10dC5ieXRlaW1nLmNvbS9vcmlnaW4vcGdjLWltYWdlLzA3NjZmYjE3YjNkZjQ0ZWZhZjIwMTYxNTJkZGNjNTIz?x-oss-process=image/format,png)

# SQL语句基础知识与优化
## SQL语句主要分类
- DDL(Data Definition Language)语句: CREATE, DROP, ALTER等
- DQL(Data Query Language)语句: 主要是SELECT
- DML(Data Manipulation Language)语句：主要指INSERT, DELETE, UPDATE
- DCL(Data Control Language)语句：指权限功能相关比如GRANT, REVOKE, COMMIT, ROLLBACK等。

## SQL约束有哪些
主键约束、外键约束：略
唯一约束：要求保证每列数据没有相同的值
默认约束：插入新数据时对没有指定数据的列设置为默认值或者默认的默认值NULL
check约束：check通过逻辑表达式判断数据有效性并以此为约束

## 子查询
子查询可以分成下面几种：

标量子查询：指子查询返回的结果是一个值，可以通过各类运算符与之运算如：
```sql
SELECT * FROM user WHERE age = (SELECT Max(age) FROM all_users);
```

列子查询：指子查询返回的是一个列，通常可以用IN, ALL, ANY等操作符与之进行计算如：
```sql
SELECT * FROM user WHERE name IN (SELECT name FROM all_users);
```

行子查询：指子查询返回的是一个行，此时通常用元组等式来判断如
```sql
SELECT * FROM user WHERE (name, age) = (SELECT name, age FROM all_users WHERE id=1);
```

表子查询：子查询返回一个多行多列的子表（临时表），这里也可以用元组IN来做判断如：
```sql
SELECT * FROM user WHERE (name, age) IN (SELECT name,age FROM all_users WHERE age>=10);
```

## 联结的种类
联结包括内联结，左右外联结，全外联结和交叉联结。
根据是否表与自身联结还可以分化出一个自联结的概念。当然自联结和上面这些联结分类并不处于同一个概念维度。
其中MySQL不支持全外联结。

假如我们有这两张表：
表L:
```text
A   B
a1  b1
a2  b2
a3  b3
```
表R:
```text
B   C
b1  c1
b2  c2
b4  c4
```

则内联结：`SELECT L.*, R.* FROM L JOIN R ON L.B=R.B;` 得到：
```text
A   B   B   C
a1  b1  b1  c1
a2  b2  b2  c2
```

左外联结：`SELECT L.*, R.* FROM L LEFT JOIN R ON L.B=R.B;`。得到(N表示NULL)
```text
A   B   B   C
a1  b1  b1  c1
a2  b2  b2  c2
a3  b3  N   N
```
右外联结就是R表在前的左连接，相当于只有b4 c4没有a3 b3的情况，就不重复写了。

交叉联结：`SELECT L.*, R.* FROM L, R;`不带任何限定条件，因此相当于把A的每一行和B的每一行配对，做一个笛卡尔积。得到
```text
A   B   B   C
a1  b1  b1  c1
a1  b1  b2  c2
...
a3  b3  b4  c3
```
在这个后面加上限定条件，这其实就变成了简单的内联结。
由于使用交叉联结 + 限定条件的方式，还是会生成一个很大的临时表，所以能用JOIN解决的时候尽量应该用JOIN解决。

## IN和EXISTS的区别
这两个关键字都用于子查询匹配的场景。我们将原表称为外表，而子查询查询的表称为内表。
于是范式大概是`外表字段 IN/EXISTS (内表范围)`。这个语句的原理其实是：

两者区别在于，使用EXISTS时会先进行外表查询，然后将每行代入内表查看是否满足条件。
IN则反过来，先进行子查询确定内表范围，然后再代入外表过滤结果集。

通常，先确定一个小范围比较有效率，因此外表比内表大的时候，IN更好；反之，外表比内表小的时候EXISTS更好。

而对于NOT EXISTS，总是比NOT IN要更好。因为NOT EXISTS会用索引而NOT IN只会进行全表扫描。

## varchar和char
varchar可变长，因此体现出两者的优劣性。
因为可变长，varchar更加灵活，且更加节省空间（不会因为字符长度小于指定值而用空格padding）。
但是由于可变长，offset就不管用，因此存储速度上varchar略慢一点。

>补充一点，int(10)和varchar(10)/char(10)有什么区别
>
>这两种定义的根本就不是同一类型的数据。int(10)中的10只是表示显示数据的长度，比如对于1这个数，int(10)显示
>0000000001，而int(3)可能就显示001。两者都是占用4个字节。
>
>而varchar和char则是真的指出了用几位去存储一个数据。

## DROP, DELETE, TRUNCATE
DROP用于删除整个表数据和表结构。
TRUNCATE用于删除整个表数据，但是保留表结构。
注意这两者都是DDL，所以不能回滚。

DELETE通常用于行的删除，不加限定条件是也可删除整个表数据，但是一行行删除，比较费时。
另外DELETE是DML，可以回滚。

## UNION和UNION ALL
UNION合并结果时去重并排序。
UNION ALL合并结果时直接合并，不去重也不排序。
UNION ALL更快。（废话

## 慢查询，慢查询日志，如何优化
可通过对`slow_query_log`等开启对慢查询日志的记录。
优化思路有
- 查看执行计划，看SQL是否走了索引
- 垂直、水平分库，从根本上解决慢查询
- 优化limit分页

## 主键用自增ID和UUID的优劣
一般使用自增ID即可。
自增ID的好处有
- 字段长度小，比较大小很快
- 可轻松按序存放，方便主键索引的建立

相对的自增ID也有一些缺点，比如
- 通过自增ID可以推测业务量等
- 数据迁移、表合并比较麻烦

总体来说，自增ID还是完胜UUID的

## 为什么某列无值时尽量应该用空值而非NULL
即，为什么列尽量应该设置NOT NULL
- Count等聚合函数不统计NULL值
- 参与字段数值比较时，NULL比较难处理

## 如何优化WHERE子句条件
- 尽量不使用不等于号
- 尽量用UNION ALL代替OR
- 对WHERE或者ORDER BY涉及的列建立索引
- 尽量避免IN或者NOT IN从而引发全表扫描

## SQL执行很慢的原因
如果是偶尔很慢，可能恰好遇到了锁，或者redo log日志写满了正在将log同步到磁盘中去。

如果总是很满，可能是SQL本身不够优化，或者没走到索引等。

# 大表的优化策略

## 大表数据查询的优化思路有哪些
- 使用索引
- SQL语句逻辑优化
- 水平/垂直分表
- 使用缓存
- 读写分离
等等

## 什么是垂直/水平分库分表
垂直分表：将原来一个表的字段分成多个表，每个表存储一部分字段。通常将常用字段整到一个表，不常用整另一个。
垂直分表的好处是可以提升热门数据的查询效率，减少IO竞争。因为表内数据都是存在数据页上的。如果一行的字段过多，导致一个数据页能存放的行数就变少，
检索表时要频繁切换数据页等。

垂直分库：类似的，将原来一个库中的各个表部署到不同的数据库，不同的数据库也可以放到不同的服务器上。
垂直分库的好处也是类似的，提升IO效率，降低单机的资源限制

垂直分库分表的劣势：
整体数据上会多出冗余的主键列。
事务处理会变复杂。
仍然会有单表数据过大的问题。


水平分表分库：不解释
水平分库分表的好处是同样，可以减少IO竞争，解决单个表数据量过大问题。
缺点是分片事务的一致性很难保证。跨节点的SQL性能会受到影响。数据扩展难度大，不易维护。

## 分库分表后如何保持主键的全局唯一性
有多种可能的解决方案。
- UUID，用UUID的话基本可以保证全局唯一性。但是UUID的坏处上面也说过。

- 利用额外表自增ID。在分库分表后，在数据库中设立一个全局的用于生成自增ID的表。每当要新生成一个ID时，无论其要插入在哪个分库分表中，
先在这个额外的表中插入一条空数据另其生成一个新ID，然后取这个新ID作为主键再插入分库分表实际数据。

- Redis生成法：用Redis的自增机制生成ID。

