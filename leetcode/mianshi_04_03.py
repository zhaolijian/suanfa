# 给定一棵二叉树，设计一个算法，创建含有某一深度上所有节点的链表（比如，若一棵树的深度为 D，则会创建出 D 个链表）。返回一个包含所有深度的链表的数组。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def listOfDepth(self, tree: TreeNode):
        if not tree:
            return [[]]
        array = [tree]
        res = [ListNode(tree.val)]
        temp = []
        while array:
            cur = array.pop(0)
            if cur.left:
                temp.append(cur.left)
            if cur.right:
                temp.append(cur.right)
            if not array:
                if temp:
                    root = ListNode(temp[0].val)
                    cur = root
                    for i in range(1, len(temp)):
                        cur.next = ListNode(temp[i].val)
                        cur = cur.next
                    res.append(root)
                array = temp
                temp = []
        return res


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    cur = root
    cur.left = TreeNode(2)
    cur.right = TreeNode(3)
    l = cur.left
    l.left = TreeNode(4)
    l.right = TreeNode(5)
    r = cur.right
    r.right = TreeNode(7)
    ll = l.left
    ll.left = TreeNode(8)
    print(s.listOfDepth(root))