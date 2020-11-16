# 最大重叠区间数目，要求O(n)时间  ??? 应该是nlogn
# 有一个party，许多人来参加。一个记录仪记录下了每个人到达的时间 s_i 和离开的时间 e_i ，
# 也就是说每个人在party的时间为 [ s_i, t_i ]。求出这个party 同一时刻最多接纳了多少人。例如：
# arrl[]={1, 2, 9, 5, 5}   exit[]={4, 5, 12, 9, 12}
class Solution:
    def func(self, arr, exit):
        arr.sort()
        exit.sort()
        length = len(arr)
        i, j = 0, 0
        res = 0
        temp = 0
        while i < length and j < length:
            # 进入时间小于等于离开时间，人数加1
            if arr[i] <= exit[j]:
                temp += 1
                i += 1
                res = max(res, temp)
            else:
                # 进入时间大于离开时间，人数减1
                temp -= 1
                j += 1
        return res


if __name__ == '__main__':
    s = Solution()
    arr = [1, 2, 9, 5, 5]
    exit = [4, 5, 12, 9, 12]
    print(s.func(arr, exit))