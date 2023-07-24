# Python - Data Structure

날짜: 2023년 7월 24일

## 데이터 구조 - Data Structure

⇒ 여러 데이터를 효과적으로 사용, 관리하기 위한 구조

### 자료 구조

- 컴퓨터 공학에서는 ‘자료 구조’ 라고 함
- 각 데이터를 효율적인 저장, 관리를 위한 구조를 나눠 놓은 것

## 그래서 오늘은❓

### 데이터 구조 활용

⇒ 문자열, 리스트, 딕셔너리 등 각 데이터 구조의 메서드를 호출하여 다양한 기능을 활용하기

---

## 메서드 - method

⇒ 객체에 속한 함수, 객체의 상태를 조작하거나 동작을 수행

<aside>
  
    🗒️ 메서드 특징

    - 클래스 (class) 내부에 정의되는 함수
    - 클래스는 파이썬에서 ‘타입을 표현하는 방법’

    ⇒ 객체 = 클래스

</aside>

```python
#클래스 확인 법
print(help(list))

#class list(object)  ->  클래스인 것을 확인 할 수 있음
#|  list(iterable=(), /)
#|
#|  Built-in mutable sequence.
#|
#|  If no argument is given, the constructor creates a new empty list.      
#|  The argument must be an iterable if specified.
#|
#|  Methods defined here:
#|  MORE...
# q를 입력하면 다시 명령어를 칠 수 있도록 빠져 나옴
```

```python
#메서드 호출 방법
#데이터 타입 객체.메서드()

#문자열 메서드 예시
print('hello'.capitalize())
#Hello

#리스트 메서드 예시
numbers = [1, 2, 3]
numbers.append(4)

print(numbers)
#[1, 2, 3, 4]
```

---

## 시퀀스 데이터 구조

### Sequence Types

⇒ 여러 개의 값들을 순서대로 나열하여 저장하는 자료형
→ str, list, tuple, range

---

## 문자열

### 조회 / 탐색 및 검증 메서드

- .find(x) : x의 첫 번째 위치를 반환하고 없으면 -1을 반환

```python
print('banana'.find('a'))
# 1
print('banana'.find('z'))
# - 1
```

- .index(x) : x의 첫 번째 위치를 반환하고 없으면 에러 발생

```python
print('banana'.index('z'))
# 값이 있으면 find와 동일하게 작동하지만 값이 없다면
# ValueError : substring not found라는 에러 발생
# => 해당 에러가 전체 코드 중간에 발생한다면 전체 작동이 멈추게 됨
```

- .isupper(x) / .islower(x) : 문자열이 모두 대문자 / 소문자로 이루어져 있는지 확인

```python
string1 = 'HELLO'
string2 = 'Hello'
print(string1.isupper())
# True
print(string2.isupper())
# False
print(string1.islower())
# False
print(string2.islower())
# False
```

- .inalpha(x) : 문자열이 알파벳으로만 이루어져 있는지 확인

```python
string1 = 'Hello'
string2 = '123'
print(string1.isalpha())
# True
print(string2.isalpha())
# False
```

- .istitle(x) : 타이틀 형식의 여부를 확인

```python
string1 = "Hello World"
string2 = "This Is A Title"
string3 = "not Title Case"
string4 = "123 Title"

print(string1.istitle())  
# True
print(string2.istitle())  
# True
print(string3.istitle())  
# False
print(string4.istitle())  
# False
```

### 조작 메서드 (새로운 문자열 반환)

