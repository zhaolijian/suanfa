# 给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。
# 这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。


# 哈希表
# 方法1
from collections import defaultdict
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        str_array = s.split(" ")
        length = len(str_array)
        if length != len(pattern):
            return False
        c = defaultdict(list)
        for i, ele in enumerate(pattern):
            c[ele].append(i)
        s = set()
        for key in c.keys():
            l = c[key]
            s.add(str_array[l[0]])
            temp_len = len(l)
            if temp_len <= 1:
                continue
            for i in range(1, temp_len):
                if str_array[l[i]] != str_array[l[i - 1]]:
                    return False
        return len(c.keys()) == len(s)


# 方法2
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        str_array = s.split(" ")
        length = len(str_array)
        if length != len(pattern):
            return False
        char2string, string2char = {}, {}
        for c, string in zip(pattern, str_array):
            if(c in char2string and char2string[c] != string) or (string in string2char and string2char[string] != c):
                return False
            char2string[c] = string 
            string2char[string] = c
        return True