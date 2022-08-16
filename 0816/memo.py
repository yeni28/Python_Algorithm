

def BF(A, B):
    i = 0
    j = 0
    cnt = 0

    for s in range(len(A)):
        while j <= b and i < a:
            if A[i] == B[j]:
                i += 1
                j += 1
            else:
                i = i - j + 1
                j = 0
        if j == b:
            cnt += 1
            return cnt
        else:
            pass

T = int(input())

for tc in range(1, T + 1):
    A,B = input().split()
    b = len(B)
    a = len(A)
    result = BF(A, B)

    print(f'#{tc} {result}')
