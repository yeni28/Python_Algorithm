T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cnt = [0] * 5

    while True:
        if N % 2 != 0:
            break
        N = N // 2
        cnt[0] += 1

    while True:
        if N % 3 != 0:
            break
        N = N // 3
        cnt[1] += 1

    while True:
        if N % 5 != 0:
            break
        N = N // 5
        cnt[2] += 1

    while True:
        if N % 7 != 0:
            break
        N = N // 7
        cnt[3] += 1

    while True:
        if N % 11 != 0:
            break
        N = N // 11
        cnt[4] += 1


    small_number = ""
    for i in cnt:
        small_number += str(i) + " "

    print(f'#{tc} {small_number}')


    #다른 풀이

    #
    # n = int(input())
    # numbers = [2,3,5,7,11]
    # cnt = [0] * 5
    #
    # for i in range(5):
    #     temp_n = n #n을 계속 나누면서 진행
    #
    #     while temp_n % numbers[i] == 0:
    #         temp_n //= numbers[i]
    #         cnt[i] += 1
    #