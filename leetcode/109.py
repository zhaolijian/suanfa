class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 方法1
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def getLength(head: ListNode) -> int:
            ret = 0
            while head:
                ret += 1
                head = head.next
            return ret

        def buildTree(left: int, right: int) -> TreeNode:
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode()
            root.left = buildTree(left, mid - 1)
            nonlocal head
            root.val = head.val
            head = head.next
            root.right = buildTree(mid + 1, right)
            return root

        length = getLength(head)
        return buildTree(0, length - 1)


# 方法2
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def getMiddle(left, right):
            l, r = left, left
            while r != right and r.next != right:
                l = l.next
                r = r.next.next
            return l

        def buildTree(left, right):
            if left == right:
                return None
            mid = getMiddle(left, right)
            root = TreeNode(mid.val)
            root.left = buildTree(left, mid)
            root.right = buildTree(mid.next, right)
            return root

        return buildTree(head, None)


if __name__ == '__main__':
    s = Solution()
    tail = ListNode(9, None)
    second = ListNode(5, tail)
    t = ListNode(0, second)
    f = ListNode(-3, t)
    head = ListNode(-10, f)
    print(s.sortedListToBST(head))
