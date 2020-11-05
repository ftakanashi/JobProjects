## 题目描述

给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。

返回所有这些可能的句子。

说明：

- 分隔时可以重复使用字典中的单词。
- 你可以假设字典中没有重复的单词。

示例 1：

>输入:
>
>s = "catsanddog"
>
>wordDict = ["cat", "cats", "and", "sand", "dog"]
>
>输出:
>
>[
>
>  "cats and dog",
>
>  "cat sand dog"
>
>]

示例 2：

>输入:
>
>s = "pineapplepenapple"
>
>wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
>
>输出:
>
>[
>
>  "pine apple pen apple",
>
>  "pineapple pen apple",
>
>  "pine applepen apple"
>
>]
>
>解释: 注意你可以重复使用字典中的单词。

示例 3：

>输入:
>
>s = "catsandog"
>
>wordDict = ["cats", "dog", "sand", "and", "cat"]
>
>输出:
>
>[]

### 解法1 带有状态保存的DFS
首先先说明一些共通且显而易见的东西。比如给出的词典是一个List，显然后期的计算中会涉及判断一个substring是否存在在词典中，如果使用List的话比较
计算是O(n)的。因此可以考虑把wordDict给先整成一个set或者dict这样的哈希类型，这样in操作就可以O(1)完成了。

这题目乍一看似乎可以用DFS来解决。于是我写下了第一版代码：
```python
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        wordSet = set(wordDict)

        def dfs(n: int, prefix: str, totalRes: List):

            if n == len(s):
                totalRes.append(prefix.strip())
                return

            i = n + 1
            while i <= len(s):
                word = s[n:i]
                if word in wordSet:
                    new_prefix = prefix + word + ' '
                    dfs(i, new_prefix, totalRes)

                i += 1

        total_res = []
        dfs(0, '', total_res)

        return total_res
```
简单说明一下上述代码，重点看DFS函数。DFS函数接收的n表示，到s[n]为止的字符串已经找到了合理的分词方法，这种分词方法用prefix参数表示。

而totalRes列表则是一个返回值的容器。当某个递归递归到整个字符串的末尾，则totalRes可以出来收割成果，即prefix。

在还没有递归到末尾的时候，从当前位置向后看若干个字母的片段，如果片段在词典中，那么就可以扩张prefix并且在这个片段之后开始新一轮的递归。

这版代码，有点像用DFS走迷宫的思路，从0点开始依次向右扫描，碰到通的路就记录下来。

对于一些简单的case，这版代码都AC了。
但是一提交，在下面这个case中，运行时间超时：

```text
"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
```

这种case就是抬杠…

#### 改1
嘛，来分析一下原因。

显然，DFS代码运行时，有大量重复的计算。比如按照上面代码，在第一层递归，n=0,i=1的情况计算内完成之后，
开始计算n=0,i=2的情况时，针对第三个位置，又要重复计算一遍整个第三个位置以后的所有情况。

换言之，n=0,i=1的时候，第二层递归的`dfs(2, 'a a ', total_res)`和n=0,i=2时第一层递归的`dfs(2, 'aa', total_res)`
两者本质上计算的内容是一样的。

再换言之，在获取了所有`a a ****`（`****`代表了所有第三个a及其以后所有a的分割情况）之后，还要重新计算`aa ****`。
而实际上这两边的`****`是完全一致的

很自然的，想到如果可以用一个cache把这个"`****`"给保存下来就好了，这样第二次计算就可以直接取值避免重复计算。

但是！正如上面所说，这版代码类似于DFS走迷宫。

**从范式上来说，DFS当前已经走过的路径通过prefix这个参数层层传递给下一层递归，递归的过程中如果符合条件则不断"扩张"prefix。
而在探索中，各种各样得到扩张的prefix本身就是结果，只要在合适的时候收割这些结果，DFS本身并不需要return什么东西。**

**这是一种自上而下的DFS。**

由于是自上而下的，在这个题目场景里即从左到右的，很难把后缀缓存（如果是缓存前缀的话倒是OK）。

为了达到缓存目的，可以把dfs改成从右向左扫描；或者把DFS范式改成自下而上的。这里采用后者

**从范式上来说，DFS无需层层维护一个共通的内容，而是通过DFS末尾return出一些东西。这样由于递归终止的时候扫描已经结束，
所以层层return回来的话，自下而上的内容会丰富起来。同时在这个题的场景中，就是我们需要的后缀缓存了。**

首先先不管缓存，用自下而上的方式实现的代码：

```python
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]: 
        
        wordSet = set(wordDict)
        
        def dfs(n: int):

            if n == len(s):
                return
            
            i = n + 1
            res = []
            while i <= len(s):
                word = s[n:i]
                if word in wordSet:
                    suffix_patterns = dfs(i)
                    if suffix_patterns is None:
                        res.append(word)
                    else:
                        for suffix_pattern in suffix_patterns:
                            res.append(word + ' ' + suffix_pattern)
                i += 1

            return res

        return dfs(0)
```

此时，DFS函数的用意就很明确，即返回一个列表，其中的内容是位置s[i:]这个substring里，
所有可能的分割形式。
如此层层递归回来，把当前的词给prepend到递归回得到的suffix前面，形成本轮递归要返回的内容。

至此，代码范式改变了。但是提交的话还是会超时。接下来往里面加入cache机制即可。

cache的问题无非就是在哪里写入并且在哪里读取。如上所述，cache内容是某个位置i，以及其之后s[i:]的分割类型的对应。基于这一点，
在return res之前写入，在进行dfs正式计算前读取即可。（后一个还有两种选择，进入下一层递归前直接判断i是否存在在cache中，第二种是
在进入下一层递归的最开始判断n是否在cache中。我的最后代码采取后一种）

最终代码详见main.py