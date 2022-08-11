T = int(input())
A = [1,2,3,4,5,6,7,8,9,10,11,12]

for tc in range(1,T+1):
    N, K = map(int, input().split())

#집합 A의 부분집합 중 N개의 원소 개수
# 원소의 합은 K인 부분집합의 개수

    # 전체 부분집합
    n = len(A)
    result = 0

    for i in range(1<<n): # 부분집합의 개수
        sum_count = 0
        cnt = 0
        for j in range(n): # 원소의 수(len(A))만큼 비교한 비트
            if i & (1<<j):
                sum_count += A[j] # 부분집합의 개별 원소를 더해준다(한 줄에 한 부분집합이 나옴)
                cnt += 1 #원소 개수를 세기 위한 변수
        if sum_count == K and cnt == N: #합이 K이고 원소개수가 N인것
            result += 1




    print(f'#{tc} {result}')