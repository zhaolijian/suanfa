# 给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
class Solution:
    def twoSum(self, numbers, target: int):
        length = len(numbers)
        left, right = 0, length - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1


if __name__ == '__main__':
    s = Solution()
    numbers = [2,7,11,15]
    target = 9
    print(s.twoSum(numbers, target))