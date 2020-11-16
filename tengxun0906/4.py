from collections import defaultdict
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        d = defaultdict(int)
        for i in range(n):
            l = list(map(int, input().split()))
            l.sort()
            d[tuple(l)] += 1
        res = ''
        for key in d.keys():
            if d[key] > 1:
                res = 'YES'
                break
        print('NO' if res != 'YES' else res)