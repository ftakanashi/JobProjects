> 参考：MySQL必知必会（第五版）
>
> 其他参考：https://www.zhihu.com/question/19552975

# SQL入门和MySQL的介绍
>都是一些很基本的介绍，只挑选一些可能有些用的记录一下。

`SHOW DATABASES;`可以查看当前MySQL中维护了哪些数据库。
`USE xxx;`用来切换当前数据库。

在一个数据库中时使用`SHOW TABLES;`可以查看所有表的概况。
`SHOW COLUMNS FROM ttt;`则可以查看某一个表中各个字段的情况。能够起到同样作用的语句还有`DESCRIBE ttt;`。

其他的SHOW相关的语句还包括了
```text
SHOW STATUS     查看服务状态信息
SHOW CREATE DATABASE ddd    查看创建ddd数据库的SQL语句
SHOW CREATE TABLE ttt       查看创建ttt表的SQL语句
SHOW GRANTS                 查看所有用户的权限
SHOW GRANTS FOR uuu         查看uuu用户的权限
SHOW ERRORS                 查看服务器错误信息
SHOW WARNINGS               查看服务器警告信息
```

# 检索: 初级
以下说明中使用的例子表结构如下
```sql
CREATE TABLE `world` (
  `Code` varchar(3) NOT NULL DEFAULT '',
  `Name` varchar(52) NOT NULL DEFAULT '',
  `Continent` NOT NULL DEFAULT 'Asia',
  `Region` varchar(26) NOT NULL DEFAULT '',
  `SurfaceArea` decimal(10,2) NOT NULL DEFAULT '0.00',
  `IndepYear` smallint DEFAULT NULL,
  `Population` int NOT NULL DEFAULT '0',
  `LifeExpectancy` decimal(3,1) DEFAULT NULL,
  `GNP` decimal(10,2) DEFAULT NULL,
  `GNPOld` decimal(10,2) DEFAULT NULL,
  `LocalName` varchar(45) NOT NULL DEFAULT '',
  `GovernmentForm` varchar(45) NOT NULL DEFAULT '',
  `HeadOfState` varchar(60) DEFAULT NULL,
  `Capital` int DEFAULT NULL,
  `Code2` varchar(2) NOT NULL DEFAULT '',
  PRIMARY KEY (`Code`)
);
```

## 检索唯一值
用到`DISTINCT`关键字。
语法上，写在列的前面比如
```sql
SELECT DISTINCT name FROM world;
```
需要注意DISTINCT必须要用在所有列前面。而当他修饰的是多个列时，表明这些列的全部值都不同的情况，而不是部分不同的情况。

## 限制检索结果
用到`LIMIT`关键字。

用法大概分成两种，后面跟一个还是两个数字。
跟两个数字时比如:
```sql
SELECT * FROM world LIMIT 5,3;
```
表示选择不带limit时结果中，从(0开始计数的)第五行开始的三行。即原结果中的第5，6，7行。

若只有一个数字，则等价于从第零行开始，即
```sql
SELECT * FROM world LIMIT 5; 等价于
SELECT * FROM world LIMIT 0,5;
```

如果想指定选中第n行，可以指定参数为`LIMIT n,1`。

当供检索的行数不够时，即LIMIT尝试返回越界的行时，并不会报错，而是返回能返回的所有行。

## 排序检索结果
用到`ORDER BY`语句。

一般的写法是
```sql
SELECT * FROM world ORDER BY region;    // 以面积大小选择所有国家
```

以上是以一个字段作为排序依据的情况。如果需要多个字段作为依据，只要在`ORDER BY`后面加上用逗号分隔的多个字段即可。
字段的优先级自然是从左到右依次减小，如：
```sql
SELECT name, continent FROM world ORDER BY continent, name;
```

通过ORDER BY发生的排序动作，默认是升序的。如果需要改为降序，则在相关依据字段后面加上关键字`DESC`即可。
如
```sql
SELECT name, continent FROM world ORDER BY continent, name DESC;
```
一个小点：其实也可以通过关键字`ASC`显式指定升序，当然这么做意义不大，因为默认就是升序的。

关于文本数据的排序：
在MySQL和大多数数据库中，文本型数据默认不区分大小写，换言之，使用`ORDER BY`对文本型数据进行排序时，数据库并不能做到将所有大写字母都排在小写字母前面。
但另一方面，如果确实需要这么做，可以在MySQL的后台进行变量的修改从而让引擎区分大小写。当然这需要数据库的管理员权限。

