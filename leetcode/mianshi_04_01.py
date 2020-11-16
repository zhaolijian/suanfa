from collections import defaultdict


class Solution:
    def findWhetherExistsPath(self, n: int, graph, start: int, target: int) -> bool:
        if n == 0:
            return False
        init = defaultdict(set)
        for s, end in graph:
            init[s].add(end)

        def func(start, target, visited):
            if target == start:
                return True
            elif visited[start]:
                return False
            visited[start] = True
            for ele in init[start]:
                if func(ele, target, visited):
                    return True
            return False

        # 防止出现环
        visited = [False for i in range(n)]
        return func(start, target, visited)


if __name__ == '__main__':
    s = Solution()
    n = 25
    graph = [[0, 1], [0, 3], [0, 10], [0, 18], [1, 2], [1, 7], [1, 11], [1, 12], [2, 4], [2, 5], [2, 13], [2, 16], [3, 6],
     [3, 8], [4, 9], [5, 17], [7, 20], [7, 22], [8, 10], [10, 19], [11, 15], [13, 14], [14, 21], [15, 23], [19, 24],
     [20, 22]]
    start = 0
    target = 12
    print(s.findWhetherExistsPath(n, graph, start, target))