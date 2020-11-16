class Solution:
    def func(self, n, m, array_a, array_b):
        return sorted(list(set(array_a + array_b)))


if __name__ == '__main__':
    l1 = list(map(int, input().split()))
    n, m = l1[0], l1[1]
    array_a = list(map(int, input().split()))
    array_b = list(map(int, input().split()))
    s = Solution()
    result = s.func(n, m, array_a, array_b)
    print(" ".join(map(str, result)))
