# 实现 strStr() 函数。
# 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。


# 方法1 KMP  该题中效果不是很好，但是时间复杂度为O（m+n）
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 构建next数组
        def build_next(p):
            next = [0, 0]
            j = 0
            for i in range(1, len(p)):
                while j > 0 and p[i] != p[j]:
                    j = next[j]
                if p[i] == p[j]:
                    j += 1
                next.append(j)
            return next

        if not needle:
            return 0
        next = build_next(needle)
        # needle串当前遍历位置
        j = 0
        for i in range(len(haystack)):
            while j > 0 and haystack[i] != needle[j]:
                j = next[j]
            if haystack[i] == needle[j]:
                j += 1
            if j == len(needle):
                return i - len(needle) + 1
        return -1


# 方法2 时间复杂度O(mn)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        len_hay, len_needle = len(haystack), len(needle)
        if len_needle > len_hay:
            return -1
        for i in range(len_hay):
            if len_hay - i < len_needle:
                return -1
            j = 0
            temp = i
            while j < len_needle:
                if haystack[temp] == needle[j]:
                    if j == len_needle - 1:
                        return i
                    j += 1
                    temp += 1
                else:
                    break
        return -1