# 给定一个偶数长度的数组，其中不同的数字代表着不同种类的糖果，每一个数字代表一个糖果。你需要把这些糖果平均分给一个弟弟和一个妹妹。
# 返回妹妹可以获得的最大糖果的种类数。


class Solution:
    def distributeCandies(self, candies) -> int:
        # 统计糖果的种类数
        # 如果糖果的种类数 >= 糖果总数的一半,那么直接返回糖果总数的一半
        # 否则返回糖果的种类数
        s = set(candies)
        if len(s) >= len(candies) // 2:
            return len(candies) // 2
        return len(s)