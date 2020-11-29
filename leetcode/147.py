# 对链表进行插入排序
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 方法1
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        dummyHead = ListNode(0)
        dummyHead.next = head
        lastSorted = head
        curr = head.next

        while curr:
            if lastSorted.val <= curr.val:
                lastSorted = lastSorted.next
            else:
                prev = dummyHead
                while prev.next.val < curr.val:
                    prev = prev.next
                lastSorted.next = curr.next
                curr.next = prev.next
                prev.next = curr
            curr = lastSorted.next

        return dummyHead.next


# 方法2
# class Solution:
#     def insertionSortList(self, head: ListNode) -> ListNode:
#         dummy = ListNode(None)
#         cur = head
#         while cur:
#             temp = dummy.next
#             last = dummy
#             while temp and temp.val < cur.val:
#                 temp = temp.next
#                 last = last.next
#             if not temp:
#                 last.next = ListNode(cur.val)
#             else:
#                 insert = ListNode(cur.val)
#                 insert.next = temp
#                 last.next = insert
#             cur = cur.next
#         return dummy.next


if __name__ == '__main__':
    s = Solution()
    # head = ListNode(4)
    # head.next = ListNode(2)
    # cur = head.next
    # cur.next = ListNode(1)
    # cur = cur.next
    # cur.next = ListNode(3)
    head = ListNode(1)
    head.next = ListNode(1)
    print(s.insertionSortList(head))