## 条件过滤检索结果
主要是使用`WHERE`子句。
WHERE子句要配合不同的操作符从而实现不同的过滤行为。支持的操作符，不同的数据库系统间有些微妙的不同，以MySQL为例，支持如下操作符：
```text
=               等于
!= (或者<>)      不等于
<, <=           小于（等于）
>, >=           大于（等于）
BETWEEN         在指定的两个值中间，值通常是数字类型或者日期等
```

以上操作符是针对单个条件的。WHERE子句后面还可以是多个条件。
条件之间的逻辑关系，可以用AND, OR, NOT等关键字来连接表示。
关键字IN则可以简化多个OR连接的等于条件的写法。

在MySQL中，NOT关键字可以对IN, BETWEEN, EXISTS等子句进行逻辑取反。
如：
```sql
SELECT name, surfacearea FROM world WHERE surfacearea NOT BETWEEN 100000 AND 9000000 ORDER BY surfacearea;
```

## 通配符过滤检索结果
进行基于通配符的过滤的时候，需要使用谓词`LIKE`。虽然这个关键字看起来和上面的操作符并没有区别，但是从定义上来说更应该被称为谓词。
注意SQL中使用通配符匹配时，默认是匹配整个串的，即如果用正则来表达，则默认要在其表达式前后分别加上一个`^`和`$`。

最常用的通配符是`%`，类似于正则表达式中的`*`，即指零到任意多个字符。
而`%`虽然能匹配零个字符，但是不能和NULL值匹配，这一点是需要注意的。

另一个通配符是下划线`_`，类似于正则表达式中的`.`，即匹配一个字符。

说到通配符，通常总是以为在处理字符串，但是SQL中的类型没有编程语言那么严格。
字符串当然可以拿去匹配，然而int,float这些数字类型也可以直接拿去匹配。匹配的时候你就当他是自动转成字符串再计算匹配的吧。
如：
```sql
SELECT name, gnp FROM world WHERE gnp like '9%';    // 将所有GNP数据是9开头的国家选出来
```

使用通配符进行匹配的时候需要注意，由于是通配符，性能上通常会比较弱。
因此在能够通过其他办法实现的操作中，应尽量不使用通配符。
另外，通配符最好不要放在scheme的开头处，否则一定会大大拖慢搜索的速度。

## 正则表达式过滤检索结果
上面说到了简单的通配符进行匹配。如果要更复杂的匹配逻辑，自然就该正则上场了。
SQL中的正则匹配的使用方法和上面的通配符很像，只不过`LIKE`被换成了`REGEXP`。

此外，SQL中支持的正则也是完整正则的一小部分，大概包括如下这些正则表达：
```text
各种通配符如 . * + 等
锚点符 ^ $
选择符号 |
字符选择如 [0-9] 等
多个匹配如 {1,3} 等
```
SQL中进行上面这些特殊符号的反转义时需要用两个斜杠。比如想要匹配文本中的'.'，则在SQL的正则中应该写`REGEXP '\\.'`。
因为SQL引擎本身要解释一个斜杠，而正则表达式引擎解释另一个。

Python正则中经常出现的诸如`\d`表示所有数字之类的"字符集匹配"，这里也可以用，只不过是表达方式不太一样，比如这个`\d`在这里写成`[:digit:]`。
这方面的完整的表格，参考书的第58页。

# 检索: 计算字段
>从这里开始使用书中附带的实例数据说明。
>
>关于实例数据可以参考附录B中的内容。

通常存储在数据库中的数据的格式并不是应用程序最终想要的格式。比如计算选出的数字的平均，或者进行多个字符串字段的格式化输出等。
以上操作当然可以在取出数据之后，在应用程序中另行处理。
但是也可以直接在SQL中通过计算字段直接求出。因为SQL的引擎很牛批，一般都会更快。

换言之，计算字段并不真实存在于表中，而是在运行时在SELECT语句内部创建。

## 拼接字段
主要使用`Concat`函数。（其他数据库大多都是用加号的，MySQL却规定要用Concat函数，这点需要注意）

