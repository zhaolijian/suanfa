# 给定一个整数数组和一个整数 k，你需要在数组里找到不同的 k-diff 数对，并返回不同的 k-diff 数对 的数目。
#
# 这里将 k-diff 数对定义为一个整数对 (nums[i], nums[j])，并满足下述全部条件：
#
# 0 <= i, j < nums.length
# i != j
# |nums[i] - nums[j]| == k
# 注意，|val| 表示 val 的绝对值。


# 方法1 哈希
class Solution:
    def findPairs(self, nums, k: int) -> int:
        res = set()
        cur = set()
        for ele in nums:
            if ele - k in cur:
                res.add((ele - k, ele))
            if ele + k in cur:
                res.add((ele, ele + k))
            cur.add(ele)
        return len(res)


# 方法2 双指针
class Solution:
    def findPairs(self, nums, k: int) -> int:
        res = 0
        length = len(nums)
        nums.sort()
        slow, fast = 0, 1
        while fast < length:
            diff = nums[fast] - nums[slow]
            if diff == k:
                res += 1
                while fast < length - 1 and nums[fast] == nums[fast + 1]:
                    fast += 1
                fast += 1
                while slow < length - 1 and nums[slow] == nums[slow + 1]:
                    slow += 1
                slow += 1
                if slow >= fast:
                    fast += 1
            elif diff > k:
                slow += 1
                if slow >= fast:
                    fast += 1
            else:
                fast += 1
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [1, 3, 1, 5, 4]
    k = 0
    print(s.findPairs(nums, k))