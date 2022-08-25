
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    pizzas = list(map(int, input().split()))
    q = []
    i = 0
    for _ in range(N):
        q.append([pizzas[i], i+1]) #피자 넣어주기
        i += 1

    while len(q) > 1: #피자 하나 남을 때까지
        pizza = q.pop(0)
        pizza[0] //= 2
        if pizza[0] != 0:
            q.append(pizza)
        else:
            if i < M: #i는 피자 개수보다 작다면(인덱스 범위 조정)
                q.append([pizzas[i], i+1])
                i += 1

    print(f'#{tc} {q[0][1]}')

