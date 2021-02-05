# Alice 和 Bob 共有一个无向图，其中包含 n 个节点和 3  种类型的边：
# 类型 1：只能由 Alice 遍历。
# 类型 2：只能由 Bob 遍历。
# 类型 3：Alice 和 Bob 都可以遍历。
# 给你一个数组 edges ，其中 edges[i] = [typei, ui, vi] 表示节点 ui 和 vi 之间存在类型为 typei 的双向边。
# 请你在保证图仍能够被 Alice和 Bob 完全遍历的前提下，找出可以删除的最大边数。
# 如果从任何节点开始，Alice 和 Bob 都可以到达所有其他节点，则认为图是可以完全遍历的。
# 返回可以删除的最大边数，如果 Alice 和 Bob 无法完全遍历图，则返回 -1 。


# 错误。。。
from collections import defaultdict
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges) -> int:
        def find(node, parent):
            if parent[node] != node:
                parent[node] = find(parent[node], parent)
            return parent[node]

        def union(node1, node2, parent, number):
            nonlocal res
            root_1, root_2 = find(node1, parent), find(node2, parent)
            if root_1 != root_2:
                parent[root_2] = root_1
                number -= 1
            else:
                res += 1
            return number

        d = defaultdict(list)
        parent_alice = [i for i in range(n + 1)]
        parent_bob = [i for i in range(n + 1)]
        # 联通分量数
        number_alice, number_bob = n, n
        # 多余边数
        res = 0
        for type, first, second in edges:
            d[(first, second)].append(type)
        for key in d.keys():
            d[key].sort()
            # 两个节点之间没有类型3的边,那么就只能是类型1和类型2,按正常处理即可
            if d[key][-1] != 3:
                for type in d[key]:
                    if type == 1:
                        number_alice = union(key[0], key[1], parent_alice, number_alice)
                    elif type == 2:
                        number_bob = union(key[0], key[1], parent_bob, number_bob)
            # 两个节点之间有类型3的边,那么type1和type2的边完全是多余的
            else:
                for type in d[key]:
                    if type == 1:
                        res += 1
                    elif type == 2:
                        res += 1
                    else:
                        # 是否Alice和Bob都不需要type3类型的边,两个节点就已经连通
                        flag_alice, flag_bob = False, False
                        # 如果之前未连通,那么正常连通即可
                        if find(key[0], parent_alice) != find(key[1], parent_alice):
                            number_alice = union(key[0], key[1], parent_alice, number_alice)
                        else:
                            flag_alice = True
                        if find(key[0], parent_bob) != find(key[1], parent_bob):
                            number_bob = union(key[0], key[1], parent_bob, number_bob)
                        else:
                            flag_bob = True
                        # alice和bob都不需要type3类型的边就已经连通了,那么这条边就是多余的
                        if flag_alice and flag_bob:
                            res += 1
        return -1 if number_alice != 1 or number_bob != 1 else res


if __name__ == '__main__':
    s = Solution()
    n = 13
    edges = [[1,1,2],[2,1,3],[3,2,4],[3,2,5],[1,2,6],[3,6,7],[3,7,8],[3,6,9],[3,4,10],[2,3,11],[1,5,12],[3,3,13],[2,1,10],[2,6,11],[3,5,13],[1,9,12],[1,6,8],[3,6,13],[2,1,4],[1,1,13],[2,9,10],[2,1,6],[2,10,13],[2,2,9],[3,4,12],[2,4,7],[1,1,10],[1,3,7],[1,7,11],[3,3,12],[2,4,8],[3,8,9]]
    print(s.maxNumEdgesToRemove(n, edges))