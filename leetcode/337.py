# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        def func(root):
            if not root:
                return None
            right = func(root.right)
            left = func(root.left)
            l, r, ll, lr, rl, rr = 0, 0, 0, 0, 0, 0
            if left:
                l = left.val
                if left.left:
                    ll = left.left.val
                if left.right:
                    lr = left.right.val
            if right:
                r = right.val
                if right.left:
                    rl = right.left.val
                if right.right:
                    rr = right.right.val
            root.val = max(l + r, root.val + ll + lr + rl + rr)
            return root
        if not root:
            return 0
        else:
            return func(root).val


if __name__ == '__main__':
    s = Solution()
    # [3, 2, 3, null, 3, null, 1]
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    l = root.left
    l.right = TreeNode(3)
    r = root.right
    r.right = TreeNode(1)
    print(s.rob(root))