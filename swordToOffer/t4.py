class Solution:
    # 矩阵、物品数、属性数
    def solu(self, array, n, k):
        res = 0
        if n <= 1:
            return 0
        for i in range(n):
            for j in range(i+1, n):
                temp = array[i][0] + array[j][0]
                for m in range(1, k):
                    if temp != array[i][m] + array[j][m]:
                        break
                if m == k - 1 and temp == array[i][m] + array[j][m]:
                    res += 1
        return res


if __name__ == '__main__':
    l = list(map(int, input().split()))
    n, k = l[0], l[1]
    array = []
    for i in range(n):
        temp = list(map(int, input().split()))
        array.append(temp)
    s = Solution()
    print(s.solu(array, n, k))

