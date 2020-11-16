# 方法一。复杂度O(n^2)
# -*- coding:utf-8 -*-


class Solution:
    # array 二维列表
    def Find(self, target, array):
        h = len(array)
        w = len(array[0])
        if h == 0 or w == 0:
            return False
        for i in range(h):
            if array[i][0] > target:
                return False
            for j in range(w):
                if array[i][j] < target:
                    continue
                elif array[i][j] == target:
                    return True
                else:
                    break
        return False


# 复杂度O(行数+列数) 331ms 5704k
# class Solution:
#     # array 二维列表
#     def Find(self, target, array):
#         h = len(array)
#         w = len(array[0])
#         row = h - 1
#         col = 0
#         while row >= 0 and col < w:
#             if array[row][col] > target:
#                 row -= 1
#             elif array[row][col] == target:
#                 return True
#             else:
#                 col += 1
#         return False


if __name__ == '__main__':
    s = Solution()
    array = [[1, 3, 5], [2, 4, 6]]
    target = 5
    print(s.Find(target, array))
