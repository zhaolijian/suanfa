import collections
class Solution:
    # 滑动窗口
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_p = len(p)
        len_s = len(s)
        res = []
        start = 0
        dict_p = collections.Counter(p)
        temp = {}
        for i in range(len_s):
            if i - start + 1 > len_p:
                temp[s[start]] -= 1
                start += 1
            if s[i] in dict_p:
                if s[i] in temp:
                    temp[s[i]] += 1
                else:
                    temp[s[i]] = 1
            if i - start + 1 == len_p and temp == dict_p:
                res.append(start)
            if s[i] not in dict_p:
                temp = {}
                start = i + 1
        return res