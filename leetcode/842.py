# 给定一个数字字符串 S，比如 S = "123456579"，我们可以将它分成斐波那契式的序列 [123, 456, 579]。
# 形式上，斐波那契式序列是一个非负整数列表 F，且满足：
# 0 <= F[i] <= 2^31 - 1，（也就是说，每个整数都符合 32 位有符号整数类型）；
# F.length >= 3；
# 对于所有的0 <= i < F.length - 2，都有 F[i] + F[i+1] = F[i+2] 成立。
# 另外，请注意，将字符串拆分成小块时，每个块的数字一定不要以零开头，除非这个块是数字 0 本身。
# 返回从 S 拆分出来的任意一组斐波那契式的序列块，如果不能拆分则返回 []。


class Solution:
    def splitIntoFibonacci(self, S: str):
        def dfs(cur, already):
            nonlocal res
            if cur == length:
                if len(already) >= 3:
                    res = already
                    return
                else:
                    return
            for i in range(cur, length):
                if S[cur] == '0' and i > cur:
                    continue
                if int(S[cur: i + 1]) > 2 ** 31 - 1:
                    return
                if len(already) < 2:
                    dfs(i + 1, already + [int(S[cur: i + 1])])
                else:
                    if int(S[cur: i + 1]) == already[-1] + already[-2]:
                        dfs(i + 1, already + [int(S[cur: i + 1])])

        length = len(S)
        res = []
        dfs(0, [])
        return res



if __name__ == '__main__':
    s = Solution()
    S = "123456579"
    print(s.splitIntoFibonacci(S))