# 现在你总共有 n 门课需要选，记为 0 到 n-1。
# 在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]
# 给定课程总量以及它们的先决条件，返回你为了学完所有课程所安排的学习顺序。
# 可能会有多个正确的顺序，你只要返回一种就可以了。如果不可能完成所有课程，返回一个空数组。


# 方法1 拓扑排序+bfs
from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        if not prerequisites:
            return [i for i in range(numCourses)]
        # 入度表
        indegrees = [0] * numCourses
        # 临接表
        adjoins = defaultdict(list)
        array = []
        res = []
        for first, second in prerequisites:
            indegrees[first] += 1
            adjoins[second].append(first)
        for i in range(numCourses):
            if indegrees[i] == 0:
                array.append(i)
        while array:
            temp = array.pop()
            res.append(temp)
            numCourses -= 1
            for ele in adjoins[temp]:
                indegrees[ele] -= 1
                if indegrees[ele] == 0:
                    array.append(ele)
        return res if numCourses == 0 else []


# 方法2 拓扑排序 + dfs
from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        def dfs(node):
            visisted.add(node)
            res.append(node)
            for ele in adjoins[node]:
                indegrees[ele] -= 1
                if indegrees[ele] == 0:
                    dfs(ele)

        if not prerequisites:
            return [i for i in range(numCourses)]
        indegrees = [0] * numCourses
        adjoins = defaultdict(list)
        res = []
        visisted = set()
        for first, second in prerequisites:
            indegrees[first] += 1
            adjoins[second].append(first)
        for i in range(numCourses):
            if i not in visisted and indegrees[i] == 0:
                dfs(i)
        return res if numCourses == len(res) else []


if __name__ == '__main__':
    s = Solution()
    numCourses = 2
    prerequisites = [[1, 0]]
    print(s.findOrder(numCourses, prerequisites))