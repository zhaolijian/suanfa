# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 你可以假设数组中无重复元素。


# 关于例如到底是 while(left < right) 还是 while(left <= right)，到底是right = middle呢，还是要right = middle - 1呢？问题的链接：
# https://mp.weixin.qq.com/s/fCf5QbPDtE6SSlZ1yh_q8Q
# 方法1 二分查找，时间复杂度O(nlogn),空间复杂度O(1)  左闭右闭，所以left = mid + 1、right = mid - 1
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 一共有四种情况
        # 1) 插入位置在最左侧
        # 2) 插入位置在最右侧
        # 3) 插入位置在中间且没有找到
        # 4) 数组中能找到元素
        length = len(nums)

        # 下面这两种情况的判断被包含在之后代码中了，不写就行
        # # nums为空或者插入位置在最左侧
        # if not length or target < nums[0]:
        #     return 0
        # # 插入位置在最右侧
        # if target > nums[-1]:
        #     return length

        left, right = 0, length - 1
        while left <= right:
            mid = (left + right) // 2
            if target > nums[mid]:
                left = mid + 1
            # 数组中能找到元素
            elif target == nums[mid]:
                return mid
            else:
                right = mid - 1
        # 插入位置在中间且没有找到
        return left


# 方法2 二分查找  左闭右开，所以left = mid + 1、right = mid
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)
        left, right = 0, length
        while left < right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid
        return left


# 方法3 遍历，时间复杂度O(n),空间复杂度O(1)
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)
        i = 0
        while i < length:
            if target > nums[i]:
                i += 1
            else:
                return i
        return length