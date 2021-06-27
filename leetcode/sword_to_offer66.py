# 给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中 B[i] 的值是数组 A 中除了下标 i 以外的元素的积, 即 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。
# 不能使用除法。


# 方法1 从左往右和从右往左的两次遍历
class Solution:
    def constructArr(self, a):
        length = len(a)
        if length <= 1:
            return []
        l = [1] * length
        r = [1] * length
        # 从左往右的累乘
        for i in range(1, length):
            l[i] = l[i - 1] * a[i - 1]
        # 从右往左的累乘
        for i in range(length - 2, -1, -1):
            r[i] = r[i + 1] * a[i + 1]
        return [l[i] * r[i] for i in range(length)]


# 方法2 使用一次遍历和一个常量
class Solution:
    def constructArr(self, a):
        length = len(a)
        if length < 2:
            return []
        res = [1] * length
        for i in range(1, length):
            res[i] = res[i - 1] * a[i - 1]
        temp = 1
        for i in range(length - 2, -1, -1):
            temp *= a[i + 1]
            res[i] *= temp
        return res