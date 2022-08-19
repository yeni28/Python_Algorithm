T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 노선의 개수
    route = [0] * 5001 # 정류장 5001개 만들어줌 (정류장 수만큼 크기를 가진걸로 해줘도 됨)
    for i in range(1, N+1): # 노선의 개수 입력받기
        A, B = map(int, input().split())
        for node in range(A, B+1): # A와 B가 방문하는 정류장의 범위
            route[node] += 1 # route의 정류장 번호 인덱스에 들리는 곳을 출력해준다.

    P = int(input()) # 정류장의 개수 입력받기
    terminal = []
    for j in range(P): # P개 만큼 정류장 입력받기
        C = int(input()) # 각 정류장의 번호
        terminal.append(C) #정류장 번호를 터미널 리스트에 추가해주기
    result = ""
    for k in terminal: # 각 정류장 번호
        result += str(route[k]) +" " #route에 저장된 인덱스에 정류장 방문 기록이 저장되어있다.
                                    # 공백을 포함해 이를 결과 값에 추가해준다.

    print(f'#{tc} {result}')