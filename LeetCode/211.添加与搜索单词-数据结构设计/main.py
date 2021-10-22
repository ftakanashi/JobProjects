#!/usr/bin/env python
class Trie:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.end = False

class WordDictionary:

    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        node = self.trie
        for ch in word:
            i = ord(ch) - ord('a')
            if node.children[i] is None:
                node.children[i] = Trie()
            node = node.children[i]
        node.end = True

    def search(self, word: str) -> bool:
        # print(self.trie.children[1].children[0].children[3].end)
        n = len(word)

        def dfs(node, pos):
            if pos == n:
                return node.end
            if word[pos] == '.':
                for j in range(26):
                    if node.children[j] is not None and dfs(node.children[j], pos + 1):
                        return True
                return False
            else:
                i = ord(word[pos]) - ord('a')
                if node.children[i] is None:
                    return False
                else:
                    return dfs(node.children[i], pos + 1)

        return dfs(self.trie, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)