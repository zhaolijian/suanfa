class Solution:
    def huiwen(self, number):
        return number == number[::-1]

    def func(self, N, M):
        def sushu(number):
            if number in ss:
                return True if ss[number] else False
            flag = True
            for i in range(2, number // 2 + 1):
                if number % i == 0:
                    flag = False
                    break
            ss[number] = 1 if flag else 0
            return flag

        d = {}
        ss = {}
        result = 0
        for i in range(N, M + 1):
            temp = str(i)
            f = False
            for i in range(len(temp)):
                res = temp[:i] + temp[i + 1:]
                while res and res[0] == '0':
                    res = res[1:]
                if not res:
                    continue
                elif res in d:
                    if d[res]:
                        f = True
                        break
                else:
                    if self.huiwen(res) and sushu(int(res)):
                        d[res] = True
                        f = True
                        break
                    d[res] = False
            result += 1 if f else 0
        return result


if __name__ == '__main__':
    N, M = map(int, input().split())
    s = Solution()
    print(s.func(N, M))