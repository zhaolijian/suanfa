# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 递归
# class Solution:
#     # 返回从尾部到头部的列表值序列，例如[1,2,3]
#     def printListFromTailToHead(self, listNode):
#         if listNode is None:
#             return []
#         else:
#             return self.printListFromTailToHead(listNode.next) + [listNode.val]

# 栈
# class Solution:
#     # 返回从尾部到头部的列表值序列，例如[1,2,3]
#     def printListFromTailToHead(self, listNode):
#         if listNode is None:
#             return []
#         else:
#             stack = []
#             res = []
#             while listNode is not None:
#                 stack.append(listNode.val)
#                 listNode = listNode.next
#             while len(stack) > 0:
#                 res.append(stack.pop())
#             return res


# 数组反转
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        if listNode is None:
            return []
        else:
            res = []
            while listNode:
                res.append(listNode.val)
                listNode = listNode.next
            i, j = 0, len(res) - 1
            while i < j:
                res[i], res[j] = res[j], res[i]
                i += 1
                j -= 1
            return res


if __name__ == '__main__':
    s = Solution()
    l = list(map(int, input().strip().split()))
    listNode = ListNode(l[0])
    cur = listNode
    for i in range(1, len(l)):
        cur.next = ListNode(l[i])
        cur = cur.next
    cur.next = None
    print(s.printListFromTailToHead(listNode))
