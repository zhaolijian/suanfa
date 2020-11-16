class Solution:
    def func(self, arr, l, r):
        if r < l:
            return -1000000000
        ans = arr[l]
        for i in range(l + 1, r + 1):
            ans &= arr[i]
        return ans
    def closestToTarget(self, arr, target: int) -> int:
        arr = set(arr)
        arr = sorted(list(arr))
        res = float('inf')
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                res = min(res, abs(self.func(arr, i, j) - target))
        return res


if __name__ == '__main__':
    s = Solution()
    arr = [9,12,3,7,15]
    target = 5
    print(s.closestToTarget(arr, target))