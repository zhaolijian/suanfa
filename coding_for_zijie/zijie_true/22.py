# 题目描述
# 头条的2017校招开始了！为了这次校招，我们组织了一个规模宏大的出题团队，每个出题人都出了一些有趣的题目，而我们现在想把这些题目组合成若干场考试出来，在选题之前，我们对题目进行了盲审，并定出了每道题的难度系统。一场考试包含3道开放性题目，假设他们的难度从小到大分别为a,b,c，我们希望这3道题能满足下列条件：
# a<=b<=c
# b-a<=10
# c-b<=10
# 所有出题人一共出了n道开放性题目。现在我们想把这n道题分布到若干场考试中（1场或多场，每道题都必须使用且只能用一次），然而由于上述条件的限制，可能有一些考试没法凑够3道题，因此出题人就需要多出一些适当难度的题目来让每场考试都达到要求，然而我们出题已经出得很累了，你能计算出我们最少还需要再出几道题吗？
# 输入描述:
# 输入的第一行包含一个整数n，表示目前已经出好的题目数量。
#
# 第二行给出每道题目的难度系数d1,d2,...,dn。
#
# 数据范围
#
# 对于30%的数据，1 ≤ n,di ≤ 5;
#
# 对于100%的数据，1 ≤ n ≤ 10^5,1 ≤ di ≤ 100。
#
# 在样例中，一种可行的方案是添加2个难度分别为20和50的题目，这样可以组合成两场考试：（20 20 23）和（35,40,50）。
# 输出描述:
# 输出只包括一行，即所求的答案。

# python递归次数太多会导致没有输出，所以要更改递归次数

# 方法1 while循环，不用调整递归次数
n = int(input())
array = list(map(int, input().split()))
array.sort()
res = 0
i = 0
while i < n:
    if i == n - 1:
        res += 2
        break
    elif i == n - 2:
        if array[i + 1] - array[i] <= 20:
            res += 1
        else:
            res += 4
        break
    else:
        if array[i + 2] - array[i + 1] <= 10 and array[i + 1] - array[i] <= 10:
            i += 3
        elif array[i + 1] - array[i] <= 20:
            res += 1
            i += 2
        else:
            res += 2
            i += 1
print(res)


# 方法2 递归，需要调整递归次数
import sys
sys.setrecursionlimit(10**6)

n = int(input())
array = list(map(int, input().split()))
length = n
array.sort()

def func(i):
    global res, length
    if i == length:
        return
    if i == length - 1:
        res += 2
        return
    elif i == length - 2:
        if array[i + 1] - array[i] <= 20:
            res += 1
        else:
            res += 4
        return
    else:
        if array[i + 1] - array[i] <= 10 and array[i + 2] - array[i + 1] <= 10:
            func(i + 3)
        elif array[i + 1] - array[i] <= 20:
            res += 1
            func(i + 2)
        else:
            res += 2
            func(i + 1)

res = 0
func(0)
print(res)