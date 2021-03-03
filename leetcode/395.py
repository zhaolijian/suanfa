# 给你一个字符串 s 和一个整数 k ，请你找出 s 中的最长子串， 要求该子串中的每一字符出现次数都不少于 k 。返回这一子串的长度。

# 思路： 找出字符串s中字符出现次数少于k的字符t，满足的子串只可能出现在t出现的位置分隔区间中，递归查找即可
class Solution(object):
    def longestSubstring(self, s, k):
        if len(s) < k:
            return 0
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(sub_s, k) for sub_s in s.split(c))
        return len(s)