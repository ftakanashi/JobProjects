## 题目描述

在一排树中，第 i 棵树产生 tree[i] 型的水果。

你可以从你选择的任何树开始，然后重复执行以下步骤：

1. 把这棵树上的水果放进你的篮子里。如果你做不到，就停下来。

2. 移动到当前树右侧的下一棵树。如果右边没有树，就停下来。

请注意，在选择一颗树后，你没有任何选择：你必须执行步骤 1，然后执行步骤 2，然后返回步骤 1，然后执行步骤 2，依此类推，直至停止。

你有两个篮子，每个篮子可以携带任何数量的水果，但你希望每个篮子只携带一种类型的水果。

用这个程序你能收集的水果树的最大总量是多少？
 

示例 1：
>输入：[1,2,1]
>
>输出：3
>
>解释：我们可以收集 [1,2,1]。

示例 2：
>输入：[0,1,2,2]
>
>输出：3
>
>解释：我们可以收集 [1,2,2]
>
>如果我们从第一棵树开始，我们将只能收集到 [0, 1]。

示例 3：
>输入：[1,2,3,2,2]
>
>输出：4
>
>解释：我们可以收集 [2,3,2,2]
>
>如果我们从第一棵树开始，我们将只能收集到 [1, 2]。

示例 4：
>输入：[3,3,3,1,2,1,1,2,3,3,4]
>
>输出：5
>
>解释：我们可以收集 [1,2,1,1,2]
>
>如果我们从第一棵树或第八棵树开始，我们将只能收集到 4 棵水果树。
 

提示：
- 1 <= tree.length <= 40000
- 0 <= tree[i] < tree.length

### 审题
题目一开始看的有点蒙蔽。

精炼一下问题模型，其实就是要从一个数组中找到一个最长的连续的子数组。

这个子数组符合要求：子数组中只有两种元素。

### 解法 滑动窗口
看到从数组中找一个连续的子数组，很明显可以用滑动窗口的办法来解决。

右边界一直向右扫描，直到扫描到一个不属于窗口内部两种元素的一个元素时，记录窗口长度并收缩左边界。

这里有个问题，左边界收缩到什么地方合适呢、

首先，我最开始想到的，是不是收缩到当前右边界的左边一位。但是仔细一想并不是那么单纯，应该是收缩到当前右边界左边，一块"纯净区域"的左边界。

有点拗口，看这个例子：
```text
( 3 3 3 1 1 1 1 ) 2 ...
```
显然，当窗口到达当前位置，右边界再往右一格就发现"异常"了，所以左边界收缩，但是左边界没必要收到最右边的1，而是收到第4位上的1即可。

这样新窗口就变成了
```text
3 3 3 ( 1 1 1 1 2 ) ...
```
那么怎么找到这个合适的1呢。最简单的办法当然是从右边界一个while循环想左探索找"纯净区域"的左边界。

不过while有点恐怖，所以我选择再多加一个指针，随时指向当前窗口内最靠右"纯净区域"的左边界位置。

由于用到了三个指针，所以我也愿称他为三指针法（笑

### 2022/10/17 追加
补充了另一种更加贴合滑窗模板的写法。