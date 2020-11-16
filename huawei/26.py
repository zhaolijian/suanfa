# 编写一个程序，将输入字符串中的字符按如下规则排序。
# 规则 1 ：英文字母从 A 到 Z 排列，不区分大小写。
# 如，输入： Type 输出： epTy
# 规则 2 ：同一个英文字母的大小写同时存在时，按照输入顺序排列。
# 如，输入： BabA 输出： aABb
# 规则 3 ：非英文字母的其它字符保持原来的位置。
# 如，输入： By?e 输出： Be?y
from collections import defaultdict
if __name__ == '__main__':
    while True:
        try:
            s = input()
            length = len(s)
            res = []
            d = defaultdict(list)
            for i in range(length):
                if 'A' <= s[i] <= 'Z' or 'a' <= s[i] <= 'z':
                    d[s[i]].append(i)
            for i in range(26):
                temp1 = d[chr(65 + i)]
                temp2 = d[chr(97 + i)]
                len_1, len_2 = len(temp1), len(temp2)
                p, q = 0, 0
                while p < len_1 and q < len_2:
                    if temp1[p] < temp2[q]:
                        res.append(chr(65 + i))
                        p += 1
                    else:
                        res.append(chr(97 + i))
                        q += 1
                if p < len_1:
                    res += [chr(65 + i)] * (len_1 - p)
                if q < len_2:
                    res += [chr(97 + i)] * (len_2 - q)
            for i in range(length):
                if not ('A' <= s[i] <= 'Z' or 'a' <= s[i] <= 'z'):
                # 或if not (65 <= ord(s[i]) <= 90 or 97 <= ord(s[i]) <= 122):
                    res.insert(i, s[i])
            print(''.join(res))
        except:
            break