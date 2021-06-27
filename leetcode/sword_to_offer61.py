# 从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。

# 方法1
class Solution:
    def isStraight(self, nums) -> bool:
        nums.sort()
        # 如果不为0的一样的值,则False
        for i in range(1, 5):
            if nums[i] == nums[i - 1] and nums[i] != 0:
                return False
        # 找到第一个不为大小王的下标
        number = 0
        for ele in nums:
            if ele == 0:
                number += 1
            else:
                break
        # 非0最大值减去非0最小值的结果小于5，则True，否则False
        return nums[-1] - nums[number] < 5


# 方法2
class Solution:
    def isStraight(self, nums) -> bool:
        nums.sort()
        # 如果不为0的一样的值,则False
        for i in range(1, 5):
            if nums[i] == nums[i - 1] and nums[i] != 0:
                return False
        # 大小王的个数
        number = 0
        for ele in nums:
            if ele == 0:
                number += 1
            else:
                break
        # 如果大小王的个数大于等于4,则True
        if number >= 4:
            return True
        for i in range(number + 1, 5):
            number -= nums[i] - nums[i - 1] - 1
            if number < 0:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3,4,5]
    print(s.isStraight(nums))