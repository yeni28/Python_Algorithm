bulb = list(input())
N = len(bulb)
cnt = 0
first_n_check = 0

for n in range(N):
    if bulb[n] == 'N':
        first_n_check += 1
    if first_n_check == N:
        print('0')
        break

for j in range(1, N+1):# 스위치번호는 1부터 N
    for i in range(N):  # 인덱스는 0부터 N
        if (i+1) % j == 0: #배수라면
            if bulb[i] == 'Y':
                bulb[i] = 'N'
            else:
                bulb[i] = 'Y'
    cnt += 1
    n_len = 0
    for k in range(N):
        if bulb[k] == 'N':
            n_len += 1
        if n_len == N:
            print(cnt)
            break
