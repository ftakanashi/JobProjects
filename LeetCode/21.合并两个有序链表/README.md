## 题目描述
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：
>输入：1->2->4, 1->3->4
>
>输出：1->1->2->3->4->4


### 解法1 迭代归并
显然这题就是归并排序中的归并操作。

按照归并的思想写下代码即可。

为了处理方便可以设置一个dummy head。
另外注意一边扫描完了另一边没完的情况，归并的时候要while，但是这里只要简单地把已经合并完的列表的末位
连接上还没扫描完的链表的头即可。