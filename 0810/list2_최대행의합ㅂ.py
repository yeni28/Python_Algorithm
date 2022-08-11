N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

#각 행의 값을 구하고 그 중 최대값을 출력하시오.

maxV = 0 #최대 행의 합
for i in range(N):
    rs = 0 #행의 합
    for j in range(N): #각 i행의 j열에 접근
        rs += arr[i][j]
    if maxV < rs:
        maxV = rs

print(maxV)

# 초기화하는 것을 잘 신경쓰자. 쉬운 것 부터 꼼꼼하게 따지기.
# 열의 합을 최대값으로 구하는 것도 해보자.

