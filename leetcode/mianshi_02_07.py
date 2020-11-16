# 链表相交
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 方法1 栈
# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#         stack1, stack2 = [], []
#         res = None
#         while headA:
#             stack1.append(headA)
#             headA = headA.next
#         while headB:
#             stack2.append(headB)
#             headB = headB.next
#         while stack1 and stack2:
#             temp = stack1.pop()
#             if temp == stack2.pop():
#                 res = temp
#             else:
#                 break
#         return res

# 方法2 双指针
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        temp1, temp2 = headA, headB
        # temp1: headA+None+headB
        # temp2: headB+None+headA
        while temp1 != temp2:
            temp1 = temp1.next if temp1 else headB
            temp2 = temp2.next if temp2 else headA
        return temp1


if __name__ == '__main__':
    s = Solution()
    headA = ListNode(4)
    curA = headA
    array1 = [1, 8, 4, 5]
    for ele in array1:
        curA.next = ListNode(ele)
        curA = curA.next
    headB = ListNode(5)
    curB = headB
    array2 = [0, 1, 8, 4, 5]
    for ele in array2:
        curB.next = ListNode(ele)
        curB = curB.next
    print(s.getIntersectionNode(headA, headB))
