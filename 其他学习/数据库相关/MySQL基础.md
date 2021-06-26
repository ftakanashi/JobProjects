>参考1：https://github.com/Snailclimb/JavaGuide/blob/master/docs/database/MySQL.md
>
>参考2: https://mp.weixin.qq.com/s/IiJYHoAxqTnqW0LfRAh2BQ
>
>索引：https://zhuanlan.zhihu.com/p/352181863

# MySQL基础
MySQL支持很多存储引擎。
可以在终端中键入`show engines;`查看。目前只有InnoDB支持事务，因此用得最广泛。

InnoDB（与老一点的默认引擎MyISAM相比）有以下特点：
- 支持行级锁
- 支持事务（支持事务的commit和rollback）
- 支持外键
- 支持数据库异常崩溃后的安全恢复，此过程依赖于redo log

## 锁机制
InnoDB中默认使用行级锁，但是也可以使用表级锁。
- 表级锁：MySQL中最大粒度的锁，对整张表加锁。加锁速度快，实现简单，消耗少，不会出现死锁。
- 行级锁：MySQL中最小粒度的锁，对一行数据加锁。慢、复杂、多、会死锁。

## 查询缓存
执行查询语句时会先查询缓存，如果缓存中存在结果则直接返回。
MySQL 8.0等新版本中已经移除了这个功能。

注意，这里查看缓存中是否存在结果，必然带有一个判相等的操作。而这个操作实际上是很严格的。
简单来说，要求两个查询不仅仅在字符串层面上一模一样，还要求发出查询的客户端版本、被查询的数据库等等都要完全一致。


