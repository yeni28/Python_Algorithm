N, K = map(int, input().split())
#남여 따로 카운트
f_cnt = [0] * 6 # 학년을 인덱스로 하는 카운트 배열
m_cnt = [0] * 6
for i in range(N):
    S, Y = map(int,input().split())
    if S == 0:
        f_cnt[Y-1] += 1 #S-1 = 학년을 인덱스와 맞추기
    if S == 1:
        m_cnt[Y-1] += 1

#방 개수를 구해보자
f_room = 0
m_room = 0
for f in range(6):
    if 0 < f_cnt[f] <= K:
        f_room += 1
    elif f_cnt[f] > K:
        if f_cnt[f] % K == 0:
            f_room += f_cnt[f]//K
        else:
            f_room += (f_cnt[f]//K) + 1
for m in range(6):
    if 0< m_cnt[m] <= K:
        m_room += 1
    elif m_cnt[m] > K:
        if m_cnt[m] % K == 0:
            m_room += m_cnt[m]//K
        else:
            m_room += (m_cnt[m]//K) + 1

print(f_room + m_room)



