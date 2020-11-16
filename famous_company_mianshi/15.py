# 给定一个二叉树，返回该二叉树的之字形层序遍历，（第一层从左向右，下一层从右向左，一直这样交替）
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque
class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        res = []
        array = deque([root])
        # 奇偶数行
        flag = 1
        while array:
            cur = []
            for i in range(len(array)):
                temp = array.popleft()
                if temp.left:
                    array.append(temp.left)
                if temp.right:
                    array.append(temp.right)
                cur.append(temp.val)
            if flag:
                res.append(cur)
            else:
                res.append(cur[::-1])
            if flag:
                flag = 0
            elif not flag:
                flag = 1
        return res


if __name__ == '__main__':
    s = Solution()
    # {3, 9, 20,  # ,#,15,7},
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    r = root.right
    r.left = TreeNode(15)
    r.right = TreeNode(7)
    print(s.zigzagLevelOrder(root))