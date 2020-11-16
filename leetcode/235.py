# 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 方法1
from collections import deque
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parents = {root: None}
        queue = deque([root])
        while queue:
            temp = queue.popleft()
            if temp.left:
                parents[temp.left] = temp
                queue.append(temp.left)
            if temp.right:
                parents[temp.right] = temp
                queue.append(temp.right)
        s = set()
        while p:
            s.add(p)
            p = parents[p]
        while q:
            if q in s:
                return q
            q = parents[q]


# 方法2 利用二叉搜索树的性质：左子树节点值比根节点值小，右子树节点值比根节点值大，时间复杂度O(n),空间复杂度O(1)
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        cur = root
        while cur:
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left
            elif p.val > cur.val and q.val > cur.val:
                cur = cur.right
            else:
                return cur


# 方法3，和上面思想一样，时间复杂度O(n),空间复杂度O(n)
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root
