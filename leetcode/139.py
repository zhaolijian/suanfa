# 方法1，dp
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         wordDictSet = set(wordDict)
#         length = len(s)
#         dp = [False for i in range(length + 1)]
#         dp[0] = True
#         for i in range(1, length + 1):
#             for j in range(i):
#                 if dp[j] and s[j: i] in wordDictSet:
#                     dp[i] = True
#                     break
#         return dp[length]


# 方法2 dfs + 记忆化搜索
class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        # 从该位置开始的字符串是否能够被拆分
        def func(start):
            if start >= len(s):
                return True
            if start in dict_array:
                return dict_array[start]
            # 截止位置
            for i in range(start + 1, len(s) + 1):
                cur = s[start: i]
                if cur in wordDict:
                    dict_array[start] = func(i)
                    if dict_array[start]:
                        return True
            dict_array[start] = False
            return False

        if not s:
            return True
        if not wordDict:
            return False
        dict_array = {}
        wordDict = set(wordDict)
        return func(0)


if __name__ == '__main__':
    s = Solution()
    ss = "leetcode"
    wordDict = ["leet","code"]
    print(s.wordBreak(ss, wordDict))