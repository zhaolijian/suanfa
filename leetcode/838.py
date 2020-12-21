# 一行中有 N 张多米诺骨牌，我们将每张多米诺骨牌垂直竖立。
# 在开始时，我们同时把一些多米诺骨牌向左或向右推。
# 每过一秒，倒向左边的多米诺骨牌会推动其左侧相邻的多米诺骨牌。
# 同样地，倒向右边的多米诺骨牌也会推动竖立在其右侧的相邻多米诺骨牌。
# 如果同时有多米诺骨牌落在一张垂直竖立的多米诺骨牌的两边，由于受力平衡， 该骨牌仍然保持不变。
# 就这个问题而言，我们会认为正在下降的多米诺骨牌不会对其它正在下降或已经下降的多米诺骨牌施加额外的力。
# 给定表示初始状态的字符串 "S" 。如果第 i 张多米诺骨牌被推向左边，则 S[i] = 'L'；
# 如果第 i 张多米诺骨牌被推向右边，则 S[i] = 'R'；如果第 i 张多米诺骨牌没有被推动，则 S[i] = '.'。
# 返回表示最终状态的字符串。


# 方法1
# class Solution:
#     def pushDominoes(self, dominoes: str) -> str:
#         index_l, index_r = -1, -1
#         array = list(dominoes)
#         for i, ele in enumerate(dominoes):
#             if ele == "R":
#                 if index_r != -1:
#                     while index_r + 1 < i and array[index_r + 1] == ".":
#                         array[index_r + 1] = "R"
#                         index_r += 1
#                 index_r = i
#             elif ele == "L":
#                 index_l = i
#                 if index_r == -1:
#                     while index_l - 1 >= 0 and array[index_l - 1] == ".":
#                         array[index_l - 1] = "L"
#                         index_l -= 1
#                 else:
#                     while index_r + 1 < index_l - 1:
#                         array[index_r + 1] = "R"
#                         array[index_l - 1] = "L"
#                         index_r += 1
#                         index_l -= 1
#                     index_r = -1
#         if index_r != -1:
#             for i in range(index_r + 1, len(dominoes)):
#                 array[i] = "R"
#         return "".join(array)


# 方法2 统计每一个点的受力情况
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        length = len(dominoes)
        array = [0] * length
        # 统计R的影响
        temp = 0
        for i, ele in enumerate(dominoes):
            if ele == "R":
                temp = length
            elif ele == "L":
                temp = 0
            else:
                temp = max(temp - 1, 0)
            array[i] += temp
        # 统计L的影响
        temp = 0
        for i in range(length - 1, -1, -1):
            if dominoes[i] == "R":
                temp = 0
            elif dominoes[i] == "L":
                temp = length
            else:
                temp = max(temp - 1, 0)
            array[i] -= temp
        # 值大于0说明受得右力大，值小于0说明受得左力大
        return "".join("." if ele == 0 else "R" if ele > 0 else "L" for ele in array)


if __name__ == '__main__':
    s = Solution()
    dominoes = "RL....R....R......R.......................LR.R..L.R."
    print(s.pushDominoes(dominoes))