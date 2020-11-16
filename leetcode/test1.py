# 无重复字符的最长子串
class Solution:
    def func(self, s):
        length = len(s)
        if length < 2:
            return s
        res = ""
        max_Len = 0
        window = set()
        start, end = 0, 0
        temp = 0
        while end < length:
            if s[end] not in window:
                window.add(s[end])
                temp += 1
                if temp > max_Len:
                    max_Len = temp
                    res = s[start: end + 1]
            else:
                while s[start] != s[end]:
                    window.remove(s[start])
                    start += 1
                    temp -= 1
                start += 1
            end += 1
        return res, max_Len


if __name__ == '__main__':
    s = Solution()
    ss = "adsdassadasdfg"
    res, max_Len = s.func(ss)
    print(res)
    print(max_Len)