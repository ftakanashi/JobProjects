## 题目描述

给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。

为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。

所有整数的范围在 -228 到 228 - 1 之间，最终结果不会超过 231 - 1 。

例如:

输入:
>A = [ 1, 2]
>
>B = [-2,-1]
>
>C = [-1, 2]
>
>D = [ 0, 2]
>
>输出:
>
>2

解释:
>两个元组如下:
>
>1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
>
>2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0


### 解法 哈希+相反数
N数相加系列…大多都可以用到哈希+相反数的思想。

比如三数相加的时候，和这题一样，要求得到的和都是0，因此可以先算出两个数组合的所有情况，然后去数组里找其相反数，如果存在那么就是可以加起来和
等于0了。

另一个思路，如果从暴力开始尝试，显然O(n^4)有点离谱。实际上也会超过时间限制。
和三数相加的时候思路一样，O(n^2)还勉强在接受范围内，所以先计算两两组合的情况，然后去检查各个组合和的相反数。

不论如何，这里都指示着，先两两组合。比如以A,B为一组，先保存其所有两两组合的和。然后再在C,D中寻找两两组合，其和恰好是A，B结果中的相反数，
这样就可以得到一个四个数加起来和是0的元组。

显然，中间用于保存A，B计算结果的载体可以用哈希表。

> 关于itertools和collections
>
>最朴素的做法，当然是用dict实现counter功能，用两层for
>循环实现O(n^2)遍历过程。
>
>不过基于Python battery的内置数据结构，前者可以使用collections.Counter。
>后者可使用itertools.product。
>
>对于前者而言，只是一个方便上的操作。后者而言，itertools.product产出的是一个迭代器，
>所以相比于两层循环，时间花更久但是空间花更少。