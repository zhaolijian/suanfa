class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        length = len(arr)
        if k > length:
            return 0
        else:
            start = sum(arr[:k])
            number = k * threshold
            res = 1 if start >= number else 0
            for i in range(k, length):
                start = start - arr[i - k] + arr[i]
                if start >= number:
                    res += 1
            return res