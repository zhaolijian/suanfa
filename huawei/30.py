# 按照指定规则对输入的字符串进行处理。
# 详细描述：
# 将输入的两个字符串合并。
# 对合并后的字符串进行排序，要求为：下标为奇数的字符和下标为偶数的字符分别从小到大排序。
# 这里的下标意思是字符在字符串中的位置。
# 对排序后的字符串进行操作，如果字符为‘0’——‘9’或者‘A’——‘F’或者‘a’——‘f’，
# 则对他们所代表的16进制的数进行BIT倒序的操作，并转换为相应的大写字符。
# 如字符为‘4’，为0100b，则翻转后为0010b，也就是2。转换后的字符为‘2’；
# 如字符为‘7’，为0111b，则翻转后为1110b，也就是e。转换后的字符为大写‘E’。
class Solution:
    def __init__(self):
        self.d = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}

    def reverse_char(self, number):
        temp = ''
        i = 0
        while i < 4:
            temp += '1' if number & (1 << i) else '0'
            i += 1
        val = 0
        for i in range(3, -1, -1):
            if temp[i] == '1':
                val += pow(2, 3 - i)
        if val < 10:
            return str(val)
        else:
            return chr(val + 55)


    def transfer(self, c):
        number = -1
        if '0' <= c <= '9':
            number = int(c)
        elif c in self.d:
            number = self.d[c]
        elif chr(ord(c) + 32) in self.d:
            number = self.d[chr(ord(c) + 32)]
        if number == -1:
            return c
        return self.reverse_char(number)


    def ProcessString(self, s1, s2):
        s = s1 + s2
        length = len(s)
        res = ''
        temp1, temp2 = [], []
        for i in range(length):
            if (i + 1) % 2:
                temp1.append(s[i])
            else:
                temp2.append(s[i])
        temp1.sort()
        temp2.sort()
        final = ''
        len_1, len_2 = len(temp1), len(temp2)
        for i in range(min(len_1, len_2)):
            final += temp1[i]
            final += temp2[i]
        if len_1 > len_2:
            final += temp1[-1]
        for i in range(length):
            res += self.transfer(final[i])
        return res


if __name__ == '__main__':
    while True:
        try:
            s1, s2 = input().split()
            ss = Solution()
            print(ss.ProcessString(s1, s2))
        except:
            break