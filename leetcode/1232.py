# 在一个 XY 坐标系中有一些点，我们用数组 coordinates 来分别记录它们的坐标，其中 coordinates[i] = [x, y] 表示横坐标为 x、纵坐标为 y 的点。
# 请你来判断，这些点是否在该坐标系中属于同一条直线上，是则返回 true，否则请返回 false。


# 斜率相等
class Solution:
    def checkStraightLine(self, coordinates) -> bool:
        k = float('inf')
        if coordinates[1][0] != coordinates[0][0]:
            k = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
        for i in range(2, len(coordinates)):
            temp = float('inf')
            if coordinates[i][0] != coordinates[i - 1][0]:
                temp = (coordinates[i][1] - coordinates[i - 1][1]) / (coordinates[i][0] - coordinates[i - 1][0])
            if temp != k:
                return False
        return True


# 斜率放入set集合中
class Solution:
    def checkStraightLine(self, coordinates) -> bool:
        k_set = set()
        for i in range(1, len(coordinates)):
            k = float('inf')
            if coordinates[i][0] != coordinates[i - 1][0]:
                k = (coordinates[i][1] - coordinates[i - 1][1]) / (coordinates[i][0] - coordinates[i - 1][0])
            k_set.add(k)
        return len(k_set) == 1


# 平移过原点，求出Ax+By=0中的A和B，然后遍历所有元素，看是否满足这个条件