# 给定一个整数 n，返回 n! 结果尾数中零的数量。

# 零的数量取决于2和5的数量，每10个数中由四个数是2的倍数，两个数是5的倍数，2的个数肯定比5多，所以只要统计5的数量即可
# 方法1
# 统计从1到n中，是5的倍数的值个数、5^5的倍数的值个数、5^5^5的倍数的值个数。。。相加即为5的个数。
# 因为是5的倍数的值能至少提供一个5，是25的倍数的值能至少提供两个5。。。
class Solution:
    def trailingZeroes(self, n: int) -> int:
        number = 0
        temp = 5
        # 每一轮统计是5的倍数的个数、25的倍数的个数、125的倍数的个数。。。
        while True:
            if n >= temp:
                number += n // temp
                temp *= 5
            else:
                break
        return number


# 方法2 将方法1变换下，由乘变为除
class Solution:
    def trailingZeroes(self, n: int) -> int:
        number = 0
        # 每一轮统计是5的倍数的个数、25的倍数的个数、125的倍数的个数。。。
        while n:
            number += n // 5
            n //= 5
        return number


if __name__ == '__main__':
    s = Solution()
    print(s.trailingZeroes(25))