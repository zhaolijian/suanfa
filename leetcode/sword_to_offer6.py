# 输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack[::-1]