# 根据一棵树的中序遍历与后序遍历构造二叉树。
# 注意:
# 你可以假设树中没有重复的元素。
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return None
        head = TreeNode(postorder[-1])
        l = inorder.index(postorder[-1])
        head.left = self.buildTree(inorder[: l], postorder[: l])
        head.right = self.buildTree(inorder[l + 1:], postorder[l: -1])
        return head


