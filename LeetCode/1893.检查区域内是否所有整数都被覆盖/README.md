## 题目描述
给你一个二维整数数组 ranges 和两个整数 left 和 right 。每个 ranges[i] = [starti, endi] 表示一个从 starti 到 endi 的 闭区间 。

如果闭区间 [left, right] 内每个整数都被 ranges 中 至少一个 区间覆盖，那么请你返回 true ，否则返回 false 。

已知区间 ranges[i] = [starti, endi] ，如果整数 x 满足 starti <= x <= endi ，那么我们称整数x 被覆盖了。

示例 1：
```
输入：ranges = [[1,2],[3,4],[5,6]], left = 2, right = 5
输出：true
解释：2 到 5 的每个整数都被覆盖了：
- 2 被第一个区间覆盖。
- 3 和 4 被第二个区间覆盖。
- 5 被第三个区间覆盖。
```
示例 2：
```
输入：ranges = [[1,10],[10,20]], left = 21, right = 21
输出：false
解释：21 没有被任何一个区间覆盖。
```

提示：
```
1 <= ranges.length <= 50
1 <= starti <= endi <= 50
1 <= left <= right <= 50
```

### 解法1 哈希集
因为题目给出了限定条件，所有`start_i`和`end_i`都小于等于50且所有区间数也小于等于50。
总之整体的数据量并不大，所以可以有很多做法。

我第一个想到的就是，既然最多最多就50种数，那么我就先扫描所有range，将被覆盖的数字全部都写入一个哈希集。最后检查left到right间的所有数字是否都在哈希集中即可。

类似的可以用位图法代替哈希集。这里就不多说了。

### 解法2 差分数组
一种新套路，可以用于这类区间覆盖问题。

这个套路的核心在于，构建一个差分数组`diff`。
针对题目给出的每个已经覆盖的区间，将区间头对应位置+=1，区间尾巴后一格对应位置-=1。
这么做，可以将差分数组的值定义为，`diff[0]`到`diff[i]`的前缀和是`nums[i]`被覆盖的区间数。

比如示例1中给出了`[1,2],[3,4],[5,6]`这三个区间，根据这三个区间构建起的`diff`大概长这样：
```text
nums:     0 1 2 3 4 5 6 7  8 ...
diff:     0 1 0 0 0 0 0 -1 0 ...
presum:   0 1 1 1 1 1 1 0  0 ...
```

如果再加一个`[2,5]`区间，那么`diff[2]`变成2而`diff[6]`变成0。转化前缀和后`presum[2]`到`presum[5]`变成2，而`presum[6]`仍然有1。

至此就明白了，只要`left`到`right`间每个数字对应的presum值大于0，就是true，否则false。

这题中，因为可以在遍历的过程中直接求presum值并比较i和`left, right`的大小，因此可以不显式构建presum数组。

另外值得思考的一个问题是`diff`数组的长度是多长。显然为了让每一个可能出现的值都囊括在数组中，`start_i, end_i, left, right`中最大的那个+1的下标要能取到（考虑到+1的下标要-=1）
结合题设，最大的是50，所以最大的下标要能取到51，所以数组初始化成`[0 for _ in range(52)]`。