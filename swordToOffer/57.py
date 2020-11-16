class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def GetNext(self, pNode):
        if not pNode:
            return None
        # 如果该节点有右子树，则找到右子树的最左边节点
        if pNode.right:
            temp = pNode.right
            while temp.left:
                temp = temp.left
            return temp
        # 如果该节点没有右子树，若找到第一个子树在高阶父节点左侧
        else:
            while pNode.next:
                parent = pNode.next
                if parent.left == pNode:
                    return parent
                pNode = parent
            return None
