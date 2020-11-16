# 3.30
# n个元素的数组，在它的连续子串（连续就是挨着的）中，随机取一个，然后取它的最大值，求这样取出的最大值的期望。
# （eg，就是【1、2、3】，连续子串有【1】【2】【3】【1、2】【2、3】【1、2、3】，然后比如【1、2、3】的最大值就是3）


if __name__ == '__main__':
    l = list(map(int, input().strip().split()))
    number = len(l) * (len(l) + 1)
    sum = 0
    for i in range(len(l)):
        sum += (i+1) * l[i]
    result = (sum * 2) / number
    print("%.6f" % result)
