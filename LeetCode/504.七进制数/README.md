## 题目描述
给定一个整数 num，将其转化为 7 进制，并以字符串形式输出。

示例 1:
```
输入: num = 100
输出: "202"
```
示例 2:
```
输入: num = -7
输出: "-10"
```

提示：
```
-107 <= num <= 107
```

### 解法 进制转换
没啥可说的…不断取余后倒序，进制转换套路。注意正负性。