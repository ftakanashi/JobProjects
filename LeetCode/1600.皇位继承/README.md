## 题目描述
一个王国里住着国王、他的孩子们、他的孙子们等等。每一个时间点，这个家庭里有人出生也有人死亡。

这个王国有一个明确规定的皇位继承顺序，第一继承人总是国王自己。我们定义递归函数 Successor(x, curOrder) ，给定一个人 x 和当前的继承顺序，该函数返回 x 的下一继承人。
```
Successor(x, curOrder):
    如果 x 没有孩子或者所有 x 的孩子都在 curOrder 中：
        如果 x 是国王，那么返回 null
        否则，返回 Successor(x 的父亲, curOrder)
    否则，返回 x 不在 curOrder 中最年长的孩子
```
比方说，假设王国由国王，他的孩子 Alice 和 Bob （Alice 比 Bob 年长）和 Alice 的孩子 Jack 组成。

一开始， curOrder 为 ["king"].
```
调用 Successor(king, curOrder) ，返回 Alice ，所以我们将 Alice 放入 curOrder 中，得到 ["king", "Alice"] 。
调用 Successor(Alice, curOrder) ，返回 Jack ，所以我们将 Jack 放入 curOrder 中，得到 ["king", "Alice", "Jack"] 。
调用 Successor(Jack, curOrder) ，返回 Bob ，所以我们将 Bob 放入 curOrder 中，得到 ["king", "Alice", "Jack", "Bob"] 。
调用 Successor(Bob, curOrder) ，返回 null 。最终得到继承顺序为 ["king", "Alice", "Jack", "Bob"] 。
```
通过以上的函数，我们总是能得到一个唯一的继承顺序。

请你实现 ThroneInheritance 类：
```
ThroneInheritance(string kingName) 初始化一个 ThroneInheritance 类的对象。国王的名字作为构造函数的参数传入。
void birth(string parentName, string childName) 表示 parentName 新拥有了一个名为 childName 的孩子。
void death(string name) 表示名为 name 的人死亡。一个人的死亡不会影响 Successor 函数，也不会影响当前的继承顺序。你可以只将这个人标记为死亡状态。
string[] getInheritanceOrder() 返回 除去 死亡人员的当前继承顺序列表。
```

示例：
```
输入：
["ThroneInheritance", "birth", "birth", "birth", "birth", "birth", "birth", "getInheritanceOrder", "death", "getInheritanceOrder"]
[["king"], ["king", "andy"], ["king", "bob"], ["king", "catherine"], ["andy", "matthew"], ["bob", "alex"], ["bob", "asha"], [null], ["bob"], [null]]
输出：
[null, null, null, null, null, null, null, ["king", "andy", "matthew", "bob", "alex", "asha", "catherine"], null, ["king", "andy", "matthew", "alex", "asha", "catherine"]]

解释：
ThroneInheritance t= new ThroneInheritance("king"); // 继承顺序：king
t.birth("king", "andy"); // 继承顺序：king > andy
t.birth("king", "bob"); // 继承顺序：king > andy > bob
t.birth("king", "catherine"); // 继承顺序：king > andy > bob > catherine
t.birth("andy", "matthew"); // 继承顺序：king > andy > matthew > bob > catherine
t.birth("bob", "alex"); // 继承顺序：king > andy > matthew > bob > alex > catherine
t.birth("bob", "asha"); // 继承顺序：king > andy > matthew > bob > alex > asha > catherine
t.getInheritanceOrder(); // 返回 ["king", "andy", "matthew", "bob", "alex", "asha", "catherine"]
t.death("bob"); // 继承顺序：king > andy > matthew > bob（已经去世）> alex > asha > catherine
t.getInheritanceOrder(); // 返回 ["king", "andy", "matthew", "alex", "asha", "catherine"]
```
 

提示：
```
1 <= kingName.length, parentName.length, childName.length, name.length <= 15
kingName，parentName， childName 和 name 仅包含小写英文字母。
所有的参数 childName 和 kingName 互不相同。
所有 death 函数中的死亡名字 name 要么是国王，要么是已经出生了的人员名字。
每次调用 birth(parentName, childName) 时，测试用例都保证 parentName 对应的人员是活着的。
最多调用 10^5 次birth 和 death 。
最多调用 10 次 getInheritanceOrder 。
```

### 解法 构建树 + 前序遍历
这题干有点太长了… 看了说明部分还是感觉不太明白这个继承规则。
但是看一下示例就知道了，其实可以用一个多叉树来抽象这个家族结构（其中孩子集合是一个列表，有顺序）。
而所谓的继承关系就是这个多叉树的前序遍历而已。

有了以上这个认识，这道题就没有难度了。

一个最简单朴素的做法，就是定义一个适应这道题的多叉树节点类：
```python
class Node:
    def __init__(self, name):
        self.name = name
        self.dead = False
        self.children = []
```
在题目要求设计的几个方法中，注意到birth和dead方法需要通过姓名这个字符串检索到相关节点。
因此很自然，需要在题目的类中额外定义一个`name2node`的哈希表，用于快速检索。

于是第一版代码就有了：（getInheritanceOrder方法的注释中写的是非递归版本的前序遍历）
```python
class Node:
    def __init__(self, name):
        self.name = name
        self.dead = False
        self.children = []

class ThroneInheritance:

    def __init__(self, kingName: str):
        self.family = Node(kingName)
        self.name2node = {kingName: self.family}

    def birth(self, parentName: str, childName: str) -> None:
        child = Node(childName)
        self.name2node[childName] = child
        self.name2node[parentName].children.append(child)

    def death(self, name: str) -> None:
        self.name2node[name].dead = True

    def getInheritanceOrder(self) -> List[str]:
        # res = []
        # stack = [self.family, ]
        # while stack:
        #     node = stack.pop()
        #     if not node.dead: res.append(node.name)
        #     for i in range(len(node.children) - 1, -1, -1):
        #         stack.append(node.children[i])
        # return res
        res = []
        def dfs(node):
            if not node.dead: res.append(node.name)
            for child in node.children:
                dfs(child)
        
        dfs(self.family)
        return res
```

提交之后发现虽然AC了但是总体的时间空间并不太好。
想了一会儿没觉得还有什么优化的余地，于是看了眼答案。
才发现，原来并没有必要显示建立树结构。

因为这个家族树只涉及到简单的有顺序的子节点。所以没必要单独设立一个节点类。
因为题目保证了家族中每个人的名字都不同，所以可以直接定义一个`name: [child1, child2]`之类的字典。
这个字典也无需嵌套，对于`child1`还可以有独立的一个键值对`child1: [grandchild1, grandchild2]`。

由于只是维护字符串之间的层级关系，没地方插入dead信息，因此需要额外一个哈希集用来看某个name是不是已经dead了。

最后，DFS的时候也很明显，传入name即可。
在不显示建立树结构的情况下（或者说用一个字典表示树而不是重型的类），时间和空间都得到了改善。