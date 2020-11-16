# 题目描述
# 有三只球队，每只球队编号分别为球队1，球队2，球队3，这三只球队一共需要进行 n 场比赛。现在已经踢完了k场比赛，每场比赛不能打平，踢赢一场比赛得一分，输了不得分不减分。已知球队1和球队2的比分相差d1分，球队2和球队3的比分相差d2分，每场比赛可以任意选择两只队伍进行。求如果打完最后的 (n-k) 场比赛，有没有可能三只球队的分数打平。  
# 输入描述:
# 第一行包含一个数字 t (1 <= t <= 10)
# 接下来的t行每行包括四个数字 n, k, d1, d2(1 <= n <= 10^12; 0 <= k <= n, 0 <= d1, d2 <= k)
# 输出描述:
# 每行的比分数据，最终三只球队若能够打平，则输出“yes”，否则输出“no”
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, k, d1, d2 = map(int, input().split())
        # 剩余场数
        need = n - k
        array = []
        # 如果球队1分数大于球队2,球队2大于球队3
        if k >= d1 + 2 * d2 and (k - d1 - 2 * d2) % 3 == 0:
            array.append([d1 + d2, d2, 0])
        # 如果球队1分数大于球队2,球队2小于球队3
        if k >= d1 + d2 and (k - d1 - d2) % 3 == 0:
            array.append([d1, 0, d2])
        # 如果球队1分数小于球队2,球队2大于球队3
        temp = max(d1, d2)
        if k >= 3 * temp - d1 - d2 and (k - 3 * temp + d1 + d2) % 3 == 0:
            array.append([temp - d1, temp, temp - d2])
        # 如果球队1分数小于球队2,球队2小于球队3
        if k >= 2 * d1 + d2 and (k - 2 * d1 - d2) % 3 == 0:
            array.append([0, d1, d1 + d2])
        res = False
        for i in range(len(array)):
            max_val = max(array[i])
            if need >= 3 * max_val - sum(array[i]) and (need - 3 * max_val + sum(array[i])) % 3 == 0:
                res = True
                break
        if res:
            print('yes')
        else:
            print('no')