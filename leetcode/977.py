# 给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。

# 方法1 双指针
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        length = len(A)
        res = [0] * length
        left, right, index = 0, length - 1, length - 1
        while left <= right:
            if abs(A[left]) >= abs(A[right]):
                res[index] = pow(A[left], 2)
                left += 1
            else:
                res[index] = pow(A[right], 2)
                right -= 1
            index -= 1
        return res


# 方法2 找到小于0和大于等于0的点然后用双指针
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        length = len(A)
        res = []
        left = -1
        for i in range(length):
            if A[i] < 0:
                left = i
        right = left + 1
        while left >= 0 and right < length:
            if abs(A[left]) < abs(A[right]):
                res.append(pow(A[left], 2))
                left -= 1
            else:
                res.append(pow(A[right], 2))
                right += 1
        while left >= 0:
            res.append(pow(A[left], 2))
            left -= 1
        while right < length:
            res.append(pow(A[right], 2))
            right += 1
        return res


if __name__ == '__main__':
    s = Solution()
    A = [-2, 0]
    print(s.sortedSquares(A))