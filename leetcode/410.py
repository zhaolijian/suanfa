# 分割数组的最大值
# 给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。设计一个算法使得这 m 个子数组各自和的最大值最小。
# 注意:
# 数组长度 n 满足以下条件:
# 1 ≤ n ≤ 1000
# 1 ≤ m ≤ min(50, n)


# 方法1： 二分查找,时间复杂度O(n×log(sum−maxn))， 空间复杂度O(1)
class Solution:
    def splitArray(self, nums, m: int) -> int:
        def func(value):
            res = 1
            temp = 0
            for ele in nums:
                if temp + ele > value:
                    res += 1
                    temp = ele
                else:
                    temp += ele
            return res <= m
        # 设置桶容量的最小值为数组中的最大值，桶的最大值为数组的和(这时只需一个桶),最终桶的大小肯定位于两者之间，则使用二分查找法查找
        min_val, max_val = max(nums), sum(nums)
        while min_val < max_val:
            mid = (min_val + max_val) // 2
            if func(mid):
                max_val = mid
            else:
                min_val = mid + 1
        return min_val


# 方法2 动态规划，时间复杂度O(n^2*m)，空间复杂度O(mn)
class Solution:
    def splitArray(self, nums, m: int) -> int:
        n = len(nums)
        f = [[10 ** 18] * (m + 1) for _ in range(n + 1)]
        sub = [0]
        for elem in nums:
            sub.append(sub[-1] + elem)

        f[0][0] = 0
        for i in range(1, n + 1):
            for j in range(1, min(i, m) + 1):
                for k in range(i):
                    f[i][j] = min(f[i][j], max(f[k][j - 1], sub[i] - sub[k]))

        return f[n][m]


if __name__ == '__main__':
    s = Solution()
    nums = [7,2,5,10,8]
    m = 2
    print(s.splitArray(nums, m))