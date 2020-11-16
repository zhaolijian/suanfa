# 最长连续整数子序列
a = [3, 3, 4, 7, 5, 6, 8]
n = len(a)
pre = [0] * n
dic = {}
idx = {}

MAX_len = 0
dic[a[0]] = 1
pre[0] = -1
last = 0
idx[a[0]] = 0

for i in range(1, n):
    if a[i] not in dic:
        if a[i] - 1 not in dic:
            dic[a[i]] = 1
            pre[i] = -1
        else:
            dic[a[i]] = dic[a[i] - 1] + 1
            pre[i] = idx[a[i] - 1]
        idx[a[i]] = i
    else:
        if a[i] - 1 not in dic:
            pass
        elif dic[a[i]] < dic[a[i] - 1] + 1:
            dic[a[i]] = dic[a[i] - 1] + 1
            pre[i] = idx[a[i] - 1]
            idx[a[i]] = i
    if dic[a[i]] > MAX_len:
        MAX_len = dic[a[i]]
        last = i
rtn = []
res = []
while last != -1:
    rtn.append(last)
    res.append(a[last])
    last = pre[last]
print("val:", res[::-1])
print("index:", rtn[::-1])
