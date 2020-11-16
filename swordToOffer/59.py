class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 设置一个队列，奇数行从左往右取，放后面，偶数行从右往左取，放前面，并记录每一行的个数
    def Print(self, pRoot):
        if not pRoot:
            return []
        queue = [pRoot]
        res = []
        # 记录奇数行还是偶数行
        temp = 1
        # 记录该行元素的总数
        num = 1
        while queue:
            # 记录下每行的临时数量
            t_number = 0
            # 每一行的元素集合
            cur = []
            if temp % 2 == 1:
                while num > 0:
                    cur.append(queue[0].val)
                    if queue[0].left:
                        queue.append(queue[0].left)
                        t_number += 1
                    if queue[0].right:
                        queue.append(queue[0].right)
                        t_number += 1
                    queue.pop(0)
                    num -= 1
                num = t_number
                temp += 1
                t_number = 0
                res.append(cur)
                cur = []
                continue
            if temp % 2 == 0:
                while num > 0:
                    cur.append(queue[-1].val)
                    if queue[-1].right:
                        queue = [queue[-1].right] + queue
                        t_number += 1
                    if queue[-1].left:
                        queue = [queue[-1].left] + queue
                        t_number += 1
                    queue.pop(-1)
                    num -= 1
                num = t_number
                temp += 1
                t_number = 0
                res.append(cur)
                cur = []
                continue
        return res


if __name__ == '__main__':
    s = Solution()
    pRoot = TreeNode(8)
    pRoot.left = TreeNode(6)
    pRoot.right = TreeNode(10)
    l = pRoot.left
    r = pRoot.right
    l.left = TreeNode(5)
    l.right = TreeNode(7)
    r.left = TreeNode(9)
    r.right = TreeNode(11)
    print(s.Print(pRoot))
