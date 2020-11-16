class Solution:
    def LeftRotateString(self, s, n):
        if not s:
            return s
        if n < len(s):
            return s[n:] + s[:n]
        elif n == len(s):
            return s
        else:
            temp = n % len(s)
            return s[temp:] + s[:temp]


