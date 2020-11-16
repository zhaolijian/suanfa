# 第二题部分代码：给定宽度和高度数组，求最大面积
def func(width, height):
    stack = [-1]
    res = 0
    # 累计宽度
    width_array = [0]
    for i in range(len(width)):
        width_array.append(width_array[-1] + width[i])
    width_array.append(0)
    for i in range(len(width)):
        while stack[-1] != -1 and height[stack[-1]] >= height[i]:
            res = max(res, height[stack.pop()] * (width_array[i] - width_array[stack[-1] + 1]))
        stack.append(i)
    max_index = stack[-1]
    while stack[-1] != -1:
        res = max(res, height[stack.pop()] * (width_array[max_index] - width_array[stack[-1] + 1]))
    return res


if __name__ == '__main__':
    width = [2, 3, 1, 2]
    height = [2, 3, 2, 1]
    print(func(width, height))