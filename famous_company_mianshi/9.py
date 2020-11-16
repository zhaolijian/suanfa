# 输入两个链表，找出它们的第一个公共结点。
# （注意因为传入数据是链表，所以错误测试数据的提示是用其他方式显示的，保证传入数据是正确的）
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        cur_1, cur_2 = pHead1, pHead2
        while cur_1 != cur_2:
            cur_1 = cur_1.next if cur_1 else pHead2
            cur_2 = cur_2.next if cur_2 else pHead1
        return cur_1