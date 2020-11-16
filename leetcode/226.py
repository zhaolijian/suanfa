# 方法1 递归
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root or (not root.left and not root.right):
            return root
        temp = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(temp)
        return root


# 或
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


# 方法2 迭代
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        queue = [root]
        while queue:
            temp = queue.pop()
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
            temp.left, temp.right = temp.right, temp.left
        return root


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        queue = [root]
        while queue:
            # 使用pop(0)比使用pop()慢很多
            temp = queue.pop(0)
            if temp.right:
                queue.append(temp.right)
            if temp.left:
                queue.append(temp.left)
            temp.left, temp.right = temp.right, temp.left
        return root