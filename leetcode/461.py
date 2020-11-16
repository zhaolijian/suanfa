# 方法1
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # 各位和1的与操作
        res = 0
        index = 0
        while x or y:
            x >>= index
            y >>= index
            index = 1
            temp1 = x & 1
            temp2 = y & 1
            if temp1 != temp2:
                res += 1
        return res


# 方法2 异或
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        temp = x ^ y
        res = 0
        # 求temp中1的数目
        while temp:
            if temp & 1 == 1:
                res += 1
            temp >>= 1
        return res


# 方法3 布赖恩·克尼根算法
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        temp = x ^ y
        res = 0
        while temp:
            res += 1
            temp &= (temp - 1)
        return res


if __name__ == '__main__':
    s = Solution()
    x = 1
    y = 4
    print(s.hammingDistance(x, y))