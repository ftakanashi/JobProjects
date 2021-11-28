## 题目描述
写一个 bash 脚本以统计一个文本文件 words.txt 中每个单词出现的频率。

为了简单起见，你可以假设：

- words.txt只包括小写字母和 ' ' 。
- 每个单词只由小写字母组成。
- 单词间由一个或多个空格字符分隔。

示例:
```
假设 words.txt 内容如下：

the day is sunny the the
the sunny is is
你的脚本应当输出（以词频降序排列）：

the 4
is 3
sunny 2
day 1
说明:

不要担心词频相同的单词的排序问题，每个单词出现的频率都是唯一的。
你可以使用一行 Unix pipes 实现吗？
```

### 解法 活用xargs + sort uniq组合拳
这个关键点我觉得在于如何将原文件中的一行行句子给分割成全是单词的形式。
做法当然有很多，可以用`tr`，而我这里是用了`xargs`。

`xargs`给人是一种接在pipeline中的感觉，但是实际上其做的是文本层面的整理。具体的参数啥的可以查文档，这里就不多说了。

一旦分割成单词，那显然就是`sort | uniq -c | sort -rn`这套组合拳了。
另外输出要求词频在词后面，所以最后还要接一个`awk`调整前后。

最终答案：
```shell script
# Read from the file words.txt and output the word frequency list to stdout.
cat words.txt | xargs -n1 | sort | uniq -c | sort -nr | awk '{print $2 " " $1}'
```