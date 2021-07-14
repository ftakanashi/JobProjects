# 其他

## ORM执行效率（Django或者Flask都是）

> 资料：https://stackoverflow.com/questions/25696120/why-is-django-orm-so-much-slower-than-raw-sql

通常认为，ORM的执行速度比原生的 raw SQL 要慢很多。这通常可以归结为以下几点原因。

- 在数据检索前，ORM需要将你的一长串代码逻辑给转换成一个SQL，这本身就需要耗费一定时间，逻辑越复杂，耗费的时间肯定就越长。更不用说有些复杂逻辑ORM无法生成，或者说要写出符合逻辑的ORM代码不如直接写raw SQL。
- 在数据检索时，注意ORM并没有我们想象的那么智能，很多时候他只负责生成能用的SQL而不是最优的。所以检索时可能ORM的SQL效率不够好。
- 在数据检索后，这也是很明显的一个拖慢ORM的地方。ORM会将检索出来的数据全部都包装成相关类的对象（否则也不会叫ORM了），而这个新建对象的过程会耗费大量时间空间。

话分两头，资料中的回答评论中也有人提到，有人用Django 1.8做过实验，发现优化的不错，基本上不必raw SQL差多少了。当然这种评论毫无价值毕竟没提供数据量等信息。

总体来说，当ORM的效率过于拉胯时，就可以考虑用raw SQL来做。raw SQL一方面可以通过独立地用mysqldb模块建立连接获取数据，另一方面，Django内部其实也维护了这个连接，可以通过`django.db.connection`来调用。
和mysqldb的调用方式一样，需要通过`connection`中的`cursor`属性代表的游标来fetch数据，如：

```python
from django.db import connection
cursor = connection.cursor()
cursor.execute('SELECT * FROM xxx;')
data = cursor.fetchall()
```

