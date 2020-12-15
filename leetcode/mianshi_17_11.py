# 有个内含单词的超大文本文件，给定任意两个单词，找出在这个文件中这两个单词的最短距离(相隔单词数)。
# 如果寻找过程在这个文件中会重复多次，而每次寻找的单词不同，你能对此优化吗?


from collections import defaultdict
class Solution:
    def findClosest(self, words, word1: str, word2: str) -> int:
        d = defaultdict(list)
        for i, word in enumerate(words):
            if word == word1 or word == word2:
                d[word].append(i)
        l1 = sorted(d[word1])
        l2 = sorted(d[word2])
        len1, len2 = len(l1), len(l2)
        i, j = 0, 0
        res = float('inf')
        while i < len1 and j < len2:
            res = min(res, abs(l1[i] - l2[j]))
            if l1[i] < l2[j]:
                i += 1
            else:
                j += 1
        return res


from collections import defaultdict
class Solution:
    def findClosest(self, words, word1: str, word2: str) -> int:
        d = defaultdict(list)
        for i, word in enumerate(words):
            if word == word1 or word == word2:
                d[word].append(i)
        d[word1].sort()
        d[word2].sort()
        len1, len2 = len(d[word1]), len(d[word2])
        i, j = 0, 0
        res = float('inf')
        while i < len1 and j < len2:
            res = min(res, abs(d[word1][i] - d[word2][j]))
            if d[word1][i] < d[word2][j]:
                i += 1
            else:
                j += 1
        return res


if __name__ == '__main__':
    s = Solution()
    words = ["I","am","a","student","from","a","university","in","a","city"]
    word1 = "a"
    word2 = "student"
    print(s.findClosest(words, word1, word2))