# 给定一个整数数组 A，如果它是有效的山脉数组就返回 true，否则返回 false。
# 让我们回顾一下，如果 A 满足下述条件，那么它是一个山脉数组：
# A.length >= 3
# 在 0 < i < A.length - 1 条件下，存在 i 使得：
# A[0] < A[1] < ... A[i-1] < A[i]
# A[i] > A[i+1] > ... > A[A.length - 1]

# 方法1
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        length = len(A)
        left, right = 0, length - 1
        while left < length - 1 and A[left] < A[left + 1]:
            left += 1
        while right > 0 and A[right - 1] > A[right]:
            right -= 1
        return left == right and left != 0 and left != length - 1

# 方法2
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        length = len(A)
        if length < 3:
            return False
        index = - 1
        for i in range(1, length):
            if A[i] == A[i - 1]:
                return False
            elif A[i] < A[i - 1]:
                index = i - 1
                break
        if index == 0 or index == length - 1:
            return False
        for i in range(index + 1, length):
            if A[i] >= A[i - 1]:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    A = [9,8,7,6,5,4,3,2,1,0]
    print(s.validMountainArray(A))