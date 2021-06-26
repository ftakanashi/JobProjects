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

# 检索：联结表
通过外键，可以使两个表之间产生关联。这种关联好处多多（减少重复数据，需要修改数据时一次性修改即可等）。

上面提到过通过子查询来检索出分别位于不同表内的信息。但是子查询本质上也是一个SELECT语句，因此有多个SELECT出现。
如果使用联结表的表达， 则可以在一个SELECT语句内就搞定。

## 等值联结
```sql
SELECT vend_name, prod_name, prod_price FROM vendors, products WHERE vendors.vend_id = products.vend_id;
```
联结不一定需要显示地出现JOIN关键字。比如上面这个SQL，通过外键的`vend_id`以及通过表名来完全限定列名之后，就可以得到想要的结果。

这是因为FROM关键字后面跟了两个表。而SQL的默认行为，是会遍历上面两个表的笛卡尔积。比如原数据中两个表的记录数分别是6和14。
在没有WHERE子句做限定的情况下，总共可以返回出`6*14=84`行数据。
在通过WHERE子句进行限定过滤之后，得到了正确的结果。

对这种写法，记得一定要写WHERE子句，否则一个单纯的笛卡尔积结果没有任何意义。

这种等值联结属于内部联结（Inner Join）的一种。如果显式地使用内部联结语法，则上述SQL可以改写为
```sql
SELECT vend_name, prod_name, prod_price 
FROM vendors INNER JOIN products p ON vendors.vend_id = p.vend_id;
```
显式内联结SQL的INNER JOIN关键字显式指出两个表之间要做笛卡尔积的关系，而后的ON条件则指出了从笛卡尔积中的过滤条件。

### 联结多个表
上面的SQL联结了两个表，也可以联结更多的表：
```sql
SELECT vend_name, prod_name, prod_price, quantity FROM vendors, products, orderitems
WHERE vendors.vend_id = products.vend_id AND products.prod_id = orderitems.prod_id AND order_num = 20005;
```
这条SQL，联结了三个表。因此首先获得了三个表的三元笛卡尔积。然后再看WHERE子句的限定条件。
要求`vend_id`一致且`prod_id`一致，此时相当于是找出了每笔订单中的每个产品，其供应商的名称、产品名称、产品价格以及订购量。
最后追加`order_num=20005`，限定在一笔订单。于是我们就知道了这笔订单的详情（供应商名称、产品名称/价格/订购量）。

按照上述思路，继续拓展思考一下。
如果我们想要知道每笔订单需要付给每个供应商多少钱该怎么办？
显然，需要的信息涉及到的表还是上面那三张。同时，统计信息的粒度是每笔订单的每个供应商，因此可以想象需要加一个`GROUP BY order_num, vend_id`。
由于orderitems表是以商品为粒度的，因此在选择列的时候可以用SUM将各个商品的总价选择出来，即`SUM(quantity * item_price)`。

综上，答案是
```sql
SELECT order_num, vend_name, SUM(quantity * item_price) as total FROM vendors, products, orderitems
WHERE vendors.vend_id=products.vend_id AND products.prod_id=orderitems.prod_id
GROUP BY order_num, vendors.vend_id;
```
注意最后的`vend_id`一定带上表名，否则vendors和products中都有同名字段，会混淆。

## 自联结
除了上面说过的内部联结，还有其他各类联结。这里先来看自联结。

来看下面这条SQL
```sql
SELECT p1.prod_id, p1.prod_name FROM products p1, products p2
WHERE p1.vend_id=p2.vend_id AND p2.prod_id='DTNTR';
```
这里通过对表的别名设置，实现了products表的自联结。
所谓自联结，就是需要基于一个表内的数据对表自身进行进一步搜索的情况。
上面这条SQL实现的，其实是找出DTNTR这个产品的供应商 提供的所有产品。

因为自联结也是一种联结，原理自然还是笛卡尔积。只不过这次是自己和自己做笛卡尔积。
然后一个WHERE子句对这个笛卡尔积再做一个过滤。条件很简单，就不多说了。

另一种通过子查询实现的办法是
```sql
SELECT prod_id, prod_name FROM products WHERE vend_id=(
    SELECT vend_id FROM products WHERE prod_id='DTNTR'
);
```
子查询的办法更好理解，但是需要认识到这两种方法大多数情况下自联结的写法效率更高。

## 外部联结
之前说过内部联结。比如下面这条
```sql
SELECT c.cust_name, o.order_num FROM 
customers c INNER JOIN orders o ON c.cust_id=o.cust_id;
```
我们知道这条SQL，会从订单的视角，展示每个客户的名称以及其对应的订单号。
但是这里面有个问题，就是可能会存在一些没有下过一笔订单的客户。因为这条SQL以订单为视角，这些客户无法在结果中有所显示。
但是有些时候，我们希望他们显示出来，当然订单号这一列可以填充为NULL。
此时就该用到外联结:
```sql
SELECT c.cust_name, o.order_num FROM customers c
    LEFT JOIN orders o ON c.cust_id=o.cust_id;
```
上面这条SQL的输出，就会比之前内联结的输出多一行`|  Mouse House  |  NULL  |`。

注意到外联结具有方向性，通过关键字LEFT或者RIGHT指出。
这个方向，以LEFT为例，当写出`a LEFT JOIN b`时，说明左边的表a中每一行都会在最终结果中出现。

在上面SQL里，如果将LEFT改成RIGHT，则是反过来，说明希望orders表中每一行都出现在最终结果中。因为orders表的定义时就注册了外键到`customers.cust_id`，
所以orders中每一行的cust_id必然都不是NULL，这么一来，RIGHT JOIN的效果其实就和INNER JOIN一样了。

另一方面，因为方向性是相对的，如果将customers和orders在FROM后面互换位置，再将左连接换成右联结的话，那么效果也会和最开始一样。

