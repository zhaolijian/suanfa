# 给一非空的单词列表，返回前 k 个出现次数最多的单词。
# 返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率，按字母顺序排序。
# 方法1 哈希表+堆
from collections import Counter
from heapq import heapify, heappop
class Solution(object):
    def topKFrequent(self, words, k):
        c = Counter(words)
        heap = [(-c[word], word) for word in c.keys()]
        heapify(heap)
        return [heappop(heap)[1] for _ in range(k)]


# 方法2 哈希表
from collections import Counter, defaultdict
class Solution:
    def topKFrequent(self, words, k: int):
        c = Counter(words)
        d = defaultdict(list)
        for key in c.keys():
            d[c[key]].append(key)
        array = []
        i = 0
        for kk in sorted(d.keys())[::-1]:
            for ele in sorted(d[kk]):
                if i >= k:
                    break
                array.append(ele)
                i += 1
        return array