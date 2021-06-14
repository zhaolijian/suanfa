# 一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。


# 异或^的使用
class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        temp = 0
        for ele in nums:
            temp ^= ele
        # 找出temp中位为1的那位
        res = 0
        index = 0
        while temp:
            if (temp >> index) & 1 == 1:
                res = index
                break
            else:
                index += 1
        one, two = 0, 0
        for ele in nums:
            if (ele >> res) & 1 == 1:
                one ^= ele
            else:
                two ^= ele
        return [one, two]