# 令m和n分别表示num1和num2的长度，并且它们均不为 0，则num1和num2的乘积的长度为 m+n-1 或 m+nm+n。
# 简单证明如下：如果num1和num2都取最小值，则num1=10^(m-1),num2=10^(n-1),乘积为10^(m+n-2),长度为 m+n-1
# 如果num1和num2都取最大值，则num1=10^m-1,num2=10^n-1,乘积为10^(m+n)-10^m-10^n+1,介于10^(m+n-1)和10^(m+n)之间，
# 长度为m+n.因此创建长度为m+n的数组
# 位置为i和位置为j的乘积所在位置为i+j+1,如果值大于等于10，则进位到i+j位置。如果最高位为0则舍弃。


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        len1, len2 = len(num1), len(num2)
        res = [0] * (len1 + len2)
        for i in range(len1 - 1, -1, -1):
            val1 = int(num1[i])
            for j in range(len2 - 1, -1, -1):
                val2 = int(num2[j])
                res[i + j + 1] += val1 * val2
        for k in range(len1 + len2 - 1, 0, -1):
            res[k - 1] += res[k] // 10
            res[k] %= 10
        if res[0] == 0:
            return ''.join(str(number) for number in res[1:])
        else:
            return ''.join(str(number) for number in res)


if __name__ == '__main__':
    s = Solution()
    num1, num2 = '123', '456'
    print(s.multiply(num1, num2))