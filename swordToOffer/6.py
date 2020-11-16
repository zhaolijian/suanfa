# -*- coding:utf-8 -*-


# 方法1：普通遍历
# class Solution:
#     # 非递减序列是后一个>=前一个
#     def minNumberInRotateArray(self, rotateArray):
#         if len(rotateArray) == 0:
#             return 0
#         for i in range(len(rotateArray) - 1):
#             if rotateArray[i] > rotateArray[i + 1]:
#                 return rotateArray[i + 1]
#         # rotateArray中只有一个元素值（包括只有一个数以及所有数相等两种情况）
#         return rotateArray[0]


# 方法2：二叉遍历
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0:
            return 0
        low = 0
        high = len(rotateArray) - 1
        while low < high:
            # 比如情况10111，加上该条件后可以满足
            if rotateArray[low] < rotateArray[high]:
                return rotateArray[low]
            mid = (low + high) // 2
            # 说明mid在第一个递增序列中（其实也可以在第二个递增序列中，这样上面语句就直接return了）
            if rotateArray[mid] > rotateArray[low]:
                low = mid + 1
            # 说明mid在第二个递增序列中
            elif rotateArray[mid] < rotateArray[high]:
                high = mid
            else:
                # 比如只有2、1两个数，low=middle=0,high=1
                low += 1
        return rotateArray[low]


if __name__ == '__main__':
    s = Solution()
    # rotateArray = [1, 0, 1, 1, 1]
    rotateArray = [6501,6828,6963,7036,7422,7674,8146,8468,8704,8717,9170,9359,9719,9895,9896,9913,9962,154,293,334,492,1323,1479,1539,1727,1870,1943,2383,2392,2996,3282,3812,3903,4465,4605,4665,4772,4828,5142,5437,5448,5668,5706,5725,6300,6335]
    print(s.minNumberInRotateArray(rotateArray))
