#큐 생성

n = 5
q = [0] * n

front = rear = -1

# q.insert(0,1)을 사용할 수도 있지만 인서트를 사용하면 q가 배열로 선언이 되어있는 상태인데, 인덱스 0번에 1을 삽입하라고 하면 파이썬 안에서 있는 친구들을 한 칸 씩 뒤로 다 밀어내고, 밀어내는 작업이 원소의 개수만큼 일어나게 된다. 따라서 작업이 많아지기 때문에 인서트나 팝을 이용하지 않도록 한다.


def enQueue(item): #쿠에 원소를 삽입하는 연산, rear가 1씩 증가.
    #함수안에서 밖에있는 rear를 수정하고 싶을 때는 globalㄹ을 써줘야한다.

    global rear
    # 큐가 만약 꽉차 있다면 삽입 불가 처리
    if isFull():
        print("FULL!")
    # 그게 아니면 rear를 1 증가시키고, 큐에 원소 삽입
    else:
        rear += 1
        q[rear] = item

def deQueue() : #큐의 원소를 하나 빼내고 삭제하는 연산, front가 1씩 증가
    global front
    #큐가 만약 비어있다면 삭제 불가 처리
    if isEmpty():
        print("EMPTY!")

    # 그게 아니면 front를 1 증가시키고, 큐의 원소 하나 삭제

    else:
        front += 1
        return q[front]



def isFull(): #큐가 꽉 차 있는지 확인해주는 함수
    return rear == len(q) - 1

def isEmpty() : #큐가 비어있는지 확인해 주는 함수(큐 안에 들어있는 원소 개수가 0인지)
    return front == rear

for i in range(5): #0~4까지 삽입해준다.
    enQueue(i)

print(isFull()) #꽉 차 있는지 확인
enQueue(5) # 추가 불가처리

for i in range(5): #다섯번 빼내어서 원소가 순서대로 들어갔는지 확인
    print(deQueue())
print(isEmpty()) #비어있느냐? = True
deQueue() #다 뺀 상태에서 디큐를 하면 어떤 일이 발생하는지 - 삭제불가처리ㅣ