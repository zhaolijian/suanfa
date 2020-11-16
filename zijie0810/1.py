# 给定一个有序数组，关键字k，找出数组中距离关键字k最近的三个数，以及这三个数中的最小值和最大值数组
if __name__ == '__main__':
    array = list(map(int, input().split()))
    k = int(input())
    res = []
    length = len(array)
    index = -1
    min_val, max_val = float('inf'), float('-inf')
    for i in range(length):
        if array[i] == k:
            index = i
            break
        else:
            continue
    left, right = index - 1, index + 1
    while left >= 0 and right < length:
        if array[index] - array[left] < array[right] - array[index]:
            if len(res) < 3:
                res.append(array[left])
                min_val = min(min_val, array[left])
                max_val = max(max_val, array[left])
                left -= 1
            else:
                break
        else:
            if len(res) < 3:
                res.append(array[right])
                min_val = min(min_val, array[right])
                max_val = max(max_val, array[right])
                right += 1
            else:
                break

    k = 0
    while k < 3 - len(res) and left - k >= 0:
        res.append(array[left - k])
        min_val = min(min_val, array[left - k])
        max_val = max(max_val, array[left - k])
        k += 1
    while k < 3 - len(res) and right + k < length:
        res.append(array[right + k])
        min_val = min(min_val, array[right + k])
        max_val = max(max_val, array[right + k])
        k += 1
    print(res)
    print(min_val)
    print(max_val)