
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution1:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None: return

        # 第一次扫描
        copy_head = j = Node(head.val)
        match = {head: copy_head, None: None}
        i = head.next
        while i is not None:
            node = Node(i.val)
            j.next = match[i] = node
            j = node
            i = i.next

        # 第二次扫描
        i = head
        j = copy_head
        while j is not None:
            j.random = match[i.random]
            i = i.next
            j = j.next

        return copy_head


class Solution(object):
    def copyRandomList(self, head):
        if not head: return head

        # 第一次扫描，构建A -> A' -> B -> B' -> Null这种形式的新旧混合链表
        i = head
        while i is not None:
            new_node = Node(i.val, None, None)
            new_node.next = i.next
            i.next = new_node
            i = new_node.next

        # 基于特殊位置关系进行新链表节点间random连接
        i = head
        while i is not None:
            i.next.random = i.random.next if i.random is not None else None
            i = i.next.next

        # 拆分新旧混合链表，返回新链表
        ptr_old_list = head # A->B->C
        ptr_new_list = head.next # A'->B'->C'
        head_old = head.next
        while ptr_old_list:
            ptr_old_list.next = ptr_old_list.next.next
            ptr_new_list.next = ptr_new_list.next.next if ptr_new_list.next else None
            ptr_old_list = ptr_old_list.next
            ptr_new_list = ptr_new_list.next
        return head_old