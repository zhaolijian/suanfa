# 在一个由小写字母构成的字符串 s 中，包含由一些连续的相同字符所构成的分组。
# 例如，在字符串 s = "abbxxxxzyy" 中，就含有 "a", "bb", "xxxx", "z" 和 "yy" 这样的一些分组。
# 分组可以用区间 [start, end] 表示，其中 start 和 end 分别表示该分组的起始和终止位置的下标。上例中的 "xxxx" 分组用区间表示为 [3,6] 。
# 我们称所有包含大于或等于三个连续字符的分组为 较大分组 。
# 找到每一个 较大分组 的区间，按起始位置下标递增顺序排序后，返回结果。


# 双指针
class Solution:
    def largeGroupPositions(self, s: str):
        res = []
        number, length = 1, len(s)
        for i in range(1, length):
            if s[i] == s[i - 1]:
                if i == length - 1 and number >= 2:
                    res.append([i - number, i])
                else:
                    number += 1
            else:
                if number >= 3:
                    res.append([i - number, i - 1])
                number = 1
        return res
