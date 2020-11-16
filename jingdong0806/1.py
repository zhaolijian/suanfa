class Solution:
    def function(self, N, array1, array2):
        dp = [[0 for i in range(N)] for j in range(N)]
        dp[0][0] = 1 if array1[0] == array2[0] else 0
        for i in range(1, N):
            if array1[0] == array2[i]:
                dp[0][i] = 1
            else:
                dp[0][i] = dp[0][i - 1]
        for i in range(1, N):
            if array1[i] == array2[0]:
                dp[i][0] = 1
            else:
                dp[i][0] = dp[i - 1][0]
        for i in range(1, N):
            for j in range(1, N):
                if array1[i] == array2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]

    def func(self, N, array1, array2):
        res = self.function(N, array1, array2)
        number = res / N
        number = round(number, 2)
        return number


if __name__ == '__main__':
    N = int(input())
    array1 = list(input().split())
    array2 = list(input().split())
    s = Solution()
    result = s.func(N, array1, array2)
    if result <= 0.5:
        if len(str(result)) < 4:
            print(str(result) + '0' + ' ' + 'Yes')
        else:
            print(str(result) + ' ' + 'Yes')
    else:
        if len(str(result)) < 4:
            print(str(result) + '0' + ' ' + 'No')
        else:
            print(str(result) + ' ' + 'No')