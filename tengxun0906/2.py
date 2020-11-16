if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            array = list(map(int, input().split()))
            if n == 1:
                print(-array[-1] / array[-2])
            flag = False
            if array[-1] > 0:
                flag = True
            flag_a = True
            for i in range(n-1, -1, -2):
                if array[i] != 0:
                    flag_a = False
            if flag_a and flag:
                print('No')
        except:
            break