# 根据前序和中序重建二叉树
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        index = -1
        for i in range(len(inorder)):
            if inorder[i] == preorder[0]:
                index = i
                break
        root.left = self.buildTree(preorder[1: index + 1], inorder[:index])
        root.right = self.buildTree(preorder[index + 1:], inorder[index + 1:])
        return root