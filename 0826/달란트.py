T = int(input())
for tc in range(1, T+1):
    n, p = map(int, input().split())
    a = n//p # 묶음으로 나눠진 수
    b = a + 1 # 나눠진 수 보다 1 더 큰 수
    if a * p == n:
        max_v = a ** p
    else:
        max_v = 0
        for i in range(1, p+1):
            for j in range(1, p+1):
                if i + j == p:
                    if a * i + b * j == n:
                        if max_v < (a ** i) * (b ** j):
                            max_v = (a ** i) * (b ** j)


    print(f'#{tc} {max_v}')

