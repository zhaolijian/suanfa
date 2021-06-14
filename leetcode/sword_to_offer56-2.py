# 在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字

# 对于出现三次的数字，各二进制位出现的次数都是3的倍数。
# 因此，统计所有数字的各二进制位中1的出现次数，并对 3求余，结果则为只出现一次的数字。
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        init = [0] * 32
        for ele in nums:
            for i in range(32):
                if (ele >> i) & 1 == 1:
                    init[i] += 1
        res = 0
        for i in range(32):
            if init[i] % 3 == 1:
                res += pow(2, i)
        return res