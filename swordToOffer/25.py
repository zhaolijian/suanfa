# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


# class Solution:
#     # 返回 RandomListNode
#     def Clone(self, pHead):
#         if not pHead:
#             return None
#         currentNode = pHead
#         # 复制每个节点，将新节点插入到原节点后面
#         while currentNode:
#             cloneNode = RandomListNode(currentNode.label)
#             nextNode = currentNode.next
#             currentNode.next = cloneNode
#             cloneNode.next = nextNode
#             currentNode = nextNode
#         currentNode = pHead
#         # 复制原节点的随机指针给新节点
#         while currentNode:
#             currentNode.next.random = None if not currentNode.random else currentNode.random.next
#             currentNode = currentNode.next.next
#         # 将链表拆分为原始链表和复制后的链表
#         currentNode = pHead
#         pCloneHead = pHead.next
#         while currentNode:
#             cloneNode = currentNode.next
#             currentNode.next = cloneNode.next
#             cloneNode.next = None if not cloneNode.next else cloneNode.next.next
#             currentNode = currentNode.next
#         return pCloneHead


# 最简单写法
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if not pHead:
            return None
        head = RandomListNode(pHead.label)
        head.random = pHead.random
        head.next = self.Clone(pHead.next)
        return head


# 不能通过的原因应该是该写法返回的是节点引用（题目中写了这样会返回空），返回为空
# class Solution:
#     # 返回 RandomListNode
#     def Clone(self, pHead):
#         if not pHead:
#             return None
#         head = RandomListNode(pHead.label)
#         cur = head
#         while pHead:
#             cur.next = pHead.next
#             cur.random = pHead.random
#             cur = cur.next
#             pHead = pHead.next
#         return head


if __name__ == '__main__':
    pHead = RandomListNode(1)
    pHead.next = RandomListNode(2)
    pHead.random = RandomListNode(3)
    two = pHead.next
    two.next = RandomListNode(3)
    two.random = RandomListNode(5)
    three = two.next
    three.next = RandomListNode(4)
    three.random = None
    fourth = three.next
    fourth.next = RandomListNode(5)
    fourth.random = RandomListNode(2)
    five = fourth.next
    five.next = None
    five.random = None
    s = Solution()
    # print(s.Clone(pHead))
    result = s.Clone(pHead)
    while result:
        print(result.label)
        print(result.next)
        print(result.random)
        print()
        result = result.next
