T = int(input())
# M = 5
# terminal = [1,3,5,7,9]
for s in range(1, T+1):
    K, N, M = map(int, input().split())
    terminal = list(map(int, input().split()))
    t = [0] * (N+1)
    g = 0
    charge_num = 0
    for charger in range(0, M):
        t[terminal[charger]] += 1

    while idx_t < N+1:
        idx_t += 1
        if t[idx_t + K] == 0:
            while t[idx_t] == 1:
                for j in range(0, K):
                    print(idx_t,K,j)
                    if idx_t+K-j < idx_t:
                        charge_num = '0'
                        break
                    elif t[idx_t +K-j] == 1:
                        idx_t += (K-j)
        elif t[idx_t +K] == 1:
            charge_num += 1
            idx_t += K
    break


print(f'#{s} {charge_num}')