最后，一个小问题将聚合函数和外联结一起应用：如何统计每个客户共有几笔订单（包括没有下订单的客户）。
答案：
```sql
SELECT c.cust_name, c.cust_id, COUNT(o.order_num) as order_count
FROM customers c LEFT JOIN orders o ON c.cust_id=o.cust_id
GROUP BY c.cust_id;
```
在不使用COUNT和GROUP BY时，这就是一个简单的外联结，可以将每个客户的名称和id，以及他们的订单号分列出来。对于无订单客户，订单号的值是NULL。
接下来一个`GROUP BY cust_id`之后，数据按客户id分组。分组完了之后COUNT即可。
注意这里因为没下订单的客户，这个值应该是0，所以COUNT不能是`COUNT(*)`而是不计入NULL值的`COUNT(c.order_num)`。

# 检索：组合查询
针对一句SELECT语句会返回一些行作为结果。将这个结果视作是一个结果集，组合查询就是通过集合操作将多个SELECT语句的结果集进行集合运算的操作。

需要注意在组合查询中的各个SQL，可以检索同一张表，也可以检索不同的表而组合。

## UNION
顾名思义，UNION是取并集。
语法方面，UNION等关键字只要放在两个SELECT中间即可。因此可能会有类似下面这种SQL：
```sql
SELECT vend_id, prod_id FROM products WHERE vend_id IN (1001, 1002)
UNION
SELECT vend_id, prod_id FROM products WHERE prod_price <= 5;
```
显然如上的UNION操作完全可以用WHERE子句中的一个OR条件代替。

UNION操作还有一些规则。比如要求各条SQL选取出的列(包括表达式和聚集函数)应该相同，但SQL中这些列可以不统一顺序。
考虑到不同SELECT语句可能检索不同的表，同名的列类型可能不同，此时UNION还要求通过DBMS这些类型之间可以自动转换。

UNION会自动去重。如果想要保留去重前的结果，则需要将关键字变成UNION ALL。

UNION操作的最后可以加上ORDER BY子句进行排序。
这种SQL看上去ORDER BY是从属与最后一个SELECT语句的，但是实际上因为有UNION，ORDER BY就会修饰UNION。

# 检索：全文本搜索
在说全文本搜索之前，应当确认并非所有MySQL引擎都支持这个功能。常用的InnoDB就不支持，而MyISAM支持。
顺便一提，引擎可以以表为粒度进行设置。通过`SHOW CREATE TABLE xxx;`查看建表语句，其中可能就会有指定表的引擎。

全文本搜索提供比通配符匹配 或者 正则匹配更加高效的文本搜索方式，它还依赖于被搜索列的索引，因此在建表的时候需要通过FULLTEXT子句声明某列需要去按文本搜索。
关于这点，在CREATE语句中继续详细讲。

## 一般全文本搜索
全文本搜索主要用到`Match()`和`Against()`两个函数。
大概用法如下：
```sql
SELECT prod_id, note_text FROM productnotes 
WHERE Match(note_text) Against('rabbit');
```
如上，Match指定一个待搜索的列，Against则是指定搜索的关键词。
注意，全文本搜索在默认情况下不辨别大小写。

以上功能，其实可以用`WHERE note_text LIKE '%rabbit%'`子句实现。但是观察一下两种表达方式的输出可以发现，
输出结果有两行，但是两行顺序是不一样的。
换言之，全文本搜索对输出顺序已经自动排序了。这也是全文本搜索的好处。

两行结果中，一行的关键词rabbit位于第三个单词，另一个则在很后面。
此时，全文本搜索认为前者比后者优先级更高，因此结果排序中，前者高于后者。

事实上`Match(note_text) Against('rabbit')`这部分本身就是一个计算字段，其提供了一个文本的分数。分数越高则匹配度越高。按照匹配度的降序输出结果。
所以可以通过如下SQL来查询各种文本的匹配度
```sql
SELECT prod_id, note_text, Match(note_text) Against('rabbit') AS rank FROM productnotes;
```

## 扩展全文本搜索
看下面这个句子
```sql
SELECT note_text FROM productnotes WHERE Match(note_text) Against('anvils' WITH QUERY EXPANSION);
```
与一般的全文本搜索相比，Against内部出现了WITH QUERY EXPANSION的追加。
这部分SQL是指出了使用扩展全文本搜索。

在没有扩展时，运行SQL可以看到，返回了唯一一条文本中带有anvils的行。
而扩展之后，会返回7行。除了第一行结果外，你会发现其他行都没有anvils这个词。

其实，扩展全文本搜索，第二行虽然没有anvils这个词，但是有第一行中存在的recommend, customers等词，于是第二行也被视作相关结果返回了。
同理，第三行仍然没有anvils出现，但是也有recommend和customers。但和第二行相比，这两个词互相之间距离更加远，因此优先级也比第二行低一点。
以此类推。
换言之，扩展全文本搜索可以比较智能地搜出好多相关的行，即使行内并没有指定的关键字。

## 布尔全文本搜索
>待补充，这次先不看了


# 插入数据
以上，我们全部都在看检索数据（SELECT语句）的相关内容。
增删查改，现在来看增，即插入数据的做法。
插入数据主要用`INSERT`语句。如：
```sql
INSERT INTO customers(cust_id, cust_name, cust_address, cust_city, cust_state, cust_zip, cust_country, cust_contact, cust_email)
VALUES(NULL, 'Pep E. LaPew', '100 Main Street', 'Los Angeles', 'CA', '90046', 'USA', NULL, NULL);
```
为了防止数据在插入的时候就出问题，编写INSERT语句的时候，应当尽量写明所有列名。
对于一些有默认值或者允许NULL值的列，也可以不写明列名。

相比于查，增删改操作是十分耗时的，因为需要更新索引。因此，当有大量查询和少量增删改操作同时发来时，如果优先处理增删改操作，那么可能会引起整体性能的下降。
从这方面考虑，可以再INSERT和INTO中间加上LOW_PRIORITY，即`INSERT LOW_PRIORITY INTO`来主动降低其优先级，保证整体性能的快速。

