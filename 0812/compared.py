def my_strcmp(str1, str2):
    if str1 == str2:
        return 0
    ord_str1 = []
    ord_str2 = []
    for i in range(len(str1)):
        ord_str1.append(str1[i])
    for j in range(len(str2)):
        ord_str2.append(str2[j])

    for num in ord_str1:
        for num2 in ord_str2:
            if num > num2:
                return 1
            elif num < num2:
                return -1


print(my_strcmp('jejudo', 'jravel'))



#other sol : 파이썬에서 문자열에 부등호 사용시 문자의 ASCII값을 비교한다.

def my_strcmp2(s1,s2):
    if s1 < s2:
        return -1
    elif s1> s2:
        return 1
    else:
        return 0
    