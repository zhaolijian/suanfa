# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 该方法的思想是对于每一个节点，从上往下探索，看看是否有满足条件的路径
# class Solution:
#     def __init__(self):
#         self.res = 0
#     def pathSum(self, root: TreeNode, sum: int) -> int:
#         def func(root, sum):
#             if not root:
#                 return 0
#             else:
#                 if root.val == sum:
#                     self.res += 1
#                 func(root.left, sum - root.val)
#                 func(root.right, sum - root.val)
#         if not root:
#             return 0
#         # 分为三部分：root为路径中的一个节点、路径在root左侧、路径在root右侧
#         func(root, sum)
#         self.pathSum(root.left, sum)
#         self.pathSum(root.right, sum)
#         return self.res

# 下面两种思想相同的方法，是从下往上探索，遍历到的节点肯定是路径中的节点，比起上面不一定的方式，该方法更快
# class Solution:
#     def pathSum(self, root: TreeNode, sum: int) -> int:
#         array = [0] * 1000
#         # 根节点、和、数组、当前节点索引值(也可以说是所在层数)
#         return self.func(root, sum, array, 0)
#
#     def func(self, root, sum, array, cur):
#         if not root:
#             return 0
#         else:
#             array[cur] = root.val
#             temp = 0
#             sum_number = 0
#             for i in range(cur, -1, -1):
#                 sum_number += array[i]
#                 if sum_number == sum:
#                     temp += 1
#             return temp + self.func(root.left, sum, array, cur + 1) + self.func(root.right, sum, array, cur + 1)


# 这一种方法是上一种方法的改进，不再初始化array = [0] * 1000，节省空间
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        # 根节点、和、数组、当前节点索引值(也可以说是所在层数)
        return self.func(root, sum, [], 0)

    def func(self, root, sum, array, cur):
        if not root:
            return 0
        else:
            array.append(root.val)
            temp = 0
            sum_number = 0
            for i in range(cur, -1, -1):
                sum_number += array[i]
                if sum_number == sum:
                    temp += 1
            val1 = self.func(root.left, sum, array, cur + 1)
            if root.left:
                array.pop()
            val2 = self.func(root.right, sum, array, cur + 1)
            if root.right:
                array.pop()
            return temp + val1 + val2



if __name__ == '__main__':
    # [5,4,8,11,null,13,4,7,2,null,null,5,1]
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    l = root.left
    r = root.right
    l.left = TreeNode(11)
    ll = l.left
    lr = l.right
    ll.left = TreeNode(7)
    ll.right = TreeNode(2)
    r.left = TreeNode(13)
    r.right = TreeNode(4)
    rr = r.right
    rr.left = TreeNode(5)
    rr.right = TreeNode(1)
    s = Solution()
    sum = 22
    print(s.pathSum(root, sum))