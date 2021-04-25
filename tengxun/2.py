# 小Q在周末的时候和他的小伙伴来到大城市逛街，一条步行街上有很多高楼，共有n座高楼排成一行。
# 小Q从第一栋一直走到了最后一栋，小Q从来都没有见到这么多的楼，所以他想知道他在每栋楼的位置处能看到多少栋楼呢？
# （当前面的楼的高度大于等于后面的楼时，后面的楼将被挡住）
#
# 输入描述:
# 输入第一行将包含一个数字n，代表楼的栋数，接下来的一行将包含n个数字wi(1<=i<=n)，代表每一栋楼的高度。
# 1<=n<=100000;
# 1<=wi<=100000;
#
# 输出描述:
# 输出一行，包含空格分割的n个数字vi，分别代表小Q在第i栋楼时能看到的楼的数量。
#
# 输入例子1:
# 6
# 5 3 8 3 2 5
#
# 输出例子1:
# 3 3 5 4 4 4
#
# 例子说明1:
# 当小Q处于位置3时，他可以向前看到位置2,1处的楼，向后看到位置4,6处的楼，加上第3栋楼，共可看到5栋楼。
# 当小Q处于位置4时，他可以向前看到位置3处的楼，向后看到位置5,6处的楼，加上第4栋楼，共可看到4栋楼。

# 单调栈
while True:
    try:
        n = int(input())
        array = list(map(int, input().split()))
        res = [1] * n
        # 向左看的单调栈(递减)、向右看的单调栈(递增)
        l, r, l_number, r_number = [array[0]], [array[-1]], [0], [0]
        number = 1
        for i in range(1, n):
            l_number.append(number)
            while l:
                if l[-1] <= array[i]:
                    l.pop()
                    number -= 1
                else:
                    break
            l.append(array[i])
            number += 1
        number = 1
        for i in range(n - 2, -1, -1):
            r_number.append(number)
            while r:
                if r[-1] <= array[i]:
                    r.pop()
                    number -= 1
                else:
                    break
            r.append(array[i])
            number += 1
        r_number = r_number[::-1]
        for i in range(n):
            res[i] += l_number[i] + r_number[i]
        print(' '.join(list(map(str, res))))
    except:
        break