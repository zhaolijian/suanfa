# 3.20
# 定义上升字符串，s[i] >= s[i-1], 比如aaa, abc, acb不是
# 给定n个上升字符串，选择任意个拼起来，问能拼出来的最长上升字符串长度


def solution(l):
    # 存储到当前字符串位置的最长长度
    # 每一个值都是找到前面满足条件（当前字符串首字母大于等于前面字符串的末尾字母）的最长长度加上当前字符串长度
    if len(l) < 1:
        return 0
    else:
        init = []
        # 对l按首字母排序
        sort_l = sorted(l)
        init.append(len(sort_l[0]))
        for i in range(1, len(sort_l)):
            max_len = 0
            # 遍历前面字符串
            for j in range(i):
                # 如果当前字符串首字母大于等于前面字符串的末尾字母
                if sort_l[i][0] >= sort_l[j][-1]:
                    if (len(sort_l[i]) + init[j]) > max_len:
                        max_len = len(sort_l[i]) + init[j]
            init.append(max_len)
        return max(init)


if __name__ == '__main__':
    n = int(input())
    l = []
    for i in range(n):
        str = input()
        l.append(str)
    result = solution(l)
    print(result)
