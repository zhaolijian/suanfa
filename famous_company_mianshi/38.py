# 给定两个有序数组arr1和arr2，已知两个数组的长度都为N，求两个数组中所有数的上中位数。
# 上中位数：假设递增序列长度为n，若n为奇数，则上中位数为第n/2+1个数；否则为第n/2个数
# [要求]
# 时间复杂度为O(logN)O(logN)，额外空间复杂度为O(1)O(1)
class Solution:
    def findMedianinTwoSortedAray(self , arr1 , arr2 ):
        length = len(arr1)
        l1, r1, l2, r2 = 0, length - 1, 0, length - 1
        while l1 < r1:
            mid_1 = (l1 + r1) // 2
            mid_2 = (l2 + r2) // 2
            # 数组长度
            temp_len = r1 - l1 + 1
            if arr1[mid_1] < arr2[mid_2]:
                # 如果数组长度为偶数,则l1 = mid_1 + 1,两个新数组长度也为偶数,两个新数组的中位数即总体中位数
                # 如果数组长度为奇数,则l1 = mid_1,两个新数组长度为奇数,两个新数组的中位数即总体中位数
                l1 = mid_1 + (1 if temp_len % 2 == 0 else 0)
                r2 = mid_2
            elif arr1[mid_1] > arr2[mid_2]:
                l2 = mid_2 + (1 if temp_len % 2 == 0 else 0)
                r1 = mid_1
            else:
                return arr1[mid_1]
        return min(arr1[l1], arr2[l2])

