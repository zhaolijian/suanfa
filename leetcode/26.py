class Solution:
    def removeDuplicates(self, nums) -> int:
        if len(nums) == 0:
            return 0
        temp = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[temp] = nums[i]
                temp += 1
        return temp


if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 2]
    print(s.removeDuplicates(nums))