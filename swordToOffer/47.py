# 方法1
class Solution:
    def Sum_Solution(self, n):
        return sum(list(range(1, n+1)))


# 方法2
class Solution:
    def Sum_Solution(self, n):
        return (pow(n, 2) + n) >> 1

