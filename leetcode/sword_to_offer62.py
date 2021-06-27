# 0,1,···,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字（删除后从下一个数字开始计数）。求出这个圆圈里剩下的最后一个数字。
# 例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。


# 约瑟夫环
# 方法1 推导公式
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        ans = 0
        for i in range(2, n + 1):
            ans = (ans + m) % i
        return ans


# 方法2 模拟约瑟夫环
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        array = [i for i in range(n)]
        index = 0
        while n > 1:
            index = (index + m - 1) % n
            array.pop(index)
            n -= 1
        return array[0]