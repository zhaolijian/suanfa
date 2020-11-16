class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        l1 = []
        l2 = []
        t1 = pHead1
        t2 = pHead2
        result = None
        while t1:
            l1.append(t1)
            t1 = t1.next
        while t2:
            l2.append(t2)
            t2 = t2.next
        while l1 and l2 and l1[-1].val == l2[-1].val:
            result = l2[-1]
            l1.remove(l1[-1])
            l2.remove(l2[-1])
        return result
