class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        res, mx = 0, A[0]
        for i in range(1, len(A)):
            res = max(res, mx + A[i] - i)
            mx = max(mx, A[i] + i)
        return res