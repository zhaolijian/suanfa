# 序列化二叉树的一种方法是使用前序遍历。当我们遇到一个非空节点时，我们可以记录下这个节点的值。如果它是一个空节点，我们可以使用一个标记值记录，例如 #。


# 栈
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stack = list()
        for i in preorder.split(','):
            stack.append(i)
            while len(stack) > 2 and stack[-1] == '#' and stack[-2] == '#' and stack[-3].isdigit():
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append('#')
        return True if stack == ['#'] else False