# 从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        array = [root]
        while array:
            cur = []
            for i in range(len(array)):
                temp = array.pop(0)
                cur.append(temp.val)
                if temp.left:
                    array.append(temp.left)
                if temp.right:
                    array.append(temp.right)
            res.append(cur)
        return res