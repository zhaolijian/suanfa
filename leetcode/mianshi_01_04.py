# 回文排列
# 统计字符出现次数为奇数的个数，如果奇数字符小于等于1个，则True
import collections
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        temp = collections.Counter(s)
        res = 0
        for key, val in temp.items():
            if val % 2 != 0:
                res += 1
        return True if res <= 1 else False