## 插入多行
```sql
INSERT INTO table (field0, field1, ...)
VALUES (v00, v01, ...), (v10, v11, ...), (v20, v21, ...);
```

## 插入检索结果数据
插入语句的一个比较实用的功能，是可以将某SELECT语句的检索结果插入到表中。
这种操作的应用场景很多，比如我现在想把表中所有数据都转移到一张新表里的时候。

这种操作关键字，自然是用`INSERT`和`SELECT`了。语法也很好理解：
```sql
INSERT INTO cust_new(cust_id, cust_name, cust_address, cust_city, cust_state)
SELECT cust_id, cust_name, cust_address, cust_city, cust_state FROM customers WHERE cust_id != 1001;
```
上面的SQL中，INSERT到新表的列名恰好和SELECT旧表的列名，从名称到顺序都完全一致。
但是实际上，`INSERT SELECT`语句中，只关注顺序（因为毕竟涉及了两个表，列名可能不完全一样）。
换言之，数据库只会将后面SELECT语句选出来的数据傻傻地以同样的顺序嵌入前面的INSERT语句定义的字段顺序上。

# 更新 & 删除数据
## 更新数据
更新用到的当然就是UPDATE了。
千万千万注意UPDATE时一定要带上WHERE条件，否则很容易就更新表中所有行了。

基本句式例子如下：
```sql
UPDATE customers SET cust_email='elemer@fudd.com',
                     cust_name='The Fudds'
WHERE cust_id=10005;
```

UPDATE操作的对象可能会是多个行。如果在更新多个行的过程中，更新一个行时发生错误的话会回滚整个UPDATE操作。
在UPDATE后加上关键字IGNORE就可以忽视错误行，更新无影响的行。

## 删除数据
删除当然用DELETE。
和UPDATE一样，必须必须带有WHERE条件，否则就删除整张表了。

基本句式例子：
```sql
DELETE FROM customers WHERE cust_id=10006;
```
DELETE只能删除一整行。如果想要删除一行中的某些列，真正意义上的删除是做不到的，但是可以通过UPDATE将这列的值设置为NULL。


# 表的操作
以上所有操作都是在表内行的粒度进行的操作。在表这个层面，也可以做相关的增删改操作。

## 创建表
创建表的核心关键字是CREATE TABLE。
一个创建表的例子，如customers表：
```sql
CREATE TABLE IF NOT EXISTS customers
(
  cust_id      int       NOT NULL AUTO_INCREMENT,
  cust_name    char(50)  NOT NULL ,
  cust_address char(50)  NULL ,
  cust_city    char(50)  NULL ,
  cust_state   char(5)   NULL ,
  cust_zip     char(10)  NULL ,
  cust_country char(50)  NULL DEFAULT 'USA',
  cust_contact char(50)  NULL ,
  cust_email   char(255) NULL ,
  PRIMARY KEY (cust_id)
) ENGINE=InnoDB;
```

建表语句的各种要素都一目了然，下面挑几个地方说明一下。

#### 关于AUTO_INCREMENT。
其大体的功能我们都知道，就是可以维护一个自动自增1的ID值。这个值通常也是被指定为主键的。
同时，一个表至多只能有一个字段是AUTO_INCREMENT的。

此外，指定一个字段为AUTO_INCREMENT之后也并不影响通过手动的方式指定这个字段的值。
且mysql会维护这个字段所经历过的最大值（无论是自增得到的还是你手动插入、更新得到的）。
下一个自增1的值，就是这个最大值+1。

#### 关于DEFAULT
DEFAULT的意义是指定字段的默认值。而在MySQL中，默认值必须是常量而不能是一个函数。
这其实也是MySQL方言的一个特征。

#### 关于引擎
MySQL内置了很多引擎。可以根据不同引擎的不同性质和特点，可以根据不同的需要来选择。

比如上面提到过的MyISAM和InnoDB两种引擎。这两种引擎最基本的一个区分点就是：
- MyISAM整体性能更好，并支持全文本搜索但InnoDB不行
- InnoDB支持事务但MyISAM不行

除了这两个意外，还有一个引擎叫MEMORY。其功能特点基本和MyISAM一样，但是其将数据存储在内存而非磁盘上，因此访问很高效。

此外还应该注意一点，外键不能跨引擎相关联。

## 更新表结构
更新表结构使用ALTER TABLE关键字操作。

当表中存在大量数据时，更新表可能会引起不必要的麻烦。因此在数据库表的设计阶段就应该尽量考虑周到，从而避免后续更新表的操作。

更新表结构可以细分成更多具体的操作。
比如添加列：
```sql 
ALTER TABLE vendors ADD vend_phone char(20);
```
比如删除列
```sql
ALTER TABLE vendors DROP COLUMN vend_phone;
```

除了上述两个外，最常用的还是定义外键，比如：
```sql
ALTER TABLE orderitems
ADD CONSTRAINT fk_orderitems_orders
FOREIGN KEY (order_num) REFERENCES orders(order_num);
```
语法规则是，如果将表TableA的a字段通过外键连到表TableB的主键b字段的话：
```text
ALTER TABLE TableA
ADD CONSTRAINT fk_TableA_TableB
FOREIGN KEY (a) REFERENCES TableB(b);
```

构建外键连接时要严格注意条件。比如当前TableA.a的某个值不是TableB.b的任意一个值时，上述ALTER TABLE操作会报错。

## 删除表
删除表指将整个表（包括其数据结构定义等）全部删除。用如下语句进行。
```sql
DROP TABLE IF EXISTS xxx;
```
删除表没有确认，也无法撤销，要谨慎操作。

与删除表相关的，是清空表。只清空表中数据，保留表本身的数据结构定义以及其他。
清空表使用的是TRUNCATE TABLE语句。

