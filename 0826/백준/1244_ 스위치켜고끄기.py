N = int(input())
switch_list = list(map(int, input().split()))
S = int(input())
for _ in range(S):
    gen, num = map(int, input().split())
    idx = num -1  # 스위치의 인덱스는 번호 -1
    if gen == 1:  # 남자일 때
        for i in range(N):
            if (i+1) % num == 0: #번호가 스위치 번호의 배수라면
                # 상태를 변경해준다.
                if switch_list[i] == 0:
                    switch_list[i] = 1
                elif switch_list[i] == 1:
                    switch_list[i] = 0

    elif gen == 2:  # 여자일 때
        cnt = -1  # 스위치가 대칭인 범위 구하기
        for j in range(N):
            if -1 < idx - j and idx + j < N:
                if switch_list[idx - j] == switch_list[idx + j]:
                    cnt += 1
                else:
                    break

        # 스위치 범위까지 상태를 변경해준다.
        for k in range(idx-cnt, idx + cnt + 1):
            if switch_list[k] == 0:
                switch_list[k] = 1
            elif switch_list[k] == 1:
                switch_list[k] = 0

for i in range(0, N, 20):
    print(*switch_list[i: i + 20])