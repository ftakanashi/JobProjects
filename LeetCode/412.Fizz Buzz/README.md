## 题目描述
写一个程序，输出从 1 到 n 数字的字符串表示。

1. 如果 n 是3的倍数，输出“Fizz”；

2. 如果 n 是5的倍数，输出“Buzz”；

3. 如果 n 同时是3和5的倍数，输出 “FizzBuzz”。

示例：
```
n = 15,

返回:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
```


### 哈希优化枚举
其实这题没有任何弯弯绕。

就解题而言，其实就可以`for i in range(1, n+1)`，然后依次判断情况。
如果被3整除且被5整除就是FizzBuzz，否则如果被3整除就Fizz，以此类推，补充完整个res列表即可。

只是，如果扩展一下这道题，比如要求同时判断3,5,7,9,11的整除情况，并且被整除的数对应字符串依次拼接起来代表数字的话，
显然如果写if/else情况很复杂。

此时可以写一个哈希表，`{3: 'fizz', 5: 'buzz', 7: 'xxx'...}`
这样对于每个数字我只要遍历哈希表，构建字符串即可。

注意单纯哈希表直接遍历不一定会按照3579的顺序，可以采用OrderedDict。