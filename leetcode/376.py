# 如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为摆动序列。第一个差（如果存在的话）可能是正数或负数。少于两个元素的序列也是摆动序列。
# 例如， [1,7,4,9,2,5] 是一个摆动序列，因为差值 (6,-3,5,-7,3) 是正负交替出现的。相反, [1,4,7,2,5] 和 [1,7,4,5,5] 不是摆动序列，第一个序列是因为它的前两个差值都是正数，第二个序列是因为它的最后一个差值为零。
# 给定一个整数序列，返回作为摆动序列的最长子序列的长度。 通过从原始序列中删除一些（也可以不删除）元素来获得子序列，剩下的元素保持其原始顺序。

# 方法1 普通dp
class Solution:
    def wiggleMaxLength(self, nums) -> int:
        length = len(nums)
        if length < 2:
            return length
        up = [1] * length
        down = [1] * length
        for i in range(1, length):
            if nums[i] > nums[i - 1]:
                up[i] = max(up[i - 1], down[i - 1] + 1)
                down[i] = down[i - 1]
            elif nums[i] < nums[i - 1]:
                up[i] = up[i - 1]
                down[i] = max(down[i - 1], up[i - 1] + 1)
            else:
                up[i] = up[i - 1]
                down[i] = down[i - 1]
        return max(up[-1], down[-1])


# 方法2 优化dp
class Solution:
    def wiggleMaxLength(self, nums) -> int:
        length = len(nums)
        if length < 2:
            return length
        up, down = 1, 1
        for i in range(1, length):
            if nums[i] > nums[i - 1]:
                up = max(up, down + 1)
            elif nums[i] < nums[i - 1]:
                down = max(down, up + 1)
        return max(up, down)


# 方法3 贪心
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        length = len(nums)
        if length < 2:
            return length
        prediff = nums[1] - nums[0]
        res = 2 if prediff != 0 else 1
        for i in range(2, length):
            temp = nums[i] - nums[i - 1]
            if (temp > 0 and prediff <= 0) or (temp < 0 and prediff >= 0):
                res += 1
                prediff = temp
        return res