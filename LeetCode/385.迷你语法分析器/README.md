## 题目描述
给定一个字符串 s 表示一个整数嵌套列表，实现一个解析它的语法分析器并返回解析的结果 NestedInteger 。

列表中的每个元素只可能是整数或整数嵌套列表

示例 1：
```
输入：s = "324",
输出：324
解释：你应该返回一个 NestedInteger 对象，其中只包含整数值 324。
```
示例 2：
```
输入：s = "[123,[456,[789]]]",
输出：[123,[456,[789]]]
解释：返回一个 NestedInteger 对象包含一个有两个元素的嵌套列表：
1. 一个 integer 包含值 123
2. 一个包含两个元素的嵌套列表：
    i.  一个 integer 包含值 456
    ii. 一个包含一个元素的嵌套列表
         a. 一个 integer 包含值 789
```

提示：
```
1 <= s.length <= 5 * 104
s 由数字、方括号 "[]"、负号 '-' 、逗号 ','组成
用例保证 s 是可解析的 NestedInteger
输入中的所有值的范围是 [-106, 106]
```

### 解法 栈
这题乍一看就知道可以用栈做。
但这题的难点可能并非在于想到一个解题的算法框架，而是如何返回一个NestedInteger对象。

这题的代码注释中给出了一个`NestedInteger`对象的定义以及其中各个方法的功能。
详细的见代码文件，这里直接讲一下其中重点的几个方法。

首先是构造方法`__init__`，根据注释说明，这个类的构造方法提供一个参数`val`，如果val是一个整数，那么这个NestedInteger实例就算是
一个持有单个整数的实例，与之相关的有用的方法是`getInteger`，`isInteger`等。
若初始化时不加val参数，按照注释的说明，实例内部会初始化一个空列表。之后可以通过`add`这个方法作为接口，将其他的NestedInterger实例添加到列表中，
于是本实例就变成了持有复杂嵌套列表结构的实例了。

严格按照上面的接口逻辑，结合栈作为算法框架，就可以写出代码了。

具体的，从前向后扫描字符串s，
碰到左中括号，就将其入栈；
碰到数字以及负号，就将其解析成一个int型的数字，为了后续操作方便，包装成NestedInteger（持有单个整数的实例）后也压入栈；
碰到右中括号，自然就不用入栈，而是要将栈中的内容都弹出直到碰到与之配对的左括号。
中途弹出的部分，全部都`add`进一个新的NestedInteger实例，然后将其作为一个整体入栈。

在弹栈操作中还有一个小问题，就是弹栈和入栈顺序是反的，如果直接`xx.add(stack.pop())`，那么得到的结果会和预期的恰好完全相反。

处理这个问题倒也不难，直接用一个列表先缓存弹出来的东西，然后再逆序将东西`add`如NestedInteger实例。

以上，这题与其说是考察了栈，不如说是考察了如何根据已有接口进行编程整合的能力。