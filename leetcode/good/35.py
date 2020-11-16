# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
#
# 你可以假设数组中无重复元素。
#
# 示例 1:
#
# 输入: [1,3,5,6], 5
# 输出: 2
# 示例 2:
#
# 输入: [1,3,5,6], 2
# 输出: 1
# 示例 3:
#
# 输入: [1,3,5,6], 7
# 输出: 4
# 示例 4:
#
# 输入: [1,3,5,6], 0
# 输出: 0


# 二分查找
# 将值与数组中间位置元素比较
# 如果相等返回位置
# 如果中间位置元素大于寻找值，则在中间位置右侧开始寻找
# 如果中间位置元素小于寻找值，则在中间位置左侧开始寻找
class Solution:
    def searchInsert(self, nums, target: int) -> int:
        r = len(nums)-1
        l = 0
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return l


if __name__ == '__main__':
    s = Solution()
    list_input = list(map(int, input().strip().split()))
    number = int(input())
    result = s.searchInsert(list_input, number)
    print(result)
