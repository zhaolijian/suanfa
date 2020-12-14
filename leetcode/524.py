# 给定一个字符串和一个字符串字典，找到字典里面最长的字符串，该字符串可以通过删除给定字符串的某些字符来得到。
# 如果答案不止一个，返回长度最长且字典顺序最小的字符串。如果答案不存在，则返回空字符串。

class Solution:
    def findLongestWord(self, s: str, d) -> str:
        res = ""
        length_s = len(s)
        for ele in d:
            cur_d = 0
            cur_s = 0
            while cur_d < len(ele) and cur_s < length_s:
                if ele[cur_d] == s[cur_s]:
                    cur_d += 1
                    cur_s += 1
                else:
                    cur_s += 1
            if cur_d == len(ele) and (len(ele) > len(res) or (len(ele) == len(res) and ele < res)):
                res = ele
        return res
