# 给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。


# 方法1 dp+最高有效位   时间复杂度为O(length)
class Solution:
    def countBits(self, num: int):
        high = 0
        res = [0]
        for i in range(1, num + 1):
            if i & (i - 1) == 0:
                high = i
            res.append(res[i - high] + 1)
        return res


class Solution:
    def countBits(self, num: int):
        init = [0] * (num + 1)
        for i in range(1, num + 1):
            # 将二进制中最后一个为1的位设为0
            init[i] = init[i & (i - 1)] + 1
        return init


# 方法2 dp+最低有效位   时间复杂度为O(length)
class Solution:
    def countBits(self, num: int):
        res = [0]
        for i in range(1, num + 1):
            # >>也可以用//2替代
            res.append(res[i >> 1] + (i & 1))
        return res


# 方法3 时间复杂度为O(length)
class Solution:
    def countBits(self, num: int):
        res = [0]
        for i in range(1, num + 1):
            res.append(res[i & (i - 1)] + 1)
        return res


# 方法4 时间复杂度为O(length * len(integer))
class Solution:
    def countBits(self, num: int):
        res = [0]
        for i in range(1, num + 1):
            number = 0
            while i:
                i &= i - 1
                number += 1
            res.append(number)
        return res


if __name__ == '__main__':
    s= Solution()
    num = 4
    print(s.countBits(num))