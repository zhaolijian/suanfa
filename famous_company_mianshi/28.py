# 对于一个给定的链表，返回环的入口节点，如果没有环，返回null
class Solution:
    def detectCycle(self , head ):
        if not head or not head.next:
            return None
        slow, fast = head.next, head.next.next
        while slow != fast:
            if fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            else:
                break
        if not fast or not fast.next:
            return None
        new_head = head
        while new_head != slow:
            new_head = new_head.next
            slow = slow.next
        return new_head