# 给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
# 你可以对一个单词进行如下三种操作：
# 插入一个字符
# 删除一个字符
# 替换一个字符


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len_1, len_2 = len(word1), len(word2)
        if not word1:
            return len_2
        if not word2:
            return len_1
        dp = [[0 for i in range(len_2)] for j in range(len_1)]
        dp[0][0] = 1 if word1[0] != word2[0] else 0
        for i in range(1, len_1):
            if word1[i] == word2[0]:
                dp[i][0] = i
            else:
                dp[i][0] = dp[i - 1][0] + 1
        for j in range(1, len_2):
            if word1[0] == word2[j]:
                dp[0][j] = j
            else:
                dp[0][j] = dp[0][j - 1] + 1
        for i in range(1, len_1):
            for j in range(1, len_2):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    word1 = input()
    word2 = input()
    print(s.minDistance(word1, word2))