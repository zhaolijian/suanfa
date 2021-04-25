class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


t = int(input())
for _ in range(t):
    l = list(map(int, input().split()))
    # 节点个数、位移位数
    n, k = l[0], l[1]
    res = []
    for i in range(1, n + 1):
        res.append(i)
    print(' '.join(map(str, res)))