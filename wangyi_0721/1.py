# 反转树
# [[1,0],[2,1],[3,1]]
# [[1,0],[3,1],[2,1]]
# 树的反转，树的结构如下：[ [1,0],[2,1],[3,1],[5,2],[6,5],[7,5],[4,1] ]
# 反转结果是 [ [1,0],[4,1],[3,1],[2,1],[5,2],[7,5],[6,5] ] ,
# 题目含义如下：[1,0] 第一个元素是本节点的值，第二个元素是父节点的值。
import collections
class Solution:
    def invert_tree(self, node_data_list ):
        def dfs(root, parent):
            if parent != -1:
                res.append([root, parent])
            for i in range(len(d[root]) - 1, -1, -1):
                dfs(d[root][i], root)

        length = len(node_data_list)
        if length <= 1:
            return node_data_list
        # 根节点：子节点
        d = collections.defaultdict(list)
        for i, j in node_data_list:
            d[j].append(i)
        res = []
        dfs(0, -1)
        return res


if __name__ == '__main__':
    s = Solution()
    node_data_list = [[1,0],[2,1],[5,2],[6,5],[7,5],[3,1],[4,1]]
    print(s.invert_tree(node_data_list))