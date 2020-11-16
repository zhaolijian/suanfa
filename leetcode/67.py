# 方法1
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # 括号中的a,2表示a是一个二进制,并将之转换为十进制
        a = int(a, 2)
        b = int(b, 2)
        # 当没有进位的时候结束
        while b:
            # 进位后的余数
            temp1 = a ^ b
            # 进位数
            temp2 = (a & b) << 1
            a, b = temp1, temp2
        # bin方法为将a转换为二进制,前面带上0b,表示后面的数是二进制
        return bin(a)[2:]


# 方法2
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        len_a = len(a)
        len_b = len(b)
        length = max(len_a, len_b)
        res = ""
        if len_a < length:
            a = '0' * (length - len_a) + a
        elif len_b < length:
            b = '0' * (length - len_b) + b
        # 记录进位 
        temp = 0
        for i in range(length - 1, -1, -1):
            cur = int(a[i]) + int(b[i]) + temp
            temp = 0
            if cur >= 2:
                temp = 1
                res = str(cur % 2) + res
            else:
                res = str(cur) + res
        if temp > 0:
            res = str(temp) + res
        return res
    

if __name__ == '__main__':
    s = Solution()
    a = "1010"
    b = "1011"
    print(s.addBinary(a, b))