# 请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        array = [root]
        number = 1
        while array:
            cur = []
            for i in range(len(array)):
                temp = array.pop(0)
                cur.append(temp.val)
                if temp.left:
                    array.append(temp.left)
                if temp.right:
                    array.append(temp.right)
            if number % 2 == 1:
                res.append(cur)
            else:
                res.append(cur[::-1])
            number += 1
        return res
