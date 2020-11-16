# 给你一个整数数组 arr 。请你将数组中的元素按照其二进制表示中数字 1 的数目升序排序。
# 如果存在多个数字二进制中 1 的数目相同，则必须将它们按照数值大小升序排列。
# 请你返回排序后的数组。

# 方法1
from collections import defaultdict
class Solution:
    def sortByBits(self, arr):
        def number_ones(number):
            res = 0
            while number:
                # 这么写只计算1的个数，比下面的写法好
                number &= (number - 1)
                res += 1
            return res

        d = defaultdict(list)
        for ele in arr:
            d[number_ones(ele)].append(ele)
        res = []
        for key in sorted(d.keys()):
            d[key].sort()
            res += d[key]
        return res


# 方法2
from collections import defaultdict
class Solution:
    def sortByBits(self, arr):
        def number_ones(number):
            res = 0
            while number:
                if number & 1:
                    res += 1
                number >>= 1
            return res

        d = defaultdict(list)
        for ele in arr:
            d[number_ones(ele)].append(ele)
        res = []
        for key in sorted(d.keys()):
            d[key].sort()
            res += d[key]
        return res


if __name__ == '__main__':
    s = Solution()
    arr = [0,1,2,3,4,5,6,7,8]
    print(s.sortByBits(arr))