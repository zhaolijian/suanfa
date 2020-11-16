# 在一个行递增、列递增矩阵中找到固定值 O（n） 与每一行的最后一个值比较
def solution(l, target):
    for i in range(len(l)):
        if l[i][-1] == target:
            return i, len(l[0])-1
        elif l[i][-1] > target:
            for j in range(len(l[0])-1, -1, -1):
                if l[i][j] == target:
                    return i, j


if __name__ == '__main__':
    l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    target = 6
    print(solution(l, target))