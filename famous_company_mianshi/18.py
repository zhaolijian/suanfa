# 从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
from collections import deque
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        if not pRoot:
            return []
        array = deque([pRoot])
        res = []
        while array:
            temp = []
            for i in range(len(array)):
                cur = array.popleft()
                temp.append(cur.val)
                if cur.left:
                    array.append(cur.left)
                if cur.right:
                    array.append(cur.right)
            res.append(temp)
        return res