# -*- coding:utf-8 -*-
# import collections
#
#
# class Solution:
#     def MoreThanHalfNum_Solution(self, numbers):
#         c = collections.Counter(numbers)
#         for ele in c:
#             if c[ele] > float(len(numbers))/2:
#                 return ele
#         return 0


import collections
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        length = len(numbers)
        ccc = collections.Counter(numbers)
        for key in ccc:
            if ccc[key] > length // 2:
                return key
        return 0


if __name__ == '__main__':
    numbers = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    s = Solution()
    print(s.MoreThanHalfNum_Solution(numbers))