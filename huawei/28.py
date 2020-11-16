# 题目描述
# 若两个正整数的和为素数，则这两个正整数称之为“素数伴侣”，如2和5、6和13，它们能应用于通信加密。
# 现在密码学会请你设计一个程序，从已有的N（N为偶数）个正整数中挑选出若干对组成“素数伴侣”，挑选方案多种多样，
# 例如有4个正整数：2，5，6，13，如果将5和6分为一组中只能得到一组“素数伴侣”，而将2和5、6和13编组将得到两组“素数伴侣”，
# 能组成“素数伴侣”最多的方案称为“最佳方案”，当然密码学会希望你寻找出“最佳方案”。
# 输入:
# 有一个正偶数N（N≤100），表示待挑选的自然数的个数。后面给出具体的数字，范围为[2,30000]。
# 输出:
# 输出一个整数K，表示你求得的“最佳方案”组成“素数伴侣”的对数。
# 匈牙利算法
def issu(x):
    tem = 2
    while tem**2<=x:
        if x%tem==0:
            return False
        tem+=1
    return True
def find(a,l1,l2,l3):
    for i in range(0,len(l3)):
        if issu(a+l3[i]) and l1[i]==0:
            l1[i]=1
            if l2[i]==0 or find(l2[i],l1,l2,l3):
                l2[i] = a
                return True
    return False

try:
    while True:
        n = input()
        n = int(n)
        l = list(map(int,input().split()))
        ji,ou = [],[]
        for i in range(n):
            if l[i]%2==0:
                ou.append(l[i])
            else:
                ji.append(l[i])
        result = 0
        match = [0]*len(ou)
        for i in range(0,len(ji)):
            used = [0]*len(ou)
            if find(ji[i],used,match,ou):
                result+=1
        print(result)
except:
    pass


# 复杂度太高
if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            array = list(map(int, input().split()))
            array.sort()
            res = 0
            visited = set()
            sushu_set = set()

            def sushu(number):
                if number in sushu_set:
                    return True
                for i in range(2, number // 2 + 1):
                    if number % i == 0:
                        return False
                sushu_set.add(number)
                return True

            def func(array, cur):
                global res
                if not array:
                    res = max(res, cur)
                flag = False
                for i in range(len(array) - 1):
                    for j in range(i + 1, len(array)):
                        temp = array[i] + array[j]
                        if sushu(temp):
                            flag = True
                            if (array[i], array[j]) not in visited:
                                visited.add((array[i], array[j]))
                            func(array[:i] + array[i + 1:j] + array[j + 1:], cur + 1)
                if not flag:
                    res = max(res, cur)

            func(array, 0)
            print(res)

        except:
            break