# 题目描述：
# 当一个字符串A是由1个或多个字符串B拼接而成，我们称为"B组成了A"。例如，"ab"组成了"abab"。
# 现有两个长度小于1000的字符串S1和S2，请找出最长的字符串X，使得"X组成了S1"且"X组成了S2"，如果找不到X，返回空字符串。
# 区分大小写。

# 输入描述
# 第1行是字符串S1
#
# 第2行到字符串S2
#
# 输出描述
# 最长的字符串X，使得"X组成了S1"且"X组成了S2"，如果找不到X，返回空字符串

# 样例输入
# abcabc
# abc
# 样例输出
# abc
if __name__ == '__main__':
    while True:
        try:
            s1 = input()
            s2 = input()
            len_1, len_2 = len(s1), len(s2)
            if len(s1) > len(s2):
                s1, s2 = s2, s1
                len_1, len_2 = len_2, len_1

            def func(subset, string):
                if subset == string:
                    return True
                len_sub = len(subset)
                length = len(string)
                if length % len_sub:
                    return False
                for i in range(0, length, len_sub):
                    if string[i: i + len_sub] != subset:
                        return False
                return True

            # 找到s1的所有组成
            res = [s1]
            for i in range(len_1 // 2):
                if func(s1[:i + 1], s1):
                    res.append(s1[:i+1])

            result = ''

            for ele in res:
                if func(ele, s2) and len(ele) > len(result):
                    result = ele
            print(result)

        except:
            break