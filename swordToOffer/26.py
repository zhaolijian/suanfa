# -*- coding:utf-8 -*-
# 将二叉搜索数转换为双向链表，使用中序遍历
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#
class Solution:
    # 使用中序遍历
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return None
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree
        leftNode = self.Convert(pRootOfTree.left)
        rightNode = self.Convert(pRootOfTree.right)
        p = leftNode
        while leftNode and p.right:
            p = p.right
        if leftNode:
            p.right = pRootOfTree
            pRootOfTree.left = p
        if rightNode:
            rightNode.left = pRootOfTree
            pRootOfTree.right = rightNode
        return leftNode if leftNode else pRootOfTree