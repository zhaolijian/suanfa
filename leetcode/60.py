# 给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。
#
# 按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
#
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# 给定 n 和 k，返回第 k 个排列。


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = []
        def dfs(number, s):
            if number == n:
                res.append(s)
                return
            else:
                for i in range(1, n + 1):
                    if i not in set_array:
                        set_array.add(i)
                        dfs(number + 1, s + str(i))
                        set_array.remove(i)

        set_array = set()
        dfs(0, '')
        return res[k - 1]


if __name__ == '__main__':
    s = Solution()
    n, k = 9, 135401
    print(s.getPermutation(n, k))