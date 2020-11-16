class Solution:
    def func(self, s):
        length = len(s)
        if length <= 1:
            return s
        i = length - 1
        number = 0
        while i > 0:
            if s[i:] == s[:length - i]:
                number = max(number, length - i)
            i -= 1
        return s + s[number:]


if __name__ == '__main__':
    s = input()
    S = Solution()
    print(S.func(s))