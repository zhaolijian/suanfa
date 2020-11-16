# 给你一个整数数组 arr，请你帮忙统计数组中每个数的出现次数。
# 如果每个数的出现次数都是独一无二的，就返回 true；否则返回 false。

from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        d = Counter(arr)
        s = set()
        for key, val in d.items():
            if val in s:
                return False
            else:
                s.add(val)
        return True

