# 方法1
# class Solution:
#     def numSquares(self, n: int) -> int:
#         square = [pow(i, 2) for i in range(int(pow(n, 0.5) + 1))]
#         dp = [float('inf')] * (n + 1)
#         dp[0] = 0
#         for i in range(1, n + 1):
#             for temp in square:
#                 if temp > i:
#                     break
#                 dp[i] = min(dp[i], dp[i - temp] + 1)
#         return dp[-1]


# 方法2
# class Solution:
#     def numSquares(self, n):
#         def func(n, k):
#             if k == 1:
#                 return n in init
#             for i in init:
#                 if func(n - i, k - 1):
#                     return True
#             return False
#
#         init = set([i**2 for i in range(1, int(pow(n, 0.5)) + 1)])
#         for i in range(1, n + 1):
#             if func(n, i):
#                 return i


# 方法3 贪心算法+ BFS广度优先遍历
class Solution:
    def numSquares(self, n):
        init = [n]
        array = [pow(i, 2) for i in range(1, int(pow(n, 0.5)) + 1)]
        level = 0
        while init:
            level += 1
            temp_array = set()
            for number in init:
                for ele in array:
                    if number < ele:
                        break
                    elif number == ele:
                        return level
                    else:
                        temp_array.add(number - ele)
                init = list(temp_array)


if __name__ == '__main__':
    s = Solution()
    for _ in range(int(input())):
        n = int(input())
        print(s.numSquares(n))
