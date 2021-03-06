## 题目描述
你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字： '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' 。

每个拨轮可以自由旋转：例如把 '9' 变为  '0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。

锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。

列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。

字符串 target 代表可以解锁的数字，你需要给出最小的旋转次数，如果无论如何不能解锁，返回 -1。

示例 1:
```
输入：deadends = ["0201","0101","0102","1212","2002"], target = "0202"
输出：6
解释：
可能的移动序列为 "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202"。
注意 "0000" -> "0001" -> "0002" -> "0102" -> "0202" 这样的序列是不能解锁的，
因为当拨动到 "0102" 时这个锁就会被锁定。
```
示例 2:
```
输入: deadends = ["8888"], target = "0009"
输出：1
解释：
把最后一位反向旋转一次即可 "0000" -> "0009"。
```
示例 3:
```
输入: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
输出：-1
解释：
无法旋转到目标数字且不被锁定。
```
示例 4:
```
输入: deadends = ["0000"], target = "8888"
输出：-1
```

提示：
- 死亡列表 deadends 的长度范围为 [1, 500]。
- 目标数字 target 不会在 deadends 之中。
- 每个 deadends 和 target 中的字符串的数字会在 10,000 个可能的情况 '0000' 到 '9999' 中产生。

### 解法 BFS
典型的DFS/BFS题。只是这题中，由于要求的是最短路径，其实BFS比DFS的效率更高，因为可以不用探索所有状态。

从抽象化的角度来说，其实这道题可以看做是一个简单的四维地图上的探索。

在一般二维地图上，从一个格子出发可以探索的范围是，上下方向和左右方向各自+-1的范围，即总共四种可能。

而这题，由于有四个位数，每个位置都可以+-1，所以总共八种可能。除此之外并无深意。
也就是说，相当于是让你探索在四维地图中从原点0,0,0,0总到目标target坐标的最短路径，地图上的deadends这些点是障碍物。
仅此而已。

下面说说DFS和BFS的区别。在DFS中，虽然可以探索到每一条可能的路径，但是那条最优路径不一定是第一次探索到的那条（和具体的探索方向顺序有关）。
但是对于BFS，因为他是稳扎稳打，一层一层逐渐向外探索，第一次到达目标点时记录下的路径，那就是最短路劲。

因此使用BFS，可以在第一次碰到到达target的情况后直接返回，而不用继续探索。

事实上，代码表明如果探索全路径，BFS在LC的所有testcase上要花5000ms左右。但是如果第一次碰到就直接返回，
那就只要1000ms左右。

最后注意因为要返回操作次数，所以探索过程中操作次数的信息要实时维护在队列里。
因此队列中是(密码,到达此密码的操作次数)的二元组。