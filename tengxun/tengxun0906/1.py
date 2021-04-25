from collections import defaultdict

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        array = list(map(int, input().split()))
        d = defaultdict(int)
        for i in range(n):
            d[array[i]] += 1
        flag = False
        for key in d.keys():
            if d[key] >= 2:
                flag = True
                break
        if not flag:
            print(0)
        else:
            # 每个位置最长序列
            l = [1]
            # 递减栈
            stack_l = [array[0]]
            r = [1]
            # 递减栈，从后往前遍历
            stack_r = [array[-1]]
            temp = 1
            for i in range(1, n):
                if array[i] < stack_l[-1]:
                    stack_l.append(array[i])
                    l.append(len(stack_l) + 1)
                else:
                    temp = len(stack_l)
                    for j in range(temp - 1, -1, -1):
                        # 第一个小的数更改为
                        if array[i] > stack_l[j]:
                            continue
                        elif array[i] == stack_l[j]:
                            l.append(j + 1)
                            break
                        else:
                            stack_l[j + 1] = array[i]
                            l.append(j + 1)

            temp = 1
            for i in range(n - 2, -1, -1):
                if array[i] < stack_r[-1]:
                    stack_r.append(array[i])
                    r.append(len(stack_r) + 1)
                else:
                    temp = len(stack_r)
                    for j in range(temp - 1, -1, -1):
                        if array[i] > stack_r[j]:
                            continue
                        elif array[i] == stack_r[j]:
                            r.append(j + 1)
                            break
                        else:
                            stack_r[j + 1] = array[i]
                            r.append(j + 1)


            r = r[::-1]
            res = 0
            for i in range(n):
                if d[array[i]] >= 2:
                    # 找到下一个相同值
                    for j in range(i + 1, n):
                        if array[j] == array[i]:
                            res = max(res, 2 * min(l[i], r[j]))
            print(res)

