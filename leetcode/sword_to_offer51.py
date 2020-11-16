# # 数组中的逆序对
# class Solution:
#     def __init__(self):
#         self.res = 0
#
#     def reversePairs(self, nums) -> int:
#         def func(nums):
#             length = len(nums)
#             if length <= 1:
#                 return nums
#             mid = length // 2
#             left = func(nums[:mid])
#             right = func(nums[mid:])
#             result = []
#             i, j = 0, 0
#             len_l, len_r = len(left), len(right)
#             while i < len_l and j < len_r:
#                 if left[i] <= right[j]:
#                     result.append(left[i])
#                     i += 1
#                 else:
#                     result.append(right[j])
#                     self.res += len_l - i
#                     j += 1
#             if i < len_l:
#                 result += left[i:]
#             if j < len_r:
#                 result += right[j:]
#             return result
#
#         func(nums)
#         return self.res

class Solution:
    def reversePairs(self, nums) -> int:
        def func(nums):
            nonlocal res
            if len(nums) <= 1:
                return nums
            mid = (len(nums) - 1) // 2
            array = []
            l, r = func(nums[: mid + 1]), func(nums[mid + 1:])
            i, j = 0, 0
            len_l, len_r = mid + 1, len(nums) - 1 - mid
            while i < len_l and j < len_r:
                if l[i] <= r[j]:
                    array.append(l[i])
                    i += 1
                else:
                    res += len_l - i
                    array.append(r[j])
                    j += 1
            if i < len_l:
                array += l[i:]
            if j < len_r:
                array += r[j:]
            return array
        res = 0
        func(nums)
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [7,5,6,4]
    print(s.reversePairs(nums))