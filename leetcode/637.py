# 给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。
from collections import deque
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        res = []
        array = deque([root])
        while array:
            temp = 0
            length = len(array)
            for i in range(length):
                node = array.popleft()
                temp += node.val
                if node.left:
                    array.append(node.left)
                if node.right:
                    array.append(node.right)
            res.append(temp / length)
        return res