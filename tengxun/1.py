# 小Q想要给他的朋友发送一个神秘字符串，但是他发现字符串的过于长了，于是小Q发明了一种压缩算法对字符串中重复的部分进行了压缩，
# 对于字符串中连续的m个相同字符串S将会压缩为[m|S](m为一个整数且1<=m<=100)，例如字符串ABCABCABC将会被压缩为[3|ABC]，
# 现在小Q的同学收到了小Q发送过来的字符串，你能帮助他进行解压缩么？
#
# 输入描述:
# 输入第一行包含一个字符串s，代表压缩后的字符串。
# S的长度<=1000;
# S仅包含大写字母、[、]、|;
# 解压后的字符串长度不超过100000;
# 压缩递归层数不超过10层;
#
# 输出描述:
# 输出一个字符串，代表解压后的字符串。
#
# 输入例子1:
# HG[3|B[2|CA]]F
#
# 输出例子1:
# HGBCACABCACABCACAF
while True:
    try:
        s = input()
        res, number, stack = '', 0, []
        for ele in s:
            if 'A' <= ele <= 'Z':
                res += ele
            elif ele == '|':
                stack.append((res, number))
                res, number = '', 0
            elif ele == ']':
                last_res, last_number = stack.pop()
                res = last_res + last_number * res
            elif '0' <= ele <= '9':
                number = number * 10 + int(ele)
        print(res)
    except:
        break
