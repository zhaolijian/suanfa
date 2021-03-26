# 存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除所有重复的元素，使每个元素 只出现一次 。
# 返回同样按升序排列的结果链表。
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
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