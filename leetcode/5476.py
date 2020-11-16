# 给你一个由 不同 整数组成的整数数组 arr 和一个整数 k 。
# 每回合游戏都在数组的前两个元素（即 arr[0] 和 arr[1] ）之间进行。比较 arr[0] 与 arr[1] 的大小，较大的整数将会取得这一回合的胜利并保留在位置 0 ，较小的整数移至数组的末尾。当一个整数赢得 k 个连续回合时，游戏结束，该整数就是比赛的 赢家 。
# 返回赢得比赛的整数。
# 题目数据 保证 游戏存在赢家。


class Solution:
    def getWinner(self, arr, k: int) -> int:
        length = len(arr)
        if k >= length - 1:
            return max(arr)
        res_0, res_1 = 0, 0
        while True:
            if arr[0] > arr[1]:
                res_1 = 0
                res_0 += 1
                if res_0 >= k:
                    return arr[0]
                temp = arr[1]
                arr.pop(1)
                arr.append(temp)
            else:
                res_0 = 0
                res_1 += 1
                if res_1 >= k:
                    return arr[1]
                temp = arr[0]
                arr.pop(0)
                arr.append(temp)
                res_0, res_1 = res_1, res_0


if __name__ == '__main__':
    s = Solution()
    arr = [1,25,35,42,68,70]
    k = 1
    print(s.getWinner(arr, k))