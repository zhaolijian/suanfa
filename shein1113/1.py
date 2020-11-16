# 给一个字符串，对于其中的字母/数字/空格统计出现次数，次数不同按照次数由多到少输出，次数相同按照ascii从小到大输出
from collections import defaultdict
def func(s):
    d = defaultdict(int)
    another_d = defaultdict(list)
    res = []
    for ele in s:
        if 'a' <= ele <= 'z':
            d[ele] += 1
        elif 'A' <= ele <= 'Z':
            d[ele] += 1
        elif ord('0') <= ord(ele) <= ord('9'):
            d[ele] += 1
        elif ele == ' ':
            d[ele] += 1
    for key, val in d.items():
        another_d[val].append(key)
    # key是个数,val是字符
    for key in sorted(another_d.keys(), reverse=True):
        for val in sorted(another_d[key]):
            res.append(val)
    return ''.join(res)

while True:
    try:
        s = input()
        print(func(s))
    except:
        break