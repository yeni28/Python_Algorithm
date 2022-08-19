T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cnt = 0
    max_route = 0
    rooms = [0] * 401
    for _ in range(N):
        A, B = map(int, input().split())

        # 공통적으로 변경해줘야 할 조건이 많다면,
        # 변수 값을 if 문으로 설정해주는 방법도 있다. (베리굿)
        if A > B: # A가 B보다 크면, 두 값을 반대로 바꿔주면 된다.
            A, B = B, A
        if A % 2 == 0: # A가 짝수일 때는, 홀수도 못가니까 A에서 1 빼줌
            A = A - 1
        if B % 2 == 1: # 도착지점이 홀수일때는 짝수도 못가니까 B에서 1 더해줌
            B = B + 1

        for room in range(A, B+1):
            rooms[room] += 1 # 인덱스에 방문 기록 저장

        for i in range(len(rooms)): #최댓값 구하기
            if max_route < rooms[i]:
                max_route = rooms[i]

    print(f'#{tc} {max_route}')
