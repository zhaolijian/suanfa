# 美团打算选调n名业务骨干到n个不同的业务区域，本着能者优先的原则，公司将这n个人按照业务能力从高到底编号为1~n。
# 编号靠前的人具有优先选择的权力，每一个人都会填写一个意向，这个意向是一个1~n的排列，表示一个人希望的去的业务区域顺序，如果有两个人同时希望去某一个业务区域则优先满足编号小的人，每个人最终只能去一个业务区域。
#
# 例如3个人的意向顺序都是1 2 3，则第一个人去1号区域，第二个人由于1号区域被选择了，所以只能选择2号区域，
# 同理第三个人只能选择3号区域。
#
# 最终请你输出每个人最终去的区域。

if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            # 岗位对应的人
            init = [0] * n
            # 人对应的岗位
            res = [0] * n
            for ele in range(n):
                array = list(map(int, input().split()))
                for i in range(n):
                    if init[array[i] - 1] == 0:
                        init[array[i] - 1] = ele + 1
                        break
            for j, ele in enumerate(init):
                res[ele - 1] = j + 1
            print(' '.join(map(str, res)))
        except:
            break
