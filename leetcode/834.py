# 给定一个无向、连通的树。树中有 N 个标记为 0...N-1 的节点以及 N-1 条边 。
# 第 i 条边连接节点 edges[i][0] 和 edges[i][1] 。
# 返回一个表示节点 i 与其他所有节点距离之和的列表 ans。
from collections import defaultdict
class Solution:
    def sumOfDistancesInTree(self, N: int, edges):
        if not edges:
            return [0]
        res = [0 for i in range(N)]
        edges.sort(key = lambda x: (x[0], x[1]))
        parents = defaultdict(tuple)
        sons = defaultdict(list)
        # 所有节点的祖先节点集合
        grands = defaultdict(set)
        visisted = {0}
        for i, j in edges:
            sons[i].append(j)
            sons[j].append(i)
        array = [0]
        parents[0] = (None, 0)
        layer = 1
        while array:
            length = len(array)
            for i in range(length):
                temp = array.pop(0)
                for j in sons[temp]:
                    if j not in visisted:
                        array.append(j)
                        parents[j] = (temp, layer)
                        grands[j] = grands[j].union(grands[temp])
                        grands[j].add(temp)
                        visisted.add(j)
            layer += 1

        def func(start, end, i):
            for j in range(start, end):
                # 如果i的祖先节点中有j
                if j in grands[i]:
                    res[i] += parents[i][1] - parents[j][1]
                # j的祖先节点中有i
                elif i in grands[j]:
                    res[i] += parents[j][1] - parents[i][1]
                else:
                    # 找到它们共同的祖先节点
                    temp, temp2, index = i, j, i
                    if parents[i][1] > parents[j][1]:
                        temp, temp2, index = j, i, j
                    while parents[temp][0] != None:
                        if parents[temp][0] in grands[temp2]:
                            res[i] += parents[index][1] + parents[temp2][1] - 2 * parents[parents[temp][0]][1]
                            break
                        temp = parents[temp][0]


        # 找到两个节点之间的距离
        for i in range(N):
            func(0, i, i)
            func(i + 1, N, i)
        return res


if __name__ == '__main__':
    N = 5
    edges = [[2,0],[4,2],[3,1],[1,0]]
    s = Solution()
    print(s.sumOfDistancesInTree(N, edges))