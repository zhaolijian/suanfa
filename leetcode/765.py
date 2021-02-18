# N 对情侣坐在连续排列的 2N 个座位上，想要牵到对方的手。 计算最少交换座位的次数，以便每对情侣可以并肩坐在一起。 一次交换可选择任意两人，让他们站起来交换座位。
# 人和座位用 0 到 2N-1 的整数表示，情侣们按顺序编号，第一对是 (0, 1)，第二对是 (2, 3)，以此类推，最后一对是 (2N-2, 2N-1)。
# 这些情侣的初始座位  row[i] 是由最初始坐在第 i 个座位上的人决定的。


# 方法1 并查集
# m对情侣构成一个坐错环（即连通分量），则需要交换m-1次，所以统计连通分量的个数，用length//2-连通分量数即为交换次数
class Solution:
    def minSwapsCouples(self, row) -> int:
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(node1, node2):
            parent[find(node2)] = find(node1)

        length = len(row)
        parent = [i for i in range(length // 2)]
        for i in range(0, length, 2):
            union(row[i] // 2, row[i + 1] // 2)
        res = sum(i == find(i) for i in range(length // 2))
        return length // 2 - res


# 方法2 贪心
class Solution:
    def minSwapsCouples(self, row) -> int:
        map = {ele: i for i, ele in enumerate(row)}
        res, length = 0, len(row)
        for i in range(0, length, 2):
            first, second = row[i] // 2, row[i + 1] // 2
            if first != second:
                if row[i] % 2 == 0:
                    # row[i] + 1 原先所在位置
                    index = map[row[i] + 1]
                    row[i + 1], row[index] = row[index], row[i + 1]
                    # 更新索引
                    map[row[index]] = index
                else:
                    # row[i] - 1 原先所在位置
                    index = map[row[i] - 1]
                    row[i + 1], row[index] = row[index], row[i + 1]
                    # 更新索引
                    map[row[index]] = index
                res += 1
        return res


if __name__ == '__main__':
    s = Solution()
    row = [1,4,0,5,8,7,6,3,2,9]
    print(s.minSwapsCouples(row))