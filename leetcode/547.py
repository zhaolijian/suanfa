# 老547
# 班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，
# 那么我们可以认为 A 也是 C 的朋友。所谓的朋友圈，是指所有朋友的集合。
# 给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，表示已知第 i 个和 j 个学生互为朋友关系，
# 否则为不知道。你必须输出所有学生中的已知的朋友圈总数。

# 新547，就是改了改说法，本质一样
# 有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。
# 省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。
# 给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，
# 而 isConnected[i][j] = 0 表示二者不直接相连。返回矩阵中 省份 的数量。


# 方法1 dfs，
class Solution:
    def findCircleNum(self, isConnected) -> int:
        def dfs(index):
            nonlocal length
            for i in range(length):
                if isConnected[index][i] == 1 and i not in visisted:
                    visisted.add(i)
                    dfs(i)

        length = len(isConnected)
        res = 0
        visisted = set()
        for i in range(length):
            if i not in visisted:
                visisted.add(i)
                res += 1
                dfs(i)
        return res
#
#
# # 方法2 bfs，发现bfs总是比dfs复杂度低
class Solution:
    def findCircleNum(self, isConnected) -> int:
        length = len(isConnected)
        res = 0
        # 访问过的节点
        visisted = set()
        for i in range(length):
            if i not in visisted:
                array = [i]
                visisted.add(i)
                res += 1
                while array:
                    temp = array.pop()
                    for j in range(length):
                        if isConnected[temp][j] == 1 and j not in visisted:
                            array.append(j)
                            visisted.add(j)
        return res


# 方法3 并查集
# class Solution:
#     def findCircleNum(self, isConnected) -> int:
#         def find(index):
#             if parent[index] != index:
#                 parent[index] = find(parent[index])
#             return parent[index]
#
#         def union(node1, node2):
#             parent[find(node1)] = find(node2)
#
#
#         length = len(isConnected)
#         parent = [i for i in range(length)]
#         for i in range(length):
#             for j in range(i):
#                 if isConnected[i][j] == 1:
#                     union(i, j)
#         return sum(find(i) == i for i in range(length))


if __name__ == '__main__':
    s = Solution()
    # M = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
    M = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
    print(s.findCircleNum(M))