# -*- coding:utf-8 -*-


# 判断某数组是不是二叉搜索树后序遍历的结果
class Solution:
    # 二叉搜索树,左节点比根节点小,右节点比根节点大
    # 后序遍历: 左右中
    def VerifySquenceOfBST(self, sequence):
        if not sequence:
            return False
        if len(sequence) == 1:
            return True
        root = sequence[-1]
        # 右子树分界点
        r = -1
        for i in range(len(sequence)-1):
            if sequence[i] > root:
                r = i
                break
        # 判断右子树是否符合条件
        if r >= 0:
            for j in range(r, len(sequence)-1):
                if sequence[j] < root:
                    return False
        # 说明只有左子树或只有右子树
        if r <= 0:
            return self.VerifySquenceOfBST(sequence[:-1])
        else:
            return self.VerifySquenceOfBST(sequence[:r]) and self.VerifySquenceOfBST(sequence[r:])


if __name__ == '__main__':
    s = Solution()
    seq = [7,4,6,5]
    print(s.VerifySquenceOfBST(seq))
