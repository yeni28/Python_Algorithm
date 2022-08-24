import time
start = time.time()

# q = []
# n = 1000000 #마이쮸의 개수
# m = 0 #지금까지 나눠준 마이쮸의 개수
# p = 1 # 마이쮸를 나눠주기 시작할  사람의 번호
# v = 0  #마지막에 받는 사람이 누군지?
#
#
# while m < n:
#     q.append((p, 1, 0)) #마이쮸를 받을 사람을 줄에 세운다. (번호표주기) append로 구현
#     v, c, my = q.pop(0) #ppo() => 맨 마지막 원소 / pop(0) => 첫번째 원소를 준다.
#     # print(f'큐에 남이있는 사람수 {len(q)+1}, 받아갈 마이쮸 개수 : {c}, 나눠준 개수{m}')
#     m += c
#     #마이쮸를 받았으니, 다시 받기 위해 줄의 맨 뒤로 이동.
#     q.append((v, c+1, my + c))
#     p += 1 # 줄서는 번호 1씩 증가
#
#     #q가 끝나면
# print(f'마지막 받은 사람: {v}')
#
# #종료시간 측정
# print(f'걸린시간 {time.time() - start }')

from collections import deque
p = 1
q = deque()
n = 1000000 #마이쮸 개수
m = 0
v = 0

while m < n :
    q.append((p, 1, 0)) #번호, 마이쮸 개수, 내가 받은 순서
    v, c, my = q.popleft() #맨 왼쪽에서 원소 빼기
    m += c
    q.append((v, c+1, my+c))
    p += 1

print(f'걸린시간 {time.time() - start }')