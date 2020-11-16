# 题目描述
# 有一个仅包含’a’和’b’两种字符的字符串s，长度为n，每次操作可以把一个字符做一次转换（把一个’a’设置为’b’，或者把一个’b’置成’a’)；但是操作的次数有上限m，问在有限的操作数范围内，能够得到最大连续的相同字符的子串的长度是多少。
# 输入描述:
# 第一行两个整数 n , m (1<=m<=n<=50000)，第二行为长度为n且只包含’a’和’b’的字符串s。
# 输出描述:
# 输出在操作次数不超过 m 的情况下，能够得到的 最大连续 全’a’子串或全’b’子串的长度。


# 滑动窗口
# if __name__ == '__main__':
#     n,m = map(int,input().split())
#     array = input()
#     res = 0
#     l, r = 0, 0
#     # b串中更改a的次数、a串中更改b的次数
#     an, bn = 0, 0
#     while r < n:
#         if array[r] == 'a':
#             an += 1
#         else:
#             bn += 1
#         if an <= m or bn <= m:
#             r += 1
#         else:
#             if (r - l) > res:
#                 res = r - l
#             if array[l] == 'a':
#                 an -= 1
#             else:
#                 bn -= 1
#             l += 1
#             r += 1
#     print(res)


if __name__ == '__main__':
    while True:
        try:
            n, m = map(int, input().split())
            string = input()
            l, r = 0, 0
            number = 0
            res = m
            # 全a子串
            while r < n:
                if string[r] == 'b':
                    if number + 1 <= m:
                        number += 1
                        res = max(res, r - l + 1)
                        r += 1
                    else:
                        while string[l] != 'b':
                            l += 1
                        number -= 1
                        l += 1
                else:
                    res = max(res, r - l + 1)
                    r += 1

            # 全b字串
            l, r = 0, 0
            number = 0
            while r < n:
                if string[r] == 'a':
                    if number + 1 <= m:
                        number += 1
                        res = max(res, r - l + 1)
                        r += 1
                    else:
                        while string[l] != 'a':
                            l += 1
                        number -= 1
                        l += 1
                else:
                    res = max(res, r - l + 1)
                    r += 1
            print(res)
        except:
            break