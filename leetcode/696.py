# 给定一个字符串 s，计算具有相同数量0和1的非空(连续)子字符串的数量，并且这些子字符串中的所有0和所有1都是组合在一起的。
# 重复出现的子串要计算它们出现的次数。
# 方法1 时间复杂度O(n)，空间复杂度O(1)
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res = 0
        # 上一个字符长度,当前遍历索引
        last, end = 0, 0
        length = len(s)
        while end < length:
            c = s[end]
            temp = 0
            while end < length and s[end] == c:
                temp += 1
                end += 1
            res += min(last, temp)
            last = temp
        return res


# 方法2 用一个数组存储连续0/1的个数，时间复杂度O(n),空间复杂度O(n)
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res = 0
        init = []
        cur = 0
        length = len(s)
        while cur < length:
            temp = s[cur]
            val = 0
            while cur < length and s[cur] == temp:
                val += 1
                cur += 1
            init.append(val)
        if len(init) == 1:
            return 0
        for i in range(1, len(init)):
            res += min(init[i - 1], init[i])
        return res


if __name__ == '__main__':
    s = Solution()
    ss = "00110"
    print(s.countBinarySubstrings(ss))