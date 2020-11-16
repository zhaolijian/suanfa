# -*- coding:utf-8 -*-
# class Solution:
#     def Power(self, base, exponent):
#         return pow(base, exponent)

from __future__ import division


# class Solution:
#     def Power(self, base, exponent):
#         try:
#             if base == 0 and exponent <= 0:
#                 return
#         except RuntimeError:
#             print("输出值错误")
#         if base == 0 and exponent > 0:
#             return 0
#         if base != 0 and exponent == 0:
#             return 1
#         temp = 1
#         if exponent < 0:
#             temp = 0
#         abs_e = abs(exponent)
#         res = 1
#         for i in range(abs_e):
#             res *= base
#         return res if temp else 1/res

# class Solution:
#     def Power(self, base, exponent):
#         try:
#             while base == 0 and exponent <= 0:
#                 break
#         except RuntimeError:
#             print("输入值错误")
#         if base == 0 and exponent > 0:
#             return 0
#         elif base != 0 and exponent == 0:
#             return 1
#         elif base != 0 and exponent == 1:
#             return base
#         elif base != 0 and exponent == -1:
#             return 1/base
#         else:
#             # 如果n为偶数，那么base^n = base^(n/2)*base^(n/2)
#             # 如果n为奇数，那么base^n = base((n-1)/2)*base((n-1)/2)*base
#             if exponent % 2 == 0:
#                 return self.Power(base, exponent/2) * self.Power(base, exponent/2)
#             else:
#                 return self.Power(base, (exponent-1)/2) * self.Power(base, (exponent-1)/2) * base


# 快速求幂算法

class Solution:
    def Power(self, base, exponent):
        try:
            if base == 0 and exponent <= 0:
                return
        except RuntimeError:
            print("输入值错误")
        if base == 0 and exponent > 0:
            return 0
        elif base != 0 and exponent == 0:
            return 1
        else:
            # 将exponent转换为二进制数，要求的数=base的二进制位次方之和
            e = abs(exponent)
            temp = base
            result = 1
            while e > 0:
                # 最后一位是1
                if e & 1 == 1:
                    result *= temp
                temp = temp * temp
                e = e >> 1
            return result if exponent > 0 else 1/result


class Solution:
    def Power(self, base, exponent):
        try:
            if base == 0 and exponent <= 0:
                return
        except RuntimeError:
            print("输入值错误")
        if base == 0 and exponent > 0:
            return 0
        elif base != 0 and exponent == 0:
            return 1
        else:
            # 将exponent转换为二进制数，要求的数=base的二进制位次方之和
            e = abs(exponent)
            result = 1
            while e > 0:
                # 最后一位是1
                if e & 1 == 1:
                    result *= base
                base = base *  base
                e = e >> 1
            return result if exponent > 0 else 1/result


if __name__ == '__main__':
    s = Solution()
    base = 2
    exponent = -3
    # print(pow(1.5, 2))
    print(s.Power(base, exponent))
