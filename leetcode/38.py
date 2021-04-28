class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        if n == 2:
            return "11"
        res = "11"
        for i in range(3, n + 1):
            new_res = ""
            number = 1
            for i in range(1, len(res)):
                if res[i] == res[i - 1]:
                    number += 1
                    if i == len(res) - 1:
                        new_res += str(number) + str(res[i])
                else:
                    new_res += str(number) + str(res[i - 1])
                    if i == len(res) - 1:
                        new_res += "1" + str(res[i])
                    else:
                        number = 1
            res = new_res
        return res