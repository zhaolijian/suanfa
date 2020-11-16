# 给定一个二叉树，确定它是否是一个完全二叉树。
# 百度百科中对完全二叉树的定义如下：
# 若设二叉树的深度为 h，除第 h 层外，其它各层 (1～h-1) 的结点数都达到最大个数，第 h 层所有的结点都连续集中在最左边，这就是完全二叉树。
# （注：第 h 层可能包含 1~ 2h 个节点。）
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 方法1 借助左子节点值是当前节点值的两倍，右子节点值是当前节点值的两倍+1
class Solution(object):
    def isCompleteTree(self, root):
        nodes = [(root, 1)]
        i = 0
        while i < len(nodes):
            node, v = nodes[i]
            i += 1
            if node:
                nodes.append((node.left, 2*v))
                nodes.append((node.right, 2*v+1))

        return nodes[-1][1] == len(nodes)


# class Solution:
#     def isCompleteTree(self, root: TreeNode) -> bool:
#         if not root or (not root.left and not root.right):
#             return True
#         array = [root]
#         # 当前层是否满足2^(level-1)个节点
#         flag = True
#         while array:
#             length = len(array)
#             # 下一层是否满足紧挨条件
#             flg = True
#             for i in range(length):
#                 temp = array.pop(0)
#                 # 当前层不满足都是满的,则下一层不能有节点
#                 if not flag:
#                     if temp.left or temp.right:
#                         return False
#                 else:
#                     if temp.left:
#                         if not flg:
#                             return False
#                         array.append(temp.left)
#                     else:
#                         flg = False
#                         flag = False
#                     if temp.right:
#                         if not flg:
#                             return False
#                         array.append(temp.right)
#                     else:
#                         flg = False
#                         flag = False
#         return True


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.right = TreeNode(3)
    print(s.isCompleteTree(root))