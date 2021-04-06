# 给定一个增序排列数组 nums ，你需要在 原地 删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。
# 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。


class Solution:
    def removeDuplicates(self, nums) -> int:
        left = 1
        number = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                number += 1
                if number <= 2:
                    nums[left] = nums[i]
                    left += 1
            else:
                nums[left] = nums[i]
                left += 1
                number = 1
        return left


if __name__ == '__main__':
    s = Solution()
    nums = [1,1,1,2,2,3]
    print(s.removeDuplicates(nums))