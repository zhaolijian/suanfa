# n 块石头放置在二维平面中的一些整数坐标点上。每个坐标点上最多只能有一块石头。
# 如果一块石头的 同行或者同列 上有其他石头存在，那么就可以移除这块石头。
# 给你一个长度为 n 的数组 stones ，其中 stones[i] = [xi, yi] 表示第 i 块石头的位置，返回 可以移除的石子 的最大数量。


# dfs  超过95%
from collections import defaultdict
class Solution:
    def removeStones(self, stones) -> int:
        # 横坐标: 横坐标相等的集合
        dict_x = defaultdict(list)
        # 纵坐标: 纵坐标相等的集合
        dict_y = defaultdict(list)
        for x, y in stones:
            dict_x[x].append((x, y))
            dict_y[y].append((x, y))

        def dfs(node):
            if node not in visisted:
                visisted.add(node)
                for ele in dict_x[node[0]]:
                    dfs(ele)
                for ele in dict_y[node[1]]:
                    dfs(ele)

        visisted = set()
        res = 0
        for ele in stones:
            if tuple(ele) not in visisted:
                res += 1
                dfs(tuple(ele))
        return len(stones) - res


# bfs  超过95%
from collections import defaultdict
class Solution:
    def removeStones(self, stones) -> int:
        # 横坐标: 横坐标相等的集合
        dict_x = defaultdict(list)
        # 纵坐标: 纵坐标相等的集合
        dict_y = defaultdict(list)
        for x, y in stones:
            dict_x[x].append((x, y))
            dict_y[y].append((x, y))
        visisted = set()
        res = 0
        for ele in stones:
            if tuple(ele) not in visisted:
                res += 1
                array = [tuple(ele)]
                while array:
                    temp = array.pop()
                    visisted.add(temp)
                    for ele in dict_x[temp[0]]:
                        if ele not in visisted:
                            array.append(ele)
                    for ele in dict_y[temp[1]]:
                        if ele not in visisted:
                            array.append(ele)
        return len(stones) - res


# 并查集 效果和dfs/bfs差不多
# 思路是，将两个点是否横坐标相同或者纵坐标相同的二维情况转化为一维情况，因为横纵坐标的值的范围为[0,10000]，
# 所以可以通过使一个坐标加减一个超过10000的数实现，使得同一个点的横纵坐标画上等号
class Solution:
    def removeStones(self, stones) -> int:
        def find(node):
            if parents[node] != node:
                parents[node] = find(parents[node])
            return parents[node]

        def union(node1, node2):
            parents[find(node2)] = find(node1)

        # x + y各自最多10001个取值,这创建一个20005大小的数组
        parents = [i for i in range(20005)]
        for x, y in stones:
            union(x, y + 10001)

        res = set()
        for ele in stones:
            if parents[ele[0]] == ele[0]:
                res.add(ele[0])
        return len(stones) - len(res)

# 并查集   效果较差，但是能过
class Solution:
    def removeStones(self, stones) -> int:
        def find(node):
            if parents[node] != node:
                parents[node] = find(parents[node])
            return parents[node]

        def union(node1, node2):
            parents[find(node1)] = find(node2)

        length = len(stones)
        parents = [i for i in range(length)]
        # 这复杂度太高了
        for i in range(length):
            for j in range(i + 1, length):
                # 如果两个点的横坐标或者纵坐标相等,则合并
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    union(i, j)
        res = 0
        for i in range(length):
            # 如果parents[i] == i,则i为根节点
            if parents[i] == i:
                res += 1
        return length - res


if __name__ == '__main__':
    s = Solution()
    stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
    print(s.removeStones(stones))