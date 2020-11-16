# 方法1 快速排序
class Solution:
    def sortArray(self, nums):
        def func(left, right):
            if right <= left:
                return
            low, high = left, right
            key = nums[left]
            while left < right:
                while left < right and nums[right] >= key:
                    right -= 1
                nums[left] = nums[right]
                while left < right and nums[left] <= key:
                    left += 1
                nums[right] = nums[left]
            nums[left] = key
            func(low, left - 1)
            func(left + 1, high)

        length = len(nums)
        func(0, length - 1)
        return nums

# 方法2 sorted方法
# class Solution:
#     def sortArray(self, nums):
#         return sorted(nums)


# 方法3 归并排序
# class Solution:
#     def sortArray(self, nums):
#         length = len(nums)
#         if length <= 1:
#             return nums
#         mid = length // 2
#         left = self.sortArray(nums[:mid])
#         right = self.sortArray(nums[mid:])
#         i, j = 0, 0
#         res = []
#         while i < mid and j < length - mid:
#             if left[i] < right[j]:
#                 res.append(left[i])
#                 i += 1
#             else:
#                 res.append(right[j])
#                 j += 1
#         if i < mid:
#             res += left[i:]
#         if j < length - mid:
#             res += right[j:]
#         return res


if __name__ == '__main__':
    s = Solution()
    nums = [5,1,1,2,0,0]
    print(s.sortArray(nums))