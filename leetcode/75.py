# 两侧双指针
class Solution:
    def sortColors(self, nums) -> None:
        if len(nums) == 0:
            return
        # 红色交换位置,蓝色交交换位置
        l, current, r = 0, 0, len(nums) - 1
        while current <= r:
            if nums[current] == 0:
                nums[current], nums[l] = nums[l], nums[current]
                l += 1
                current += 1
            elif nums[current] == 2:
                nums[current], nums[r] = nums[r], nums[current]
                r -= 1
            else:
                current += 1

                
if __name__ == '__main__':
    s = Solution()
    nums = list(map(int, input().split()))
    print(s.sortColors(nums))

# 单侧双指针
# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         length = len(nums)
#         if length == 0:
#             return
#         # 每一种颜色球的插入位置
#         red, white = 0, 0
#         for i in range(length):
#             if nums[i] == 0:
#                 nums.insert(red, 0)
#                 nums.pop(i + 1)
#                 red += 1
#                 white += 1
#             elif nums[i] == 1:
#                 nums.insert(white, 1)
#                 nums.pop(i + 1)
#                 white += 1