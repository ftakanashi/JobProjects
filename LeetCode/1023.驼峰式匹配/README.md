## 题目描述
如果我们可以将小写字母插入模式串 pattern 得到待查询项 query，那么待查询项与给定模式串匹配。（我们可以在任何位置插入每个字符，也可以插入 0 个字符。）

给定待查询列表 queries，和模式串 pattern，返回由布尔值组成的答案列表 answer。只有在待查项 queries[i] 与模式串 pattern 匹配时， answer[i] 才为 true，否则为 false。

示例 1：
```
输入：queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
输出：[true,false,true,true,false]
示例：
"FooBar" 可以这样生成："F" + "oo" + "B" + "ar"。
"FootBall" 可以这样生成："F" + "oot" + "B" + "all".
"FrameBuffer" 可以这样生成："F" + "rame" + "B" + "uffer".
```
示例 2：
```
输入：queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa"
输出：[true,false,true,false,false]
解释：
"FooBar" 可以这样生成："Fo" + "o" + "Ba" + "r".
"FootBall" 可以这样生成："Fo" + "ot" + "Ba" + "ll".
```
示例 3：
```
输出：queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBaT"
输入：[false,true,false,false,false]
解释： 
"FooBarTest" 可以这样生成："Fo" + "o" + "Ba" + "r" + "T" + "est".
```

提示：
```
1 <= queries.length <= 100
1 <= queries[i].length <= 100
1 <= pattern.length <= 100
所有字符串都仅由大写和小写英文字母组成。
```

### 解法 双指针
如果没有大写字母不能随意插入这个限制的话，那么其实这题就是判断pattern是不是某个query的子序列就是了。
因此可以使用基本的判断子序列的框架，即双指针稍加改造来做这题。

双指针在分别扫描query和pattern的时候，query上的指针显然会动的比较多，因此可以以query为基准，判断`query[j]`是否等于`pattern[i]`。
显然，等于的时候两个指针都往前移即可。
不等于的时候，通常直接让`j += 1`继续往下扫描，最后看`i`能否到达`pattern`的 末尾即可。

然而这里还多了一个大写字母的限制。
即当`query[j]`是个大写字母，且不等于`pattern[i]`的时候，按照题意，此时是直接False的。

更多细节看代码吧。

说实话这道题上面描述的这种做法给人一种抓不透的感觉。实际上第一次AC我也是用了超复杂的做法， 
先将query和pattern分别按照驼峰分节切割开，再比对每节的首个大写字母，再判断剩余小写字母是否是序列包含关系（此时就是一个简单的序列包含双指针判断了）…