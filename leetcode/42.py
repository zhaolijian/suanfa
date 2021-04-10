# 方法1 动态编程
# 思路，遍历每个元素，找到该元素左侧最大值和该元素右侧最大值，取最小值减去该元素值
class Solution:
    def trap(self, height) -> int:
        length = len(height)
        if length < 3:
            return 0
        left_max_value, right_array, res = height[0], [height[-1]], 0
        for i in range(length - 2, -1, -1):
            if height[i] > right_array[-1]:
                right_array.append(height[i])
            else:
                right_array.append(right_array[-1])
        right_array = right_array[::-1]
        for i in range(1, length):
            left_max_value = max(left_max_value, height[i])
            temp = min(left_max_value, right_array[i]) - height[i]
            res += temp
        return res


# 方法2：栈
# class Solution:
#     def trap(self, height) -> int:
#         stack = []
#         res = 0
#         for i in range(len(height)):
#             while stack and height[i] > height[stack[-1]]:
#                 temp = stack.pop()
#                 if not stack:
#                     break
#                 h = min(height[i], height[stack[-1]]) - height[temp]
#                 w = i - stack[-1] - 1
#                 res += h * w
#             stack.append(i)
#         return res


# 方法3，双指针
class Solution:
    def trap(self, height) -> int:
        l, r = 0, len(height) - 1
        ans = 0
        left_max, right_max = 0, 0
        while l < r:
            if height[l] < height[r]:
                if height[l] >= left_max:
                    left_max = height[l]
                else:
                    ans += left_max - height[l]
                l += 1
            else:
                if height[r] >= right_max:
                    right_max = height[r]
                else:
                    ans += right_max - height[r]
                r -= 1
        return ans


if __name__ == '__main__':
    s = Solution()
    # height = [0,1,0,2,1,0,1,3,2,1,2,1]
    height = [2, 1, 0, 3]
    print(s.trap(height))