拼接的时候还可以使用`Trim`, `LTrim`和`Rtrim`（类比strip, lstrip和rstrip）来去除两端的空格。
（注意SQL不区分大小写，但是规范上来说，这些函数应该写成每个单词首字母大写形式）

>字段的别名
>
>在计算字段后面加上子句`AS xxx`可以将这个计算字段临时命名一个别名`xxx`。

## 算术计算字段
简单的四则运算符号就可以作为一个计算字段直接跟在select关键字后，比如:
```sql
select prod_id, quantity, item_price, quantity * item_price as total_price from orderitems where order_num=20005 order by total_price desc;
```

由于select后面的字段可以是计算字段，而计算字段又可以灵活地得来（比如用MySQL内置函数，或者四则运算等）。
因此也可以使用简单的比如`SELECT 2 * 3;`或者`SELECT Trim(' abc ');`, `SELECT Now();`之类的简单语句来验证系统是否工作正常。

## 函数计算字段
上面提到的Concat其实就是一个利用函数计算出来的计算字段。
可以用在这里的函数大概分成几类，文本处理函数，数值算术函数（比四则更加复杂一点的），日期处理函数，MySQL本身相关的函数。

下面将一些常用的罗列一下：

### 文本处理函数
```text
函数                 返回值
Left(field, n)      前n个字符
Length(field)       长度
# Locate()          
Lower(field)        小写化
Upper(field)        大写化
Trim(field), LTrim(field), RTrim(field)     去除 两边/左边/右边 所有空格
SubString(field, a, b)      返回第a个字符到第b个字符间子串，用Python的切片方式来写应该是[a-1:b+1]
```

### 日期处理函数
MySQL中有时间日期对象，因此通常鼓励在数据库中存储这些对象而不是单纯的字符串。这样可以避免格式不统一等问题。

常用的函数如下(d表示MySQL中的一个时间日期对象)：
```text
AddDate(d, n)       在d的基础上加上n天后的时间
AddTime(d, s)       在d的基础上加上s秒后的时间
CurDate(), CurTime()           当前日期/时间 
Date(d)             获取某个对象的日期部分
Time(d)             获取某个对象的时间部分
DateDiff(d1, d2)    两个日期的差值
Date_Format(d, str) 将d格式化成str规定的格式（如%Y%m%d%H%M%S)

Year(d), Month(d), Day(d), DayOfWeek(d), Hour(d), Minute(d), Second(d) 是获取d的相应部分的函数
```

在WHERE等子句需要手动指定某个时间日期时，通常可以用`%Y-%m-%d %H:%M:%S`的标准格式来指出。
而变量部分最好用上述函数括起来，以避免奇怪的问题。比如书的示例：
```sql
SELECT order_id FROM orders WHERE Date(order_date) = '2005-09-01';
```
如果前面不用Date函数处理，那么如果`order_date`不是零点的话这个等号是取不到的。
再比如之前提到过的BETWEEN子句可以用于日期的比较：
```sql
SELECT order_id FROM orders WHERE Date(order_date) BETWEEN '2005-09-01' AND '2005-09-30';
```

### 数值处理函数
数值处理比较简单就不多说了。
```text
Abs(n)      返回n的绝对值
Sin, Cos, Tan(n)        三角函数
Exp(n)      求对数
Mod(n, r)   求余
Sqrt(n)      开方

Rand()      返回一个随机的0-1间的数  
Pi()        返回圆周率
```

### 聚合处理函数
聚合函数大多也是广义上的数值处理。但是与上面每个函数接收的是一个参数不同的是，
聚合处理函数接收的参数是若干个数组成的序列，即数组。
而这样一个数组，当然，是列方向的一个数组。

常见的聚合函数有：
```text
AVG     计算列平均值
COUNT   计数行数
MAX,MIN 计算最大、最小值
SUM     计算和
```

关于COUNT，还有一个特殊用法，在参数位置写一个星号：`COUNT(*)`。
这是表示单纯的统计所有记录形成了多少行。
如果是`COUNT(col)`这种形式，那么只统计col列的值不为NULL的行为有效行，而如果是上面这种星号，就不管有没有NULL全统计了。

类似的，MAX和MIN也都不统计相关列的值是NULL的记录。

除了原生的列，聚合函数也可以处理计算字段如：
```sql
SELECT AVG(item_price * quantity) FROM orderitems;
```

