# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

# 方法1
class Solution:
    def __init__(self):
        self.res = True

    def verifyPostorder(self, postorder) -> bool:
        def func(postorder):
            if not postorder:
                return
            root = postorder[-1]
            index = -1
            for i in range(len(postorder) - 1):
                if postorder[i] > root:
                    index = i
                    break
            if index == -1:
                func(postorder[:-1])
            else:
                for j in range(index + 1, len(postorder) - 1):
                    if postorder[j] < root:
                        self.res = False
                        return
                func(postorder[:index])
                func(postorder[index:-1])

        func(postorder)
        return self.res


# 方法2 思路与上面方法基本一样，但是简单很多
class Solution:
    def verifyPostorder(self, postorder: [int]) -> bool:
        def recur(i, j):
            if i >= j: return True
            p = i
            while postorder[p] < postorder[j]: p += 1
            m = p
            while postorder[p] > postorder[j]: p += 1
            return p == j and recur(i, m - 1) and recur(m, j - 1)

        return recur(0, len(postorder) - 1)


# 方法3 看不太懂
class Solution:
    def verifyPostorder(self, postorder: [int]) -> bool:
        stack, root = [], float("+inf")
        for i in range(len(postorder) - 1, -1, -1):
            if postorder[i] > root: return False
            while(stack and postorder[i] < stack[-1]):
                root = stack.pop()
            stack.append(postorder[i])
        return True


if __name__ == '__main__':
    s = Solution()
    postorder = [5, 2, -17, -11, 25, 76, 62, 98, 92, 61]
    print(s.verifyPostorder(postorder))