# 给定一个无重复元素的有序整数数组 nums 。
# 返回 恰好覆盖数组中所有数字 的 最小有序 区间范围列表。也就是说，nums 的每个元素都恰好被某个区间范围所覆盖，并且不存在属于某个范围但不属于 nums 的数字 x 。
# 列表中的每个区间范围 [a,b] 应该按如下格式输出：
# "a->b" ，如果 a != b
# "a" ，如果 a == b


class Solution:
    def summaryRanges(self, nums):
        if not nums:
            return []
        res = []
        left, right = 0, 1
        while right < len(nums):
            if nums[right] != nums[right - 1] + 1:
                if nums[right - 1] == nums[left]:
                    res.append(str(nums[left]))
                else:
                    res.append(str(nums[left]) + "->" + str(nums[right - 1]))
                left = right
            right += 1
        if nums[right - 1] == nums[left]:
            res.append(str(nums[left]))
        else:
            res.append(str(nums[left]) + "->" + str(nums[right - 1]))
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [0,2,3,4,6,8,9]
    print(s.summaryRanges(nums))