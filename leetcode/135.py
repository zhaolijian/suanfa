# 老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。
# 你需要按照以下要求，帮助老师给这些孩子分发糖果：
# 每个孩子至少分配到 1 个糖果。
# 相邻的孩子中，评分高的孩子必须获得更多的糖果。
# 那么这样下来，老师至少需要准备多少颗糖果呢？


# 两次遍历
class Solution:
    def candy(self, ratings) -> int:
        length = len(ratings)
        if length < 2:
            return 1
        res = [1] * length
        for i in range(1, length):
            if ratings[i] > ratings[i - 1]:
                res[i] = res[i - 1] + 1
        for j in range(length - 2, -1, -1):
            if ratings[j] > ratings[j + 1]:
                res[j] = max(res[j], res[j + 1] + 1)
        return sum(res)


if __name__ == '__main__':
    s = Solution()
    ratings = [1,3,2,2,1]
    print(s.candy(ratings))