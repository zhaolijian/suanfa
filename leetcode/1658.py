# 给你一个整数数组 nums 和一个整数 x 。每一次操作时，你应当移除数组 nums 最左边或最右边的元素，然后从 x 中减去该元素的值。
# 请注意，需要 修改 数组以供接下来的操作使用。
# 如果可以将 x 恰好 减到 0 ，返回 最小操作数 ；否则，返回 -1 。


# 这个题不断的左删右删，结果就是左边区间的累加和+右边区间的累加和=x，要看到本质，不要使用按照题目的思想一步一步计算，使用dfs的形式
# 方法1  累加和+哈希表
class Solution:
    def minOperations(self, nums, x: int) -> int:
        if sum(nums) < x:
            return -1
        res = float('inf')
        l_array, r_array = {}, {}
        left, right = 0, 0
        for i, ele in enumerate(nums):
            left += ele
            if left > x:
                break
            l_array[left] = i + 1
            if left == x:
                res = min(res, i + 1)
        for j, ele in enumerate(nums[::-1]):
            right += ele
            if right > x:
                break
            r_array[right] = j + 1
            if right == x:
                res = min(res, j + 1)
        for temp in l_array:
            if x - temp in r_array:
                res = min(res, l_array[temp] + r_array[x - temp])
        return res if res != float('inf') else -1


# 方法2 左右最短即中间最长 双指针
class Solution:
    def minOperations(self, nums, x: int) -> int:
        # 左右最短,即使中间最长,即求连续子区间的和等于sum(nums)-x的最长区间
        sum_val = sum(nums)
        length = len(nums)
        if sum_val < x:
            return -1
        if sum_val == x:
            return length
        target = sum_val - x
        left, right = 0, 0
        # 累加和
        cur_val = 0
        res = float('inf')
        while right < length:
            cur_val += nums[right]
            while cur_val >= target and left <= right:
                if cur_val == target:
                    res = min(res, length - right + left - 1)
                cur_val -= nums[left]
                left += 1
            right += 1
        return res if res != float('inf') else -1


# dfs，超时
# class Solution:
#     def minOperations(self, nums, x: int) -> int:
#         res = float('inf')
#
#         def func(nums, val, number):
#             nonlocal res
#             if not nums:
#                 return
#             if nums[0] == val or nums[-1] == val:
#                 res = min(res, number + 1)
#                 return
#             if nums[0] < val:
#                 func(nums[1:], val - nums[0], number + 1)
#             if nums[-1] < val:
#                 func(nums[:-1], val - nums[-1], number + 1)
#
#         func(nums, x, 0)
#         return -1 if res == float('inf') else res


if __name__ == '__main__':
    s = Solution()
    nums = [8828,9581,49,9818,9974,9869,9991,10000,10000,10000,9999,9993,9904,8819,1231,6309]
    x = 134365
    print(s.minOperations(nums, x))