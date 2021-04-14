#!/usr/bin/env python

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.child = {}
        self.end = False

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self    # 指针初始化在根节点
        for ch in word:
            if ch not in node.child:
                node.child[ch] = Trie()
            node = node.child[ch]
        node.end = True

    def searchPath(self, word: str):    # 共通方法，因为调用此方法后根据要求需要判断搜索有没有完成以及完成时指针的end是不是True，因此返回两个量
        node = self
        for ch in word:
            if ch not in node.child:
                return False, None
            node = node.child[ch]
        return True, node

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        flag, point = self.searchPath(word)
        return flag and point.end    # 只有搜索完成且完成时指针的end是True才说明word作为一个完整单词存在于树中

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        flag, point = self.searchPath(prefix)
        return flag    # 只需要完成搜索即可，完成时指针的end不影响判断。

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)