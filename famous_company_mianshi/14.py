# 分别按照二叉树先序，中序和后序打印所有的节点。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 方法1
class Solution:
    def threeOrders(self , root ):
        first = []
        mid = []
        last = []
        def func(root):
            if not root:
                return
            first.append(root.val)
            func(root.left)
            mid.append(root.val)
            func(root.right)
            last.append(root.val)
        func(root)
        return [first, mid, last]


# 方法2
class Solution:
    def threeOrders(self, root):
        def first_select(root):
            if not root:
                return []
            elif not root.left and not root.right:
                return [root.val]
            return [root.val] + first_select(root.left) + first_select(root.right)

        def mid_select(root):
            if not root:
                return []
            elif not root.left and not root.right:
                return [root.val]
            return mid_select(root.left) + [root.val] + mid_select(root.right)

        def last_select(root):
            if not root:
                return []
            elif not root.left and not root.right:
                return [root.val]
            return last_select(root.left) + last_select(root.right) + [root.val]

        res = []
        res.append(first_select(root))
        res.append(mid_select(root))
        res.append(last_select(root))
        return res


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(s.threeOrders(root))