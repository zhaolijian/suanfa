# 小团惹小美生气了，小美要去找小团“讲道理”。小团望风而逃，他们住的地方可以抽象成一棵有n个结点的树，
# 小美位于x位置，小团位于y位置。小团和小美每个单位时间内都可以选择不动或者向相邻的位置转移，
# 假设小美足够聪明，很显然最终小团会无路可逃，只能延缓一下被“讲道理”的时间，
# 请问最多经过多少个单位时间后，小团会被追上。
# 输入描述
# 输入第一行包含三个整数n，x，y，分别表示树上的结点数量，小美所在的位置和小团所在的位置。(1<=n<=50000)
#
# 接下来有n-1行，每行两个整数u，v，表示u号位置和v号位置之间有一条边，即u号位置和v号位置彼此相邻。
#
# 输出描述
# 输出仅包含一个整数，表示小美追上小团所需的时间。
# 样例输入
# 5 1 2
# 2 1
# 3 1
# 4 2
# 5 3
# 样例输出
# 2
# 若小美是小团的祖先节点,则为小美位置到叶子节点的高度差
# 否则,为小美位置到根节点的高度差+数的高度-1
from collections import defaultdict
if __name__ == '__main__':
    while True:
        try:
            n, x, y = map(int, input().split())
            sons = defaultdict(list)
            parents = defaultdict(int)
            for _ in range(n - 1):
                temp1, temp2 = map(int, input().split())
                if temp1 > temp2:
                    temp1, temp2 = temp2, temp1
                parents[temp2] = temp1
                sons[temp1].append(temp2)
            if x == y:
                print(0)
            # 获得temp1/temp2到根节点的高度
            def find(node):
                res = 0
                root = node
                while parents[node]:
                    node = parents[node]
                    res += 1
                    root = node
                return res, root

            len_x, root = find(x)
            len_y, root = find(y)
            # 找根节点到叶子节点高度
            length = 0
            def tree_length(node, cur):
                global length
                if not sons[node]:
                    length = max(length, cur)
                    return
                else:
                    for ele in sons[node]:
                        tree_length(ele, cur + 1)

            tree_length(root, 0)

            # 判断小美是小团的祖先节点
            s = set()
            tuan = y
            while tuan:
                s.add(tuan)
                tuan = parents[tuan]
            flag = True if x in s else False
            if flag:
                print(length - len_x)
            else:
                print(length + len_x)

        except:
            break