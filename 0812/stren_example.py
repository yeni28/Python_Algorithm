#
# a = ['a','b','c','\0']
#
# def strlen(a):
#     cnt = 0
#     i = 0
#     while a[i] != "\0":
#         cnt += i
#     return cnt
#
# print(strlen(a))


# 2. 문자열 뒤집기

#sol1
s = 'Reverse this strings'


def my_revers(str):
    reverse_str = ""
    for i in range(len(str)-1, -1, -1):
        reverse_str += str[i]

    return reverse_str

print(my_revers(s))


#sol2 : 잘안됨
def my_revers2(str):
    n = l
    s_list = list(s)
    for i in range(len(str)):
        for j in range(len(str)-1):
            str[i], str[i+j] = str[i+j], str[i]
    return str

print(my_revers2(s))

#sol3 : SWAP

def my_revers3(s):
    #sol2 참조
    for i in range(n//2):
        s_list[i], s_list[n-i-1] = s_list[n-i-1], s_list[i]
# 뒤에는 for문 써서 넣어주기