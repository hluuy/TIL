# Algorithm - APS 기본 Queue Part.1

날짜: 2023년 8월 17일

## Queue

⇒ 스택과 마찬가지로 삽입과 삭제의 위치가 제한적인 자료구조

<aside>
💡 선입 선출 구조 ( FIFO : First In First Out )

- 큐에 삽입한 순서대로 원소가 저장되어, 가장 먼저 삽입된 원소(First In)는 가장 먼저 삭제(First Out)된다.
- 저장된 원소 중 첫 번째 원소 = 머리, Front, 삭제된 위치
- 저장된 원소 중 마지막 원소 = 꼬리, Rear
- Queue의 기본 연산
    - 삽입 : enQueue
    - 삭제 : deQueue
</aside>

| 연산 | 기능 |
| --- | --- |
| enQueue( item ) | Queue의 뒤쪽(rear 다음)에 원소를 삽입하는 연산 |
| deQueue() | Queue의 앞쪽(front)에서 원소를 삭제하고 반환하는 연산 |
| createQueue() | 공백 상태의 큐를 생성하는 연산 |
| isEmpty() | Queue가 공백상태인지를 확인하는 연산 |
| isFull() | Queue가 포화상태인지를 확인하는 연산 |
| Qpeek() | Queue의 앞쪽(front)에서 원소를 삭제 없이 반환하는 연산 |

<aside>
🗒️ Queue의 연산 과정

1. 공백 Queue 생성 : createQueue(): ← front = rear = -1
2. 원소 A 삽입 : enQueue(A): ← front = -1, rear = A (Q[0] Queue의 0번 인덱스)
3. 원소 B 삽입 : enQueue(B): ← front = -1, rear = B (Q[1])
4. 원소 반환 / 삭제 : deQueue(): ← front = Q[0]( A 삭제 ), rear = B
5. 원소 C 삽입 : enQueue(C): ← front = Q[0], rear = C(Q[2])
6. 원소 반환 / 삭제 : deQueue(): ← front = Q[1]( B 삭제 ), rear = C
7. 원소 반환 / 삭제 : deQueue(): ← front = Q[2]( C 삭제 ), rear = Q[2]
</aside>

---

## Queue의 구현

### 선형 Queue

<aside>
🗒️ 1차원 배열을 이용한 Queue

- 큐의 크기 = 배열의 크기
- front : 저장된 첫 번째 원소의 인덱스
- rear : 저장된 마지막 원소의 인덱스

상태 표현

- 초기 상태 : front = rear = -1
- 공백 상태 : front == rear
- 포화 상태 : rear == n - 1 ( n : 배열의 크기, n - 1 : 배열의 마지막 인덱스 )

초기 공백 큐 생성

- 크기 n인 1차원 배열 생성
- front와 rear를 -1 로 초기화
</aside>

<aside>
🗒️ Queue의 구현 과정

- 삽입 : enQueue( item )
    - 마지막 원소 뒤에 새로운 원소를 삽입하기 위해
        - rear 값을 하나 증가시켜 새로운 원소를 삽입할 자리를 마련
        - 그 인덱스에 해당하는 배열원소 Q[rear]에 item을 저장
- 삭제 : deQueue()
    - 가장 앞에 있는 원소를 삭제하기 위해
        - front 값을 하나 증가시켜 Queue에 남아있게 될 첫 번째 원소 이동
        - 새로운 첫 번째 원소를 리턴 함으로써 삭제와 동일한 기능을 함
- 공백 상태 및 포화 상태 검사 : isEmpty(), isFull()
    - 공백 상태 : front == rear
    - 포화 상태 : rear == n - 1 ( n : 배열의 크기, n - 1 : 배열의 마지막 인덱스 )
- 검색 : Qpeek()
    - 가장 앞에 있는 원소를 검색하여 반환하는 연산
    - 현재 front의 한 자리 뒤(front + 1)에 있는 원소, 즉 Queue의 첫 번째에 있는 원소를 반환
</aside>

```python
# 선형 Queue에서의 삽입과 삭제
def enQ(data):
    global rear
    if rear == Qsize - 1:
        print('Q is Full')
    else:
        rear += 1
        Q[rear] = data

def deQ():
    global front
    if front == rear: # 비어있으면
        print('Queue is Empty')
        return -1
    else:
        front += 1
        return Q[front]

Qsize = 3
Q = [0] * Qsize
rear = -1
front = -1

enQ(1)
enQ(2)
rear += 1 #enQ(3)
Q[rear] = 3

while front != rear : # Queue가 비어 있지 않으면
    front += 1
    print(Q[front])
# print(deQ())
# print(deQ())
# print(deQ())
# print(deQ())
```

<aside>
❗ 선형 Queue 이용 시 문제점

- 잘못된 포화 상태 인식
    - 선형 Queue를 이용하여 원소의 삽입과 삭제를 계속할 경우, 배열의 앞 부분에 활용할 수 있는 공간이 있음에도 불구하고, rear = n - 1인 상태
    - 즉, 포화 상태로 인식하여 더 이상의 삽입을 수행하지 않게 됨
    
    <포화 상태로 잘못 인식>
    
    |  | [0] | [1] | [2] | [3] |
    | --- | --- | --- | --- | --- |
    | Q |  |  | front | rear                   |
- 해결 방법 1
    - 매 연산이 이루어질 때마다 저장된 원소들을 배열의 앞 부분으로 모두 이동시킴
    - 원소 이동에 많은 시간이 소요되어 Queue의 효율성이 급격히 떨어짐
