
T = int(input())

for tc in range(1, T+1):
    A, B = input().split()
    a = len(A)
    b = len(B)
    cnt = 0

    # A에 포함된 B의 전체글자를 제외한 A의 문자열 개수를 구하기
    i = 0
    j = 0

    while i < a:
        if A[i] != B[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
        if j == b:
            cnt += 1
            j = 0
            
    result = a - ((b-1) * cnt)

    print(f'#{tc} {result}')