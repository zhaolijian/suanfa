# 找公共父节点(最根处节点为1)
# 例子如下，不是本来题目的例子，应该差不多，6代表有6个节点，它下面接的是5条双向路径，再然后是接的要求目标路程数，接着是目标路程，说的不太好，
# 举个例子吧 6 4 ，那么6必须到3，然后3到2，2到4，这个过程中经过的最小点是2，所以第一行输出是2.
# 5 3也是同理，5经过4，经过2，最后达到3，所以第二行输出2，这个看了之前有同学说的应该是用图的深搜？不太懂，太菜了
# 输入：
# 6
# 1 2
# 2 3
# 2 4
# 4 5
# 3 6
# 2
# 6 4
# 5 3
# 输出：
# 2
# 2

# 输入
# 9
# 1 2
# 1 3
# 4 2
# 2 5
# 2 6
# 3 7
# 8 3
# 3 9
# 3
# 4 5
# 5 7
# 7 9
# 输出 [2 1 3]
# 需要建立父节点序列
from collections import defaultdict
class Solution:
    def func(self, N, array, K, tasks):
        # 目的是构建子节点-父节点字典
        def dfs(root):
            if root == 1:
                parents[root] = -1
            for ele in d[root]:
                if not visited[ele - 1]:
                    parents[ele] = root
                    array.append(ele)
                    visited[ele - 1] = 1

        parents, d = defaultdict(int), defaultdict(list)
        for ele1, ele2 in array:
            d[ele1].append(ele2)
            d[ele2].append(ele1)
        array = [1]
        visited = [0 for i in range(N)]
        visited[0] = 1
        while array:
            dfs(array.pop(0))
        res = []
        # 找t1和t2公共最近祖先节点
        for t1, t2 in tasks:
            set_t1 = set()
            while t1 != -1:
                set_t1.add(t1)
                t1 = parents[t1]
            while t2 != -1:
                if t2 in set_t1:
                    res.append(t2)
                    break
                else:
                    t2 = parents[t2]
        return res


if __name__ == '__main__':
    s = Solution()
    # 敌军控制的n个城市
    N = int(input())
    # 直连道路城市对
    array = []
    for i in range(N - 1):
        temp = list(map(int, input().split()))
        array.append(temp)
    # 需要执行的传递任务数量
    K = int(input())
    tasks = []
    # 传递任务的起始终止城市对 1<=Mi<=Ni<N
    for i in range(K):
        temp = list(map(int, input().split()))
        tasks.append(temp)
    print(s.func(N, array, K, tasks))