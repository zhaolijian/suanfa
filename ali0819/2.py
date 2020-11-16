class Solution:
    def func(self, n, m, a, b, c):
        def dfs(i, j, index):
            nonlocal res
            if i > n and j > m:
                res = False
                return
            if i < n and b < m and a[i] != c[index] and b[j] != c[index]:
                res = False
                return
            elif i < n and j < m and a[i] == b[j]:
                dfs(i + 1, j, index + 1)
                dfs(i, j + 1, index + 1)
            elif i < n and a[i] == c[index]:
                dfs(i + 1, j, index + 1)
            elif j < m and b[j] == c[index]:
                dfs(i, j + 1, index + 1)

        i, j = 0, 0
        index = 0
        res = True
        dfs(i, j, index)
        return "possilbe" if res else "not possible"


if __name__ == '__main__':
    T = int(input())
    s = Solution()
    for _ in range(T):
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        c = list(map(int, input().split()))
        print(s.func(n, m, a, b, c))