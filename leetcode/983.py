# 从前往后的dp
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        last_day = days[-1]
        # days数组中遍历到的位置
        temp = 0
        # 到该天的最低花费
        dp = [0 for i in range(last_day + 1)]
        for i in range(1, last_day + 1):
            if i == days[temp]:
                l1 = dp[i - 1]
                l7 = dp[i - 7] if i - 7 >= 0 else 0
                l30 =  dp[i - 30] if i - 30 >= 0 else 0
                dp[i] = min(l1 + costs[0], l7 + costs[1], l30 + costs[2])
                temp += 1
            else:
                dp[i] = dp[i - 1]
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    # days = [1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,21,24,25,27,28,29,30,31,34,37,38,39,41,43,44,45,47,48,49,54,57,60,62,63,66,69,70,72,74,76,78,80,81,82,83,84,85,88,89,91,93,94,97,99]
    # costs = [9,38,134]
    days = [1, 4, 6, 7, 8, 20]
    costs = [2, 7, 15]
    print(s.mincostTickets(days, costs))