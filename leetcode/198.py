class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        init = [0 for i in range(len(nums))]
        init[0] = nums[0]
        init[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            init[i] = max(init[i - 2] + nums[i], init[i - 1])
        return init[-1]