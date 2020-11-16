# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 广度优先遍历
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        if not pRoot:
            return []
        temp = [pRoot]
        res = []
        # 每一层的节点数
        number = 1
        while temp:
            cur = []
            # 下一层节点数
            next_number = 0
            while number > 0:
                cur.append(temp[0].val)
                number -= 1
                if temp[0].left:
                    temp.append(temp[0].left)
                    next_number += 1
                if temp[0].right:
                    temp.append(temp[0].right)
                    next_number += 1
                temp.pop(0)
            res.append(cur)
            number = next_number
        return res


if __name__ == '__main__':
    s = Solution()
    pRoot = TreeNode(8)
    pRoot.left = TreeNode(6)
    pRoot.right = TreeNode(10)
    l = pRoot.left
    r = pRoot.right
    l.left = TreeNode(5)
    l.right = TreeNode(7)
    r.left = TreeNode(9)
    r.right = TreeNode(11)
    print(s.Print(pRoot))