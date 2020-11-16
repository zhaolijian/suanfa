# 给定一个n，求[1,n]这n个数字的排列组合有多少个。条件：相邻的两个数字差的绝对值不能等于1
# 思路：简单的回溯算法，注意保存上一次访问的位置用于判定绝对值
class Solution:
    def func(self, n):
        def function(array, rest):
            if len(array) == n:
                res.append(array)
            else:
                for i in range(len(rest)):
                    if not array:
                        function([rest[i]], rest[:i] + rest[i + 1:])
                    elif abs(rest[i] - array[-1]) != 1:
                        function(array + [rest[i]], rest[:i] + rest[i + 1:])

        res = []
        init = [i for i in range(1, n + 1)]
        function([], init)
        return res


if __name__ == '__main__':
    s = Solution()
    n = int(input())
    print(s.func(n))




