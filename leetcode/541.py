# 给定一个字符串 s 和一个整数 k，你需要对从字符串开头算起的每隔 2k 个字符的前 k 个字符进行反转。
# 如果剩余字符少于 k 个，则将剩余字符全部反转。
# 如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = ""
        length = len(s)
        for i in range(0, length, 2 * k):
            if i + k <= length:
                res += s[i: i + k][::-1]
                res += s[i + k: i + 2 * k]
            elif i + k > length:
                res += s[i: length][::-1]
                break
        return res


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = ""
        length = len(s)
        i = 0
        while i < length:
            if i + 2 * k <= length:
                res += s[i: i + k][::-1]
                res += s[i + k: i + 2 * k]
                i = i + 2 * k
            elif i + k <= length:
                res += s[i: i + k][::-1]
                res += s[i + k: length]
                break
            else:
                res += s[i: length][::-1]
                break
        return res