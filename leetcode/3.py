# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
#
# 示例 1:
#
# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:
#
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:
#
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)
        init = []
        ans = 0
        for i in s:
            if i not in init:
                init.append(i)
            else:
                index = init.index(i)
                init = init[index+1:]
                init.append(i)
            if len(init) > ans:
                ans = len(init)
        return ans


# 方法2 滑动窗口
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        if length < 2:
            return length
        max_Len = 0
        window = set()
        start, end = 0, 0
        while end < length:
            if s[end] not in window:
                window.add(s[end])
                if end - start + 1 > max_Len:
                    max_Len = end - start + 1
            else:
                while s[start] != s[end]:
                    window.remove(s[start])
                    start += 1
                start += 1
            end += 1
        return max_Len


if __name__ == '__main__':
    ss = Solution()
    s = input().strip()
    result = ss.lengthOfLongestSubstring(s)
    print(result)