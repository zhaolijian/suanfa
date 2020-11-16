# 二分查找
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        def func(mid):
            h, w = n - 1, 0
            temp = 0
            while h >= 0 and w < len(matrix[0]):
                if matrix[h][w] <= mid:
                    temp += h + 1
                    w += 1
                else:
                    h -= 1
            return temp >= k

        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            if func(mid):
                right = mid
            else:
                left = mid + 1
        return left