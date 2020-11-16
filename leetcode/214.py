# 给定一个字符串 s，你可以通过在字符串前面添加字符将其转换为回文串。找到并返回可以用这种方式转换的最短回文串。
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        length = len(s)
        len_huiwen = 1
        for i in range(length // 2 + 1):
            if s[:i] == s[i: 2 * i][::-1]:
                len_huiwen = max(len_huiwen, 2 * i)
            if 2 * i + 1 <= length and s[:i] == s[i + 1: 2 * i + 1][::-1]:
                len_huiwen = max(len_huiwen, 2 * i + 1)
        return s[len_huiwen:][::-1] + s


if __name__ == '__main__':
    s = Solution()
    ss =  "abcd"
    print(s.shortestPalindrome(ss))