# 题目描述：
# 将字母A-Z按顺序编码为0-25，给出一个由A-Z构成的字符串，找出与它编码结果一致的不同字符串的数量（不包含输入字符串）。
# ABC 1   ABC、AM

# 过了80。。。
while True:
    try:
        s = input().strip()
        init = ""
        for ele in s:
            init += str(ord(ele) - ord('A'))
        res = 0
        visisted = {s}

        # 数字构成的字符串、字符串
        def dfs(number, already):
            global res
            if not number:
                if already not in visisted:
                    visisted.add(already)
                    res += 1
                return
            temp = 0
            for i, ele in enumerate(number):
                if i == 0 and ele == '0':
                    dfs(number[1:], already + 'A')
                    break
                temp = temp * 10 + int(ele)
                if 0 <= temp <= 25:
                    dfs(number[i + 1:], already + chr(temp + ord('A')))
                else:
                    break
        dfs(init, "")
        print(res)
    except:
        break