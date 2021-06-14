# 给定 pushed 和 popped 两个序列，每个序列中的 值都不重复，只有当它们可能是在最初空栈上进行的推入 push 和弹出 pop 操作序列的结果时，返回 true；否则，返回 false 。


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        left = 0
        for ele in pushed:
            stack.append(ele)
            while stack and stack[-1] == popped[left]:
                stack.pop()
                left += 1
        return not stack