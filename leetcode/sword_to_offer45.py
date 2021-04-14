# 输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。


# 自定义排序字符串
from functools import cmp_to_key
class Solution:
    def minNumber(self, nums) -> str:
        def cmp(x, y):
            if x + y > y + x:
                return 1
            elif x + y < y + x:
                return -1
            else:
                return 0
        strs = map(str, nums)
        result = sorted(strs, key=cmp_to_key(cmp))
        return "".join(result)