## 重命名表
一句话：
```sql
RENAME TABLE old_name TO new_name;
```

# 视图
前面联结的章节中提到过，可以通过多个表以及表间外键关系的互相相等来联结多个表比如：
```sql
SELECT v.vend_name, p.prod_name, c.cust_name
FROM vendors v, products p, orders o, orderitems oi, customers c
WHERE c.cust_id=o.cust_id AND o.order_num=oi.order_num AND oi.prod_id=p.prod_id AND v.vend_id=p.vend_id;
```
就是一个很复杂的联通了五张表的SQL。这个SQL想要获取到的结果是供应商名称、商品名称和客户名称之间的对应。

再比如，
```sql
SELECT cust_name, cust_contact
FROM customers, orders, orderitems
WHERE customers.cust_id=orders.cust_id AND orderitems.order_num=orders.order_num AND prod_id='TNT2';
```
很明显，这条SQL企图通过一个`prod_id`来找到所有订购了这个商品的客户的名称以及联系人。

在示例数据的场景中，相信以商品名称或者商品ID来搜索客户联系人的操作一定非常常用。但是如此常用的一个操作，居然要这么长一个SQL。
在不能改变表结构的情况下，这个略显得有些麻烦了。
这是就可以使用视图。

视图表观上是一个表。比如上面这个串联三个表的SQL，试想如果存在一个表productscustomers，直接将`prod_id`和`cust_name`关联起来，不通过
任何订单信息作为跳板，那就很方便了：
```sql
SELECT cust_name, cust_contact FROM productscustomers WHERE prod_id='TNT2';
```
虽然数据库中实际上不存在这张表，但我们可以通过视图将上面串联三表的SQL等价为一个虚拟的表。

视图本身不包含任何数据，可以将其视为一个已经被封装好的函数。
外部使用者可以调用他，但是不必要知道他内部是如何实现的。
当实际表中的数据发生了变化，那么通过调用视图得到的内容当然也会发生变化。

### 为什么使用视图
第一，重用复杂的SQL语句。
第二，通过将原表隐藏，将视图暴露给用户的方式，使得用户只能见到一部分数据，即权限管理。
第三，视图可以返回与底层格式与表示不同的数据

### 视图还有哪些性质
- 视图必须唯一命名
- 视图创建数目无限制
- 视图可以嵌套。即视图外面包视图
- 如果视图的定义中带有ORDER BY而外部调用视图时也有ORDER BY，并且两者冲突时，外部的ORDER BY优先级更高
- 视图不能索引
- 视图可以和表一起使用，比如联结

## 视图操作
因为视图就是个虚拟表，所以表层面的增删改查语句语法差不多。
比如
```sql
CREATE VIEW view_name AS
SELECT ... # 复杂SQL
```
而也有
```sql
SHOW CREATE VIEW view_name;
DROP VIEW view_name;
CREATE OR REPLACE VIEW view_name xxx    # 相当于CREATE TABLE IF NOT EXISTS
```

下面是一个创建视图的实例：
```sql
CREATE VIEW productscustomers AS
    SELECT c.cust_name, c.cust_contact, oi.prod_id
    FROM customers c, orders o, orderitems oi
    WHERE c.cust_id=o.cust_id AND oi.order_num=o.order_num;
```
运行完成后数据库中就存在了一个叫productscustomers的视图实例。
视图维护的，就是上面这条定义SQL中检索到的数据。

上述创建方法还是最一般的情况。
除此之外还可以设置一些计算字段来固化一些常用的信息。
比如之前我们在说字符串处理函数的时候提到过对于供应商可以有：
```sql
SELECT Concat(RTrim(vend_name), '(', RTrim(vend_country), ')') AS vend_title
FROM vendors ORDER BY vend_name;
```
如果在其他场合中，经常要用到上述定义的如`ACME (USA)`这样格式的供应商信息，每次都写这么大一串很累。可以定义这样一个视图：
```sql
CREATE VIEW vendorlocations AS
    SELECT vend_id, Concat(RTrim(vend_name), '(', RTrim(vend_country), ')') AS vend_title
    FROM vendors ORDER BY vend_name;
```
这样，以后需要这类特定格式的输出时只需要从`vendorlocations`中获取就行了。

其他的计算字段，比如四则运算字段、聚合字段等，都可以通过同样的原理进行通过视图的固化，避免每次都写繁琐的SQL。

当然需要记住，视图只是一个封装好的函数，所以封装进去的SQL每次都还是要被执行的。
因此并不会带来性能的提升。相反，如果嵌套的视图过多，还有可能带来性能的大幅度下降。


以上创建的所有视图，外部使用者都通过SELECT对其进行调用。
即视图主要用于数据检索的方便。

这也是视图最初的目的，应当尽量遵从这种设计理念。
虽然语法上允许调用视图时使用写操作（如INSERT, UPDATE和DELETE），一般情况下这些操作会被反馈到基表中去。

但是如果视图定义中带有一些表达使得MySQL无法确定到底怎么修改基表时，通常就不允许修改。
上述表达可能有下面几种：
```text
分组
聚合函数
联结
子查询
并
```

可以看到稍微复杂点的SQL都会带有这些东西，换言之，大多数视图都是不允许进行写操作的。
这也印证了其设计理念，即尽量只用于数据检索（读操作）。

# 存储过程
如果说视图对应了系统中的单条命令，那么存储过程就对应了批处理或者脚本之类的概念。
一个存储过程是多条SQL的集合，并且这多条SQL之间通常都具有逻辑关系，可能对执行顺序以及条件分支等有要求。

和视图一样，使用存储过程是为了化繁为简，同时降低犯错误的可能。
另外也有一些安全方面的考虑，这点和使用视图的想法也是一样的。

