## 题目描述
给你一个二维整数数组 logs ，其中每个 logs[i] = [birthi, deathi] 表示第 i 个人的出生和死亡年份。

年份 x 的 人口 定义为这一年期间活着的人的数目。第 i 个人被计入年份 x 的人口需要满足：x 在闭区间 [birthi, deathi - 1] 内。注意，人不应当计入他们死亡当年的人口中。

返回 人口最多 且 最早 的年份。

示例 1：
```
输入：logs = [[1993,1999],[2000,2010]]
输出：1993
解释：人口最多为 1 ，而 1993 是人口为 1 的最早年份。
```
示例 2：
```
输入：logs = [[1950,1961],[1960,1971],[1970,1981]]
输出：1960
解释： 
人口最多为 2 ，分别出现在 1960 和 1970 。
其中最早年份是 1960 。
```

提示：
```
1 <= logs.length <= 100
1950 <= birthi < deathi <= 2050
```

### 解法 差分数组
用差分数组的思路还是比较明显的。
不过这题的每个区间的端点的绝对值都比较大，必然不能傻傻的直接开数组。

一个可行的办法是将1950到2050这段映射到0到100上。
或者像我一样，用哈希表的形式呈现差分数组。

具体的，首先将`logs`输入中的所有年份都统一放到一个数组中，同时记录其是区间的开始还是结束。
一个方便的做法是将开始定为1，结束定为-1，方便后面处理。
比如`(1950, 1), (1960, -1), (1960, 1) ... `

然后用哈希表将所有数据以差分数组的形式维护起来。
然后顺序遍历哈希表中的所有key，进行差分的总和统计，遍历过程中随时记录最大人口数以及到达最大人口数的年份即可。
注意因为要求人口最多且最早的年份，因此遍历过程中的`max`判断条件应该不包括等号。

以上。