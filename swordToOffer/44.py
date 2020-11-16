class Solution:
    def ReverseSentence(self, s):
        array = list(s.strip().split())
        if len(array) <= 1:
            return s
        result = ""
        for i in range(len(array) - 1, 0, -1):
            result += array[i]
            result += " "
        result += array[0]
        return result
