# 给你一个字符串 s，以及该字符串中的一些「索引对」数组 pairs，其中 pairs[i] = [a, b] 表示字符串中的两个索引（编号从 0 开始）。
# 你可以 任意多次交换 在 pairs 中任意一对索引处的字符。
# 返回在经过若干次交换后，s 可以变成的按字典序最小的字符串。


# 方法1 并查集 有关联关系的字符集合中的任意字符都可以交换，所以只要得到所有的字符集合，按照顺序从小到大放在相应的位置上即可
from collections import defaultdict
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # 位置tuple: 字符sorted_list

        def find(node):
            if parents[node] != node:
                parents[node] = find(parents[node])
            return parents[node]

        def union(node1, node2):
            parents[find(node1)] = find(node2)

        length = len(s)
        parents = [i for i in range(length)]
        # 根节点: 字符list
        tuples = defaultdict(list)
        for first, second in pairs:
            union(first, second)
        for i in range(length):
            tuples[find(i)].append(s[i])
        for key in tuples:
            tuples[key].sort(reverse=True)
        res = ""
        for i in range(length):
            res += tuples[find(i)].pop()
        return res