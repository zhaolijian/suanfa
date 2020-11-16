# 长度为n的字符串中包含m个不同的字符，找出包含这m个不同字符的最小子串。
import collections
class Solution:
    def func(self, string):
        set_array = set(string)
        res = len(string)
        # m个不同字符
        m = len(set_array)
        start = 0
        temp = collections.defaultdict(int)
        for i in range(len(string)):
            temp[string[i]] += 1
            if len(temp.keys()) == m:
                while len(temp.keys()) == m:
                    temp[string[start]] -= 1
                    if temp[string[start]] == 0:
                        temp.pop(string[start])
                    start += 1
                res = min(res, i - start + 2)
        return res


if __name__ == '__main__':
    s = Solution()
    string = input()
    print(s.func(string))