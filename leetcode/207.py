# 有向无环图
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 将入度为0的放入队列中,每次从队列中取元素,遍历其邻接表,将入度减1
        indegrees = [0 for i in range(numCourses)]
        adgacency = [[] for i in range(numCourses)]
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
