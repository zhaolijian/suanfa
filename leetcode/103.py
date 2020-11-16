# 给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        if not root:
            return []
        array = [root]
        res = []
        flag = 1
        while array:
            cur = []
            length = len(array)
            if flag % 2:
                for i in range(length):
                    cur.append(array[i].val)
            else:
                for i in range(length - 1, -1, -1):
                    cur.append(array[i].val)
            res.append(cur)
            for i in range(length):
                temp = array.pop(0)
                if temp.left:
                    array.append(temp.left)
                if temp.right:
                    array.append(temp.right)
            flag += 1
        return res