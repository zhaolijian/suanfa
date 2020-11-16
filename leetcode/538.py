class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 后序遍历
class Solution:
    def __init__(self):
        self.total = 0

    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        else:
            self.convertBST(root.right)
            self.total += root.val
            root.val = self.total
            self.convertBST(root.left)
        return root

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(5)
    root.left = TreeNode(2)
    root.right = TreeNode(13)
    print(s.convertBST(root))