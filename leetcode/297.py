class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 方法1 层序遍历
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = ""
        if not root:
            return ""
        elif not root.left and not root.right:
            return str(root.val)
        else:
            queue = [root]
            while queue:
                temp = queue.pop(0)
                if temp:
                    res += (str(temp.val) + ",")
                    queue.append(temp.left)
                    queue.append(temp.right)
                else:
                    res += ("None,")
            res = res[:-1]
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None
        else:
            array = data.split(",")
            root = TreeNode(array.pop(0))
            length = len(array)
            init = [root]
            while length > 0:
                cur = init.pop(0)
                if length > 0:
                    if array[0] == 'None':
                        cur.left = None
                    else:
                        cur.left = TreeNode(array[0])
                        init.append(cur.left)
                    array.pop(0)
                    length -= 1
                if length > 0:
                    if array[0] == 'None':
                        cur.right = None
                    else:
                        cur.right = TreeNode(array[0])
                        init.append(cur.right)
                    array.pop(0)
                    length -= 1
            return root


# 方法2 先序遍历
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def dfs(root, string):
            if not root:
                return string + "None,"
            else:
                string += (str(root.val) + ",")
                string = dfs(root.left, string)
                string = dfs(root.right, string)
            return string

        return dfs(root, "")

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def func(array):
            temp = array.pop(0)
            if temp == 'None':
                return None
            root = TreeNode(temp)
            root.left = func(array)
            root.right = func(array)
            return root

        array = data.split(",")
        return func(array)



if __name__ == '__main__':
    s = Codec()
    root = TreeNode(1)
    cur = root
    cur.left = TreeNode(2)
    cur.right = TreeNode(3)
    cur = cur.right
    cur.left = TreeNode(4)
    cur.right = TreeNode(5)
    result = s.serialize(root)
    print(result)
    print(s.deserialize(result))