- 해결 방법 2
    - 1차원 배열을 사용하되, 논리적으로는 배열의 처음과 끝이 연결되어 원형 형태의 큐를 이룬다고 가정하고 사용
    - 원형 Queue의 논리적 구조
        - Q[0] - Q[1] - Q[2] - Q[3] … - Q[n - 2] - Q[n - 1] - Q[0]
</aside>

### 원형 Queue

<aside>
🗒️ 원형 Queue의 구조

- 초기 공백 상태
    - front = rear = 0
- Index의 순환
    - front와 rear의 위치가 배열의 마지막 인덱스인 n - 1을 가리킨 후, 그 다음에는 논리적 순환을 이루어 배열의 처음 인덱스인 0으로 이동해야 함
    - 이를 위해 나머지 연산자 mod를 사용
- front 변수
    - 공백 상태와 포화 상태 구분을 쉽게 하기 위해 front가 있는 자리는 사용하지 않고 항상 빈 자리로 둠
- 삽입 위치 및 삭제 위치
    
    
    |  | 삽입 위치 | 삭제 위치 |
    | --- | --- | --- |
    | 선형 Queue | rear = rear + 1 | front = front + 1 |
    | 원형 Queue | rear = (rear + 1) mod n | front = (front + 1) mod n |
</aside>

<aside>
🗒️ 원형 Queue의 구현 과정

- 초기 공백 Queue 생성
    - 크기 n인 1차원 배열 생성
    - front와 rear를 0으로 초기화
- 공백 상태 및 포화 상태 검사 : isEmpty(), isFull()
    - 공백 상태 : front == rear
    - 포화 상태 : 삽입할 rear의 다음 위치 == 현재 front
    -(rear + 1) mod n == front
- 삽입 : enQueue(item)
    - 마지막 원소 뒤에 새로운 원소를 삽입하기 위해
        - rear 값을 조정하여 새로운 원소를 삽입할 자리를 마련
        - rear ← (rear + 1) mod n:
        - 그 인덱스에 해당하는 배열원소 cQ[rear]에 item 저장
- 삭제 : deQueue, delete()
    - 가장 앞에 있는 원소를 삭제하기 위해
        - front 값을 조정하여 삭제할 자리를 준비
        - 새로운 front 원소를 리턴 함으로써 삭제와 동일한 기능을 함
</aside>

```python
# 원형 Queue에서의 삽입과 삭제
def enQ(data):
    global rear
    # if (rear + 1) % cQsize == front: # Queue를 꽉 차게되면 출력
    #     print('cQ is Full')
    # else:
    # if (rear+1)%cQsize: # 오래된 데이터는 버려도 될 경우 front를 한 칸 밀면서 값을 저장하기
    #     (front+1)%cQsize
    rear = (rear + 1) % cQsize # Queue가 꽉 찼을 때의 상황을 따로 정해주지 않으면 덮어쓰게 된다
    cQ[rear] = data

def deQ():
    global front
    front = (front + 1) % cQsize
    return cQ[front]

cQsize = 4
cQ = [0] *cQsize
front = 0
rear = 0

enQ(1)
enQ(2)
enQ(3)
# print(deQ()) # deQ가 적절히 이루어지지 않으면
# print(deQ())
enQ(4)
enQ(5)
print(deQ())
print(deQ())
```

### 우선순위 Queue - Priority Queue

<aside>
🗒️ 우선순위 Queue의 특성

- 우선순위를 가진 항목들을 저장하는 큐
- FIFO 순서가 아니라 우선순위가 높은 순서대로 먼저 나가게 됨

우선순위 Queue의 적용 분야

- 시뮬레이션 시스템
- 네트워크 트래픽 제어
- 운영체제의 테스크 스케줄링

우선순위 Queue의 구현

- 배열을 이용한 우선순위 Queue
- 리스트를 이용한 우선순위 Queue

우선순위 Queue의 기본 연산

- 삽입 : enQueue
- 삭제 : deQueue

배열을 이용하여 우선순위 Queue 구현

- 배열을 이용하여 자료 저장
- 원소를 삽입하는 과정에서 우선순위를 비교하여 적절한 위치에 삽입하는 구조
- 가장 앞에 최고 우선순위의 원소가 위치하게 됨

문제점

- 배열을 사용하므로, 삽입이나 삭제 연산이 일어날 때 원소의 재배치가 발생
- 이에 소요되는 시간이나 메모리 낭비가 큼
</aside>

---

## Queue의 활용 - 버퍼(Buffer)

### 버퍼 - Buffer

- 데이터를 한 곳에서 다른 한 곳으로 전송하는 동안 일시적으로 그 데이터를 보관하는 메모리의 영역
- 버퍼링 : 버퍼를 활용하는 방식 또는 버퍼를 채우는 동작을 의미

<aside>
🗒️ 버퍼의 자료 구조

- 버퍼는 일반적으로 입출력 및 네트워크와 관련된 기능에서 이용됨
- 순서대로 입력 / 출력 / 전달되어야 하므로 FIFO 방식의 자료 구조인 Queue가 활용됨
</aside>

<aside>
🗒️ 키보드 버퍼 과정

1. 사용자가 키보드를 입력 (A P S)
2. 입력된 키보드가 버퍼됨 (A P S)
3. 키보드 입력 버퍼에 Enter가 입력되면
4. 프로그램 실행 영역 (S P A를 연산)
</aside>