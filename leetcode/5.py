# 从中间往两边扩展，较快
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        res = ""
        for i in range(len(s) - 1):
            temp = 0
            if s[i] == s[i + 1]:
                temp += 1
                while i - temp >= 0 and i + temp + 1 < len(s):
                    if s[i - temp] == s[i + temp + 1]:
                        temp += 1
                    else:
                        break
                if 2 * temp > len(res):
                    res = s[i - temp + 1: i + temp + 1]
            # 考虑回文奇数
            temp = 1
            while i - temp >= 0 and i + temp < len(s):
                if s[i - temp] == s[i + temp]:
                    temp += 1
                else:
                    break
            if 2 * temp - 1 > len(res):
                res = s[i - temp + 1: i + temp]
        return res


# 方法2 动态规划
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        res = ""
        init = [[False for i in range(len(s))] for j in range(len(s))]
        for l in range(len(s)):
            for i in range(len(s)):
                j = i + l
                if j >= len(s):
                    break
                elif l == 0:
                    init[i][j] = True
                elif l == 1:
                    init[i][j] = (s[i] == s[j])
                else:
                    init[i][j] = (init[i + 1][j - 1] and s[i] == s[j])
                if init[i][j] and l + 1 > len(res):
                    res = s[i: j + 1]
        return res


if __name__ == '__main__':
    s = Solution()
    # ss = "esbtzjaaijqkgmtaajpsdfiqtvxsgfvijpxrvxgfumsuprzlyvhclgkhccmcnquukivlpnjlfteljvykbddtrpmxzcrdqinsnlsteonhcegtkoszzonkwjevlasgjlcquzuhdmmkhfniozhuphcfkeobturbuoefhmtgcvhlsezvkpgfebbdbhiuwdcftenihseorykdguoqotqyscwymtjejpdzqepjkadtftzwebxwyuqwyeegwxhroaaymusddwnjkvsvrwwsmolmidoybsotaqufhepinkkxicvzrgbgsarmizugbvtzfxghkhthzpuetufqvigmyhmlsgfaaqmmlblxbqxpluhaawqkdluwfirfngbhdkjjyfsxglsnakskcbsyafqpwmwmoxjwlhjduayqyzmpkmrjhbqyhongfdxmuwaqgjkcpatgbrqdllbzodnrifvhcfvgbixbwywanivsdjnbrgskyifgvksadvgzzzuogzcukskjxbohofdimkmyqypyuexypwnjlrfpbtkqyngvxjcwvngmilgwbpcsseoywetatfjijsbcekaixvqreelnlmdonknmxerjjhvmqiztsgjkijjtcyetuygqgsikxctvpxrqtuhxreidhwcklkkjayvqdzqqapgdqaapefzjfngdvjsiiivnkfimqkkucltgavwlakcfyhnpgmqxgfyjziliyqhugphhjtlllgtlcsibfdktzhcfuallqlonbsgyyvvyarvaxmchtyrtkgekkmhejwvsuumhcfcyncgeqtltfmhtlsfswaqpmwpjwgvksvazhwyrzwhyjjdbphhjcmurdcgtbvpkhbkpirhysrpcrntetacyfvgjivhaxgpqhbjahruuejdmaghoaquhiafjqaionbrjbjksxaezosxqmncejjptcksnoq"
    ss = "ccc"
    print(s.longestPalindrome(ss))