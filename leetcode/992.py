# 给定一个正整数数组 A，如果 A 的某个子数组中不同整数的个数恰好为 K，则称 A 的这个连续、不一定独立的子数组为好子数组。
# （例如，[1,2,3,1,2] 中有 3 个不同的整数：1，2，以及 3。）
# 返回 A 中好子数组的数目。
from collections import defaultdict
class Solution:
    def subarraysWithKDistinct(self, A, K: int) -> int:
        # 最多有number个不同整数
        def atMost(number):
            d = defaultdict(int)
            res, left = 0, 0
            for right, ele in enumerate(A):
                d[ele] += 1
                while len(d) > number:
                    d[A[left]] -= 1
                    if d[A[left]] == 0:
                        d.pop(A[left])
                    left += 1
                res += right - left + 1
            return res

        # 最多为K个不同整数-最多为K-1个不同整数,则结果为恰好有K个不同整数
        return atMost(K) - atMost(K - 1)


# 两层for循环的方法会超时
class Solution:
    def subarraysWithKDistinct(self, A, K: int) -> int:
        res = 0
        length = len(A)
        for j in range(length):
            set_array = set()
            for i in range(j, length):
                set_array.add(A[i])
                if len(set_array) == K:
                    res += 1
                elif len(set_array) > K:
                    break
        return res


if __name__ == '__main__':
    s = Solution()
    A = [1,2,1,2,3]
    K = 2
    print(s.subarraysWithKDistinct(A, K))