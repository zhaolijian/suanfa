# 给你两个长度相同的字符串，s 和 t。
# 将 s 中的第 i 个字符变到 t 中的第 i 个字符需要 |s[i] - t[i]| 的开销（开销可能为 0），也就是两个字符的 ASCII 码值的差的绝对值。
# 用于变更字符串的最大预算是 maxCost。在转化字符串时，总开销应当小于等于该预算，这也意味着字符串的转化可能是不完全的。
# 如果你可以将 s 的子字符串转化为它在 t 中对应的子字符串，则返回可以转化的最大长度。
# 如果 s 中没有子字符串可以转化成 t 中对应的子字符串，则返回 0。

# 双指针
# class Solution:
#     def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
#         length = len(s)
#         init = [0] * length
#         for i in range(length):
#             init[i] = abs(ord(s[i]) - ord(t[i]))
#         res, cur, left, right = 0, 0, 0, 0
#         while right < length:
#             cur += init[right]
#             while cur > maxCost:
#                 cur -= init[left]
#                 left += 1
#             right += 1
#             res = max(res, right - left)
#         return res

# 双指针
# class Solution:
#     def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
#         length = len(s)
#         init = [0] * length
#         for i in range(length):
#             init[i] = abs(ord(s[i]) - ord(t[i]))
#         res = 0
#         left, right = 0, 0
#         while right < length:
#             while init[right] > maxCost and left < right:
#                 maxCost += init[left]
#                 left += 1
#             if init[right] <= maxCost:
#                 maxCost -= init[right]
#                 right += 1
#                 res = max(res, right - left)
#             else:
#                 left += 1
#                 right += 1
#         return res


from bisect import bisect_left
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        length = len(s)
        init = [0] * length
        res = 0
        for i in range(length):
            init[i] = abs(ord(s[i]) - ord(t[i]))
        for i in range(1, length):
            init[i] += init[i - 1]
        init = [0] + init
        for i in range(1, length + 1):
            start = bisect_left(init, init[i] - maxCost)
            res = max(res, i - start)
        return res


if __name__ == '__main__':
    s = Solution()
    ss ="abcde"
    t = "bcdfg"
    cost = 3
    print(s.equalSubstring(ss, t, cost))