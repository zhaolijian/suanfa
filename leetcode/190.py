# 颠倒给定的 32 位无符号整数的二进制位。
# 提示：
# 请注意，在某些语言（如 Java）中，没有无符号整数类型。在这种情况下，输入和输出都将被指定为有符号整数类型，并且不应影响您的实现，
# 因为无论整数是有符号的还是无符号的，其内部的二进制表示形式都是相同的。
# 在 Java 中，编译器使用二进制补码记法来表示有符号整数。因此，在上面的 示例 2 中，输入表示有符号整数 -3，输出表示有符号整数 -1073741825。
# 进阶:
# 如果多次调用这个函数，你将如何优化你的算法？

# 方法1 分治算法 时间复杂度O(1)
class Solution:
    def __init__(self):
        self.dict = {}

    def reverseBits(self, n):
        if n in self.dict:
            return self.dict[n]
        init_val = n
        # 左边16位和右边16位交换
        n = (n >> 16) | (n << 16)
        # 相邻8位交换
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        # 相邻4位交换
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        # 相邻两位交换
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        # 相邻一位交换
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        # 交换后便实现了逆序
        self.dict[init_val] = n
        return n

    # 0xff00ff00  11111111000000001111111100000000
    # 0xf0f0f0f0  11110000111100001111000011110000
    # 0xcccccccc  11001100110011001100110011001100
    # 0xaaaaaaaa  10101010101010101010101010101010


# 方法2 逐位遍历 时间复杂度O(logn)
class Solution:
    def __init__(self):
        self.dict = {}

    def reverseBits(self, n: int) -> int:
        if n in self.dict:
            return self.dict[n]
        result = 0
        i = 0
        while i < 32 and n:
            # 这个或操作是重点
            result |= (n & 1) << (31 - i)
            n >>= 1
            i += 1
        self.dict[n] = result
        return result