class Solution:
    def LastRemaining_Solution(self, n, m):
        if n < 1 or m < 1:
            return -1
        last = 0
        for i in range(2, n + 1):
            last = (last + m) % i
        return last


if __name__ == '__main__':
    s = Solution()
    n = int(input())
    m = int(input())
    print(s.LastRemaining_Solution(n, m))
