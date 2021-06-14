# 请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。


# 方法1 递归
class Solution:
    def isSymmetric(self, root) -> bool:
        if not root or (not root.left and not root.right):
            return True
        def func(l, r):
            if not l and not r:
                return True
            if not l or not r:
                return False
            if l.val != r.val:
                return False
            return func(l.left, r.right) and func(l.right, r.left)

        return func(root.left, root.right)


# 方法2
class Solution:
    def isSymmetric(self, root) -> bool:
        if not root or (not root.left and not root.right):
            return True
        stack = [root.left, root.right]
        while stack:
            first, second = stack.pop(), stack.pop()
            if not first and not second:
                continue
            elif not first or not second:
                return False
            elif first.val != second.val:
                return False
            else:
                stack.append(first.right)
                stack.append(second.left)
                stack.append(first.left)
                stack.append(second.right)
        return True