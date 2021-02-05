# 中位数是有序序列最中间的那个数。如果序列的大小是偶数，则没有最中间的数；此时中位数是最中间的两个数的平均数。
# 例如：
# [2,3,4]，中位数是 3
# [2,3]，中位数是 (2 + 3) / 2 = 2.5
# 给你一个数组 nums，有一个大小为 k 的窗口从最左端滑动到最右端。窗口中有 k 个数，每次窗口向右移动 1 位。
# 你的任务是找出每次窗口移动后得到的新窗口中元素的中位数，并输出由它们组成的数组。


# 滑动窗口+二分法（使用insort）
from bisect import bisect_left, insort
class Solution:
    def medianSlidingWindow(self, nums, k: int):
        sorted_array = sorted(nums[:k])
        length = len(nums)
        res = []
        for i in range(k - 1, length):
            if k % 2:
                res.append(sorted_array[(k - 1) // 2])
            else:
                res.append((sorted_array[k // 2 - 1] + sorted_array[k // 2]) / 2)
            rm_index = bisect_left(sorted_array, nums[i + 1 - k])
            sorted_array.pop(rm_index)
            if i < length - 1:
                insort(sorted_array, nums[i + 1])
        return res


# 滑动窗口+二分法（不使用insort）
from bisect import bisect_left
class Solution:
    def medianSlidingWindow(self, nums, k: int):
        sorted_array = sorted(nums[:k])
        length = len(nums)
        res = []
        for i in range(k - 1, length):
            if k % 2:
                res.append(sorted_array[(k - 1) // 2])
            else:
                res.append((sorted_array[k // 2 - 1] + sorted_array[k // 2]) / 2)
            rm_index = bisect_left(sorted_array, nums[i + 1 - k])
            sorted_array.pop(rm_index)
            if i < length - 1:
                insert_index = bisect_left(sorted_array, nums[i + 1])
                sorted_array.insert(insert_index, nums[i + 1])
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(s.medianSlidingWindow(nums, k))