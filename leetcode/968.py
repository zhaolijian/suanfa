# 给定一个二叉树，我们在树的节点上安装摄像头。
# 节点上的每个摄影头都可以监视其父对象、自身及其直接子对象。
# 计算监控树的所有节点所需的最小摄像头数量。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 从底向上
class Solution:
    def __init__(self):
        self.res = 0

    # 0表示需要被拍, 1表示被拍, 2表示该节点架摄像头
    def minCameraCover(self, root: TreeNode) -> int:
        def func(root):
            if not root:
                return 1
            l = func(root.left)
            r = func(root.right)
            if l == 0 or r == 0:
                self.res += 1
                return 2
            if l == 2 or r == 2:
                return 1
            else:
                return 0
        if func(root) == 0:
            self.res += 1
        return self.res


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(0)
    root.left = TreeNode(0)
    root.right = TreeNode(0)
    l = root.left
    l.right = TreeNode(0)
    r = root.right
    r.left = TreeNode(0)
    lr = l.right
    lr.right = TreeNode(0)
    print(s.minCameraCover(root))