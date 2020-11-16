# Definition for singly-linked list.
# 回文链表，时间复杂度：O(n)， 空间复杂度O(1)
# 思路：遍历链表，获取链表长度，找到中间节点，使链表前半部分反转或者后半部分反转，然后判断部分是否相同
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def reverse(mid_node):
            last_head, cur = None, mid_node
            while cur:
                temp = cur.next
                cur.next = last_head
                last_head = cur
                cur = temp
            return last_head

        if not head or not head.next:
            return True
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        mid_length, half = length // 2, length // 2
        mid_node = head
        while mid_length > 0:
            mid_node = mid_node.next
            mid_length -= 1
        last_head = reverse(mid_node)
        while half > 0:
            if head.val != last_head.val:
                return False
            half -= 1
            head = head.next
            last_head = last_head.next
        return True