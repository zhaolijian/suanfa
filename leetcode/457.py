# 给定一个含有正整数和负整数的环形数组 nums。 如果某个索引中的数 k 为正数，则向前移动 k 个索引。相反，如果是负数 (-k)，则向后移动 k 个索引。
# 因为数组是环形的，所以可以假设最后一个元素的下一个元素是第一个元素，而第一个元素的前一个元素是最后一个元素。
# 确定 nums 中是否存在循环（或周期）。循环必须在相同的索引处开始和结束并且循环长度 > 1。
# 此外，一个循环中的所有运动都必须沿着同一方向进行。换句话说，一个循环中不能同时包括向前的运动和向后的运动。
class Solution:
    def circularArrayLoop(self, nums) -> bool:
        length = len(nums)
        temp = nums + nums
        temp1 = nums[::-1] + nums[::-1]
        for i, number in enumerate(nums):
            if number > 0:
                start = i
                # 循环长度
                number = 0
                while start < i + length:
                    if temp[start] < 0:
                        break
                    number += 1
                    start += temp[start]
                    if start == i + length:
                        if number == 1:
                            return False
                        return True
            else:
                cur = length - 1 - i
                start = cur
                # 循环长度
                number = 0
                while start < cur + length:
                    if temp1[start] > 0:
                        break
                    number += 1
                    start += abs(temp1[start])
                    if start == cur + length:
                        if number == 1:
                            return False
                        return True
        return False


if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3,4,5]
    print(s.circularArrayLoop(nums))