class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        length = len(coins)
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in coins:
            for j in range(i, amount + 1):
                dp[j] = min(dp[j], dp[j - i] + 1)
        return dp[-1] if dp[-1] != float('inf') else -1