# 方法1 时间复杂度O(n),空间复杂度O(1)
class Solution:
    def findUnsortedSubarray(self, nums) -> int:
        length = len(nums)
        if length <= 1:
            return 0
        low, high = float('inf'), float('-inf')
        for i in range(length - 1):
            if nums[i + 1] < nums[i]:
                low = min(low, nums[i + 1])
        for i in range(length - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                high = max(high, nums[i])
        res_l, res_m = -1, -1
        for i in range(length):
            if nums[i] > low:
                res_l = i
                break
        for j in range(length - 1, -1, -1):
            if nums[j] < high:
                res_m = j
                break
        #  res_l == -1（res_r == -1）说明是单调递增
        return res_m - res_l + 1 if res_l != -1 else 0

# 方法2 栈 时间复杂度O(n),空间复杂度O（n）
# 从左往右遍历，不断压栈，使得栈中元素非递减，如果遍历值比栈的元素大，则弹出栈元素，从而找到左侧起始位置
# 从右往左遍历，。。。

if __name__ == '__main__':
    s = Solution()
    # nums = [2,6,4,8,10,9,15]
    nums = [1,2,3,4]
    print(s.findUnsortedSubarray(nums))