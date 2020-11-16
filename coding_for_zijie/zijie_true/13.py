while True:
    try:
        n, m = map(int, input().split())
        res = 0
        while m > 0:
            res += n
            m -= 1
            n = pow(n, 0.5)
        # print('%.2f', res)
        print(round(res, 2))
    except:
        break