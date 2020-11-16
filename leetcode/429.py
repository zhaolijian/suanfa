# 给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node'):
        if not root:
            return []
        res = []
        array = [root]
        while array:
            length = len(array)
            cur_array = []
            for i in range(length):
                temp = array.pop(0)
                for ele in temp.children:
                    array.append(ele)
                cur_array.append(temp.val)
            res.append(cur_array)
        return res