# 合并 k 个已排序的链表并将其作为一个已排序的链表返回。分析并描述其复杂度。
# 复杂度为nlogn，n为所有链表中元素的总和
# 可以设置k个指针，遍历，复杂度为nlogk(还没有写，一会补充)
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


import heapq
class Solution:
    def mergeKLists(self , lists):
        if not lists:
            return None
        dummy = ListNode(0)
        cur = dummy
        l = []
        for list in lists:
            while list:
                heapq.heappush(l, list.val)
                list = list.next
        while l:
            val = heapq.heappop(l)
            cur.next = ListNode(val)
            cur = cur.next
        return dummy.next