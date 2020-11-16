# 给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。
# 说明：
# 分隔时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
from functools import lru_cache


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        @lru_cache(None)
        def func(index):
            if index == len(s):
                return [[]]
            res = []
            for i in range(index + 1, len(s) + 1):
                if s[index: i] in wordDict:
                    rest = func(i)
                    for temp in rest:
                        res.append([s[index: i]] + temp)
            return res


        wordDict = set(wordDict)
        result = func(0)
        return [" ".join(word) for word in result]


if __name__ == '__main__':
    s = Solution()
    ss = "catsanddog"
    wordDict = ["cat","cats","and","sand","dog"]
    print(s.wordBreak(ss, wordDict))