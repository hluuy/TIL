# Python - Control of flow

날짜: 2023년 7월 20일

## 제어문 - Control Statement

⇒ 조건에 따라 코드 블록을 실행하거나 반복적으로 코드를 실행

---

## 조건문 - Conditional Statement

⇒ 주어진 조건식을 평가하여 해당 조건이 참(True)인 경우에만 코드 실행

<aside>
    
    🗒️ if,  elif,  else

</aside>

- **if statement**

```python
#기본구조
if 표현식 :
	코드블럭
elif 표현식 :
	코드블럭
else:     ->     위의 모든 조건이 false일 때 실행, 조건식이 없음
	코드블럭
```

```python
a = 3

if a > 3 :
	print('3 초과')
else :
	print('3 이하')

print(a)
```

**[예제 순서도 그림]**

```python
#복수 조건문
dust = 35

if dust > 150 :
	print('매우 나쁨')
elif dust > 80 :
	print('나쁨')
elif dust > 30 :
	print('보통')
else :
	print('좋음')

=> 동시에 모든 줄을 실행하여 하나를 찾는 것이 아니라
		위에서부터 하나하나 도장깨기하며 내려오며 맞는 조건을 찾음
```

```python
#중첩 조건문
dust = 480

if dust > 150 :
	print('매우 나쁨')
		if dust > 300 :
				print('위험해요! 나가지 마세요!')
elif dust > 80 :
	print('나쁨')
elif dust > 30 :
	print('보통')
else :
	print('좋음')
```

```python
num = int(input())

if num % 2 == 1 :
	print('홀수입니다.')
else :
	print('짝수입니다.'
```

---

## 반복문 - Loop Statement

⇒ 주어진 코드 블럭을 여러 번 반복해서 실행하는 구문

<aside>
	
	🗒️ 특정 작업을 반복적으로 수행
	주어진 조건이 참일 때 반복

</aside>

### 🌟for

⇒ 임의의 sequence 항목들을 해당 sequence에 들어있는 순서대로 반복

```python
#기본구조
for 변수 in 반복 가능한 객체
```

```python
items = ['apple', 'banana', 'kiwi']

for item in items
	print(item)

#apple
#banana
#kiwi
```

```python
country = 'korea'

for char in country:
	print(char)

#k
#o
#r
#e
#a
```

```python
for i in range(5)
	print(i)

#0
#1
#2
#3
#4
```

### 🌟인덱스로 리스트 순회

```python
numbers = [4, 6, 10, -8, 5]

for i in range(len(numbers)):
	number[i] = number[i] * 2

print(numbers)

-> 문제 풀 때 하나의 리스트만 주어지는 경우가 아니라면 range에 정수를 넣지 않는게 좋음
```

### 중첩 반복문

```python
#중첩 반복문
outers = ['A', 'B']
inners = ['c', 'd']

for outer in outers :
	for inner in inners :  ->  해당 반복이 모두 끝나야지 상위 반복으로 올라감
		print(outer, inner)

# A c / A d / B c / B d
=> 중첩 반복문에서 print가 호출되는 횟수 = len(outers) * len(inners)
```

```python
#중첩 반복문 순회
elements = [['A', 'B'], ['c', 'd']]
for elem in elements :
	print(elem)
#['A', 'B'] / ['c', 'd']
=> 지도 만들 때 주로 사용
---
elements = [['A', 'B'], ['c', 'd']]
for elem in elements :
		for item in elem :
			print(item)
#A / B / c / d
=>리스트 안의 리스트를 순회하고 싶을 경우, 리스트의 수와 for문의 수를 일치시킨다
```

### 🌟while

⇒ 주어진 조건식이 True일 경우(동안) 코드를 반복해서 실행
→ 조건식이 False가 될 때까지 반복

<aside>
	
	❗ 무한 루프에 빠지지 않도록 주의

</aside>

```python
#기본구조
while 조건식 :
	코드블럭
```

```python
a = 0

while a < 3 :
	print(a)
	a += 1

print('끝')
```

### 사용자의 입력에 따른 반복

```python
number = int(input('양의 정수를 입력해주세요 : '))

while number <= 0 :
	if number < 0 :
		print('음수를 입력했습니다.')
	else :
		print('0은 양의 정수가 아닙니다.')

	number = int(input('양의 정수를 입력해주세요 : '))

print('잘했습니다!')
```

<aside>
	
	❗ 반드시 종료 조건이 필요함

</aside>

### 적절한 반복문의 활용

- **for** : 반복 횟수가 명확하게 정해져 있는 경우에 유용
    - str, list, tuple,,,
- **while** : 반복 횟수가 불명확하고 조건에 따라 종료해야 할 때 유용
    - 사용자의 입력을 받아서 특정 조건이 충족될 때까지

---

## 반복제어

- **break** : 반복을 즉시 중지

```python
#break 예시
number = int(input('양의 정수를 입력해주세요 : '))

while number <= 0 :
	if number == -9999 :
		print('프로그램을 종료합니다.')
		break

	if number < 0 :
		print('음수를 입력했습니다.')
	else :
		print('0은 양의 정수가 아닙니다.')

	number = int(input('양의 정수를 입력해주세요 : '))

print('잘했습니다!')
```

```python
#break 예시 2
numbers = [1, 3, 5, 6, 7, 9, 10, 11]
found_even = False

for num in numbers :
	if num % 2 == 0 :
		print('첫 번째 짝수를 찾았습니다 :', num)
		found_even = True
		break

if not found_even :
	print('짝수를 찾지 못했습니다')
```

- **continue** : 다음 반복으로 건너 뜀

<aside>
	
	❗ 현재 반복문의 남은 코드를 건너뛰고 다음 반복으로 넘어감

</aside>

```python
#continue 예시
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
	if num % 2 == 0:
		continue
	print(num)

'''
1
3
5
7
9
'''
```

<aside>
	
	❗ 주의사항
	
	- break 와 continue를 남용하면 코드의 가독성을 저하시킴
	- 특정한 종료 조건을 만들어 break를, if문을 사용해 continue를 대체
</aside>

---

## List Comprehension

⇒ 간결하고 효율적인 리스트 생성 방법

```python
#List Comprehension 기본 구조
[expression for 변수 in iterable]
= list(expression for 변수 in iterable
```

```python
#활용 예시
number = [1, 2, 3, 4, 5]
squared_numbers = []

for num in numbers:
	squared_numbers.append(num**2)

print(squared_numbers)

=

numbers = [1, 2, 3, 4, 5]
squared_numbers = [num**2 for num in numbers]

print(squared_numbers)

---

new_list = []
for i in range(10):
	new_list.append(i)
print(new_list)

=

new_list = [i for i in range(10)]
print(new_list)
```

```python
#if 사용시
[expression for 변수 in iterable if 조건식]
= list(expression for 변수 in iterable if 조건식)

---

for i in range(10):
	if i % 2 == 1:
		new_list.append(i)

= 

new_list = [i for in range(10) if i % 2 == 1]
```
