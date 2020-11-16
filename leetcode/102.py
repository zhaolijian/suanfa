# 给你一个二叉树，请你返回其按层序遍历得到的节点值。（即逐层地，从左到右访问所有节点）。
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# 方法1 层次遍历，使用单数组
class Solution:
    def levelOrder(self, root: TreeNode):
        if not root:
            return []
        res = []
        array = [root]
        while array:
            length = len(array)
            cur = []
            for i in range(length):
                temp = array.pop(0)
                if temp.left:
                    array.append(temp.left)
                if temp.right:
                    array.append(temp.right)
                cur.append(temp.val)
            res.append(cur)
        return res


# 方法2，层次遍历，使用双数组：一个表示上一次层次遍历的数组，一个表示下一层层次遍历的数组
class Solution:
    def levelOrder(self, root: TreeNode):
        if not root:
            return []
        array = [root]
        res = []
        while array:
            next_array = []
            val_array = []
            for i in range(len(array)):
                val_array.append(array[i].val)
            res.append(val_array)
            while array:
                temp = array.pop(0)
                if temp.left:
                    next_array.append(temp.left)
                if temp.right:
                    next_array.append(temp.right)
            array = next_array
        return res


# 方法3，使用number值表示当前层节点数，使用next_number表示下一层节点数，代替双数组使用
class Solution:
    def levelOrder(self, root: TreeNode):
        if not root:
            return []
        array = [root]
        number = 1
        next_number = 0
        res = []
        cur_array = []
        while array:
            temp = array.pop(0)
            cur_array.append(temp.val)
            number -= 1
            if temp.left:
                array.append(temp.left)
                next_number += 1
            if temp.right:
                array.append(temp.right)
                next_number += 1
            if number == 0:
                number = next_number
                next_number = 0
                res.append(cur_array)
                cur_array = []
        return res


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(3)
    cur = root
    cur.left = TreeNode(9)
    cur.right = TreeNode(20)
    r = cur.right
    r.left = TreeNode(15)
    r.right = TreeNode(7)
    print(s.levelOrder(root))