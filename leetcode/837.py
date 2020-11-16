class Solution:
    # 思路：动态规划，从后往前推
    def new21Game(self, N: int, K: int, W: int) -> float:
        # init中的每一个元素值表示起始分数为索引值，最终结果小于等于N的概率
        init = [0] * (K + W)
        for i in range(K, min(K + W,  N + 1)):
            init[i] = 1
        init[K - 1] = 1 / W * (min(N, K + W - 1) - K + 1)
        # 上面一句话用下面注释的几行代替也可以
        # temp = 0
        # for k in range(K, K + W):
        #     temp += init[k]
        # init[K - 1] = 1 / W * temp
        for j in range(K - 2, -1, -1):
            init[j] = init[j + 1] - (1 / W) * (init[j + W + 1] - init[j + 1])
        return init[0]


# 方法2  提前判断好N、 K + W - 1的大小关系，在之后的操作用变得简单
class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        if N >= K + W - 1:
            return 1
        else:
            # init中的每一个元素值表示起始分数为索引值，最终结果小于等于N的概率
            init = [0] * (K + W)
            for i in range(K, N + 1):
                init[i] = 1
            temp = 0
            init[K - 1] = 1 / W * (N - K + 1)
            for j in range(K - 2, -1, -1):
                init[j] = init[j + 1] - (1 / W) * (init[j + W + 1] - init[j + 1])
            return init[0]


if __name__ == '__main__':
    s = Solution()
    N, K, W = 21, 17, 10
    print(s.new21Game(N, K, W))