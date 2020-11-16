# 题目描述
# 密码要求:
# 1.长度超过8位
# 2.包括大小写字母.数字.其它符号,以上四种至少三种
# 3.不能有相同长度大于2的子串重复
if __name__ == '__main__':
    while True:
        try:
            s = input()
            length = len(s)
            if length <= 8:
                print('NG')
                continue
            set_array = set()
            for i in range(length):
                if 'A' <= s[i] <= 'Z' and 0 not in set_array:
                    set_array.add(0)
                elif 'a' <= s[i] <= 'z' and 1 not in set_array:
                    set_array.add(1)
                elif '0' <= s[i] <= '9' and 2 not in set_array:
                    set_array.add(2)
                elif not ('A' <= s[i] <= 'Z') and not ('a' <= s[i] <= 'z') and not ('0' <= s[i] <= '9') and 3 not in set_array:
                    set_array.add(3)
            if len(set_array) < 3:
                print('NG')
                continue
            substring = [s[i: i + 3] for i in range(length - 2)]
            if len(set(substring)) != length - 2:
                print('NG')
                continue
            print('OK')
        except:
            break