# 配对交换。编写程序，交换某个整数的奇数位和偶数位，尽量使用较少的指令（也就是说，位0与位1交换，位2与位3交换，以此类推）。
class Solution:
    def exchangeBits(self, num: int) -> int:
        i = 0
        while i < 30:
            temp1 = num & (1 << i)
            temp2 = num & (1 << (i + 1))
            num -= temp1
            num += temp1 << 1
            num -= temp2
            num += temp2 >> 1
            i += 2
        return num