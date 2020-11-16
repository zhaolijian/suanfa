# 你有 4 张写有 1 到 9 数字的牌。你需要判断是否能通过 *，/，+，-，(，) 的运算得到 24。
class Solution:
    def judgePoint24(self, nums) -> bool:
        if not nums:
            return False
        if len(nums) == 1:
            return abs(nums[0] - 24) < 1e-6
        for i, x in enumerate(nums):
            for j, y in enumerate(nums):
                if i != j:
                    array = []
                    for k, val in enumerate(nums):
                        if k !=i and k != j:
                            array.append(nums[k])
                    for p in range(4):
                        if p < 2 and i > j:
                            continue
                        if p == 0:
                            array.append(x * y)
                        elif p == 1:
                            array.append(x + y)
                        elif p == 2:
                           array.append(x - y)
                        else:
                            if y < 1e-6:
                                continue
                            else:
                                array.append(x / y)
                        if self.judgePoint24(array):
                            return True
                        array.pop()
        return False


if __name__ == '__main__':
    s = Solution()
    nums = [4,1,8,7]
    print(s.judgePoint24(nums))