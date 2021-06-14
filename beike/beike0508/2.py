from collections import Counter
n = int(input())
l = list(map(int, input().strip().split()))
c = Counter(l)
res = 0
for key in c.keys():
    if c[key] > res:
        res = c[key]
print(res)