# 给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
# 在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
# 说明：你不能倾斜容器，且 n 的值至少为 2。

# 双指针
class Solution:
    def maxArea(self, height) -> int:
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            if height[l] <= height[r]:
                res = max(res, (r - l) * height[l])
                l += 1
            else:
                res = max(res, (r - l) * height[r])
                r -= 1
        return res


if __name__ == '__main__':
    s = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    print(s.maxArea(height))