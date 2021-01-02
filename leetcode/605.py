# 假设你有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花卉不能种植在相邻的地块上，它们会争夺水源，两者都会死去。
# 给定一个花坛（表示为一个数组包含0和1，其中0表示没种植花，1表示种植了花），和一个数 n 。
# 能否在不打破种植规则的情况下种入 n 朵花？能则返回True，不能则返回False。


class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        res = 0
        left, distance, length = -1, 0, len(flowerbed)
        if length == 1 and flowerbed[0] == 0 and n <= 1:
            return True
        for i, ele in enumerate(flowerbed):
            if ele == 1 or (i == length - 1 and ele == 0):
                distance = i - left - 1 if ele == 1 else i - left
                if left == -1 and i == length - 1 and ele == 0:
                    res = (distance + 1) // 2
                elif left == -1 or (i == length - 1 and ele == 0):
                    res += distance // 2
                elif distance > 0:
                    res += (distance - 1) // 2
                left = i
        return True if res >= n else False
