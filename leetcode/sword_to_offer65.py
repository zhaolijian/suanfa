# 不使用加减乘除做加法
class Solution:
    def add(self, a: int, b: int) -> int:
        temp = 0xffffffff
        a = a & temp
        b = b & temp
        while b != 0:
            # a保留进位后的余数，b保留进位
            a, b = a ^ b, (a & b) << 1 & temp
        return a if a <= 0x7fffffff else ~(a ^ temp)



if __name__ == '__main__':
    s = Solution()
    a, b = 1, -2
    print(s.add(a, b))