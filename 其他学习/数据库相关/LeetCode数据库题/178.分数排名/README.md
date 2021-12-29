## 题目描述
编写一个 SQL 查询来实现分数排名。

如果两个分数相同，则两个分数排名（Rank）相同。请注意，平分后的下一个名次应该是下一个连续的整数值。换句话说，名次之间不应该有“间隔”。
```
+----+-------+
| Id | Score |
+----+-------+
| 1  | 3.50  |
| 2  | 3.65  |
| 3  | 4.00  |
| 4  | 3.85  |
| 5  | 4.00  |
| 6  | 3.65  |
+----+-------+
```
例如，根据上述给定的 Scores 表，你的查询应该返回（按分数从高到低排列）：
```
+-------+------+
| Score | Rank |
+-------+------+
| 4.00  | 1    |
| 4.00  | 1    |
| 3.85  | 2    |
| 3.65  | 3    |
| 3.65  | 3    |
| 3.50  | 4    |
+-------+------+
重要提示：对于 MySQL 解决方案，如果要转义用作列名的保留字，可以在关键字之前和之后使用撇号。例如 `Rank`
```

### 解法1 子查询 Count(DISTINCT)
观察结果，发现结果有两列。
组成第一列很简单，只要一个简单的order by desc就行了。问题在于第二列如何组成。
直接考虑有些复杂，不妨考虑更加简单的情况。比如我给出一个分数X，如何查找得分为X的人，在题目设定中的排名？

这里就需要用到一个count函数的小知识点。针对某个字段，可以使用诸如`Count(DISTINCT Score)`这样的语法。这样可以求出Score字段下总共有多少种
不同的值。
根据题意，所谓的排名，其实就是`Count(DISTINCT Score) WHERE Score >= X`。
于是通过在构造第一列的order by desc语句中嵌入一个子查询，就可以构造出第二列的排名了。

具体的：
```sql
SELECT a.Score,
(SELECT Count(DISTINCT b.Score) FROM Scores b WHERE b.Score >= a.Score) as `rank`
FROM Scores a ORDER BY a.Score DESC;
```

### 解法2 内置排名函数（顺便讲下各类稍高级的排名函数）
解法1中的排名逻辑其实是日常工作中也常用的一种逻辑，因此MySQL(8.0版本以及之后)其实已经有了相关的内置函数，`dense_rank`。
其具体用法如下：
```sql
SELECT *, Dense_rank() OVER (ORDER BY Field) FROM Table;
```
dense rank函数的功能：基于某一列排序数据，进行"有并列，无间隔"的排名。
比如上面这条SQL的例子，描述一下结果长什么样的话，就是说，首先将Table中各行进行一基于Field字段的升序排序，
因为select了`*`，所以所有列都被选取出来。
接着在最后一列，添加一列排名数据。这个排名数据是从排序后的第一行开始从1开始标注。并且有并列无间隔。
比如Field的排序后的字段值序列是`100 100 300 400 400 500`的话，那么排名数据就是`1 1 2 3 3 4`。

而这恰好符合本题的题意。
本题的答案就是：
```sql
SELECT Score, Dense_rank() OVER (ORDER BY Score DESC) as `rank` FROM Scores;
```

除了dense rank，MySQL还有一些其他的内置好的比较方便的排名函数，顺便介绍一下。
以下面这张数据表为例：
```text
id      score
1       100
2       100
3       200
4       400
5       400
6       500
```

- rank
首先，既然有dense rank，那么肯定有rank。rank和dense rank的功能十分相近，只不过一般的rank进行的，
是"有并列，有间隔"的排名。
比如上面这个数据表，运行`SELECT *, Rank() OVER (ORDER BY Score) FROM Table;`，得到的结果中，排名列的序列应该是
`1 1 3 4 4 5`。

- row_number
row number某种意义上也是一种排名函数。
不过其功能本质上是给输出的行标行号。可以看做是一种"无并列，无间隔"的排名操作。
上述数据运行`SELECT *, Row_number() OVER (ORDER BY Score) FROM Table;`，得到的结果中，排名列的序列应该是
`1 2 3 4 5 6`。
对于那些Score相同的行，当然其排序就按照默认的规则，找第二基准列进行排序咯。

- ntile
这可能都不算一个排名函数吧…
这个函数的功能是，给出`Ntile(grp_num)`，可以将输出数据各个行尽可能均匀地分成`grp_num`个group。然后从1开始给group按顺序编号。每个group
内的编号一样。
比如上面数据运行`SELECT *, Ntile(3) OVER (ORDER BY Score) FROM Table;`的话，得到的排名序列是
`1 1 2 2 3 3`。
被分成了三个组