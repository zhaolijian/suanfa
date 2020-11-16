import collections
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        res = 0
        pre_mod = 0  # 存储当前位置的上一个位置的前缀和的余数加上当前位置的值对K的余数
        presum_count = collections.defaultdict(int)
        presum_count[0] = 1
        for i in range(len(A)):
            pre_mod = (pre_mod + A[i]) % K
            res += presum_count[pre_mod]  # 如果能在dict中找到相同的pre_mod，说明当前节点前的某个位置的前缀和到当前位置的前缀和间存在若干个K
            presum_count[pre_mod] += 1
        return res


if __name__ == '__main__':
    s = Solution()
    A = [8,9,7,8,9]
    K = 8
    print(s.subarraysDivByK(A, K))