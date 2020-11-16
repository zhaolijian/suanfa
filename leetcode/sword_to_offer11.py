# 旋转数组的最小数字
# 方法1 二分查找 O(logn)
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        length = len(numbers)
        left, right = 0, length - 1
        while left < right:
            mid = (left + right) // 2
            if numbers[mid] > numbers[right]:
                left = mid + 1
            elif numbers[mid] < numbers[right]:
                right = mid
            else:
                right -= 1
        return numbers[left]


# 方法2 遍历 O(n)
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        length = len(numbers)
        res = numbers[0]
        for i in range(1, length):
            if numbers[i] >= numbers[i - 1]:
                continue
            else:
                res = numbers[i]
                break
        return res