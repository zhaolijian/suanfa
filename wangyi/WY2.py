# 一条长l的笔直的街道上有n个路灯，若这条街的起点为0，终点为l，第i个路灯坐标为ai ，
# 每盏灯可以覆盖到的最远距离为d，为了照明需求，所有灯的灯光必须覆盖整条街，但是为了省电，
# 要使这个d最小，请找到这个最小的d。


if __name__ == '__main__':
    while True:
        try:
            n, l = map(int, input().split())
            array = list(map(int, input().split()))
            array.sort()
            temp = 0
            for i in range(1, n):
                temp = max(temp, array[i] - array[i - 1])
            res = max(temp / 2, array[0], l - array[-1])
            res += 0.0000001
            print('%.2f' % res)
        except:
            break