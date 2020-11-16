# 3.20
# 有一叠扑克牌，每张牌介于1和10之间
# 有四种出牌方法：
# 单出1张
# 出2张对子
# 出五张顺子，如12345
# 出三连对子，如112233
# 给10个数，表示1-10每种牌有几张，问最少要多少次能出完


def dfs(l):
    if sum(l) == 0:
        return 0
    elif tuple(l) in memory:
        return memory[tuple(l)]
    else:
        res = float('inf')
        for i in range(10):
            # 顺子
            if i < 6 and l[i] > 0 and l[i+1] > 0 and l[i+2] > 0 and l[i+3] > 0 and l[i+4] > 0:
                l[i] -= 1
                l[i+1] -= 1
                l[i+2] -= 1
                l[i+3] -= 1
                l[i+4] -= 1
                res = min(res, dfs(l) + 1)
                l[i] += 1
                l[i + 1] += 1
                l[i + 2] += 1
                l[i + 3] += 1
                l[i + 4] += 1
                memory[tuple(l)] = res
            # 连对
            if i < 8 and l[i] > 1 and l[i+1] > 1 and l[i+2] > 1:
                l[i] -= 2
                l[i+1] -= 2
                l[i+2] -= 2
                res = min(res, dfs(l) + 1)
                l[i] += 2
                l[i + 1] += 2
                l[i + 2] += 2
                memory[tuple(l)] = res
            # 对子
            if l[i] > 1:
                l[i] -= 2
                res = min(res, dfs(l) + 1)
                l[i] += 2
                memory[tuple(l)] = res
            # 单牌
            if l[i] > 0:
                l[i] -= 1
                res = min(res, dfs(l) + 1)
                l[i] += 1
                memory[tuple(l)] = res
        return res


if __name__ == '__main__':
    l = list(map(int, input().strip().split()))
    memory = {}
    print(dfs(l))








# def dfs(state):
#     if tuple(state) in memo:
#         return memo[tuple(state)]
#     if sum(state) == 0:
#         return 0
#     else:
#         res = float('inf')
#         for i in range(10):
#             # 出顺子
#             if i < 6 and state[i] > 0 and state[i + 1] > 0 and state[i + 2] > 0 and state[i + 3] > 0 and state[i + 4] > 0:
#                 state[i] -= 1
#                 state[i + 1] -= 1
#                 state[i + 2] -= 1
#                 state[i + 3] -= 1
#                 state[i + 4] -= 1
#                 res = min(res, dfs(state) + 1)
#                 state[i] += 1
#                 state[i + 1] += 1
#                 state[i + 2] += 1
#                 state[i + 3] += 1
#                 state[i + 4] += 1
#                 memo[tuple(state)] = res
#             # 出三连对子
#             if i < 8 and state[i] > 1 and state[i + 1] > 1 and state[i + 2] > 1:
#                 state[i] -= 2
#                 state[i + 1] -= 2
#                 state[i + 2] -= 2
#                 res = min(res, dfs(state) + 1)
#                 state[i] += 2
#                 state[i + 1] += 2
#                 state[i + 2] += 2
#                 memo[tuple(state)] = res
#             # 出2张对子
#             if state[i] > 1:
#                     state[i] -= 2
#                     res = min(res, dfs(state) + 1)
#                     state[i] += 2
#                     memo[tuple(state)] = res
#             # 单出一张
#             if state[i] > 0:
#                 state[i] -= 1
#                 res = min(res, dfs(state)+1)
#                 state[i] += 1
#                 memo[tuple(state)] = res
#         return res
#
# # state = list(map(int, input().split()))
# # state = [4,4,4,4,4,4,4,4,3,3]
# # print(dfs(state))
#
#
# if __name__ == '__main__':
#     memo = {}
#     l = list(map(int, input().strip().split()))
#     # 一张张出是最慢的
#     # number = sum(l)
#     # result = solution(l, number)
#     # print(result)
#
#     print(dfs(l))

