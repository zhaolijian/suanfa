# 给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）    中，按结点数值大小顺序第三小结点的值为4。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        if not pRoot or k <= 0:
            return None
        array = []

        def find(pRoot):
            if not pRoot or len(array) >= k:
                return
            find(pRoot.left)
            array.append(pRoot)
            find(pRoot.right)
        find(pRoot)
        if len(array) >= k:
            return array[k - 1]
        return None


if __name__ == '__main__':
    s = Solution()
    pRoot = TreeNode(5)
    pRoot.left = TreeNode(3)
    pRoot.right = TreeNode(7)
    l = pRoot.left
    l.left = TreeNode(2)
    l.right = TreeNode(4)
    r = pRoot.right
    r.left = TreeNode(6)
    r.right = TreeNode(8)
    k = 3
    print(s.KthNode(pRoot, k))