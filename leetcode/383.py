# 给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，判断第一个字符串 ransom 能不能由第二个字符串 magazines 里面的字符构成。如果可以构成，返回 true ；否则返回 false。
# (题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。杂志字符串中的每个字符只能在赎金信字符串中使用一次。)


# 方法1 哈希 使用哈希的方法空间消耗比较大，因为要数组+红黑树/链表
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d_ransomNote = Counter(ransomNote)
        d_magazine = Counter(magazine)
        s = set(ransomNote)
        for ele in s:
            if d_magazine[ele] < d_ransomNote[ele]:
                return False
        return True

# 方法2 数组
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        array = [0] * 26
        for ele in magazine:
            array[ord(ele) - ord('a')] += 1
        for ele in ransomNote:
            array[ord(ele) - ord('a')] -= 1
        for i in range(26):
            if array[i] < 0:
                return False
        return True