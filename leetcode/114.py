# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root or (not root.left and not root.right) :
            return root
        # 先序遍历
        stack = []
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)
        cur = root
        while stack:
            temp = stack.pop()
            if temp.right:
                stack.append(temp.right)
            if temp.left:
                stack.append(temp.left)
            cur.left = None
            cur.right = temp
            cur = cur.right