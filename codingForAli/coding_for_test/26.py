def reOrderArray(self, array):
    # k计算奇数个数
    k = 0
    for i in range(len(array)):
        # 如果array[i]是奇数，则插入到前面去,中间的所有数后移
        if array[i] % 2 == 1:
            temp = array[i]
            array[k + 1: i + 1] = array[k: i]
            array[k] = temp
            k += 1
    return array