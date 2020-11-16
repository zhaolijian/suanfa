# 树的前序遍历
# 前序遍历之递归
class Solution:
    def __init__(self):
        self.res = []

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        self.res.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)
        return self.res


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        def func(root):
            if not root:
                return
            res.append(root.val)
            func(root.left)
            func(root.right)
        func(root)
        return res


# 前序遍历之迭代
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            temp = stack.pop()
            res.append(temp.val)
            if temp.right:
                stack.append(temp.right)
            if temp.left:
                stack.append(temp.left)
        return res