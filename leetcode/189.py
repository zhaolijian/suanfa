# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。


# 方法1 翻转数组
class Solution:
    def rotate(self, nums, k: int) -> None:
        length = len(nums)
        k %= length
        nums.reverse()
        for i in range(k // 2):
            nums[i], nums[k - i - 1] = nums[k - i - 1], nums[i]
        for i in range((length - k) // 2):
            nums[k + i], nums[length - i - 1] = nums[length - i - 1], nums[k + i]

# 翻转数组
class Solution:
    def rotate(self, nums, k: int) -> None:
        length = len(nums)
        k %= length
        for i in range((length - k) // 2):
            nums[i], nums[length - k - 1 - i] = nums[length - k - 1 - i], nums[i]
        for i in range(k // 2):
            nums[length - k + i], nums[length - 1 - i] = nums[length - 1 - i], nums[length - k + i]
        nums.reverse()


# 方法2 环状替换
class Solution:
    def rotate(self, nums, k: int) -> None:
        length = len(nums)
        k %= length
        number = 0
        for i in range(k):
            current = i
            prev = nums[i]
            flag = False
            while not flag or i != current:
                flag = True
                next = (current + k) % length
                nums[next], prev = prev, nums[next]
                current = next
                number += 1
            if number == length:
                break


if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3,4,5,6,7]
    k = 3
    s.rotate(nums, k)