# 给定范围 [m, n]，其中 0 <= m <= n <= 2147483647，返回此范围内所有数字的按位与（包含 m, n 两端点）。
# 本质是找公共前缀
# 对所有数字执行按位与运算的结果是所有对应二进制字符串的公共前缀再用零补上后面的剩余位。
# 进一步来说，所有这些二进制字符串的公共前缀也即指定范围的起始和结束数字 m 和 n 的公共前缀
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        shift = 0
        while m < n:
            m >>= 1
            n >>= 1
            shift += 1
        return m << shift


# 方法2 n不断抹去右边的1，直到m==n，则这是为它们的公共前缀
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while m < n:
            n = n & (n - 1)
        return n