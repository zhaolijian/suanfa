# 队列，迭代
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root or (not root.left and not root.right):
            return True
        queue = [root.left, root.right]
        while queue:
            one = queue.pop(0)
            two = queue.pop(0)
            if not one and not two:
                continue
            elif not one or not two:
                return False
            else:
                if one.val == two.val:
                    queue.append(one.left)
                    queue.append(two.right)
                    queue.append(one.right)
                    queue.append(two.left)
                else:
                    return False
        return True


# 递归
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root or (not root.left and not root.right):
            return True
        left = root.left
        right = root.right
        return self.func(left, right)

    def func(self, left, right):
        if not left and not right:
            return True
        elif not left or not right:
            return False
        else:
            if left.val == right.val:
                return self.func(left.left, right.right) and self.func(left.right, right.left)
            else:
                return False
