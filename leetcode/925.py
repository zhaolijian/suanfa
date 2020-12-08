# 你的朋友正在使用键盘输入他的名字 name。偶尔，在键入字符 c 时，按键可能会被长按，而字符可能被输入 1 次或多次。
# 你将会检查键盘输入的字符 typed。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回 True。


# 方法1
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0
        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j - 1]:
                j += 1
            else:
                return False
        return i == len(name)


# 方法2 计算出name和typed数组中连续的元素及对应的个数，要保证typed中元素的个数>=name中对应的元素个数
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if not name and not typed:
            return True
        elif not name or not typed:
            return False

        def func(array):
            res = []
            i = 0
            while i < len(array):
                number = 1
                while i + 1 < len(array) and array[i] == array[i + 1]:
                    number += 1
                    i += 1
                res.append((array[i], number))
                i += 1
            return res

        name_array = func(name)
        typed_array = func(typed)
        length = len(name_array)
        if length != len(typed_array):
            return False
        for i in range(length):
            ele, number = name_array[i]
            ele_t, number_t = typed_array[i]
            if ele != ele_t or number > number_t:
                return False
        return True

