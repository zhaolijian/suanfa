# 方法1：使用数组存储0的位置
class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 0出现的位置
        array = []
        for i in range(len(nums)):
            if nums[i] != 0:
                if array:
                    index = array.pop(0)
                    nums[i], nums[index] = nums[index], nums[i]
                    array.append(i)
            else:
                array.append(i)


# 方法2： 遍历一次，碰到不为0的就交换
class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1


# 方法3： 两次遍历，把不为0的数前移，后面的全是0
class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        for i in range(j, len(nums)):
            nums[i] = 0


if __name__ == '__main__':
    s = Solution()
    nums = [0,1,0,3,12]
    print(s.moveZeroes(nums))