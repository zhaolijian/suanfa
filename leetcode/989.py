# 对于非负整数 X 而言，X 的数组形式是每位数字按从左到右的顺序形成的数组。例如，如果 X = 1231，那么其数组形式为 [1,2,3,1]。
# 给定非负整数 X 的数组形式 A，返回整数 X+K 的数组形式。


# 方法1
class Solution:
    def addToArrayForm(self, A, K: int):
        length = len(A)
        res = []
        for i in range(length - 1, -1, -1):
            val = A[i] + K % 10
            K //= 10
            if val >= 10:
                res.append(val - 10)
                K += 1
            else:
                res.append(val)
        while K:
            res.append(K % 10)
            K //= 10
        return res[::-1]


# 方法2
class Solution:
    def addToArrayForm(self, A, K: int):
        A_val = 0
        for i in range(len(A)):
            A_val = 10 * A_val + A[i]
        result = str(A_val + K)
        res = []
        for i in range(len(result)):
            res.append(int(result[i]))
        return res