>聚合唯一值的情况
>
>以上所有对一个列中所有值做聚合的情况，都是遍历扫描所有值的。有些时候希望出现过的值只需要扫描一次，则可以在列名前加上DISTINCT关键字。
如
>```sql
>SELECT AVG(DISTINCT prod_price) FROM products;
>```

再说一次，这些聚合操作包括之前提到过的所有算计算字段的操作，基本都可以通过从数据库中取出数据后，
在客户端代码中实现。但是还是那句话，数据库引擎对这块的优化很好，所以如果可能，应该尽量交给数据库来完成这些简单的计算。


### 分组聚合数据
>从这里开始是SQL难度的一个分界点，上面的都是最最简单的逻辑，这里开始有些难理解了。

分组主要用到了`GROUP BY`子句以及`HAVING`子句。

上面的所有聚合函数，其聚合的对象是一个列的所有行。如果我想对这个范围有所限定，那么最简单的办法就是通过WHERE子句去限定一个更小的行范围。
比如`SELECT COUNT(*) FROM products WHERE vend_id=1001;`。
另一方面，如果我想同时知道所有可能的`vend_id`各自的这个值应该怎么办？最简单的一个办法，是用一个for循环遍历所有可能的`vend_id`，跑一边上面这个SQL。
而SQL本身提供了分组功能，来实现类似操作。

从下面这个例子入手：
```sql
SELECT vend_id, COUNT(*) AS num_prod FROM products GROUP BY vend_id;
```
在GROUP BY子句之前部分的SELECT语句，已经选出了一些行。具体到这句，由于没有任何WHERE子句的限定，所以选出的行就是所有行。
然后，在GROUP BY子句中，需要指定一个或多个列名。需要注意，这些列名必须是实际存在于表中的一些列，不能是AS定义的别名或者计算字段。

这条SQL的工作，是将上面得到的这些行首先进行基于GROUP BY子句指定的列进行分组。所有指定列完全相同的记录全部都分到一个组内。（如果有NULL则NULL本身自成一组）
分组完成后，就可以按组别分别统计每个组内的一些聚合函数的值了。比如上面的`COUNT(*)`，还可以是比如`AVG(prod_price) AS avg_price`等。

需要注意，列不选用聚合函数当然也可以，但是分组后每个组内必然有若干多个记录，如果不是统计聚合函数这类反映了所有记录总的特点的值的话，
使用分组就显得没那么有意义了。

事实上，如果运行诸如`SELECT vend_id, prod_price FROM products GROUP BY vend_id;`之类的SQL后，可以得到根据`vend_id`分组后的四个组的结果，
但是选出来的`prod_price`，是表从建立开始后插入记录时，每个分组中第一个插入的记录的相关值。

#### 过滤分组
在GROUP BY得到一些分组之后，默认这些分组会全部拿来计算相关的聚合性质。
但有时候，我们并不需要所有的分组，此时我们需要一个类似于WHERE子句的功能来过滤掉一些分组。
这个功能就是HAVING子句。

还是看一个例子：
```sql
SELECT vend_id, COUNT(*) FROM products GROUP BY vend_id HAVING AVG(prod_price) >= 10;
```
在没有HAVING子句时，即上面的那个SQL的运行结果，是四行，代表了根据`vend_id`进行分组可以分成四组。
而加上HAVING子句后，MySQL还会额外的查看`AVG(prod_price)`这个聚合值，只有那些这个值大于等于10的分组才会被保留下来最终返回。

HAVING和WHERE子句很像，事实上所有WHERE子句支持的操作符等HAVING也都支持。
两者的区别就在于，一个以记录为粒度来过滤，一个以组为粒度来过滤。
另一个区别就是两者在SQL中位置的顺序，GROUP BY必须在WHERE的后面。这点下面会细说。

#### 分组与排序
有GROUP BY的SQL通常会给出分组的聚合性质。
但是分组彼此之间并没有明确的排序规则。比如上面的SQL恰好给出的结果是`vend_id`升序的，但这只是巧合。
为了得到严格的排序好的分组数据，应该在GROUP BY 后面追加ORDER BY子句。如
```sql
SELECT vend_id, COUNT(*) FROM products GROUP BY vend_id ORDER BY vend_id;
```


