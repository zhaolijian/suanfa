# 需要找到所有的抖音红人，用户数为N，关注关系有M对。(A,B)代表A关注了B。
# 关注关系具有传递关系，比如有(A,B)(B,C)，那么认为A间接关注了C。
# 如果一个用户被所有N个用户直接或间接关注，那么我们认为这个用户就是抖音红人。求抖音红人的总数。
# 输入：**
# 第一行，整数N
# 第二行，整数M
# 第三行，M*2个整数，代表M个关注关系
# 3
# 3
# 1 2 2 1 2 3
# 样例输出：
# 1
# 提示：
# 只有3用户，有直接粉丝2，间接粉丝1，所以3用户是唯一的抖音红人。


from collections import defaultdict
class Solution:
    # 用户数、数组长度、数组
    def func(self, n, m, array):
        # origin代表起点
        def findFans(origin, cur):
            for ele in sons[cur]:
                if not visited[ele]:
                    fans[origin] += 1
                    visited[ele] = True
                    findFans(origin, ele)

        # 用户和关注他的人
        sons = defaultdict(list)
        # 粉丝数
        fans = [1] * n
        for i in range(0, 2 * m, 2):
            sons[array[i + 1] - 1].append(array[i] - 1)
        for i in range(n):
            visited = [False] * n
            visited[i] = True
            findFans(i, i)
        res = 0
        for ele in fans:
            if ele == n:
                res += 1
        return res


if __name__ == '__main__':
    s = Solution()
    n = 3
    m = 3
    array = [1, 2, 2, 1, 2, 3]
    print(s.func(n, m, array))