## 执行存储过程
先不看如何定义，先来看看如何使用存储过程吧。
语法格式是这样的：
```sql
CALL productpricing(@pricelow, @pricehigh, @priceaverage);
```
通过CALL关键字提示我们现在正在调用存储过程。
而后面的其实和函数定义差不多，函数名后面小括号中带了三个参数。注意参数前用@符号。

## 定义存储过程
我们定义一个简单的存储过程：
```sql
CREATE PROCEDURE productpricing()
BEGIN
    SELECT Avg(prod_price) AS priceaverage FROM products;
END;
```
和函数定义类似，`CREATE PROCEDURE 存储过程名(参数)`是定义的起始。
随后用BEGIN和END作为存储过程体的标识，中间写具体的SQL。

定义本身不返回任何东西。
定义完成后，可通过`CALL productpricing();`来调用。
因为定义中这个过程就是一个简单的SELECT返回数据，因此调用的结果也是相同的数据返回。

## 删除存储过程
存储过程相当于是一个定义在服务端，并开放客户端使用的函数。
因此，存储过程不与某个用户或者某个用户会话相关联，而直接和服务相关联。
所以有权限的用户也可以在服务端将某个存储过程删除。

删除用语句
```sql
DROP PROCEDURE IF EXISTS productpricing;
```

当前数据库中有哪些存储过程，这些存储过程又都具有什么性质等，
这些可以通过`SHOW PROCEDURE STATUS;`查看。
类似表，`SHOW CREATE PROCEDURE xxx;`可查看定义语句。

## 更复杂的存储过程

### 带有输出参数的存储过程
上面定义了一个很简单的存储过程。
但是实际应用中，很少有这种简单一句SELECT的。
按照实践的经验，一般存储过程都不显示结果。通常其都会将结果返回到指定的变量中。

比如下面这个改良版：
```sql
CREATE PROCEDURE productpricing(
    OUT pl DECIMAL(8, 2),
    OUT ph DECIMAL(8, 2),
    OUT pa DECIMAL(8, 2)
)
BEGIN
    SELECT Min(prod_price) INTO pl FROM products;
    SELECT Max(prod_price) INTO ph FROM products;
    SELECT Avg(prod_price) INTO pa FROM products;
END;
```
在头部分，定义了存储过程有三个"输出"（以OUT关键字标明）。
每个输出都是8位有效数字，小数点后两位有效数字的浮点数。参数名分别是pl,ph,pa。
这三个参数名也是在存储过程体中被用到的。通过INTO关键字在存储过程体中或得到的结果保存在其中。

注意上述sql还只是存储过程的定义。
下一步，需要调用它。方法我们之前也讲过：
```sql
CALL PROCEDURE productpricing(@price_low, @price_high, @price_avg);
```
注意这里因为定义中规定了这个过程会有三个输出变量，因此调用时这里就需要安排三个实际的变量来对应。
实际变量前面用@符号表示。而这些变量名和上面定义的参数名，关系就像函数的实际参数和形式参数。

运行上述调用sql后你会发现并没有输出。因为定义中没有直接输出的代码。
相反，我们使用如下sql查看结果：
```sql
SELECT @price_low, @price_high, @price_avg;
```

### 带有输入参数的存储过程
定义过程时，除了用OUT声明过程返回的参数，还可以有IN声明过程接收的参数，比如：
```sql
CREATE PROCEDURE ordertotal(
    IN onumber INT,
    OUT ototal DECIMAL(8, 2)
)
BEGIN
    SELECT Sum(item_price * quantity) FROM orderitems WHERE order_num=onumber INTO ototal;
END
```

调用过程与查看结果：
```sql
CALL ordertotal(20005, @total);
SELECT @total;
```

显然，IN参数要求外部调用者在调用过程中，提供一个具体的值给存储过程使用。
具体来说，这里需要提供一个订单号，从而让存储过程的WHERE条件有具体的限制性。

### IF/ELSE条件分支结构
看这个SQL：
```sql
-- Name: ordertotal
-- Parameters: onumber = 订单号
--             taxable = 是否计入税
--             ototal = 最终输出的总价格
CREATE PROCEDURE ordertotal(
    IN onumber INT,
    IN taxable BOOLEAN,
    OUT ototal DECIMAL(8, 2)
) COMMENT 'Obtain order total, optionally adding tax'
BEGIN
    -- 声明局部变量
    DECLARE total DECIMAL(8, 2);
    DECLARE taxrate INT DEFAULT 6;

    -- 计算无税时某个订单的总价格
    SELECT Sum(item_price * quantity) FROM orderitems WHERE order_num = onumber INTO total;

    -- 如果要收税
    IF taxable THEN
        SELECT total + (total / 100 * taxrate) INTO total;
    END IF;

    -- 将计算结果保存到输出变量中
    SELECT total INTO ototal;
END;
```
这里比上面多了如下几个要素。

首先带有注释。
其次存储过程定义头部带有COMMENT作为这个存储过程的解释说明。这部分说明可以通过`SHOW PROCEDURE STATUS`看到。

然后最关键的，过程体中带有IF/ELSE条件分支。
除了简单的IF THEN和END IF，中间也可以加上`ELSEIF THEN`以及`ELSE`等经典条件分支的语法。
这些语法的功能一目了然，这里就不多说了。

# 游标
之前所有运行过的所有SQL，返回的都是一个零到多行的结果集。
这些结果集都是"一股脑"地返回出来，我们没有能力对其做行层级的操作（逐行分析或者修改等）。

而游标功能，就是把这一块拼图给补上了。

注意，MySQL中游标只支持用于存储过程返回的结果，这也是为什么游标这章放在了存储过程后面。

从无到有使用一个游标的过程是这样的：
第一步，创建（定义）游标。这本质上是定义一个SELECT语句，并且并未执行任何检索操作。
第二步，打开游标。
第三步，使用游标。即执行第一步中定义的SELECT语句。
第四步，执行完成后游标内会填有数据，将其从中取出。
第五步，关闭游标。

