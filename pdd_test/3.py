class Solution:
    def solu(self, l):
        res = []
        for i in range(len(l)):
            res.append(self.Firi(l[i]))
        return res

    def Firi(self, l):
        one, two, n = l[0], l[1], l[2]
        if n == 0:
            return one
        elif n == 1:
            return two
        res = 0
        for i in range(2, n + 1):
            res = one + two
            one = two
            two = res
        if res % 3 == 0:
            return 'YES'
        else:
            return 'NO'


if __name__ == '__main__':
    n = int(input())
    array = []
    s = Solution()
    for _ in range(n):
        l = list(map(int, input().split()))
        array.append(l)
    result = s.solu(array)
    for temp in result:
        print(temp)