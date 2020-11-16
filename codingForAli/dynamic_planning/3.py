# Description
# 给定两个字符串，返回两个字符串的最长公共子序列（不是最长公共子字符串），可能是多个。
#
# Input
# 输入第一行为用例个数， 每个测试用例输入为两行，一行一个字符串
#
# Output
# 如果没有公共子序列，不输出，如果有多个则分为多行，按字典序排序。
#
# Sample Input 1
# 1
# 1A2BD3G4H56JK
# 23EFG4I5J6K7
#
# Sample Output 1
# 23G456K
# 23G45JK


def solution(l1, l2, dp, len_1, len_2, max_res, temp, s):
    while max_res > 0:
        if len_1 > 0 and len_2 > 0 and dp[len_1][len_2] == dp[len_1-1][len_2] and dp[len_1][len_2] == dp[len_1][len_2-1]:
            solution(l1, l2, dp, len_1-1, len_2, max_res, temp, s)
            solution(l1, l2, dp, len_1, len_2 - 1, max_res, temp, s)
            return
        elif len_1 > 0 and dp[len_1][len_2] == dp[len_1 - 1][len_2]:
            len_1 -= 1
        elif len_2 > 0 and dp[len_1][len_2] == dp[len_1][len_2 - 1]:
            len_2 -= 1
        else:
            temp = l1[len_1] + temp
            len_1 -= 1
            len_2 -= 1
            max_res -= 1
    s.add(temp)


# 获得dp矩阵
def dp(l1, l2):
    init = [[0 for i in range(len(l2))] for j in range(len(l1))]
    init[0][0] = 1 if l1[0] == l2[0] else 0
    for m in range(1, len(l1)):
        init[m][0] = max(init[m-1][0], 1 if l1[m] == l2[0] else 0)
    for n in range(1, len(l2)):
        init[0][n] = max(init[0][n-1], 1 if l2[n] == l1[0] else 0)
    for p in range(1, len(l1)):
        for q in range(1, len(l2)):
            if l1[p] == l2[q]:
                init[p][q] = init[p-1][q-1] + 1
            else:
                init[p][q] = max(init[p-1][q], init[p][q-1])
    return init


if __name__ == '__main__':
    for _ in range(int(input())):
        l1 = input()
        l2 = input()
        dp = dp(l1, l2)
        max_res = dp[-1][-1]
        s = set()
        len_1 = len(l1) - 1
        len_2 = len(l2) - 1
        temp = ""
        solution(l1, l2, dp, len_1, len_2, max_res, temp, s)
        for i in sorted(list(s)):
            print(i)


