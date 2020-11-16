class Solution:
    def Add(self, num1, num2):
        # 两个数相加等于进位值+ 该位置残留值，如果进位值等于0，则说明该位置残留值等于加和
        while num2:
            # 相当于每一位相加，而不考虑进位
            result = (num1 ^ num2) & 0xffffffff
            # 求进位（相对应的位都是1的时候才进位）
            temp = (num1 & num2) << 1 & 0xffffffff
            # result + temp 或者 num1 + num2即为结果，但是不能用四则运算符，只能通过移位
            num1 = result
            num2 = temp
        return num1 if num1 <= 0x7fffffff else ~(num1 ^ 0xffffffff)


if __name__ == '__main__':
    num1 = int(input())
    num2 = int(input())
    s = Solution()
    print(s.Add(num1, num2))
