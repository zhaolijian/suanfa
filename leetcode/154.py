# 寻找旋转排序数组中的最小值 II
# 方法1 二分查找
class Solution:
    def findMin(self, nums: List[int]) -> int:
        length = len(nums)
        left, right = 0, length - 1
        while left < right:
            mid = (left + right) // 2
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            elif nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]


# 和上面方法基本一样
class Solution:
    def findMin(self, nums: List[int]) -> int:
        length = len(nums)
        left, right = 0, length - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1
        return nums[left]