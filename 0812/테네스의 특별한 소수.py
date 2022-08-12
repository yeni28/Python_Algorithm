# def get_prime(D,A,B):
#     cnt = 0
#     for n in range(A,B+1):
#         if n < 2:
#             return False
#         for i in range(A,B):
#             if n % 1 == 0:
#                 return False
#         if D in n:
#             cnt += 1
#     return cnt

def get_prime(D,A,B):

    arr = [True] * (B + 1)

    for i in range(A, B):
        if arr[i]:
            for j in range(i + i, B + 1, i):
                arr[j] = False
        a = [i for i in range(A, B + 1) if arr[i] == True]
        cnt = 0
        for num in a:
            if str(D) in str(num):
                cnt += 1
    return cnt


T = int(input())
for tc in range(1,T+1):
    D, A, B = map(int, input().split())
    print(f'#{tc} {get_prime(D,A,B)}')


