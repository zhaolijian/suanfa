# 几块石子 排成一行 ，每块石子都有一个关联值，关联值为整数，由数组 stoneValue 给出。
# 游戏中的每一轮：Alice 会将这行石子分成两个 非空行（即，左侧行和右侧行）；
# Bob 负责计算每一行的值，即此行中所有石子的值的总和。Bob 会丢弃值最大的行，Alice 的得分为剩下那行的值（每轮累加）。
# 如果两行的值相等，Bob 让 Alice 决定丢弃哪一行。下一轮从剩下的那一行开始。
# 只 剩下一块石子 时，游戏结束。Alice 的分数最初为 0 。
# 返回 Alice 能够获得的最大分数 。


# 递归 + 记忆化搜索
class Solution:
    def stoneGameV(self, stoneValue) -> int:
        def getM(array):
            if array in memo:
                return memo[array]
            else:
                length = len(array)
                if length == 1:
                    return 0
                sum_number = sum(array)
                res = 0
                left_sum = 0
                for i in range(length - 1):
                    left_sum += array[i]
                    right_sum = sum_number - left_sum
                    if left_sum < right_sum:
                        res = max(res, left_sum + getM(array[:i + 1]))
                    elif left_sum == right_sum:
                        res = max(res, left_sum + getM(array[:i + 1]), right_sum + getM(array[i + 1:]))
                    else:
                        res = max(res, right_sum + getM(array[i + 1:]))
                memo[array] = res
                return res

        memo = {}
        return getM(tuple(stoneValue))


if __name__ == '__main__':
    s = Solution()
    stoneValue =[98,77,24,49,6,12,2,44,51,96]
    print(s.stoneGameV(stoneValue))