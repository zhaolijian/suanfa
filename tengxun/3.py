# 作为程序员的小Q，他的数列和其他人的不太一样，他有个数。
# 老板问了小Q一共 m次，每次给出一个整数, 要求小Q把这些数每分为一组，然后把每组进行翻转，小Q想知道每次操作后整个序列中的逆序对个数是多少呢？
#
# 例如:
# 对于序列1 3 4 2，逆序对有(4, 2),(3, 2),总数量为2。
# 翻转之后为2 4 3 1，逆序对有(2, 1),(4, 3), (4, 1), (3, 1),总数量为4。
#
# 输入描述:
# 第一行一个数
# 第二行个数，表示初始的序列()
# 第三行一个数
# 第四行m个数表示
#
# 输出描述:
# m行每行一个数表示答案。
#
# 输入例子1:
# 2
# 2 1 4 3
# 4
# 1 2 0 2
#
# 输出例子1:
# 0
# 6
# 6
# 0
#
# 例子说明1:
# 初始序列2 1 4 3
# 2^{q_1} = 2 ->
# 第一次：1 2 3 4 -> 逆序对数为0
# 2^{q_2} = 4 ->
# 第二次：4 3 2 1 -> 逆序对数为6
# 2^{q_3} = 1 ->
# 第三次：4 3 2 1 -> 逆序对数为6
# 2^{q_4} = 4 ->
# 第四次：1 2 3 4 -> 逆序对数为0


while True:
    try:
        n = int(input())
        init = list(map(int, input().split()))
        m = int(input())
        array = list(map(int, input().split()))

        # 求逆序对数
        def func(array):
            global temp
            if len(array) <= 1:
                return array
            result = []
            mid = len(array) // 2
            l = func(array[:mid])
            r = func(array[mid:])
            i, j = 0, 0
            while i < len(l) and j < len(r):
                if l[i] < r[j]:
                    result.append(l[i])
                    temp += j
                    i += 1
                else:
                    result.append(r[j])
                    j += 1
            if i < len(l):
                temp += (len(l) - i) * len(r)
                result += l[i:]
            if j < len(r):
                result += r[j:]
            return result


        for i in range(m):
            number = pow(2, array[i])
            res = []
            for j in range(0, pow(2, n), number):
                res += init[j: j + number][::-1]
            init = res
            temp = 0
            func(res)
            print(temp)
    except:
        break