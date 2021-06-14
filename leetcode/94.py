# 二叉树的中序遍历（递归方法和非递归方法）
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 栈
class Solution:
    def inorderTraversal(self, root: TreeNode):
        if not root:
            return []
        stack = []
        res = []
        cur = root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                temp = stack.pop()
                res.append(temp.val)
                if temp.right:
                    cur = temp.right
        return res


# 栈，与上面方法类似
class Solution:
    def inorderTraversal(self, root: TreeNode):
        res = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res


# 颜色标记法，已经访问过的变为灰色，没有访问过的为白色，当从栈中取出灰色的时候放入结果集中，取出白色的时候右中左的顺序放入栈，其中白色的变为灰色
class Solution:
    def inorderTraversal(self, root: TreeNode):
        if not root:
            return []
        white, gray = 1, 0
        res = []
        stack = [[white, root]]
        while stack:
            color, cur = stack.pop()
            if color == white:
                if cur.right:
                    stack.append([white, cur.right])
                stack.append([gray, cur])
                if cur.left:
                    stack.append([white, cur.left])
            else:
                res.append(cur.val)
        return res


# 递归
class Solution:
    def __init__(self):
        self.res = []

    def inorderTraversal(self, root: TreeNode):
        def func(root):
            if not root:
                return
            func(root.left)
            self.res.append(root.val)
            func(root.right)

        func(root)
        return self.res


if __name__ == '__main__':
    s = Solution()
    print(s.inorderTraversal())