# 存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除所有重复的元素，使每个元素 只出现一次 。
# 返回同样按升序排列的结果链表。
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 方法1
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        # cur每次迭代都是一个新节点
        while cur:
            temp = cur
            while temp.next and temp.next.val == temp.val:
                temp = temp.next
            cur.next = temp.next
            cur = cur.next
        return head


# 方法2 使用set
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        s = set()
        dummy = ListNode(0)
        dummy.next = head
        pre, cur = dummy, head
        while cur:
            if cur.val in s:
                pre.next = cur.next
                cur = cur.next
            else:
                s.add(cur.val)
                pre = pre.next
                cur = cur.next
        return dummy.next