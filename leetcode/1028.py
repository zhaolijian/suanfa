# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        path, pos = list(), 0
        # 遍历字符串
        while pos < len(S):
            # 层级
            level = 0
            while S[pos] == '-':
                level += 1
                pos += 1
            value = 0
            # 获得节点值
            while pos < len(S) and S[pos].isdigit():
                value = value * 10 + (ord(S[pos]) - ord('0'))
                pos += 1
            node = TreeNode(value)
            #
            if level == len(path):
                if path:
                    path[-1].left = node
            else:
                path = path[:level]
                path[-1].right = node
            path.append(node)
        return path[0]


if __name__ == '__main__':
    s = Solution()
    ss = "1-2--3--4-5--6--7"
    print(s.recoverFromPreorder(ss))