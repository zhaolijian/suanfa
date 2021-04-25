# def func(width, height):
#     length = len(width)
#     res = 0
#     # 总宽度
#     w_num = sum(width)
#     # 记录降序索引位置和高度值
#     stack = []
#     # 记录当前宽度位置
#     for i in range(length):
#         if not stack or stack[-1] > height[i]:
#             stack.append((i, height[i]))
#         else:
#             while stack:
#                 if stack[-1][1] < height[i]:
#                     stack.pop()
#                 else:
#                     break
#             stack.append((i, height[i]))
#     for i in range()



def func(width, height):
    length = len(width)
    res = 0
    for p in range(length):
       if not 1 <= width[p] <= 100:
           return 0
    for q in range(length):
        if not 1 <= height[q] <= 100:
            return 0
    for i in range(length):
        temp = 1
        w = 1
        while i - temp >= 0 and height[i - temp] >= height[i]:
            w += width[i - temp]
            temp += 1
        temp = 1
        while i + temp < length and height[i + temp] >= height[i]:
            w += width[i + temp]
            temp += 1
        cur_area = w * height[i]
        res = max(res, cur_area)
    return res


if __name__ == '__main__':
    while True:
        try:
            s = input()
            length = len(s)
            mid = length // 2
            if length % 2 == 0:
                print(0)
                continue
            if not (s[0] == '[' and s[-1] == ']' and s[mid - 1] == ']' and s[mid + 1] == '[' and s[mid] == ','):
                print(0)
                continue
            w = s[:mid][1:-1]
            h = s[mid + 1:][1:-1]
            if not (len(w) % 2) or not (len(h) % 2) or not (len(w) == len(h)):
                print(0)
                continue
            flag = True
            for i in range(mid - 2):
                # str.isdigit为检测字符串w[i]是否是数字
                if not (i % 2) and not (str.isdigit(w[i]) and 1 <= int(w[i]) <= 100):
                    flag = False
                    break
                if i % 2 and w[i] != ',':
                    flag = False
                    break
            for i in range(mid - 2):
                if not (i % 2) and not (str.isdigit(h[i]) and 1 <= int(h[i]) <= 100):
                    flag = False
                    break
                if i % 2 and h[i] != ',':
                    flag = False
                    break
            if not flag:
                print(0)
                continue
            width = list(map(int, s[:mid][1:-1].split(',')))
            height = list(map(int, s[mid + 1:][1:-1].split(',')))
            print(func(width, height))
        except:
            break