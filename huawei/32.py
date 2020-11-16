# Catcher是MCA国的情报员，他工作时发现敌国会用一些对称的密码进行通信，比如像这些ABBA，ABA，A，123321，
# 但是他们有时会在开始或结束时加入一些无关的字符以防止别国破解。
# 比如进行下列变化 ABBA->12ABBA,ABA->ABAKK,123321->51233214　。
# 因为截获的串太长了，而且存在多种可能的情况（abaaab可看作是aba,或baaab的加密形式），
# Cathcer的工作量实在是太大了，他只能向电脑高手求助，你能帮Catcher找出最长的有效密码串吗？
if __name__ == '__main__':
    while True:
        try:
            s = input()
            length = len(s)
            res = 1
            for i in range(length):
                temp = 1
                while i - temp >= 0 and i + temp <= length:
                    if s[i - temp] == s[i + temp - 1]:
                        temp += 1
                        res = max(res, 2 * temp - 2)
                    else:
                        break
                temp = 1
                while i - temp >= 0 and i + temp < length:
                    if s[i - temp] == s[i + temp]:
                        temp += 1
                        res = max(res, 2 * temp - 1)
                    else:
                        break
            res = length if length <= 1 else res
            print(res)
        except:
            break