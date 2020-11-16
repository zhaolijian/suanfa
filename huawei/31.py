# 对字符串中的所有单词进行倒排。
# 说明：
# 1、构成单词的字符只有26个大写或小写英文字母；
# 2、非构成单词的字符均视为单词间隔符；
# 3、要求倒排后的单词间隔符以一个空格表示；如果原字符串中相邻单词间有多个间隔符时，倒排转换后也只允许出现一个空格间隔符；
# 4、每个单词最长20个字母；
if __name__ == '__main__':
    while True:
        try:
            s = input()
            res = ''
            for i in range(len(s)):
                if 'A' <= s[i] <= 'Z' or 'a' <= s[i] <= 'z':
                    res += s[i]
                else:
                    if not res or res[-1] == ' ':
                        continue
                    else:
                        res += ' '
            print(' '.join(res.split()[::-1]))
        except:
            break