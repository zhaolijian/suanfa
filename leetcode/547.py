# 班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，
# 那么我们可以认为 A 也是 C 的朋友。所谓的朋友圈，是指所有朋友的集合。
# 给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，表示已知第 i 个和 j 个学生互为朋友关系，
# 否则为不知道。你必须输出所有学生中的已知的朋友圈总数。


# 方法1 dfs，多少次dfs就有多少个朋友圈
# class Solution:
#     def findCircleNum(self, M) -> int:
#         def dfs(index):
#             nonlocal length
#             for i in range(length):
#                 if M[index][i] == 1 and not visisted[i]:
#                     visisted[i] = 1
#                     dfs(i)
#
#         # 学生个数
#         length = len(M)
#         visisted = [0] * length
#         res = 0
#         for i in range(length):
#             if not visisted[i]:
#                 dfs(i)
#                 res += 1
#         return res
#
#
# # 方法2 bfs，发现bfs总是比dfs复杂度低
# from collections import deque
# class Solution:
#     def findCircleNum(self, M) -> int:
#         length = len(M)
#         visisted = [0] * length
#         res = 0
#         array = deque([])
#         for i in range(length):
#             if not visisted[i]:
#                 res += 1
#                 array.append(i)
#                 while array:
#                     temp = array.popleft()
#                     for j in range(length):
#                         if M[temp][j] == 1 and not visisted[j]:
#                             visisted[j] = 1
#                             array.append(j)
#         return res


# 方法3 并查集
class Solution:
    def findCircleNum(self, M) -> int:
        def find(index):
            if parents[index] == index:
                return index
            parents[index] = find(parents[index])
            return parents[index]

        parents = {}
        length = len(M)
        for i in range(length):
            parents[i] = i
        for i in range(length):
            for j in range(i, length):
                if M[i][j] == 1:
                    parents[find(j)] = find(i)
        result = set()
        for i in range(length):
            result.add(find(i))
        return len(result)


if __name__ == '__main__':
    s = Solution()
    # M = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
    M = [[1,1,0],[1,1,0],[0,0,1]]
    print(s.findCircleNum(M))