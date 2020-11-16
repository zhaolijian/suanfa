# 给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。
# 假定 BST 有如下定义：
# 结点左子树中所含结点的值小于等于当前结点的值
# 结点右子树中所含结点的值大于等于当前结点的值
# 左子树和右子树都是二叉搜索树

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        ans=[]
        most=0
        last=None
        cnt=0

        def inorder(node):
            if not node:
                return
            nonlocal ans,most,last,cnt
            if node.left:
                inorder(node.left)
            if node.val==last:
                cnt+=1
            else:
                cnt=1
            if cnt==most:
                ans.append(node.val)
            elif cnt>most:
                most=cnt
                ans=[node.val]
            last=node.val
            if node.right:
                inorder(node.right)

        inorder(root)
        return ans