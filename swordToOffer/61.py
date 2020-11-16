class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 先序遍历
class Solution:
    def __init__(self):
        self.flag = -1

    def Serialize(self, root):
        if not root:
            return "#!"
        return str(root.val) + '!' + self.Serialize(root.left) + self.Serialize(root.right)

    def Deserialize(self, s):
        self.flag += 1
        l = list(s.split("!"))
        res = None
        if l[self.flag] != '#':
            res = TreeNode(int(l[self.flag]))
            res.left = self.Deserialize(s)
            res.right = self.Deserialize(s)
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
    l = s.Serialize(pRoot)
    print(l)
    print(s.Deserialize(l))