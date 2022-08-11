T = int(input())

for tc in range(1,N++1):
    N = int(input())
    # 우 하 좌 상 방향설정
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    d = 0 #내가 채우고 있는 방향

    arr = [[0] * N for _ in range(N)]  # 달팽이 크기만큼의 배열


   num = 1 #채워놓는 값
   x,y = 0,0 # 현재 값을 채워놓는 위치

   arr[x][y] = num

   #반복을 통해 달팽이를 채원갈 텐데 언제까지 채울까?
   #num이 n*n이 될 때까지 계속 반복하면 된다.

   while num < n*n:
       # 다음 위치로 가보자
       ni = i + di[d]
       nj = j + dj[d]

       #가봤더니 인덱스 범위를 벗어났거나 이미 채웠던 곳이라면, 방향을 바꿔야한다.
       #갈 수 없으면 갈 수 있을 때까지 방향을 바꿔보면서 진행
       #방향은 4번까지 밖에 못 바꾼다.
       #상하좌우가 막혀있따 => 값채우기가 끝났다. 반복문 알아서 종료

        for i in range(4): #i는 0부터 3까지
            #d = 0,1,2,3
            d = (d+i) % 4 #나올 수 있는 값의 범위가 4로 나눈 나머지와 같다.

            #다음 방향으로 가보자
            ni = ci + di[d]
            nj = cj + dj[d]

            #인덱스 범위 안 인지 검사, 내가 전에 채웠던 위치가 아닌지 검사
            if 0<= ni < n and 0<= nj <n and arr[ni][nj] == 0:
                #갈 수 있는 방향을 찾으면 방향 바꾸기를 종료
                ci = ni
                cj = nj
                break

        #여기까지 오면 갈 수 있는 방향을 찾았다
        # 값 채우기
        num += 1
        arr[ci][cj] = num

       print(f'#{tc}')
       for i in range(N):
           for j in range(N):
               print(arr[i][j], end=" ")
           print()



