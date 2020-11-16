# 滑动窗口思想，右边界不断往右滑动，直到找到第一个满足的窗口，然后往左滑动
import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        len_s = len(s)
        len_t = len(t)
        if len_t > len_s or not len_s:
            return ""
        # 总需要数
        count_need = len_t
        l, r = 0, 0
        res = ""
        res_length = float('inf')
        while r <= len_s:
            if count_need == 0:
                if r - l < res_length:
                    res_length = r - l
                    res = s[l: r]
                if s[l] in need.keys():
                    need[s[l]] += 1
                    if need[s[l]] > 0:
                        count_need += 1
                l += 1
            else:
                if r >= len_s:
                    break
                if s[r] in need.keys():
                    need[s[r]] -= 1
                    if need[s[r]] >= 0:
                        count_need -= 1
                r += 1
        return res


if __name__ == '__main__':
    ss = Solution()
    s = "ADOBECODEBANC"
    t = "ABC"
    print(ss.minWindow(s, t))