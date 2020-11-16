# -*- coding:utf-8 -*-


# 插入算法思想
# class Solution:
#     def reOrderArray(self, array):
#         k = 0
#         for i in range(len(array)):
#             # 如果array[i]是奇数
#             if array[i] % 2 == 1:
#                 j = i
#                 while j > k:
#                     tmp = array[j]
#                     array[j] = array[j-1]
#                     array[j-1] = tmp
#                     j -= 1
#                 k += 1
#         return array




# class Solution:
#     def reOrderArray(self, array):
#         k = 0
#         for i in range(len(array)):
#             # 如果array[i]是奇数，则插入到前面去,中间的所有数后移
#             if array[i] % 2 == 1:
#                 temp = array[i]
#                 array[k + 1: i + 1] = array[k: i]
#                 array[k] = temp
#                 k += 1
#         return array


class Solution:
    def reOrderArray(self, array):
        for i in range(len(array)):
            if array[i] % 2 == 0:
                for j in range(i+1, len(array)):
                    if array[j] % 2 == 1:
                        temp = array[i]
                        array[i] = array[j]
                        array[j] = temp
                        break
        return array


if __name__ == '__main__':
    s = Solution()
    array = [1, 2, 3, 4, 5, 6, 7]
    print(s.reOrderArray(array))