## 创建游标
一个创建游标的例子是像下面这样的：
```sql
CREATE PROCEDURE processorders()
BEGIN
    DECLARE ordernumbers CURSOR FOR
    SELECT order_num FROM orders;
END
```
上面，`DECLARE xxx CURSOR`是定义有游标的语法。而`FOR SELECT语句`是将某个SELECT语句与游标关联起来。

## 打开、关闭游标
上面创建了一个游标。之前提到过，游标只能在存储过程内生效，换言之，我们上面定义了一个后，存储过程随之结束，
因此其实并未使用这个游标。

使用游标前，要打开游标。同理，用完后记得关掉游标。这两个过程：
```sql
CREATE PROCEDURE processorders()
BEGIN
    DECLARE ordernumbers CURSOR FOR 
    SELECT order_num FROM orders;

    -- 打开
    OPEN ordernumbers;

    -- 用游标做些事

    -- 关闭
    CLOSE ordernumbers;
END
```
当然，如果忘记关闭游标，在存储过程执行到END的时候，游标会被引擎自动关闭。

## 使用游标
上面知道了如何打开关闭游标，但是实际上还只是打开关闭它，还是没有真正用到它。
使用游标，或者说从游标中获取当前数据，使用关键字FETCH如：
```sql
CREATE PROCEDURE processorders()
BEGIN
    DECLARE o INT;
    DECLARE ordernumbers CURSOR FOR SELECT order_num FROM orders;

    -- 打开游标
    OPEN ordernumbers;

    FETCH ordernumbers INTO o;
    SELECT o;

    -- 关闭游标
    CLOSE ordernumbers;
END;
```
这里，打开游标后使用FETCH将游标获取到的当前一行数据放进变量o。
然后，将这个o通过SELECT打印出来。

在定义完成后，`CALL`一下，结果就会返回20005这个数据。这也是游标（其定义是`SELECT order_num FROM orders`）
获取到的第一行，即定义SQL执行获得的第一行数据。

当然只获取第一行数据是没有什么意义的。
就游标来说通常我们希望有一个循环，来依次对游标获取到的数据进行逐行处理。
在存储过程中使用循环结构，通常可以通过REPEAT关键字配合CONTINUE句柄完成。
整体代码如下：
```sql
CREATE PROCEDURE processorders()
BEGIN
    DECLARE o INT;
    DECLARE done BOOLEAN DEFAULT 0;
    DECLARE t DECIMAL(8, 2);

    DECLARE ordernumbers CURSOR FOR SELECT order_num FROM orders;

    DECLARE CONTINUE HANDLER FOR SQLSTATE '02000' SET done=1;

    CREATE TABLE IF NOT EXISTS ordertotals(
        order_num INT,
        total DECIMAL(8, 2)
    );

    OPEN ordernumbers;
    REPEAT
        FETCH ordernumbers INTO o;
        CALL ordertotal(o, 1, t);
        INSERT INTO ordertotals VALUES(o, t);
    UNTIL done END REPEAT;
    CLOSE ordernumbers;
END;
```
在这个过程中，我们首先声明了一些辅助变量、一个游标。此外为了配合REPEAT，额外声明了一个CONTINUE句柄。
这个句柄的作用是，当这个过程中的某个SQL执行状态为指定状态时（02000，表示某个SQL执行结果是未找到，由于没有更多的行让REPEAT重复，就会引发这个状态），
执行特定动作（SET done=1;）。注意done是个BOOLEAN，所以相等于是置True。

顺便一提，整个声明区域的语句顺序是有严格限制的。
按种类，必须先声明普通变量，再声明游标，再声明句柄。如果顺序错乱，会报错。

接下来是一个建表语句。建立了一张新的表用来保存接下来循环处理的结果。

接着进入循环，其中`CALL ordertotal`中的过程是之前定义过的，可以根据输入来计算某一笔订单带税总价的那个。
注意SQL没有赋值语句，存储过程也不存在返回，因此比较别扭，需要一个中间的辅助变量t来保存ordertotal的计算结果，再将其用于下面的插入语句中。
这个t也在最开始就声明完成了。

定义完成后，执行以下：
```sql
CALL processorders();
```
这个SQL稍微慢一点，主要是因为涉及到了建表等操作。
运行完成后，就可以通过下面的语句，获取到每一个订单的和其带税总价的信息了：
```sql
SELECT * FROM ordertotals;
```


以上，是对游标的一个非常简单的介绍，要想获得更详细的信息，还是去网上找完整的文档吧。

# 触发器
触发器，顾名思义，就是数据库执行某个操作的时候，能够附带着一起自动运行一些操作的机制。

在MySQL中，支持触发器定义在DELETE, INSERT, UPDATE或者这三类操作上。
其他操作不支持定义触发器。

而触发器被触发后进行的自动的操作，我们称之为触发器自身的操作。
这部分操作可以是一个或者多个增删查改语句，但是注意MySQL不支持在这部分操作中使用存储过程。

## 创建触发器
创建触发器需要给出以下要素：
- 一个唯一的触发器名
- 触发器关联的表
- 触发器定义在什么操作上
- 触发器何时执行（定义在的语句执行前还是执行后）

下面是个简单的例子：

>注意，书本上没有最后的INTO操作。这是因为在MySQL5以后，不再支持触发器返回一个集合结果了。
>
>作为一个灵活变通的办法，就是将原先要选出来的结果赋值到一个变量中，后续查看这个变量值的变化了。

```sql
CREATE TRIGGER newproduct AFTER INSERT ON products
FOR EACH ROW SELECT 'Product added' INTO @ee;
```
第一行，其实就确定了上面提到的四个要素。
触发器名：newproduct
关联的表: products
定义在什么操作上: INSERT
何时: AFTER

而第二行则是给出了触发器自己的动作是什么。
FOR EACH ROW指出的是粒度，即针对每行发生INSERT（即新插入一行）时执行动作。
最后的`SELECT 'Product added'`是被执行的动作。这里就好比是简单print一串信息。

