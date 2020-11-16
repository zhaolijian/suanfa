class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        init = [1]
        temp = 1
        for i in range(1, len(nums)):
            temp = temp * nums[i - 1]
            init.append(temp)
        temp = 1
        for i in range(len(nums) - 2, -1, -1):
            temp = temp * nums[i + 1]
            init[i] *= temp
        return init