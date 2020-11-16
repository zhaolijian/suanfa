# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 思路就是对于每个节点，都把左右节点交换
# class Solution:
#     # 返回镜像树的根节点
#     def Mirror(self, root):
#         if root is None:
#             return None
#         temp = root.left
#         root.left = root.right
#         root.right = temp
#         self.Mirror(root.left)
#         self.Mirror(root.right)
#         return root


class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if not root:
            return None
        head = root
        temp = head.left
        head.left = self.Mirror(root.right)
        head.right = self.Mirror(root.left)
        return head


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(8)
    root.left = TreeNode(6)
    root.right = TreeNode(10)
    cur1 = root.left
    cur2 = root.right
    cur1.left = TreeNode(5)
    cur1.right = TreeNode(7)
    cur2.left = TreeNode(9)
    cur2.right = TreeNode(11)
    r = s.Mirror(root)
    print(r.val)

