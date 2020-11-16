class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 临接表
        t1 = [[] for _ in range(numCourses)]
        # 入度
        t2 = [0 for _ in range(numCourses)]
        # 存储没有入度的节点
        queue = []
        res = []
        for cur, pre in prerequisites:
            t1[pre].append(cur)
            t2[cur] += 1
        for i in range(numCourses):
            if t2[i] == 0:
                queue.append(i)
        while queue:
            numCourses -= 1
            temp = queue.pop(0)
            res.append(temp)
            for ele in t1[temp]:
                t2[ele] -= 1
                if t2[ele] == 0:
                    queue.append(ele)
        return res if numCourses == 0 else []

