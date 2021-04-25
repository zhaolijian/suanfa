# 题目描述：
# 在机票业务中，我们常常用到各种字母数字组合的信息，如机场代码“SHA”，航班代码“CA522”等。
# 为了节省存储空间，减少字符串操作，我们把英文大小写字母和数字进行编码，每个字符编码为一个6位的二进制编码。
# 这样一个含5个字符的字符串，用一个32位的整数就可以表示，其中编码占用30位，空置两位（2+5*6）。
# 一个含10个字符的字符串，用两个32位的整数就可以表示（2+5*6,  2+5*6）
# 字符二进制编码规则：
# 'a'编码为000001, 'b'编码为000010 ... 'z'编码为011010
# 'A'编码为011011 ... 'Z'编码为110100
# '0'编码为110101 ... '9'编码为111110
#
# 字符串编码示例：
# “Aa0Z9”编码为整数 453467454 （00011011 00000111 01011101 00111110）
# “a”编码为整数 1 （00000000 00000000 00000000 00000001）
# “Aa0Z9a”编码为整数453467454 1 （输出格式是第一个数字+空格+第二个数字）
#
# 现要求将输入的字符串转为整数数组，不符合编码规范的字符编码为000000进行占位
# 输入描述
# 输入一个字符串，如：
# Aa0Z9
# 更多例子：
# Aa0Z9a
# a*
#
# 输出描述
# 转换后的整数，不同数字之间用一个空格隔开，最后一个数字之后不要跟空格
# 453467454
# 更多例子：
#
# 453467454 【空格】1
#
# 64
# 样例输入
# Aa0Z9
# 样例输出
# 453467454
if __name__ == '__main__':
    while True:
        try:
            s = input()
            # 转换为二进制字符串
            bin_string = ''
            for i in range(len(s)):
                if 'a' <= s[i] <= 'z':
                    bin_number = bin(ord(s[i]) - ord('a') + 1)[2:]
                    bin_string += '0' * (6 - len(bin_number)) + bin_number
                elif 'A' <= s[i] <= 'Z':
                    bin_number = bin(ord(s[i]) - ord('A') + 27)[2:]
                    bin_string += '0' * (6 - len(bin_number)) + bin_number
                elif '0' <= s[i] <= '9':
                    bin_string += bin(int(s[i]) + 53)[2:]
                else:
                    bin_string += '000000'
            init = []
            res = []
            for i in range(0, len(bin_string), 30):
                init.append(bin_string[i: i + 30])
            for i in range(len(init)):
                temp = 0
                temp_len = len(init[i])
                for j in range(temp_len):
                    temp += int(init[i][temp_len - j - 1]) << j
                res.append(temp)
            print(' '.join(map(str, res)))
        except:
            break