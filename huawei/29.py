# 1、对输入的字符串进行加解密，并输出。
# 2加密方法为：
# 当内容是英文字母时则用该英文字母的后一个字母替换，同时字母变换大小写,如字母a时则替换为B；字母Z时则替换为a；
# 当内容是数字时则把该数字加1，如0替换1，1替换2，9替换0；
# 其他字符不做变化。
# 3、解密方法为加密的逆过程。
# 接口描述：
# 实现接口，每个接口实现1个基本操作：
# void Encrypt (char aucPassword[], char aucResult[])：在该函数中实现字符串加密并输出
# 说明：
# 1、字符串以\0结尾。
# 2、字符串最长100个字符。
# int unEncrypt (char result[], char password[])：在该函数中实现字符串解密并输出
# 说明：
# 1、字符串以\0结尾。
# 2、字符串最长100个字符。
def Encrypt(string):
    res = ""
    for i in range(len(string)):
        if 'a' <= string[i] <= 'y':
            res += chr(ord(string[i]) - 31)
        elif string[i] == 'z':
            res += 'A'
        elif 'A' <= string[i] <= 'Y':
            res += chr(ord(string[i])+ 33)
        elif string[i] == 'Z':
            res += 'a'
        elif '0' <= string[i] <= '8':
            res += str(int(string[i]) + 1)
        elif string[i] == '9':
            res += '0'
        else:
            res += string[i]
    return res


def unEncrypt(string):
    res = ""
    for i in range(len(string)):
        if 'b' <= string[i] <= 'z':
            res += chr(ord(string[i]) - 33)
        elif string[i] == 'a':
            res += 'Z'
        elif 'B' <= string[i] <= 'Z':
            res += chr(ord(string[i]) + 31)
        elif string[i] == 'A':
            res += 'z'
        elif '1' <= string[i] <= '9':
            res += str(int(string[i]) - 1)
        elif string[i] == '0':
            res += '9'
        else:
            res += string[i]
    return res


if __name__ == '__main__':
    while True:
        try:
            s1 = input()
            s2 = input()
            print(Encrypt(s1))
            print(unEncrypt(s2))
        except:
            break