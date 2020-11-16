class Solution:
    def func(self, s):
        length = len(s)
        res = 2 * length - 1
        for i in range(length):
            # 单侧奇数回文
            if 2 * i + 1 <= length and s[:i] == s[2*i: i: -1]:
                res = min(res, 2 * length - 2 * i - 1)
            # s[i - 1: 2 * i - length: -1]同样也是左闭右开
            if 2 * i - length + 1 >= 0 and s[i + 1:] == s[i - 1: 2 * i - length: -1]:
                res = min(res, 2 * i + 1)
            # 单侧偶数回文
            if 2 * i <= length and s[:i] == s[2 * i - 1: i - 1: -1]:
                res = min(res, 2 * length - 2 * i)
            if 2 * i - length >= 0 and s[i:] == s[i - 1: 2 * i - length - 1: -1]:
                res = min(res, 2 * i)
        return res


if __name__ == '__main__':
    S = Solution()
    s = input()
    print(S.func(s))