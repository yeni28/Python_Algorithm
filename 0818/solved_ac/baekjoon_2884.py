H,M = map(int,input().split())
n = 45

if M < n:
    if H == 0:
        H1 = 23
        M1 = M + 60 - n
    else:
        M1 = M + 60 - n
        H1 = H - 1
elif M >= n:
    M1 = M - n
    H1 = H

print(H1, M1)

