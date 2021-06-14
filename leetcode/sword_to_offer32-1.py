# 从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。
class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        array = [root]
        while array:
            temp = array.pop(0)
            res.append(temp.val)
            if temp.left:
                array.append(temp.left)
            if temp.right:
                array.append(temp.right)
        return res