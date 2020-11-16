# 填充每个节点的下一个右侧节点指针
# 给定一个完美二叉树，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


# 方法1 使用数组存储每一层节点
# 时间复杂度O(N),空间复杂度O(N)
# 如果要是不完美二叉树也可以用
class Solution:
    def connect(self, root):
        if not root:
            return root
        array = [root]
        while array:
            length = len(array)
            for i in range(length):
                temp = array.pop(0)
                if i < length - 1:
                    temp.next = array[0]
                if temp.left:
                    array.append(temp.left)
                if temp.right:
                    array.append(temp.right)
        return root


# 方法2 借助next实现
# 间复杂度O(N),空间复杂度O(1）
# 如果要是不完美二叉树，则不能用了，因为leftmost.left可能为None
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        leftmost = root
        while leftmost.left:
            temp = leftmost
            while temp:
                temp.left.next = temp.right
                if temp.next:
                    temp.right.next = temp.next.left
                temp = temp.next
            leftmost = leftmost.left
        return root