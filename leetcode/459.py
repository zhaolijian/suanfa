# 给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。


# 方法1
# 将字符串拼接，从1开始找，如果找到得位置不为len(s),则说明s可以由多个字串拼接而成。
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s + s).find(s, 1) != len(s)


# 方法2
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def func(s, sub, length):
            if not s:
                return True
            if len(s) < length:
                return False
            if s[:length] != sub:
                return False
            return func(s[length:], sub, length)

        n = len(s)
        for i in range(1, n // 2 + 1):
            if func(s, s[:i], i):
                return True
        return False


# 方法3 KMP
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def build_next(p):
            res = [0, 0]
            j = 0
            for i in range(1, len(p)):
                while j > 0 and p[i] != p[j]:
                    j = res[j]
                if p[i] == p[j]:
                    j += 1
                res.append(j)
            return res

        next = build_next(s)
        return True if next[-1] != 0 and len(s) % (len(s) - next[-1]) == 0 else False


# 超时
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)
        dp = [[False for i in range(length)] for j in range(length + 1)]
        for i in range(length):
            dp[0][i] = True
        for i in range(1, length + 1):
            if s[i - 1] == s[0]:
                dp[i][0] = dp[i - 1][0]
        for i in range(2, length + 1):
            for j in range(1, i):
                if s[:j + 1] == s[i - j - 1:i]:
                    dp[i][j] = dp[i - j - 1][j]
        for i in range(length // 2):
            if dp[-1][i] == True:
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    string = "aba"
    print(s.repeatedSubstringPattern(string))
