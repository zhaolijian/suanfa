# 给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）中，按结点数值大小顺序第三小结点的值为4。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if not pRoot or k <= 0:
            return None
        res = []
        def func(root):
            if not root or len(res) >= k:
                return
            func(root.left)
            res.append(root)
            func(root.right)
        func(pRoot)
        return res[k - 1] if len(res) >= k else None


if __name__ == '__main__':
    s = Solution()
    pRoot = TreeNode(8)
    pRoot.left = TreeNode(6)
    pRoot.right = TreeNode(10)
    l = pRoot.left
    l.left = TreeNode(5)
    l.right = TreeNode(7)
    r = pRoot.right
    r.left = TreeNode(9)
    r.right = TreeNode(11)
    k = 1
    print(s.KthNode(pRoot, k))