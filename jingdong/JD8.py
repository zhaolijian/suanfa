if __name__ == '__main__':
    while True:
        try:
            A = int(input())
            sum_number = 0
            for i in range(2, A):
                temp = A
                while temp:
                    sum_number += temp % i
                    temp //= i
            if sum_number % (A - 2) == 0:
                print(str(sum_number // (A - 2)) + "/" + str(1))
            else:
                for m in range(A // 2, 0, -1):
                    if sum_number % m == 0 and (A - 2) % m == 0:
                        print(str(sum_number // m) + "/" + str((A - 2) // m))
                        break
        except:
            break


if __name__ == '__main__':
    while True:
        try:
            A = int(input())
            sum_number = 0
            for i in range(2, A):
                temp = A
                k = 0
                while temp:
                    while temp >= pow(i, k):
                        k += 1
                    val = temp // pow(i, k - 1)
                    temp %= pow(i, k - 1)
                    sum_number += val
                    k = 0

            if sum_number % (A - 2) == 0:
                print(str(sum_number // (A - 2)) + "/" + str(1))
            else:
                for m in range(A // 2, 0, -1):
                    if sum_number % m == 0 and (A - 2) % m == 0:
                        print(str(sum_number // m) + "/" + str((A - 2) // m))
                        break
        except:
            break