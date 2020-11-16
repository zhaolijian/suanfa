# 二分查找元素在有序数组中的位置，如果不存在，输出-1，如果存在，输出下标（存在多个，输出下标最小的）。
class Solution:
    # def func(self, nums, number):
    #     length = len(nums)
    #     left, right = 0, length - 1
    #     while left <= right:
    #         mid = (left + right) // 2
    #         if nums[mid] == number:
    #             return mid
    #         elif nums[mid] < number:
    #             left = mid + 1
    #         else:
    #             right = mid - 1
    #     return -1

    def func(self, nums, number):
        def solu(left, right):
            nonlocal res
            mid = (left + right) // 2
            if nums[mid] == number:
                res = mid
            if left < mid:
                solu(left, mid - 1)
            if mid < right:
                solu(mid + 1, right)

        length = len(nums)
        res = -1
        solu(0, length - 1)
        return res


if __name__ == '__main__':
    nums = list(map(int, input().split()))
    number = int(input())
    s = Solution()
    print(s.func(nums, number))