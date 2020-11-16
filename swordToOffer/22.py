# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 创建一个temp队列，将根节点放入到temp队列中，从队列中取元素，放入到res队列中，
# 当取元素时判断取的元素有没有子节点，如果有子节点，则将子节点加入到temp队列中
class Solution:
    def PrintFromTopToBottom(self, root):
        if root is None:
            return []
        res = []
        temp = [root]
        while temp:
            res.append(temp[0].val)
            if temp[0].left:
                temp.append(temp[0].left)
            if temp[0].right:
                temp.append(temp[0].right)
            temp.pop(0)
        return res



