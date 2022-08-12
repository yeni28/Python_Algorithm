#str()함수를 사용하지 않고 구현하는 itoa()함수
def my_itoa (int):
    num_list = ""
    if int < 0:
        int *= -1
    # num_list += chr(int)

    return num_list

print(my_itoa(97))


# 내 풀이는 잘못됨 교수님 풀이가 진짜임
# 숫자 -> 문자열 / 숫자에서 한 자리씩 떼는 것은 %10 이를 활용

def itoa(a):
    i = 10
    s = ""#숫자를 문자열로 바꾼 결과
    while a > 0 :
        mod = a % i #
        s += chr(ord('0') + mod)
        a //= 10


    return s[::-1]

a = 1234
b = itoa(a)

print(a)
print(b)
print(type(a))
print(type(b))
