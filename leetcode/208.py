# Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。
# 请你实现 Trie 类：
# Trie() 初始化前缀树对象。
# void insert(String word) 向前缀树中插入字符串 word 。
# boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
# boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。


# 方法1 前缀树
class Trie:
    def __init__(self):
        self.sons = [None] * 26
        self.isEnd = False

    def insert(self, word: str) -> None:
        cur = self
        for w in word:
            temp = ord(w) - ord('a')
            if cur.sons[temp] is None:
                cur.sons[temp] = Trie()
            cur = cur.sons[temp]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self
        for w in word:
            temp = ord(w) - ord('a')
            if cur.sons[temp]:
                cur = cur.sons[temp]
            else:
                return False
        return cur.isEnd == True

    def startsWith(self, prefix: str) -> bool:
        cur = self
        for w in prefix:
            temp = ord(w) - ord('a')
            if cur.sons[temp]:
                cur = cur.sons[temp]
            else:
                return False
        return True


# 方法2 投机取巧，最好不要用。startsWith的时间复杂度很高，因为要遍历所有set集合中的元素，看是否能够进行startwith匹配
class Trie:

    def __init__(self):
        self.trie = set()

    def insert(self, word: str) -> None:
        self.trie.add(word)

    def search(self, word: str) -> bool:
        if word in self.trie:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        for ele in self.trie:
            if len(ele) < len(prefix):
                continue
            else:
                if prefix == ele[:len(prefix)]:
                    return True
        return False
