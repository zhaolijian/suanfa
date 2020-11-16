class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        dictionary = set(dictionary)
        length = len(sentence)
        dp = [0 for i in range(length + 1)]
        # 遍历值为长度
        for i in range(1, length + 1):
            dp[i] = dp[i - 1] + 1
            for j in range(i):
                if sentence[j: i] in dictionary:
                    dp[i] = min(dp[i], dp[j])
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    dictionary = ["looked", "just", "like", "her", "brother"]
    sentence = "jesslookedjustliketimherbrother"
    print(s.respace(dictionary, sentence))