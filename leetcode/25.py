# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
# k 是一个正整数，它的值小于或等于链表的长度。
# 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 方法1 栈,不过并不满足常数额外空间（k值小于等于链表长度）
# class Solution:
#     def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
#         dummy = ListNode(0)
#         # 上一次迭代的最后一个节点
#         p = dummy
#         while True:
#             count = k
#             stack = []
#             # 下一次迭代的起始节点
#             tmp = head
#             while count and tmp:
#                 stack.append(tmp)
#                 tmp = tmp.next
#                 count -= 1
#             # 说明剩下的节点不够k个
#             if count:
#                 p.next = head
#                 break
#             while stack:
#                 p.next = stack.pop()
#                 p = p.next
#             p.next = tmp
#             head = tmp
#         return dummy.next


# 方法2 尾插法
# class Solution:
#     def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
#         dummy = ListNode(0)
#         dummy.next = head
#         pre, tail = dummy, dummy
#         while True:
#             count = k
#             while count and tail:
#                 count -= 1
#                 tail = tail.next
#             if not tail: break
#             head = pre.next
#             while pre.next != tail:
#                 cur = pre.next # 获取下一个元素
#                 # pre与cur.next连接起来,此时cur(孤单)掉了出来
#                 pre.next = cur.next
#                 cur.next = tail.next # 和剩余的链表连接起来
#                 tail.next = cur #插在tail后面
#             # 改变 pre tail 的值
#             pre = head
#             tail = head
#         return dummy.next


# 方法3 递归
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        cur = head
        count = 0
        while cur and count != k:
            cur = cur.next
            count += 1
        if count == k:
            cur = self.reverseKGroup(cur, k)
            while count:
                tmp = head.next
                head.next = cur
                cur = head
                head = tmp
                count -= 1
            head = cur
        return head