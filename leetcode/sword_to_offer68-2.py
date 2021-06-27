# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        array = [root]
        parent = {root:None}
        while array:
            temp = array.pop(0)
            if temp.left:
                array.append(temp.left)
                parent[temp.left] = temp
            if temp.right:
                array.append(temp.right)
                parent[temp.right] = temp
        s = set()
        while p:
            s.add(p)
            p = parent[p]
        while q:
            if q in s:
                return q
            q = parent[q]