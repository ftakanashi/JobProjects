## 题目描述
给定一个整数，写一个函数来判断它是否是 3 的幂次方。如果是，返回 true ；否则，返回 false 。

整数 n 是 3 的幂次方需满足：存在整数 x 使得 n == 3^x


### 解法1 一般迭代
不解释了

### 解法2 取对数求解
本质上应该是一样的，只不过这里借助了math.log这个函数而已。

需要注意，计算机实现，这个函数必然返回float，然而float并不精确，
导致如果是一个整数幂，返回的值可能在正确的整数n的上下一个很小的范围内浮动，记得考虑这个误差。