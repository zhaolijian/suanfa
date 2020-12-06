# 给定一个直方图(也称柱状图)，假设有人从上面源源不断地倒水，最后直方图能存多少水量?直方图的宽度为 1。

# 两次遍历
class Solution:
    def trap(self, height) -> int:
        length = len(height)
        res = 0
        if length < 3:
            return 0
        max_array = [height[-1]]
        for i in range(length - 2, -1, -1):
            max_array.append(max(max_array[-1], height[i]))
        max_array = max_array[::-1]
        max_height = 0
        for i in range(length):
            if height[i] > max_height:
                max_height = height[i]
            res += min(max_height, max_array[i]) - height[i]
        return res


class Solution:
    def trap(self, height) -> int:
        length = len(height)
        if length < 3:
            return 0
        res = 0
        left_max = [0] * length
        right_max = [0] * length
        left_max[0], right_max[-1] = height[0], height[-1]
        for i in range(1, length):
            left_max[i] = max(left_max[i - 1], height[i])
        for i in range(length - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])
        for i in range(length):
            res += min(left_max[i], right_max[i]) - height[i]
        return res


# 方法2 双指针之比较最大值
class Solution:
    def trap(self, height) -> int:
        length = len(height)
        if length < 3:
            return 0
        left, right = 0, length - 1
        left_max, right_max = height[left], height[right]
        res = 0
        while left < right:
            if left_max < right_max:
                res += left_max - height[left]
                left += 1
                left_max = max(left_max, height[left])
            else:
                res += right_max - height[right]
                right -= 1
                right_max = max(right_max, height[right])
        return res


# 双指针之比较遍历当前值
class Solution:
    def trap(self, height) -> int:
        length = len(height)
        if length < 3:
            return 0
        left, right = 0, length - 1
        left_max, right_max = height[left], height[right]
        res = 0
        while left < right:
            if height[left] < height[right]:
                res += min(left_max, right_max) - height[left]
                left += 1
                left_max = max(left_max, height[left])
            else:
                res += min(left_max, right_max) - height[right]
                right -= 1
                right_max = max(right_max, height[right])
        return res


if __name__ == '__main__':
    s = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(s.trap(height))