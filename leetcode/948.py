# 你的初始 能量 为 P，初始 分数 为 0，只有一包令牌 tokens 。其中 tokens[i] 是第 i 个令牌的值（下标从 0 开始）。
# 令牌可能的两种使用方法如下：
# 如果你至少有 token[i] 点 能量 ，可以将令牌 i 置为正面朝上，失去 token[i] 点 能量 ，并得到 1 分 。
# 如果我们至少有 1 分 ，可以将令牌 i 置为反面朝上，获得 token[i] 点 能量 ，并失去 1 分 。
# 每个令牌 最多 只能使用一次，使用 顺序不限 ，不需 使用所有令牌。
# 在使用任意数量的令牌后，返回我们可以得到的最大 分数 。


class Solution:
    def bagOfTokensScore(self, tokens, P: int) -> int:
        # 想要获取分数从数组左侧翻牌子,想要获取更多的能量从数组右侧翻牌子
        tokens.sort()
        res = 0
        score = 0
        length = len(tokens)
        left, right = 0, length - 1
        while left <= right:
            while left <= right and P >= tokens[left]:
                P -= tokens[left]
                score += 1
                left += 1
                res = max(res, score)
            if right > left and score > 0:
                score -= 1
                P += tokens[right]
                right -= 1
            else:
                break
        return res


if __name__ == '__main__':
    s = Solution()
    tokens = [100,200,300,400]
    P = 200
    print(s.bagOfTokensScore(tokens, P))