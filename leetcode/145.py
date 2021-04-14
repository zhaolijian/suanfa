# 二叉树的后序遍历

# 方法1 递归
class Solution:
    def __init__(self):
        self.res = []

    def postorderTraversal(self, root):
        if not root:
            return
        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        self.res.append(root.val)
        return self.res


# 方法2 迭代
class Solution:
    def postorderTraversal(self, root):
        if not root:
            return []
        init = [root]
        res = []
        while init:
            temp = init.pop()
            res.append(temp.val)
            if temp.left:
                init.append(temp.left)
            if temp.right:
                init.append(temp.right)
        return res[::-1]


# 方法3 颜色标记法
class Solution:
    def postorderTraversal(self, root):
        if not root:
            return []
        red, white = 1, 0
        stack = [(root, white)]
        res = []
        while stack:
            temp, color = stack.pop()
            if color == red:
                res.append(temp.val)
            else:
                stack.append((temp, red))
                if temp.right:
                    stack.append((temp.right, white))
                if temp.left:
                    stack.append((temp.left, white))
        return res