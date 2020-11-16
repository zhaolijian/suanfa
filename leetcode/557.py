# 给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
class Solution:
    def reverseWords(self, s: str) -> str:
        l = list(s.split())
        res = []
        for i in range(len(l)):
            res.append(l[i][::-1])
        return ' '.join(res)