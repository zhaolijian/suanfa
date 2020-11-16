class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 方法1 递归
# 思想：求最近公共祖先，两种情况：一个是左子树中含有一个节点，右子树中含有一个节点
# 另一个是p/q中有一个节点和当前节点相同，并且当前节点的左子树或者右子树中有另外一个节点
# 返回最近公共祖先，而不返回靠近根节点祖先原因：靠近根节点祖先节点的l、r只有一个为true，进不了if子句
# class Solution:
#     def __init__(self):
#         self.res = None
#
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         def func(root, p, q):
#             if not root:
#                 return False
#             l = func(root.left, p, q)
#             r = func(root.right, p, q)
#             if (l and r) or ((root.val == p.val or root.val == q.val) and (l or r)):
#                 self.res = root
#             return root.val == p.val or root.val == q.val or l or r
#
#         func(root, p, q)
#         return self.res


# 方法2： 存储所有节点的父节点，找到p节点的所有祖先节点，然后遍历q的祖先节点，找到第一个相同的返回
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node, pre):
            d[node] = pre
            if node.left:
                dfs(node.left, node)
            if node.right:
                dfs(node.right, node)

        d = {}
        dfs(root, None)
        p_parents = set()
        while p:
            p_parents.add(p)
            p = d[p]
        while q:
            if q in p_parents:
                return q
            q = d[q]


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(5)
    input1 = root.left
    root.right = TreeNode(1)
    l = root.left
    l.left = TreeNode(6)
    l.right = TreeNode(2)
    r = root.right
    r.left = TreeNode(0)
    r.right = TreeNode(8)
    lr = l.right
    lr.left = TreeNode(7)
    lr.right = TreeNode(4)
    input2 = lr.right
    print(s.lowestCommonAncestor(root, input1, input2))