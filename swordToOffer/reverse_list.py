# s = "111"
# s[0] = 'a'
# print(s)
# b = [1,2,3,4]
# print(b[::-1])
# print(b[3::-1])

# a = None
# test = []
# test.append(a)
# print(test)
# print(5.0/2)
# print(5.0//2)


# 链表反转
def solution(pHead):
    if not pHead or pHead.next is None:
        return pHead
    next = pHead.next
    pHead.next = None
    while next:
        temp = next.next
        next.next = pHead
        pHead = next
        next = temp
    return pHead


if __name__ == '__main__':
    input_values = map(int, input())
    print(input_values)