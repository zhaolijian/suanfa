class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        start = 0
        res = ""
        x = str(x)
        if x[0] == '+':
            start = 1
        elif x[0] == '-':
            sign = -1
            start = 1
        for i in range(start, len(x)):
            res = x[i] + res
        res = sign * int(res)
        return res if -pow(2, 31) <= res <= pow(2, 31) - 1 else -1

if __name__ == '__main__':
    s = Solution()
    x = int(input())
    print(s.reverse(x))
