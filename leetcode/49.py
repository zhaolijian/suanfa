# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。


# 对字符串排序作为键
from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs):
        d = defaultdict(list)
        for ele in strs:
            d[Counter(ele)].append(ele)
        return list(d.values())


# 把字符串中出现的字符个数作为键
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        d = defaultdict(list)
        for ele in strs:
            init = [0] * 26
            for c in ele:
                init[ord(c) - ord('a')] += 1
            d[tuple(init)].append(ele)
        return list(d.values())