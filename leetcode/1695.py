# 给你一个正整数数组 nums ，请你从中删除一个含有 若干不同元素 的子数组。删除子数组的 得分 就是子数组各元素之 和 。
# 返回 只删除一个 子数组可获得的 最大得分 。
# 如果数组 b 是数组 a 的一个连续子序列，即如果它等于 a[l],a[l+1],...,a[r] ，那么它就是 a 的一个子数组。


class Solution:
    def maximumUniqueSubarray(self, nums) -> int:
        res, cur = 0, 0
        left, right = 0, 0
        length = len(nums)
        s = set()
        while right < length:
            if nums[right] not in s:
                s.add(nums[right])
                cur += nums[right]
                res = max(res, cur)
                right += 1
            else:
                while nums[left] != nums[right]:
                    s.remove(nums[left])
                    cur -= nums[left]
                    left += 1
                s.remove(nums[left])
                cur -= nums[left]
                left += 1
        return res