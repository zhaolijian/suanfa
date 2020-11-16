# 给你一个整数数组 arr 和一个整数 k。
# 首先，我们要对该数组进行修改，即把原数组 arr 重复 k 次。
# 举个例子，如果 arr = [1, 2] 且 k = 3，那么修改后的数组就是 [1, 2, 1, 2, 1, 2]。
# 然后，请你返回修改后的数组中的最大的子数组之和。
# 注意，子数组长度可以是 0，在这种情况下它的总和也是 0。
# 由于 结果可能会很大，所以需要 模（mod） 10^9 + 7 后再返回。 
class Solution:
    def kConcatenationMaxSum(self, arr, k: int) -> int:
        length = len(arr)
        res = 0
        if length < 2:
            return max(arr[0], res)
        sum_number = sum(arr)
        # arr最大子数组
        max_single, temp = 0, 0
        for i in range(length):
            temp += arr[i]
            if temp > 0:
                max_single = max(max_single, temp)
            else:
                temp = 0
        # arr右侧最大子数组
        max_r, temp = 0, 0
        for i in range(length - 1, -1, -1):
            temp += arr[i]
            max_r = max(max_r, temp)
        # arr左侧最大子数组
        max_l, temp =0, 0
        for i in range(length):
            temp += arr[i]
            max_l = max(max_l, temp)
        if sum_number > 0:
            return max(max_r + (k - 2) * sum_number + max_l, max_single) % 1000000007
        else:
            return max(max_r + max_l, max_single) % 1000000007


if __name__ == '__main__':
    s = Solution()
    arr = [-5,4,-4,-3,5,-3]
    k = 3
    print(s.kConcatenationMaxSum(arr, k))