<aside>

  
  🗒️ [EBNF 표기법](https://url.kr/otk5wf)


</aside>

- .replace(old, new[ , count]) : 바꿀 대상 글자를 새로운 글자로 바꿔서 반환

```python
text = 'Hello, World!'
new_text = text.replace('world', 'Python')
print(new_text)
# Hello, Pyhton!
```

- .strip([chars]) : 문자열의 시작과 끝에 있는 공백 혹은 지정한 문자를 제거

```python
text = '   Hello, world!'
new_text = text.strip()
print(new_text)
# 'Hello, world!'
```

- ⭐.split(sep=None, maxsplit = -1) : 지정한 문자를 구분자(기본 값 → sep=None)로 문자열을 분리하여 문자열의 리스트로 변환

```python
text = 'Hello, world!'
words = text.split(',')
print(words)
# ['Hello', 'world!']
```

- ⭐‘separator’.join([iterable)] : iterable 요소들을 원래의 문자열을 구분자로 이용하여 하나의 문자열로 연결

```python
words = ['Hello', 'world!']
text = '-'.join(words)
print(text)
# 'Hello-world!'
```

- 기타등등

```python
text = 'heLLo, woRLD!'
new_text1 = text.capitalize()
new_text2 = text.title()
new_text3 = text.upper()
new_text4 = text.swapcase()

print(new_text1)
# Hello, world!
print(new_text2)
# Hello, World!
print(new_text3)
# HELLO, WORLD!
print(new_text4)
# HELLO, WOrLD!
```

<aside>
  
    🗒️ 메서드는 이어서 사용 가능

</aside>

```python
text = 'hello, woRld!'

new_text = text.swapcase().replace('l', 'z')

print(new_text)
# HEzzo, WOrLD!
```

---

## 리스트

### 값 추가 및 삭제 메서드

- ⭐.append(x) : 리스트 마지막에 항목 x를 추가

```python
numbers = [1, 2, 3]
numbers2 = [4, 5, 6]

numbers.append(numbers2)
print(numbers)
# [1, 2, 3, [4, 5, 6]]

# => 리스트는 값이 복사되는 것이 아닌 본체의 값이 변경됨
```

- ⭐.extend(iterable) : 리스트에 다른 반복 가능한 객체의 모든 항목을 추가

```python
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
print(my_list)
# [1, 2, 3, 4, 5, 6]
```

<aside>
  
    🗒️ append와 extend의 차이

    - append는 리스트 그 자체 그대로 들어감
    - extend는 리스트 안의 값이 들어감
    
</aside>

- .insert(i, x) : 리스트의 지정한 인덱스 i 위치에 항목 x를 삽입

```python
my_list = [1, 2, 3]
my_list.insert(1, 5)
print(my_list)
# [1, 5, 2, 3]
```

- .remove(x) : 리스트에서 첫 번째로 일치하는 항목을 삭제

```python
my_list = [1, 2, 3]
my_list.remove(2)
print(my_list)
# [1, 3]
```

- ⭐.pop(i) : 리스트에서 지정한 인덱스의 항목을 제거하고 반환, i를 작성하지 않을 경우 마지막 항목 제거

```python
my_list = [1, 2, 3, 4, 5]

item1 = my_list.pop()
item2 = my_list.pop(0)

print(item1)
# 5
print(item2)
# 1
print(my_list)
# [2, 3, 4]
```

- .clear() : 리스트의 모든 항목을 삭제

```python
my_list = [1, 2, 3]
my_list.clear()
print(my_list)
# []
```

### 탐색 및 정렬 메서드

- .index(x, start, end) : 리스트에서 첫 번째로 일치하는 항목의 인덱스를 반환

```python
my_list = [1, 2, 3]
index = my_list.index(2)
print(index)
# 1 -> 찾은 값의 인덱스 값을 반환
```

- ⭐.reverse() : 리스트의 순서를 역순으로 변경(값의 순서만 역순, 정렬하는 것이 아님)

```python
my_list = [1, 3, 2, 8, 1, 9]
my_list.reverse()
print(my_list)
# [9, 1, 8, 2, 3, 1]
```

- ⭐.sort() : 원본 리스트를 오름차순으로 정렬

```python
my_list = [3, 2, 1]
my_list.sort()
print(my_list)
# [1, 2, 3] -> 원본이 변경되어 어떠한 값을 반환하는 것이 아님

# 내림차순을 원할 때
my_list.sort(reverse = True)
print(my_list)
# [3, 2, 1]
```

- ⭐.sorted() : 원본 리스트를 복사하여 오름차순으로 정렬 후 반환 ⇒ 함수

```python
numbers = [3, 2, 1]
print(numbers.sort())
# None -> 원본을 바꾸는 것이기 때문에 따로 값이 반환되지 않음
print(numbers)
# [1, 2, 3]

numbers = [3, 2, 1]
print(sorted(numbers))
# [1, 2, 3] 
print(numbers)
# [3, 2, 1]
```

- .count(x) : 리스트에서 항목 x가 등장한 횟수를 반환

```python
my_list = [1, 2, 2, 3, 3, 3]
count = my_list.count(3)
print(count)
# 3
```

---

- .isdecimal() : 문자열이 모두 숫자 문자( 0 ~ 9)로만 이루어져 있어야 True 반환
- .isdigit() : 유니코드 숫자도 인식 ( ①도 인식 )
- .innumeric() : .isdigit()과 유사하지만, 몇 가지 추가적인 유니코드 문자들을 인식

<aside>
  
    🗒️ isdecimal ⊆ isdigit ⊆ isnumeric

</aside>

| isdecimal | isdigit | isnumeric | 예시 |
| --- | --- | --- | --- |
| True | True | True |  |
| False | True | True |  |
| False | False | True |  |
| False | False | False |  |

---

## 내일은,,,

```python
numbers = [1, 2, 3]
#할당
list1 = numbers
#슬라이싱
list2 = numbers[:]

numbers[0] = 100

print(list1)
# [100, 2 ,3]
print(list2)
# [1, 2, 3]
# ->  슬라이싱 한 리스트는 새롭게 할당된 [1, 2, 3]을 가져 온 것이라 값이 변경되지 않음
```
