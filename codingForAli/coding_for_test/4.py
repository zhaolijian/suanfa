# 阿里 3.25
# 给出一个二维矩阵，这个矩阵的每一行和每一列都是一个独立的等差数列，其中一些数据缺失了，
# 现在需要推理隐藏但是可以被唯一确定的数字，然后对输入的查询进行回答。
#
# 输入描述：
# 第一行，n,m,q分别表示矩阵的行数，列数和查询的条数。
# 接下来的n行，每行m个数表示这个矩阵，0表示缺失数据。
# −10^9≤Aij​≤10^9
# 接下来q行，每行两个数字i,j表示对矩阵中第i行第j列的数字进行查询。
#
# 输出描述：
# 如果可以确定该位置的数字，则输出数字，如果不能确定则输出UNKNOWN。


# 行数、列数、数据矩阵、查询条数， 查询矩阵
def solution(n, m, l, num, select):
    # 如果数据矩阵每一行只有小于等于一个非0值，则该行的其他位置都是unknown
    # 如果数据矩阵的每一行有大于等于两个非0值，则任意选择两个求出差值，然后将0值位置填充即可。
    init = l.copy()
    for i in range(n):
        # 统计每行的非0值个数
        temp = 0
        # 存放两个位置、值
        array = []
        for j in range(m):
            if l[i][j] != 0 and len(array) < 4:
                temp += 1
                array.append(j)
                array.append(l[i][j])
        # 避免0表示unknown以及等差数列中真的有0值
        if temp <= 1:
            for q in range(m):
                if init[i][q] == 0:
                    init[i][q] = None
        # 如果数据矩阵的每一行有大于等于两个非0值，则任意选择两个求出差值，然后将0值位置填充即可
        if temp > 1:
            cha = (array[3] - array[1]) / (array[2] - array[0])
            for p in range(m):
                if init[i][p] == 0:
                    # 如果为0的位置在array[0]前面
                    if p < array[0]:
                        init[i][p] = array[1] - (array[0] - p) * cha
                    else:
                        init[i][p] = array[1] + (p - array[0]) * cha
    # 返回结果
    result = []
    for t in range(num):
        result.append(init[select[t][0]-1][select[t][1]-1])
    return result


if __name__ == '__main__':
    l1 = list(map(int, input().strip().split()))
    # 行数、列数、查询条数
    n, m, q = l1[0], l1[1], l1[2]
    l = []
    select = []
    for i in range(n):
        l.append(list(map(int, input().strip().split())))
    for j in range(q):
        select.append(list(map(int, input().strip().split())))
    result = solution(n, m, l, q, select)
    for o in result:
        if o is None:
            print("UNKNOWN")
        else:
            print(o)
