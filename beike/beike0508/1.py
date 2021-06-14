l = list(map(int, input().split()))
# 商品种数、订单数量
n, m = l[0], l[1]
dict = {}
for _ in range(n):
    # 商品名称、售出一份收益、库存数量
    s, w, c = input().strip().split()
    w = int(w)
    c = int(c)
    dict[s] = [w, c]

need = []
for _ in range(m):
    # 商品名称、需求数量
    t, d = input().strip().split()
    d = int(d)
    need.append((t, d))
res = 0
flag = False
for i, (t, d) in enumerate(need):
    if t in dict and dict[t][1] >= d:
        dict[t][1] -= d
        res += dict[t][0] * d
    else:
        print(-(i + 1))
        flag = True
        break
if not flag:
    print(res)