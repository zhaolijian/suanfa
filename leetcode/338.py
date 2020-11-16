# 方法1
class Solution:
    def countBits(self, num: int):
        # 最低有效位: 一个数的一半等于该数的二进制数去掉最后一位
        init = [0] * (num + 1)
        for i in range(1, num + 1):
            init[i] = init[i // 2] + (i & 1)
        return init


# 方法2
class Solution:
    def countBits(self, num: int):
        init = [0] * (num + 1)
        for i in range(1, num + 1):
            # 将二进制中最后一个为1的位设为0
            init[i] = init[i & (i - 1)] + 1
        return init


if __name__ == '__main__':
    s= Solution()
    num = 4
    print(s.countBits(num))