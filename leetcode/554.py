# 你的面前有一堵矩形的、由多行砖块组成的砖墙。 这些砖块高度相同但是宽度不同。你现在要画一条自顶向下的、穿过最少砖块的垂线。
# 砖墙由行的列表表示。 每一行都是一个代表从左至右每块砖的宽度的整数列表。
# 如果你画的线只是从砖块的边缘经过，就不算穿过这块砖。你需要找出怎样画才能使这条线穿过的砖块数量最少，并且返回穿过的砖块数量。
# 你不能沿着墙的两个垂直边缘之一画线，这样显然是没有穿过一块砖的。


from collections import defaultdict
class Solution:
    def leastBricks(self, wall) -> int:
        heigth = len(wall)
        res = heigth
        d = defaultdict(set)
        for i in range(heigth):
            number = 0
            for j in range(len(wall[i]) - 1):
                number += wall[i][j]
                d[number].add(i)
        for key in d.keys():
            res = min(res, heigth - len(d[key]))
        return res