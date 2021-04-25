def bin_func(number):
    res = []
    for i in range(31, -1, -1):
        temp = 1 if number & (1 << i) else 0
        res.append(temp)
    return res


def toString(array):
    return ''.join(array)
    # res = ''
    # for i in range(32):
    #     res += str(array[i])
    # return res


if __name__ == '__main__':
    while True:
        try:
            l = list(map(int, input().split()))
            length = len(l)
            # 所有数的二进制形式
            array = []
            # 所有数的移位后的字符串
            res = []
            # 整数结果集
            result = []
            for i in range(length):
                # 当前数的二进制形式
                cur = bin_func(l[i])
                # 交换位置
                for j in range(0, 31, 2):
                    cur[j], cur[j + 1] = cur[j + 1], cur[j]
                array.append(cur)
            # 移位
            first = array[-1][-2:] + array[0][:-2]
            # 第一个数
            res.append(toString(first))
            for i in range(1, length):
                last = array[i - 1][-2:]
                final = last + array[i][:-2]
                res.append(toString(final))
            # 将所有的字符串转换为整数
            for i in range(length):
                cur_number = 0
                cur_string = res[i]
                for j in range(31, -1, -1):
                    cur_number += int(cur_string[31 - j]) << j
                result.append(str(cur_number))
            print(' '.join(result))
        except:
            break
