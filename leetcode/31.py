# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
# 必须原地修改，只允许使用额外常数空间。
# 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        def quick_sort(left, right):
            if left >= right:
                return
            low, high = left, right
            key = nums[left]
            while left < right:
                while left < right and nums[right] >= key:
                    right -= 1
                nums[left] = nums[right]
                while left < right and nums[left] <= key:
                    left += 1
                nums[right] = nums[left]
            nums[left] = key
            quick_sort(low, left - 1)
            quick_sort(left + 1, high)

        # 是否有更大排列
        flag = False
        # 从后往前遍历第一个不符合后者比前者大的位置
        index = -1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                flag = True
                index = i - 1
                break
        # 说明已经是最大的排列了,则返回最小排列
        if not flag:
            left, right = 0, len(nums) - 1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        # 有更大排列
        else:
            # 找到比index位置值大的最小值
            # 差
            number = float('inf')
            bigger_index = -1
            for i in range(index + 1, len(nums)):
                if nums[i] > nums[index] and nums[i] - nums[index] < number:
                    number = nums[i] - nums[index]
                    bigger_index = i
            nums[bigger_index], nums[index] = nums[index], nums[bigger_index]
            # 使得nums[index+1:]称为一个升序队列,可以使用快速排序
            quick_sort(index + 1, len(nums) - 1)


class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return nums
        flag = 0
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                flag = 1
                # 选择比 nums[i - 1] 大的最小值
                temp = float('inf')
                index = 0
                for j in range(i, len(nums)):
                    if nums[j] > nums[i - 1] and nums[j] - nums[i - 1] < temp:
                        temp = nums[j] - nums[i - 1]
                        index = j
                nums[i - 1], nums[index] = nums[index], nums[i -1]
                # 冒泡排序
                for k in range(i, len(nums) - 1):
                    for m in range(len(nums) - 1, k, -1):
                        if nums[m] < nums[m + 1]:
                            nums[m], nums[m + 1] = nums[m + 1], nums[m]
                break
        if flag == 0:
            l, r = 0, len(nums) - 1
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1


if __name__ == '__main__':
    s = Solution()
    nums = list(map(int, input().split()))
    print(s.nextPermutation(nums))