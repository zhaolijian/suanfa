# 题目描述
# 我叫王大锤，是一家出版社的编辑。我负责校对投稿来的英文稿件，这份工作非常烦人，因为每天都要去修正无数的拼写错误。
# 但是，优秀的人总能在平凡的工作中发现真理。我发现一个发现拼写错误的捷径：
# 1. 三个同样的字母连在一起，一定是拼写错误，去掉一个的就好啦：比如 helllo -> hello
# 2. 两对一样的字母（AABB型）连在一起，一定是拼写错误，去掉第二对的一个字母就好啦：比如 helloo -> hello
# 3. 上面的规则优先“从左到右”匹配，即如果是AABBCC，虽然AABB和BBCC都是错误拼写，应该优先考虑修复AABB，结果为AABCC
# 请听题：请实现大锤的自动校对程序
# 输入描述:
# 第一行包括一个数字N，表示本次用例包括多少个待校验的字符串。
# 后面跟随N行，每行为一个待校验的字符串。
# 输出描述:
# N行，每行包括一个被修复后的字符串。
N = int(input())
final = []
for _ in range(N):
    string = input()
    if not string:
        final.append(string)
    else:
        # 对于三个及以上连续相同字符,剩下两个
        # 对于AABB这类的去掉第二个重复字母中的一个
        res = ''
        temp = 1
        cur = string[0]
        for i in range(1, len(string)):
            if string[i] == string[i - 1]:
                temp += 1
            else:
                if temp >= 2:
                    res += cur * 2
                else:
                    res += cur
                cur = string[i]
                temp = 1
        # 针对最后一个字符串的处理
        if temp >= 2:
            res += cur * 2
        else:
            res += cur
        result = res[0]
        # 上个字符是否长度等于2
        flag = False
        for i in range(1, len(res)):
            if res[i] == res[i - 1]:
                if flag:
                    flag = False
                else:
                    result += res[i]
                    flag = True
            else:
                result += res[i]
                if i + 1 < len(res) and res[i + 1] != res[i]:
                    flag = False
        final.append(result)
for ele in final:
    print(ele)
