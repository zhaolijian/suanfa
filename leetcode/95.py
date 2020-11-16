# 给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 方法1 记忆化搜索，解释见方法2
class Solution:
    def generateTrees(self, n: int):
        def func(start, end):
            if (start, end) in memo:
                return memo[(start, end)]
            if start > end:
                return [None]
            res = []
            for i in range(start, end + 1):
                l = func(start, i - 1)
                r = func(i + 1, end)
                for left in l:
                    for right in r:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        res.append(root)
                memo[(start, end)] = res
            return res

        # 记忆化
        memo = {}
        return func(1, n) if n else []


# 方法2 无记忆化搜索
class Solution:
    def generateTrees(self, n: int):
        # 选好函数参数很重要：start、end
        def generateTrees(start, end):
            if start > end:
                return [None]

            allTrees = []
            for i in range(start, end + 1):  # 枚举可行根节点
                # 获得所有可行的左子树集合
                leftTrees = generateTrees(start, i - 1)
                # 获得所有可行的右子树集合
                rightTrees = generateTrees(i + 1, end)
                # 从左子树集合中选出一棵左子树，从右子树集合中选出一棵右子树，拼接到根节点上
                for l in leftTrees:
                    for r in rightTrees:
                        currTree = TreeNode(i)
                        currTree.left = l
                        currTree.right = r
                        allTrees.append(currTree)

            return allTrees

        return generateTrees(1, n) if n else []


if __name__ == '__main__':
    s = Solution()
    n = int(input())
    print(s.generateTrees(n))