# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。
# 栈
class Solution:
    def largestRectangleArea(self, heights) -> int:
        stack = [-1]
        res = 0
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                res = max(res, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)
        while stack[-1] != -1:
            res = max(res, heights[stack.pop()] * (len(heights) - stack[-1] - 1))
        return res


if __name__ == '__main__':
    s = Solution()
    heights = [2, 1, 5, 5, 6, 2, 3]
    print(s.largestRectangleArea(heights))