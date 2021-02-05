# 爱丽丝和鲍勃有不同大小的糖果棒：A[i] 是爱丽丝拥有的第 i 根糖果棒的大小，B[j] 是鲍勃拥有的第 j 根糖果棒的大小。
# 因为他们是朋友，所以他们想交换一根糖果棒，这样交换后，他们都有相同的糖果总量。（一个人拥有的糖果总量是他们拥有的糖果棒大小的总和。）
# 返回一个整数数组 ans，其中 ans[0] 是爱丽丝必须交换的糖果棒的大小，ans[1] 是 Bob 必须交换的糖果棒的大小。
# 如果有多个答案，你可以返回其中任何一个。保证答案存在。
class Solution:
    def fairCandySwap(self, A, B):
        sum_A, sum_B = sum(A), sum(B)
        set_A = set(A)
        for ele in B:
            # sum_A - x + ele = sum_B - ele + x
            temp = (sum_A + 2 * ele - sum_B) / 2
            if temp in set_A:
                return [int(temp), ele]
