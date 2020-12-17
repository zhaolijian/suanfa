# 给定一个正整数数组 nums。
# 找出该数组内乘积小于 k 的连续的子数组的个数。
class Solution:
    def numSubarrayProductLessThanK(self, nums, k: int) -> int:
        res = 0
        left, right = 0, 0
        val = 1
        while right < len(nums):
            val *= nums[right]
            if val < k:
                right += 1
            else:
                res += right - left
                val //= nums[left]
                left += 1
                if right > left:
                    val //= nums[right]
                    right -= 1
                else:
                    val = 1
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [10,5,2,6]
    k = 100
    print(s.numSubarrayProductLessThanK(nums, k))