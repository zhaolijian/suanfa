# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
# 注意：
# 答案中不可以包含重复的四元组。


class Solution:
    def fourSum(self, nums, target: int):
        length = len(nums)
        res = []
        nums.sort()
        for i in range(length - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            else:
                for j in range(i + 1, length - 2):
                    if j == i + 1 or nums[j] != nums[j - 1]:
                        number = target - nums[i] - nums[j]
                        left, right = j + 1, length - 1
                        while left < right:
                            if nums[left] + nums[right] == number:
                                res.append([nums[i], nums[j], nums[left], nums[right]])
                                while left + 1 < right and nums[left] == nums[left + 1]:
                                    left += 1
                                left += 1
                                while right - 1 > left and nums[right] == nums[right - 1]:
                                    right -= 1
                                right -= 1
                            elif nums[left] + nums[right] > number:
                                right -= 1
                            else:
                                left += 1
        return res