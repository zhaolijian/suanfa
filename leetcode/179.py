# 给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
# 注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。

# 方法1 使用自定义排序比较数字
from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums) -> str:
        def cmp(x, y):
            len_x = len(str(x))
            len_y = len(str(y))
            temp_x = x * pow(10, len_y) + y
            temp_y = y * pow(10, len_x) + x
            if temp_x > temp_y:
                return 1
            elif temp_x < temp_y:
                return -1
            else:
                return 0

        result = sorted(nums, key=cmp_to_key(cmp), reverse=True)
        return "0" if result[0] == 0 else "".join(map(str, result))


# 方法2 使用自定义排序比较字符串
from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums) -> str:
        def cmp(x, y):
            if x + y > y + x:
                return 1
            elif x + y < y + x:
                return -1
            else:
                return 0

        strs = map(str, nums)
        result = sorted(strs, key=cmp_to_key(cmp), reverse=True)
        return "0" if result[0] == "0" else "".join(result)