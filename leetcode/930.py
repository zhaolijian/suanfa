# 在由若干 0 和 1  组成的数组 A 中，有多少个和为 S 的非空子数组。

from collections import Counter
class Solution(object):
    def numSubarraysWithSum(self, A, S):
        P = [0]
        for x in A:
            P.append(P[-1] + x)
        count = Counter()

        ans = 0
        for x in P:
            ans += count[x]
            count[x + S] += 1

        return ans


if __name__ == '__main__':
    s = Solution()
    A = [1,0,1,0,1]
    S = 2
    print(s.numSubarraysWithSum(A, S))