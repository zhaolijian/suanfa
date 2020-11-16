# 题目描述
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
# 一维动态规划问题


class Solution:
    def jumpFloor(self, number):
        if number <= 0:
            return 0
        elif number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            return self.jumpFloor(number-1) + self.jumpFloor(number-2)


if __name__ == '__main__':
    s = Solution()
    for i in range(10):
        print(s.jumpFloor(i))


