# 判断一棵树是否是平衡二叉树
# 空树或者左右子树的高度差不大于1
# 子树也同样满足这个性质


class Solution:
    def IsBalanced_Solution(self, pRoot):
        bool, max_height = self.height(pRoot)
        return bool

    def height(self, pRoot):
        if not pRoot:
            return True, 0
        if not pRoot.left and not pRoot.right:
            return True, 1
        bool = False
        bool1, h1 = self.height(pRoot.left)
        bool2, h2 = self.height(pRoot.right)
        if abs(h1 - h2) <= 1 and bool1 and bool2:
            bool = True
        return bool, max(h1, h2) + 1

