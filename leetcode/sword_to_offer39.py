# 数组中出现次数超过一半的数字
# 方法1： 投票算法
# 由于众数出现的次数超过数组长度的一半；若记众数的票数+1 ，非众数的票数−1 ，则一定有所有数字的票数和>0 。
class Solution:
    def majorityElement(self, nums) -> int:
        candidata = -1
        number = 0
        for i in range(len(nums)):
            if number == 0:
                candidata = nums[i]
            number += 1 if candidata == nums[i] else - 1
        return candidata

# 方法2 哈希
# 方法3 排序