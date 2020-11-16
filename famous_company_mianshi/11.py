# 方法1 数学转换，复杂度O(1)
import math
class Solution:
    def sqrt(self, x):
        if x == 0:
            return 0
        temp = math.exp(0.5 * math.log(x))
        return temp + 1 if (temp + 1) * (temp + 1) <= x else temp


# 方法2 二分查找,复杂度O(logn)
import math
class Solution:
    def sqrt(self, x):
        l, r = 0, x
        res = 0
        while l <= r:
            mid = (l + r) // 2
            if pow(mid, 2) <= x:
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return res