综上，这个触发器定义后，之后每次往products中插入一行新数据时，控制台都会输出Product added这条信息。

>注意目前触发器只支持定义在表上，而不能定义在视图上。
>
>另外，一个表的一个操作的一个时间点只能定义一个触发器。因为有三种操作和两个时间点，所以一个表最多可以定义6个触发器。

注意到，除了AFTER，还可以定义BEFORE触发器。
此时触发器操作会在主操作之前发生。若这个操作失败了，那么主操作也不会被执行。
同理，如果主操作失败了，那么AFTER触发器也不会被执行。

## 删除触发器
```sql
DROP TRIGGER newproduct;
```
触发器不能更新or覆盖，因此要修改只能先删除再新建。

## 使用触发器
下面按照触发器定义在不同操作上作为分类依据，讲讲各种触发器。

### INSERT触发器
INSERT触发器，其本身操作的代码中，可以有一个名为NEW的固定变量。这个变量指代新插入的一行。

如果是BEFORE INSERT触发器，显然编辑这个NEW的相关值，可以做到在插入前最后修正一次赋值。
如：
```sql
CREATE TRIGGER neworder AFTER INSERT ON orders
FOR EACH ROW SELECT NEW.order_num INTO @ee;
```
上面这个SQL创立的触发器，可以将每次插入一条新订单信息时，该订单的订单号返回出来。
由于订单号是`AUTO_INCREMENT`列，因此这个触发器或许很有用。

### DELETE触发器
和INSERT触发器类似，DELETE触发器在其本身操作的代码中可以带有一个名为OLD的固定变量，用于指代即将被删除的那一行。
有所不同的是，OLD的各个属性都是只读的，无法更改。这也是符合逻辑的。如果一行数据将被成功删除，那么修改其数据并没有意义。
如果删除将失败，那么不能修改其原来数据。

在一些自动归档工作中，DELETE触发器可能很有用，例如：
```sql
CREATE TRIGGER deleteorder BEFORE DELETE ON orders
FOR EACH ROW
BEGIN
    INSERT INTO archive_orders(order_num, order_date, cust_id)
    VALUES(OLD.order_num, OLD.order_date, OLD.cust_id);
END;
```
建立后，只要我们有一个归档表`archive_orders`，那么从正表`orders`中每删除一行数据，该条数据就会相当于被移入归档表了。

### UPDATE触发器
类比上面两种触发器，UPDATE的代码中会有一个OLD固定变量，一个NEW固定变量，分别指代更新前和更新后的值。
和之前一样，OLD的各个属性是只读的，而NEW的各个属性可以被修改。
这里，MySQL还规定了BEFORE UPDATE触发器只能访问NEW，而AFTER UPDATE只能访问OLD。

例子：
```sql
CREATE TRIGGER updatevendor ON vendors
FOR EACH ROW SET NEW.vend_state = Upper(NEW.vend_state);
```
这个触发器确保每次更新vendors表的`vend_state`字段时，最终被更新上去的字母都是大写的。


以上就是对触发器的一个简单介绍了。

# 事务处理
事务处理用来维护数据库内数据的完整性和一致性。它保证了成批的MySQL操作要么完全执行，要么完全不执行。
正如之前所说，是否支持事务处理分引擎。InnoDB是一个支持事务的引擎。

讲事务处理之前，先明确几个术语：
- 事务：指一组SQL语句（通常带有UPDATE，DELETE，INSERT等写操作）
- 回退：撤销指定SQL语句的过程
- 提交：将未存储生效的SQL结果写入数据库表
- 保留点：事务处理过程中可设置的临时占位符，相比于回退整个事务，可以只回退到保留点。

## 回退
事务处理最简答的一个作用就是回退已经发生改变的数据，如：
```sql
SELECT * FROM ordertotals;
START TRANSACTION;
DELETE FROM ordertotals;
SELECT * FROM ordertotals;
ROLLBACK;
SELECT * FROM ordertotals;
```
关键字`START TRANSACTION`用来标识一个事务块的开始。
开始之后的相关语句都处于事务块中，直到碰到结束事务块的相关语句如ROLLBACK或者COMMIT之类的。

这里，一共会有三组关于ordertotals中数据的返回。
第一行就是正常返回。接着事务块开始后，我们将ordertotals数据清空了。此后再查看数据返回，当然返回的是空。
再往后，一个rollback，将数据回滚到事务块开始之前。此后再查看数据，又变成了原来有数据的状态。

值得一提的是，ROLLBACK只对INSERT, UPDATE, DELETE语句有效。对SELECT无效（好像回滚SELECT也没什么必要）
对DROP, CREATE等也无效。（这些语句可以出现在事务块中，但其执行的操作不会被回滚）

## 提交
很多时候，我们希望出错回滚，无错则执行。这种想法换一个思路就是，我们在保留原数据的前提下执行操作，
当执行出错时，直接停止操作（此时原数据仍未被改动）。
当执行无措时，才选择将得到的新结果覆盖到原数据上。这个过程就是提交COMMIT做的了。

例子：
```sql
START TRANSACTION;
DELETE FROM orderitems WHERE order_num=20010;
DELETE FROM orders WHERE order_num=20010;
COMMIT;
```
我们知道示例数据中，每一笔订单其实都保存在了`orders`和`orderitems`两个表里。分别维护了这个订单和客户的关系以及订单和产品的关系。

那么，当我们想从系统中删除一笔订单时，势必要删除这两张表中的相关行。
然而如果一条一条执行，当第一条执行完后遇到突发情况使得第二条没能顺利执行，此时就会发生数据不一致。

使用COMMIT机制，则第一条执行完后只是知道要做什么，原数据并未发生改动。
第二条也如此。若两条都执行完，知道我们要怎么做了之后，再去覆盖原数据，则可以保证数据一致性。

如上面回滚中提到的，COMMIT也同时表示了事务块的结束。

