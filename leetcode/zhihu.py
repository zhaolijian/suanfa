class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def func(self, root):
        if not root or (not root.left and not root.right):
            return root
        array = [root]
        cur_number = 1 # 当前层节点数
        left = root
        next_number = 0 # 下一层节点数
        while array:
            cur = array.pop(0)
            if cur.left:
                array.append(cur.left)
                next_number += 1
            if cur.right:
                array.append(cur.right)
                next_number += 1
            cur_number -= 1
            if cur != left:
                left.next = cur
                cur = left.next
            if cur_number == 0:
                cur.next = None
                if array:
                    left = array[0] # 更新下一层的最左侧节点
                cur_number = next_number
        return root


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    l = root.left
    r = root.right
    l.left = TreeNode(4)
    l.right = TreeNode(5)
    print(s.func(root))