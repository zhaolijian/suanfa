class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        new_head, cur = None, head
        while cur:
            temp = cur.next
            cur.next = new_head
            new_head = cur
            cur = temp
        return new_head

# 方法1 迭代
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         if not head or not head.next:
#             return head
#         cur = head
#         next_node = head.next
#         cur.next = None
#         while next_node:
#             temp = next_node.next
#             next_node.next = cur
#             cur = next_node
#             next_node = temp
#         return cur


# 方法2 递归
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        res = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return res


# 方法3 递归
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def func(pre, head):
            if head is None:
                return pre
            temp = head.next
            head.next = pre
            return func(head, temp)
        return func(None, head)

if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    cur = head
    for i in range(2, 4):
        cur.next = ListNode(i)
        cur = cur.next
    print(s.reverseList(head))