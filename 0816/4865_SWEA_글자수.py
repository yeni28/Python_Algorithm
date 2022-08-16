

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    N = len(str1)
    M = len(str2)

# 1에 포함된 글자들이 2에 몇 개씩 들어있는지 찾는다.
# 그중 가장 많은 글자의 '개수'를 출력한다.

    cnt = [0] * (N)
    for i in range(N):
        for j in range(M):
            if str1[i] == str2[j]:
                cnt[i] += 1
    #cnt에서 가장 높은 숫자를 출력한다.

    for num in range(len(cnt)-1):
        maxV = num
        for j in range(num + 1, N):
            if cnt[maxV] < cnt[j]:
                maxV = j
        cnt[maxV], cnt[num] = cnt[num], cnt[maxV]
        result = cnt[0] #선택정렬을 통해 제일 큰 값을 맨 앞으로 보낸다


    print(f'#{tc} {result}')




