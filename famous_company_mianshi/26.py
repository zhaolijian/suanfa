# 实现一个特殊功能的栈，在实现栈的基本功能的基础上，再实现返回栈中最小元素的操作。
class Solution:
    def getMinStack(self , op ):
        # write code here
        # 当前位置最小元素集合
        min_val = []
        stack = []
        res = []
        for i in range(len(op)):
            if op[i][0] == 1:
                stack.append(op[i][1])
                if not min_val or min_val[-1] > op[i][1]:
                    min_val.append(op[i][1])
                else:
                    min_val.append(min_val[-1])
            elif op[i][0] == 2:
                stack.pop()
                min_val.pop()
            elif op[i][0] == 3:
                res.append(min_val[-1])
        return res


if __name__ == '__main__':
    s = Solution()
    op = [[1,3],[1,2],[1,1],[3],[2],[3]]
    print(s.getMinStack(op))