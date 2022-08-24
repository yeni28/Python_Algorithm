T = 10
for tc in range(1, T+1):
    n = int(input())
    pwd = list(map(int, input().split()))
    front = 0
    Flag = True

    while Flag:
        for i in range(1, 6):
            pwd[front] -= i
            pwd.append(pwd.pop(front))

            if pwd[front - 1] <= 0:
                pwd[front - 1] = 0
                Flag = False
                break

    print(f'#{tc}', end=' ')
    for j in range(8):
        print(pwd[j], end=' ')
