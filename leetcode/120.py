class Solution:
    def minimumTotal(self, triangle) -> int:
        h = len(triangle)
        dp = [float('inf') for i in range(h + 2)]
        dp[1] = triangle[0][0]
        for i in range(1, h):
            for j in range(i, -1, -1):
                dp[j + 1] = min(dp[j], dp[j + 1]) + triangle[i][j]
        return min(dp)



if __name__ == '__main__':
    s = Solution()
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    print(s.minimumTotal(triangle))