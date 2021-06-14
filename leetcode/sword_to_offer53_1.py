# 统计一个数字在排序数组中出现的次数。


# 方法1  二分查找
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def func(nums, flag):
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] > target or (flag and nums[mid] == target):
                    right = mid
                else:
                    left = mid + 1
            return left

        index = func(nums, True)
        if index == len(nums) or nums[index] != target:
            return 0
        # return func(nums, False) - index
        # 在右半段nums[index:]找,target最右边的下一个位置为：nums[index:] + index
        # 区间长度nums[index:] + index - index = nums[index:]
        return func(nums[index:], False)


# 方法2
# from bisect import bisect_left, bisect_right
#
#
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         if not nums:
#             return 0
#         index_left = bisect_left(nums, target)
#         index_right = bisect_right(nums, target)
#         if index_left < len(nums) and nums[index_left] == target:
#             left = index_left
#         else:
#             return 0
#         return index_right - left


if __name__ == '__main__':
    s = Solution()
    nums = [5,7,7,8,8,10]
    target = 8
    print(s.search(nums, target))