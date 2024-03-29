# 输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
# B是A的子结构， 即 A中有出现和B相同的结构和节点值。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 递归
class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def find(root1, root2):
            if not root2:
                return True
            elif not root1 or root1.val != root2.val:
                return False
            else:
                return find(root1.left, root2.left) and find(root1.right, root2.right)

        if not A or not B:
            return False
        if A.val == B.val and find(A, B):
            return True
        return self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)


# 层次遍历
class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def find(root1, root2):
            if not root2:
                return True
            elif not root1 or root1.val != root2.val:
                return False
            else:
                return find(root1.left, root2.left) and find(root1.right, root2.right)

        if not A or not B:
            return False
        array = [A]
        while array:
            temp = array.pop(0)
            if temp.left:
                array.append(temp.left)
            if temp.right:
                array.append(temp.right)
            if temp.val == B.val and find(temp, B):
                return True
        return False