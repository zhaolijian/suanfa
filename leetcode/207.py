# 你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。
# 在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1]
# 给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？


# 方法1 有向无环图 效率很高  入度表+临接表+bfs
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        # 将入度为0的放入队列中,每次从队列中取元素,遍历其邻接表,将入度减1
        indegrees = [0] * numCourses
        adgacency = defaultdict(list)
        queue = []
        for ele, pre in prerequisites:
            indegrees[ele] += 1
            adgacency[pre].append(ele)
        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)
        while queue:
            temp = queue.pop(0)
            numCourses -= 1
            for i in adgacency[temp]:
                indegrees[i] -= 1
                if indegrees[i] == 0:
                    queue.append(i)
        return not numCourses


# 方法2 普通dfs，复杂度较高，有更优化的dfs，比较复杂
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        d = defaultdict(list)
        for first, second in prerequisites:
            d[second].append(first)

        def dfs(node):
            for key in d.keys():
                if key not in visisted and node in d[key]:
                    return
            visisted.add(node)
            for ele in d[node]:
                dfs(ele)

        if not prerequisites:
            return True
        visisted = set()
        for ele in range(numCourses):
            if ele not in visisted:
                dfs(ele)
        return len(visisted) == numCourses


if __name__ == '__main__':
    s = Solution()
    numCourses = 3
    prerequisites = [[1,0]]
    print(s.canFinish(numCourses, prerequisites))