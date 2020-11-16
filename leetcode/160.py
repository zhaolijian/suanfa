class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 方法1 栈
# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#         if not headA or not headB:
#             return None
#         s1, s2 = [], []
#         res = None
#         while headA:
#             s1.append(headA)
#             headA = headA.next
#         while headB:
#             s2.append(headB)
#             headB = headB.next
#         while s1 and s2:
#             temp = s1.pop()
#             if temp == s2.pop():
#                 res = temp
#             else:
#                 return res
#         return res


# 方法2 哈希表
# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#         if not headA or not headB:
#             return None
#         temp = set()
#         while headA:
#             temp.add(headA)
#             headA = headA.next
#         while headB:
#             if headB in temp:
#                 return headB
#             headB = headB.next
#         return None


# 方法3： a + all + b = b + all + a
# a 为链表A中不公共部分，all为公共部分，b为链表B中不公共部分

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        n_a, n_b = 0, 0
        cur_a, cur_b = headA, headB
        while n_a < 2 and n_b < 2:
            if cur_a == cur_b:
                return cur_a
            if cur_a is None:
                cur_a = headB
                n_a += 1
            elif cur_b is None:
                cur_b = headA
                n_b += 1
            else:
                cur_a = cur_a.next
                cur_b = cur_b.next
        return None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        na, nb = headA, headB
        while na != nb:
            na = na.next if na else headB
            nb = nb.next if nb else headA
        return na

# 思路同上，另一种比较复杂的写法
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        n_a, n_b = 0, 0
        cur_a, cur_b = headA, headB
        while n_a < 2 and n_b < 2:
            if cur_a == cur_b:
                return cur_a
            if cur_a is None:
                cur_a = headB
                n_a += 1
            elif cur_b is None:
                cur_b = headA
                n_b += 1
            else:
                cur_a = cur_a.next
                cur_b = cur_b.next
        return None


if __name__ == '__main__':
    s = Solution()
    head1 = ListNode(4)
    cur1 = head1
    cur1.next = ListNode(1)
    cur1 = cur1.next
    cur1.next = ListNode(8)
    cur1 = cur1.next
    cur1.next = ListNode(4)
    cur1 = cur1.next
    cur1.next = ListNode(5)

    head2 = ListNode(5)
    cur2 = head2
    cur2.next = ListNode(0)
    cur2 = cur2.next
    cur2.next = ListNode(1)
    cur2 = cur2.next
    cur2.next = ListNode(8)
    cur2 = cur2.next
    cur2.next = ListNode(4)
    cur2 = cur2.next
    cur2.next = ListNode(5)

    print(s.getIntersectionNode(head1, head2))