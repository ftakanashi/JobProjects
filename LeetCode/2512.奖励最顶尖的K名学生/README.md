## 题目描述
给你两个字符串数组 positive_feedback 和 negative_feedback ，分别包含表示正面的和负面的词汇。不会 有单词同时是正面的和负面的。

一开始，每位学生分数为 0 。每个正面的单词会给学生的分数 加 3 分，每个负面的词会给学生的分数 减  1 分。

给你 n 个学生的评语，用一个下标从 0 开始的字符串数组 report 和一个下标从 0 开始的整数数组 student_id 表示，其中 student_id[i] 表示这名学生的 ID ，这名学生的评语是 report[i] 。每名学生的 ID 互不相同。

给你一个整数 k ，请你返回按照得分 从高到低 最顶尖的 k 名学生。如果有多名学生分数相同，ID 越小排名越前。

示例 1：
```
输入：positive_feedback = ["smart","brilliant","studious"], negative_feedback = ["not"], report = ["this student is studious","the student is smart"], student_id = [1,2], k = 2
输出：[1,2]
解释：
两名学生都有 1 个正面词汇，都得到 3 分，学生 1 的 ID 更小所以排名更前。
```
示例 2：
```
输入：positive_feedback = ["smart","brilliant","studious"], negative_feedback = ["not"], report = ["this student is not studious","the student is smart"], student_id = [1,2], k = 2
输出：[2,1]
解释：
- ID 为 1 的学生有 1 个正面词汇和 1 个负面词汇，所以得分为 3-1=2 分。
- ID 为 2 的学生有 1 个正面词汇，得分为 3 分。
学生 2 分数更高，所以返回 [2,1] 。
```

提示：
```
1 <= positive_feedback.length, negative_feedback.length <= 104
1 <= positive_feedback[i].length, negative_feedback[j].length <= 100
positive_feedback[i] 和 negative_feedback[j] 都只包含小写英文字母。
positive_feedback 和 negative_feedback 中不会有相同单词。
n == report.length == student_id.length
1 <= n <= 104
report[i] 只包含小写英文字母和空格 ' ' 。
report[i] 中连续单词之间有单个空格隔开。
1 <= report[i].length <= 100
1 <= student_id[i] <= 109
student_id[i] 的值 互不相同 。
1 <= k <= n
```

### 解法 哈希表 排序
这题看似很简单，只是一个字符串处理基础上的模拟题而已。
但是如果使用比较朴素的思路去做还是会超时。

我最开始想的朴素思路是，先把 `positive_feedbacks` 和 `negative_feedbacks` 中的单词分别进行哈希集合化，
然后挨个遍历学生的评语，计算分数，最后将分数排序即可。
不过这样超时了。

虽然从原理上来看感觉差别是不大的，但是如果将所有单词用哈希表保存起来，保存成单词->分数的对应的话，整体就会快很多…

另外如果把所有分数都算出来再总体排序，其耗时也会比一直维护一个堆更长…

总之给出的代码是可以AC的。