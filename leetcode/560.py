class Solution:
    def subarraySum(self, nums, k: int) -> int:
        if len(nums) == 0:
            return 0
        # 初始化字典（哈希表），设置-1项的值为0
        # 存储前缀及出现次数
        d = {0: 1}
        pre_sum = 0
        cnt = 0
        for num in nums:
            pre_sum += num
            # 从开始到当前遍历值之前的值（m）之间的和，如果等于pre_sum-k，则说明从m之后到当前遍历值的和为k
            if d.get(pre_sum-k):
                cnt += d[pre_sum-k]
            if d.get(pre_sum):
                d[pre_sum] += 1
            else:
                d[pre_sum] = 1
        return cnt


if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 1]
    k = 2
    print(s.subarraySum(nums, k))