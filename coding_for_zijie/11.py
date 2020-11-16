# 需要找到所有的抖音红人，用户数为N，用户为1-N,关注关系有M对。(A,B)代表A关注了B。关注关系具有传递关系，比如有(A,B)(B,C)，那么认为A间接关注了C。
# 如果一个用户被所有N - 1个用户直接或间接关注，那么我们认为这个用户就是抖音红人。求抖音红人的总数。
# 输入：
# 第一行，整数N
# 第二行，整数M
# 第三行，M*2个整数，代表M个关注关系
# 输出：
# 整数
# 样例输入：
# 3
# 3
# 1 2 2 1 2 3
# 样例输出：
# 1
# 提示：
# 只有3用户，有直接粉丝2，间接粉丝1，所以3用户是唯一的抖音红人。
from collections import defaultdict
class Solution:
    # 用户数、关系对数
    def func(self, N, M, array):
        def dfs(root, son):
            for ele in d[son]:
                if not visited[ele - 1]:
                    visited[ele - 1] = True
                    res[root - 1] += 1
                    dfs(root, ele)

        # 存储该用户和他的粉丝
        d = defaultdict(set)
        res = [1 for i in range(N)]
        for i in range(0, len(array), 2):
            d[array[i + 1]].add(array[i])
        for i in range(N):
            visited = [False for i in range(N)]
            visited[i] = True
            # 根节点、子节点
            dfs(i + 1, i + 1)
        result = 0
        for ele in res:
            if ele == N:
                result += 1
        return res, result


if __name__ == '__main__':
    s = Solution()
    N = int(input())
    M = int(input())
    array = list(map(int, input().strip().split()))
    res, result = s.func(N, M, array)
    print(res)
    print('共有{}个明星节点'.format(result))