# 将十进制转换为二进制
class Solution:
    def toBin(self, number):
        if not number:
            return ""
        else:
            temp1 = self.toBin(number // 2)
            temp2 = str(number % 2)
            return temp1 + temp2


if __name__ == '__main__':
    s = Solution()
    number = 100
    print(s.toBin(number))
