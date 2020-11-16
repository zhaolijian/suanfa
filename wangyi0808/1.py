# 给定一个数组，数组中的元素能够拆分成多少素数之和（1不是素数）
if __name__ == '__main__':
    n = int(input())
    array = list(map(int, input().split()))

    def func(number):
        return number // 2

    res = 0
    for ele in array:
        res += func(ele)
    print(res)
