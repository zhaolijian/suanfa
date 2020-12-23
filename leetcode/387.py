# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

# 方法1 哈希表存储个数
from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        for i, ele in enumerate(s):
            if c[ele] == 1:
                return i
        return -1


# 方法2 哈希表存储位置
from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = defaultdict(int)
        for i, ele in enumerate(s):
            if ele not in d:
                d[ele] = i
            else:
                d[ele] = -1
        for ele in s:
            if d[ele] != -1:
                return d[ele]
        return -1


# 哈希表+队列
class Solution:
    def firstUniqChar(self, s: str) -> int:
        position = dict()
        q = collections.deque()
        n = len(s)
        for i, ch in enumerate(s):
            if ch not in position:
                position[ch] = i
                q.append((ch, i))
            else:
                position[ch] = -1
                while q and position[q[0][0]] == -1:
                    q.popleft()
        return -1 if not q else q[0][1]