另外值得一提，目前为止所有的写操作都被设置了自动提交（autocommit）。
可以通过`SET autocommit=0;`，将这个功能关闭。这样的话没运行一次写操作，后面如果不跟上`COMMIT;`，那么操作不会生效。

## 保留点
很好理解，就是线性事务处理中的存档点。

在事务块中，可以加入`SAVEPOINT xxx;`来声明存档点。
又可以`ROLLBACK TO xxx`来指定回滚到某个存档点。

使用`RELEASE SAVEPOINT`可以手动释放存档点。这样节省空间但无法回滚到被释放的存档点了。

# 字符、本地化相关
对于数据库中的文本，肯定得有相应的字符集去编码。
另外SQL自带排序功能，这又涉及到对于文本数据按照什么依据去排序。这个又叫做"校对"。

当前数据库支持哪些字符集以及哪些校对可以用下面这两个命令查看：
```sql
SHOW CHARACTER SET;
SHOW COLLATION;
```
其中校对的命名是有规律的。首先校对针对某个字符集而言。接着就是排序的具体依据。对于西方语言通常还要考虑大小写，忽视大小写加后缀ci。
于是就有类似于`utf8_unicode_ci`，这个校对的意思就是说，以unicode顺序为依据对utf8字符集排序，同时忽略英文字母大小写。

当前在使用的字符集合校对通常是安装数据库时设置的默认值，这两个值可以通过下面命令看：
```sql
SHOW VARIABLES LIKE 'character%';
SHOW VARIABLES LIKE 'collation%';
```

对字符集合校对的设置通常有很多层级，比如整个服务层级的，数据库层级的，还有之前CREATE TABLE语句中也提到过的表层级的。更有甚者，可以在定义表时
为某个列设置字符集和校对。
一个更加完整的，对一个表设置字符集和校对的语句是这样的：
```sql
CREATE TABLE mytable(
    column1 INT,
    column2 VARCHAR(10)
)DEFAULT CHARACTER SET hebrew
 COLLATE hebrew_general_ci
```

# 安全管理
这章主要是一些mysql数据库管理层面的一些东西。

## 用户相关
首先是查看所有用户的相关信息：
```sql
USE mysql;
SELECT * FROM user;
```
这些信息在mysql数据库的user表中。
运行上述SQL时要先保证当前用户对mysql数据库有读的权限。

接着是创建新用户：
```sql
CREATE USER username IDENTIFIED BY 'p@$$w0rd';
```


重命名用户：
```sql
RENAME USER username_old TO username_new;
```


删除用户：
```sql
DROP USER username;
```
运行上述SQL后直接将用户以及其相关的所有权限记录都删除。


修改用户的密码：
```sql
SET PASSWORD FOR username = Password('new password');
```
注意Password函数是将明文转化为散列值的函数，一定得有。
去掉上述FOR username则是修改自己密码的SQL。

## 权限相关
查看某用户的权限：
```sql
SHOW GRANTS FOR username;
```
这个SQL返回的是，用户的所有权限记录。一条权限记录由三个部分组成。即
- 权限类型
- 对象数据范围
- 权限用户（及其主机）

默认情况下，可能会看到一个`GRANT USAGE ON *.* TO username@'%';`
这里的`USAGE`，对应权限类型。虽说叫USAGE，但其实指的是没有权限。
也就是说当某个用户只有上面这一条grant的时候，实际上这个用户没有读写任何数据的权利。
>书中表28-1给出了常见的各种权限类型。

`*.*`指对象数据范围，即全数据库的全部表。

`username@'%'`表示权限用户及主机，即所有主机上的username用户。注意一个好的创建用户的习惯是带上主机名。如果不带则使用
默认的通配符主机`'%'`。


使用GRANT关键字以及相关SQL可以修改权限，如：
```sql
GRANT SELECT ON crashcourse.* TO username;
```
就是将在crashcourse中所有表的SELECT的权限授予username用户。

GRANT的反操作是REVOKE，使用将上述SQL中的GRANT TO换成REVOKE FROM，SQL就变成了撤销权限的SQL
```sql
REVOKE SELECT ON crashcourse.* FROM username;
```

从上述语法中可以看出，对象的数据范围可以是服务器、数据库、数据库中的某个表这些。
实际上，还可以更加精细到某个特定的列、或者某个特定的存储过程。

# 数据库维护
以前积累的关于数据库维护的相关信息，我都记录在了这篇文章里：
>https://www.cnblogs.com/franknihao/p/7265667.html

## 数据备份
通常在数据库服务器上可以使用mysqldump命令进行数据的备份。这种备份通常是数据库级别的。

mysqldump的原理是将表、视图、存储过程等实体的定义语句，以及表中所有数据的插入语句都以规范SQL的形式导出。
这样，只要在另一个数据库中导入这些SQL，就可以复原出一模一样的数据库了。

## 数据库维护
`ANALYZE TABLE orders;`之类的语句可以检查表键是否正确。

`CHECK TABLE orders;`针对表的许多问题进行检查。

`OPTIMIZE TABLE orders;`当某个表中刚删除大量数据，可以通过这个命令来让引擎回收这个表的空间，优化整体性能。

## 数据库日志
mysql的日志分成错误日志，查询日志，二进制日志，慢查询日志等。
这些日志默认都是不开启记录的。需要手动开启或者启动时，配置文件or命令行带上相关的option。

这里不展开了，需要的时候百度即可。

## 数据库调优及其他
`SHOW PROCESSLIST;`可以查看当前正在运行的所有SQL以及已经建立的和客户端之间的连接。
`KILL`可以强行终止进程。

`EXPLAIN`语句可以让MySQL解释如何执行一条SELECT语句，可以帮助分析性能瓶颈。

`UNION`似乎总是比多个`OR`条件更加快。

建立索引可以有效改善检索的性能，但是对写操作的性能有害。需要权衡。

 