再来看一个比较综合的，分组的例子：
```sql
SELECT order_num, SUM(quantity * item_price) AS order_total FROM orderitems
WHERE order_item < 4
GROUP BY order_num HAVING order_total >= 50
ORDER BY order_total;
```
在没有任何子句的情况下，只有第一行的情况下，注意这个SQL返回的是一行而不是所有行。
因为select的是一个SUM而不是单纯的计算字段。
其实反过来说，如果select了SUM还select了其他列的话，势必就需要分组了。

在分组前，还用了一个WHERE子句继续限定了需要分组的列是哪些。
接着，一个分组+HAVING，分组完成后过滤掉了一些不符合条件的组。
最后，分组结果以`order_total`为依据排序。

#### SELECT的子句的顺序
至此，SELECT语句的子句已经接触过了以下这些
```text
WHERE
GROUP BY
HAVING
ORDER BY
LIMIT
```
而符合SQL语法规则的这些子句的组装顺序，是从上到下的。换言之，一个用了以上所有子句的合法SQL应该长这样：
```sql
SELECT * FROM table WHERE xxx GROUP BY xxx HAVING xxx ORDER BY xxx LIMIT xxx;
```

# 检索: 子查询
当一个SELECT嵌套到另一个SELECT语句中，里层的SELECT语句也被称为一个子查询。

使用子查询，通常是因为我们需要的数据逻辑在一个表内无法完整获得，而需要通过表和表之间的关系来获得想要的数据逻辑。

## 子查询作为WHERE子句的条件
比如针对示例数据，一个order的相关信息被存放在好几个表里。
如果我希望找到 "所有订购了物品TNT2的客户的名称以及联系人是谁"。首先，在orderitems表中可以确定订购了TNT2产品的所有订单号。
其次，在orders表中可以找到相关订单号对应的客户id。
最后还需到customers表中，根据客户id找到客户的名称以及联系人。

整个过程用嵌套的select语句表示如下：
```sql
SELECT cust_name, cust_contact FROM customers WHERE cust_id IN (
    SELECT cust_id FROM orders WHERE order_num IN (
        SELECT order_num FROM orderitems WHERE prod_id='TNT2'
    )
);
```

## 子查询作为计算字段
如果将一个SELECT语句本身也看做一个函数，那么子查询也可以构建成一个计算字段。

比如问题：要求给出每个客户的名称以及他们各自的订单数量。
orders表中维护了每个客户的订单数量，而表中代表客户的字段是cust_id，而不保存任何客户的详细信息。
客户的详细信息则需要到customers表中搜索。

此时就需要进行一个跨表的搜索了。
具体的，如果我们指定某个cust_id比如10001的话，计数SQL很好写：`SELECT COUNT(*) FROM orders WHERE cust_id=10001;`。
现在我们要遍历所有客户而不是指定id，遍历所有客户的SQL也很好写：`SELECT cust_name FROM customers;`。

上面这个遍历SQL，是一行行处理的，在处理过程中，显然会确定一个cust_id，于是以上面第二条SQL为基干，可以扩展一个子查询构成的计算字段：
```sql
SELECT cust_name,
    (SELECT COUNT(*) FROM orders WHERE customers.cust_id = orders.cust_id) AS order_count
FROM customers;
```
SQL的解析执行过程现在还不太懂，但SQL本身不难懂。
简单来说，外层SQL遍历了所有客户，遍历到一行的时候自然就确定了其cust_id，将其作为依据放到里层的SQL中，自然就可以找到相应客户的订单数量了。

类似的思想，还可以以上述第一条SQL作为基干。我们知道GROUP BY可以依据cust_id进行分组：
```sql
SELECT cust_id, COUNT(*) AS order_count FROM orders GROUP BY cust_id;
```
这其实是遍历了每个组。而我们现在要知道的不是组对应的客户的id而是客户名，类似的，依据cust_id作为桥梁，可以建立计算字段来从customers表中获取信息：
```sql
SELECT
       (SELECT cust_name FROM customers WHERE orders.cust_id = customers.cust_id) AS name,
       COUNT(*) AS count
FROM orders GROUP BY cust_id;
```
当然需要注意的是，因为这种方案以orders表作为基干，因此那些没有一笔订单的客户，没有留任何信息在orders表中，因此也就无从知晓了。
根据具体情况，还是要具体来决定如何设计SQL语句。

