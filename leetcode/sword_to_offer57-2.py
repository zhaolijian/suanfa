# 输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
# 序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。


# 方法1
# class Solution:
#     def findContinuousSequence(self, target: int):
#         res = []
#         for i in range(1, target // 2 + 1):
#             temp = 0
#             cur = i
#             while temp < target:
#                 temp += cur
#                 if temp == target:
#                     res.append([j for j in range(i, cur + 1)])
#                 cur += 1
#         return res


# 滑动窗口
class Solution:
    def findContinuousSequence(self, target: int):
        # 左指针、右指针、累加和
        l, r, cur = 1, 1, 0
        res = []
        while l <= target // 2:
            if cur < target:
                cur += r
                r += 1
            elif cur > target:
                cur -= l
                l += 1
            else:
                res.append([j for j in range(l, r)])
                cur += r - l
                l += 1
                r += 1
        return res


if __name__ == '__main__':
    s = Solution()
    target = 9
    print(s.findContinuousSequence(target))