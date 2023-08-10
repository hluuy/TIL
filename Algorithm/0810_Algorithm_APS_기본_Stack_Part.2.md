# Algorithm - APS 기본 Stack Part.2

날짜: 2023년 8월 10일

## 동적 계획 - Dynamic Programming

⇒ 그리디 알고리즘과 같이 최적화 문제를 해결하는 알고리즘

⇒ 입력 크기가 작은 부분 문제들을 모두 해결한 후에 그 해들을 이용하여 보다 큰 크기의 부분 문제들을 해결하여, 최종적으로 원래 주어진 입력의 문제를 해결하는 알고리즘

<aside>
    
    🗒️ 피보나치 수 DP 적용
    → 피보나치 수는 부분 문제의 답으로부터 본 문제의 답을 얻을 수 있으므로 최적 부분 구조로 이루어져 있음

    1. 문제를 부분 문제로 분할한다.
        1. Fibo(n) 함수는 Fibo(n-1)과 Fibo(n-2)의 합
        2. Fibo(n-1)은 Fibo(n-2)와 Fibo(n-3)의 합
        3. Fibo(n)은 Fibo(n-1), Fibo(n-2), … , Fibo(1), Fibo(0)의 부분집합으로 나뉨
    2. 부분 문제로 나누는 일을 끝냈으면 가장 작은 부분 문제부터 해를 구함
    3. 결과를 테이블에 저장하고, 테이블에 저장된 부분 문제의 해를 이용하여 상위 문제의 해를 구함
</aside>

```python
def fibo(n):
    f = [0] * (n + 1)
    f[0] = 0
    f[1] = 1
    for i in range(2, n + 1) : # 값의 범위를 알고 있다면 미리 n 값을 지정하여 값을 저장하고
        f[i] = f[i - 1] + f[i - 2] # 가져옴
        
    return f[n]
print(fibo())
```

<aside>
    
    🗒️ DP의 구현 방식

    - recursive 방식 : fib1()
    - iterative 방식  : fib2()
    - memoization을 재귀적 구조에 사용하는 것보다 반복적 구조로 DP를 구현한 것이 성능 면에서 보다 효율적
    - 재귀적 구조는 내부에 시스템 호출 스택을 사용하는 오버헤드가 발생하기 때문
</aside>

---

## 깊이 우선 탐색 - Depth First Search, DFS

- 시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳 까지 깊이 탐색해 가다가 더 이상 갈 곳이 없게 되면, 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아와서 다른 방향의 정점으로 탐색을 계속 반복하여 결국 모든 정점을 방문하는 순회방법
- 가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시 깊이 우선 탐색을 반복해야 하므로 후입선출 구조의 스택 사용
- 재귀나 반복구조로 구현 가능
- 스택에서만 사용하는 게 아님

<aside>
    
    ⭐ DFS 알고리즘

    1. 시작 정점 v를 결정하여 방문함
    2. 정점 v에 인접한 정점 중에서
        1. 방문하지 않은 정점 w가 있으면, 정점 v를 스택에 push하고 정점 w를 방문 그리고 w를 v로 하여 다시 2. 를 반복
        2. 방문하지 않은 정점이 없으면, 탐색의 방향을 바꾸기 위해서 스택을 pop하여 받은 가장 마지막 방문 정점을 v로 하여 다시 2. 를 반복
    3. 스택이 공백이 될 때 까지 2. 를 반복

    ❗빠짐없이, 중복없이

</aside>

<aside>
    
    ❓ DFS 예

    1. 초기 상태 : 배열 visited를 False로 초기화하고, 공백 스택을 생성

![Untitled](https://github.com/hluuy/TIL/assets/103430344/456d79d5-2a9b-4088-8666-16d0554044d9)
    
    
    1. 정점 A를 시작으로 깊이 우선 탐색을 시작 → visited[A] = true
    2. 정점 A에 방문하지 않은 정점 B, C가 있으므로 A를 스택에 push, 인접 정점 B와 C 중에서 오름차순에 따라 B를 선택하여 탐색 → visited[B] = true
    3. B에 방문하지 않은 D, E가 있으므로 B를 스택에 push, 인접한 D, E 중에서 오름차순에 따라 D를 탐색 → visited[D] = true
    4. D에 방문하지 않은 F가 있으므로 D를 push, 인접한 F를 탐색 → visited[F] = true
    5. F에 방문하지 않은 E, G가 있으므로 F를 push, 인접한 E, G 중 오름차순에 따라 E를 탐색 → visited[E] = true
    6. E에 방문하지 않은 C가 있으므로 E를 push, 인접한 C를 탐색 → visited[C] =true
    7. C에 방문하지 않은 인접 정점이 없으므로, 마지막 정점으로 돌아가기 위해 스택을 pop하여 받은 정점 E에 대해 방문하지 않은 인접 정점이 있는지 확인 → pop(stack)

![Untitled 1](https://github.com/hluuy/TIL/assets/103430344/2008e004-86bd-471f-8eb5-2acfc5789476)
    
    
    1. E에 방문하지 않은 인접 정점이 없으므로 다시 스택을 pop하여 F로 돌아가 인접정점이 있는지 확인 → pop(stack)
    2. F에 방문하지 않은 G가 있으므로 F를 push하고, G를 선택하여 탐색 → visited[G] = true
    3. 이후 G에 방문하지 않은 인접정점이 없으므로 pop을 하며 방문하지 않은 정점이 있는지 확인
    4. F → D → B → A ( 스택 상 순서대로 ) pop을 하며 돌아가면서 방문하지 않은 정점이 있는지 확인
    5. A에 도착했을 때, pop을 해야하는데 스택이 공백이므로 깊이 우선 탐색을 종료

![Untitled 2](https://github.com/hluuy/TIL/assets/103430344/8799f246-3829-4bdc-8cc4-42bb3d448d20)


</aside>


    
⚠️연습문제⚠️

![Untitled 3](https://github.com/hluuy/TIL/assets/103430344/47b55282-1d37-4a1d-84b7-6cd95534df0d)


    ```python
    '''
    V E
    v1 w1 v2 w2 ...
    7 8
    1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
    '''
    
    def dfs(n, V, adj_m):
        stack = [] # stack 생성
        visited = [0] * (V + 1) # visited 생성
        visited[n] = 1
        print(n)
        while True:
            for w in range(1, V): # 현재 정점 n에 인접하고 미방문 w 찾기
                if adj_m[n][w] == 1 and visited[w] == 0 : # 현재 정점에 인접해있고 방문하지 않았을 경우
                    stack.append(n) # push(v), v = w
                    n = w
                    print(n) # do(w)
                    visited[n] = 1 # w 방문 표시
                    break # for w, n에 인접인 w c를 찾은 경우
            else:
                if stack :# 스택에 지나온 정점이 남아있으면
                    n = stack.pop() #pop()해서 다시 다른 w를 찾을 n 준비
                else: # 스택이 비어 있으면
                    break # 탐색 끝
        return
    
    V, E = map(int, input().split())  # 1번부터 V번 정점, E개의 간선
    arr = list(map(int, input().split()))
    adj_m = [[0] * (V + 1) for _ in range(V + 1)]
    for i in range(E):
        v1, v2 = arr[i * 2], arr[i * 2 + 1]
        adj_m[v1][v2] = 1
        adj_m[v2][v1] = 1
    
    dfs(1 ,V, adj_m)
    ```

