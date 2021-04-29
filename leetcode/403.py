# 一只青蛙想要过河。 假定河流被等分为若干个单元格，并且在每一个单元格内都有可能放有一块石子（也有可能没有）。 青蛙可以跳上石子，但是不可以跳入水中。
# 给你石子的位置列表 stones（用单元格序号 升序 表示）， 请判定青蛙能否成功过河（即能否在最后一步跳至最后一块石子上）。
# 开始时， 青蛙默认已站在第一块石子上，并可以假定它第一步只能跳跃一个单位（即只能从单元格 1 跳至单元格 2 ）。
# 如果青蛙上一步跳跃了 k 个单位，那么它接下来的跳跃距离只能选择为 k - 1、k 或 k + 1 个单位。 另请注意，青蛙只能向前方（终点的方向）跳跃。


from collections import defaultdict
class Solution:
    def canCross(self, stones) -> bool:
        s = set(stones)
        # 到达某个位置的步长
        d = defaultdict(set)
        d[0].add(0)
        for ele in stones:
            for step in d[ele]:
                for i in [-1, 0, 1]:
                    if ele + step + i == stones[-1]:
                        return True
                    if step + i > 0 and ele + step + i in s:
                        d[ele + step + i].add(step + i)
        return False