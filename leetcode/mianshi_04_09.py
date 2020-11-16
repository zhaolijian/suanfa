# 从左向右遍历一个数组，通过不断将其中的元素插入树中可以逐步地生成一棵二叉搜索树。
# 给定一个由不同节点组成的二叉搜索树，输出所有可能生成此树的数组。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def BSTSequences(self, root: TreeNode) -> List[List[int]]:
        # 当前遍历节点,下次可以访问的节点队列,当前二叉搜索树数组
        def func(root, array, path):
            if root.left:
                array.append(root.left)
            if root.right:
                array.append(root.right)
            if not array:
                res.append(path)
                return
            for index, ele in enumerate(array):
                func(ele, array[:index] + array[index + 1:], path + [ele.val])

        if not root:
            return [[]]
        res= []
        func(root, [], [root.val])
        return res


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print(s.BSTSequences(root))