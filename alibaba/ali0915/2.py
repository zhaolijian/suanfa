# a,b字符串，只有0，1组成，找出c，既不是a的子序列，也不是b的子序列，求c的最短长度
# 0
# 1
# 2

# 011001
# 100110
#

if __name__ == '__main__':
    while True:
        try:
            a = input()
            b = input()

            # 判断sub是否是string的子序列
            # def func(sub, string):
            #     l1, l2 = 0, 0
            #     while l1 < len(sub) and l2 < len(string):
            #         if sub[l1] == string[l2]:
            #             l1 += 1
            #         l2 += 1
            #     if l1 == len(sub):
            #         return True
            #     return False

            def func(sub, string):
                temp = sub_a if string == a else sub_b
                if sub[:-1] in temp:
                    for i in range(temp[sub[:-1]] + 1, len(string)):
                        if sub[-1] == string[i]:
                            temp[sub] = i
                            return True
                    return False
                elif len(sub) == 1:
                    for i in range(len(string)):
                        if sub[0] == string[i]:
                            temp[sub] = i
                            return True
                    return False
                return False

            # 深度遍历，不断向sub后面添加0或1，判断添加后的字符串是否是a或者b的子序列
            def dfs(sub):
                global res, result
                for i in range(2):
                    is_a, is_b = func(sub + str(i), a), func(sub + str(i), b)
                    if not is_a and not is_b:
                        res = min(res, len(sub) + 1)
                        # 最终字符串
                        # result = sub + str(i)
                        return
                    else:
                        dfs(sub + str(i))

            sub_a = {}
            sub_b = {}

            # 最终结果
            res = max(len(a), len(b)) + 1
            # 最终字符串，用于调试
            # result = ''
            dfs('')
            print(res)
            # print(result)

        except:
            break
