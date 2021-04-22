from collections import defaultdict

# 模块总数
M = int(input())
N = int(input())
d = defaultdict(list)
# 出现依赖的模块集合
set_array = set()
for _ in range(N):
    l = list(map(int, input().split()))
    set_array.add(l[0])
    set_array.add(l[1])
    d[l[0]].append(l[1])


def dfs(number, set_array, d):
    if number not in d:
        return False
    for k in d[number]:
        if k in set_array:
            return True
        set_array.add(k)
        if dfs(k, set_array, d):
            return True
        set_array.remove(k)
    return False

# 是否有循环依赖
flag = False
for key in d.keys():
    temp = set()
    temp.add(key)
    if dfs(key, temp, d):
        flag = True
        break

# 无用模块数
useless = M - len(set_array)
if not flag:
    print(max(0, 10 - useless))
else:
    print(max(0, 8 - useless))