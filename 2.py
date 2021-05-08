class TreeNode:
    def __init__(self, left=None, right=None, val=0):
        self.left = left
        self.right = right
        self.val = val

array = [3,9,20,None,None,15,7]

def buildTree(array):
    def func(node_list, array):
        if not array:
            return
        i = 0
        length = len(array)
        res = []
        for node in node_list:
            if node is not None:
                if i < length:
                    node.left = TreeNode(array[i]) if array[i] is not None else None
                    res.append(node.left)
                    i += 1
                if i < length:
                    node.right = TreeNode(array[i]) if array[i] is not None else None
                    res.append(node.right)
                    i += 1
            else:
                res.append(None)
                res.append(None)
        func(res, array[i:])

    if not array:
        return None
    root = TreeNode(val=array[0])
    func([root], array[1:])
    return root

root = buildTree(array)
print(root)
