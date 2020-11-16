# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        s = s.strip()
        if not s:
            return 0
        if len(s) == 1 and (s[0] == '+' or s[0] == '-'):
            return 0
        single = 1
        if s[0] == '-':
            single = -1
        res = 0
        for i in range(len(s)):
            if i == 0 and (s[i] == '+' or s[i] == '-'):
                continue
            if s[i] < '0' or s[i] > '9':
                return 0
            res = res * 10 + ord(s[i]) - 48
        return single * res


if __name__ == '__main__':
    s = Solution()
    string = input()
    print(s.StrToInt(string))

