# 给你一棵树（即，一个连通的无环无向图），这棵树由编号从 0  到 n - 1 的 n 个节点组成，且恰好有 n - 1 条 edges 。
# 树的根节点为节点 0 ，树上的每一个节点都有一个标签，也就是字符串 labels 中的一个小写字符（编号为 i 的 节点的标签就是 labels[i] ）
# 边数组 edges 以 edges[i] = [ai, bi] 的形式给出，该格式表示节点 ai 和 bi 之间存在一条边。
# 返回一个大小为 n 的数组，其中 ans[i] 表示第 i 个节点的子树中与节点 i 标签相同的节点数。
# 树 T 中的子树是由 T 中的某个节点及其所有后代节点组成的树。
from collections import Counter, defaultdict
# 方法1
class Solution:
    def countSubTrees(self, n: int, edges, labels: str):
        edge_map = defaultdict(list)
        for edge in edges:
            edge_map[edge[0]].append(edge[1])
            edge_map[edge[1]].append(edge[0])

        def _dfs(i):
            visited.add(i)
            # 字符数字典(关键)
            data = Counter({labels[i]: 1})
            for nxt in edge_map[i]:
                if nxt not in visited:
                    # 合并子树的字符数
                    data += _dfs(nxt)
            # 设置当前节点的结果字符数
            ans[i] = data[labels[i]]
            return data

        visited = set()
        ans = [1] * n
        _dfs(0)
        return ans



class Solution:
    def countSubTrees(self, n: int, edges, labels: str):
        def dfs(root, pre):
            temp = Counter({labels[root]: 1})
            for ele in d[root]:
                # 当ele等于pre时，说明ele为root的父节点，已经访问过了
                if ele != pre:
                    temp += dfs(ele, root)
            res[root] = temp[labels[root]]
            return temp

        res = [1] * n
        d = defaultdict(list)
        for i in range(n - 1):
            d[edges[i][0]].append(edges[i][1])
            d[edges[i][1]].append(edges[i][0])
        dfs(0, -1)
        return res


if __name__ == '__main__':
    s = Solution()
    n = 4
    edges = [[0, 2], [0, 3], [1, 2]]
    labels = "aeed"
    print(s.countSubTrees(n, edges, labels))
