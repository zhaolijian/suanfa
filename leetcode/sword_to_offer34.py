# 输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        def func(root, target, already):
            # 非叶子结点(比如某节点的左节点为空但是有右结点)或者根节点为空节点
            if not root:
                return
            # 叶子结点
            if not root.left and not root.right:
                if target == root.val:
                    already += [root.val]
                    res.append(already)
                return
            func(root.left, target - root.val, already + [root.val])
            func(root.right, target - root.val, already + [root.val])
        res = []
        func(root, target, [])
        return res