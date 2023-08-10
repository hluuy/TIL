# Algorithm - APS 기본 LIST 2 Part.1

날짜: 2023년 8월 2일

## 2차원 배열

- 1차원 List를 묶어놓은 List
- 2차원 이상의 다차원 List는 차원에 따라 index를 선언
- 2차원 List의 선언 : 세로 길이(행의 개수), 가로 길이(열의 개수)를 필요로 함
- Python에서는 데이터 초기화를 통해 변수 선언과 초기화가 가능

<aside>
🗒️ 2차원 배열
arr = [[0, 1, 2, 3], [4, 5, 6, 7]]

| 0 | 1 | 2 | 3 |
| --- | --- | --- | --- |
| 4 | 5 | 6 | 7 |

→ List arr

</aside>

```python
#[참고]
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)
# 3
# 1 2 3
# 4 5 6
# 7 8 9
N = int(input())
arr = [list(map(int, input())) for _ in range(N)
# 3
# 123
# 456
# 789
```

### 배열 순회

⇒ n * m 배열에서의 n*m 개의 모든 원소를 빠짐없이 조사하는 방법

```python
# i 행의 좌표
# j 열의 좌표

# 행 우선 순회
max_v = 0
for i in range(n):
		S = 0
		for j in range(m):
				f(Array[i][j]) # 필요한 연산 수행
		if max_v < S:
				max_v = S

# 열 우선 순회
for j in range(m):
		for i in range(n):
				f(Array[i][j]) # 필요한 연산 수행

# 지그재그 순회
for i in range(n):
		for j in range(m):
				f(Array[i][j + (m - 1 - 2 * j) * ( i % 2 )]) # 홀수일 때만 동작하도록
# A[i][m - 1 - j] / - j = j - 2j 
```

### 델타를 이용한 2차 배열 탐색

⇒ 2차 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법

```python

```

|  | j - 1 | j | j + 1 |
| --- | --- | --- | --- |
| i - 1 |  |  |  |
| i |  | [i][j] |  |
| i + 1 |  |  |  |