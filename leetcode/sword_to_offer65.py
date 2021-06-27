# 不使用加减乘除做加法
class Solution:
    def add(self, a: int, b: int) -> int:
        temp = 0xffffffff
        # 截取1-32位
        a = a & temp
        b = b & temp
        while b != 0:
            # a保留进位后的余数，b保留进位
            a, b = a ^ b, (a & b) << 1 & temp
        # a ^ temp 意思是将1-32位按位取反
        # ～ 意思是将整个数字取反
        # ~(a ^ temp) 意思是32位以上的位取反，1-32位不变，从而将补码还原至 Python 的存储格式
        return a if a <= 0x7fffffff else ~(a ^ temp)


if __name__ == '__main__':
    s = Solution()
    a, b = 1, -2
    print(s.add(a, b))