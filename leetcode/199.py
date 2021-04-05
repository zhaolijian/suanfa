# 二叉树的右视图
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 方法1 除了结果数组外只需要一个数组
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        array = [root]
        while array:
            length = len(array)
            for i in range(length):
                temp = array.pop(0)
                if temp.left:
                    array.append(temp.left)
                if temp.right:
                    array.append(temp.right)
                if i == length - 1:
                    res.append(temp.val)
        return res


# 方法2 除了结果数组外需要两个数组
class Solution:
    def rightSideView(self, root: TreeNode):
        if not root:
            return []
        res = []
        array = [root]
        while array:
            res.append(array[-1].val)
            temp = []
            for ele in array:
                if ele.left:
                    temp.append(ele.left)
                if ele.right:
                    temp.append(ele.right)
            array = temp
        return res


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    l = root.left
    r = root.right
    l.right = TreeNode(5)
    r.right = TreeNode(4)
    print(s.rightSideView(root))