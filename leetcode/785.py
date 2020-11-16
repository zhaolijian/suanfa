# 并查集 
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # 查找根节点
        def find(x):
            if init[x] == x:
                return x
            else:
                init[x] = find(init[x])
            return init[x]

        length = len(graph)
        for ele in graph:
            ele.sort()
        init = [i for i in range(length)]
        for index, val in enumerate(graph):
            for j in range(1, len(val)):
                init[find(val[j])] = find(val[0])
            for j in range(len(val)):
                if find(index) == find(val[j]):
                    return False
        return True
