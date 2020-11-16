# -*- coding:utf-8 -*-
# 借助一个辅助栈，将入栈序列中的元素先放入辅助栈中，
# 然后比较辅助栈的栈顶元素和弹出序列的第一个元素，如果一样则删除，
# 直到辅助栈的栈顶元素和弹出序列的第一个元素不同，这时候再将入栈序列中的元素放入辅助栈中。。。
# 最后如果辅助栈为空，则True,否则False


class Solution:
    def IsPopOrder(self, pushV, popV):
        # 辅助栈
        stack = []
        for i in range(len(pushV)):
            stack.append(pushV[i])
            while stack and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
        return False if stack else True
