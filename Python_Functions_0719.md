# Python - Functions

날짜: 2023년 7월 19일

## 🌟함수 - Function
⇒ 특정 작업을 수행하기 위한 재사용 가능한 코드 묶음

- 재사용성이 높아지고, 코드의 가독성과 유지 보수성 향상

---

## 내장함수 - Built-in function

- Python이 기본적으로 제공하는 함수
- 별도의 import없이 사용 가능
- [Python Documentation](https://docs.python.org/3/library/functions.html?highlight=built) 에서 확인 가능

### 함수호출 - function call

- function_name(argument)
- 함수를 실행하기 위해 함수의 이름을 사용하여 해당 함수의 코드 블럭을 실행

---

## 함수의 구조

```python
def make_sum(parm1, parm2):     ->   input = parameter
"""이것은 두 수를 받아
두 수의 합을 반환하는 함수입니다.

>>> make_sum(1, 2)              ->   Docstring / function Body
3
"""
return pram1 + pram2            ->   output = return value
```

### 함수의 정의와 호출

- def 키워드로 시작

<aside>

    🗒️ def 함수 이름 ( 매개변수) :

</aside>

- 이후 들여쓰기 된 코드 블록 = 함수 body
- 필요한 경우 return을 통해 반환할 값 명시
- 함수의 이름과 인자를 전달해야 함수를 호출할 수 있음

```python
def greet(name):  #함수 정의
	message = 'Hello' + name
	return message    #return이 없다면 None이 자동으로 리턴됨

result = greet("Alice")  #함수 호출
print(result)
```

<aside>

    ❗ 함수가 나왔을 때, 함수 호출문부터 확인하자

</aside>


---

## 매개변수와 인자

- 매개변수 - Parameter : 함수를 정의할 때
- 인자 - Argument : 함수를 호출할 때
    
    ⇒ 둘은 위치 상 동일한 위치에 존재한다
    
    ```python
    def add_numbers(x, y):  #x와 y는 매개변수
    	result = x + y
    	return result
    
    a = 2
    b = 3
    sum_result = add_numbers(a, b)  #a와 b는 인자
    print(sum_result)
    ```
    

---

## 인자의 종류

- 위치인자 - Positional Arguments
    - 함수 호출 시 인자의 위치에 따라 전달되는 인자
    - 함수 호출 시 반드시 값을 전달해야함
    
    ```python
    def greet(name, age):
    	print(f'안녕하세요, {name}님! {age}살 이시군요.')
    
    greet('Alice', 25) -> 안녕하세요, Alice님! 25살 이시군요.
    ```
    

- 기본 인자 값 - Default Arguments Values
    - 함수 정의에서 매개변수에 기본 값을 할당하는 것
    - 호출 시 인자를 전달하지 않으면 기본 값이 매개변수에 할당
    
    ```python
    def greet(name, age = 30):
    	print(f'안녕하세요, {name}님! {age}살이시군요.')
    
    greet('Bob')  ->  안녕하세요, Bob님! 30살이시군요.
    greet('Charlie', 40)  -> 안녕하세요, Charlie님! 40살이시군요.
    ```
    
- 키워드 인자 - Keyword Arguments
    - 함수 호출 시 인자의 이름과 함께 값을 전달하는 인자
    - 매개변수와 인자를 일치 시키지 않고, 특정 매개변수에 값을 할당할 수 있음
    - 인자의 순서는 중요하지 않으며 인자의 이름을 명시하여 전달
    - 단, 호출 시 키워드 인자는 위치 인자 뒤에 위치해야 함
    
    ```python
    def greet(name, age):
    	print(f'안녕하세요, {name}님! {age}살이시군요.')
    
    greet(name='Dave', age = 35)  ->  안녕하세요, Dave님! 35살이시군요.
    greet(age = 35, 'Dave')  ->  error
    greet(age = 35, name = 'Dave')  ->  안녕하세요, Dave님! 35살이시군요.
    greet(35, 'Dave')  ->  안녕하세요, 35님! Dave살이시군요.
    ```
    
- 임의의 인자 목록 - Arbitrary Argument Lists
    - 정해지지 않은 개수의 인자를 처리하는 인자
    → 몇 개를 입력 받을지 몰라 메모리 낭비가 있을 수 있음
    - 함수 정의 시 매개변수 앞에 ‘ * ‘를 붙여 사용하며, 여러 개의 인자를 tuple로 처리
    
    ```python
    def calculate_sum(*arg):
    	print(args)
    	total = sum(args)
    	print(f'합계: {total}'}
    
    """
    (1, 2, 3)
    합계: 6
    """
    calculate_sum(1, 2, 3)
    ```
    
- 임의의 키워드 인자 목록 - Arbitrary Keyword Argument Lists
    - 정해지지 않은 개수의 키워드 인자를 처리하는 인자
    - 함수 정의 시, 매개변수 앞에 ‘ ** ‘를 붙여 사용
    - 여러 개의 인자로 dictionary로 묶어 처리
    
    ```python
    def calc_sum(**kwargs)
    	print(kwargs)
    
    print_info(name='Eve', age = 30)  ->  {'name': 'Eve', 'age': 30}
    ```
    

### 함수 인자 권장 작성순서

- 위치 → 기본 → 가변 → 키워드 → 가변 키워드 순으로 작성
- 단, 모든 상황에 적용되는 것은 아니며, 상황에 따라 달라질 수 있음

---

## 🌟함수와 Scope

⇒ 함수는 코드 내부에 local scope를 생성하며, 그 외의 공간인 global scope로 구분

- global scope : 코드 어디서든 참조할 수 있는 공간
- local scope : 함수가 만든 scope ( 함수 내에서만 참조 가능 )

```python
def func( ):
	num = 20
	print('local', num)  ->  local 20

func( )

print('global', num)  ->  error
=> global scope엔 num이 없기에 사용할 수 없다
```

### 변수 수명주기(Lifecycle)

- built-in scope
    - Python이 실행된 이후부터 영원히 유지
- global scope
    - 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
- local scope
    - 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지

### 이름 검색 규칙 - Name Resolution

- Python에서 사용되는 이름들은 특정한 이름 공간에 저장되어 있음
- LEBG Rule
    
    <aside>

        🗒️ Local scope : 지역 범위
        
        Enclosed scope : 지역 범위 한 단계 위의 범위
        
        Global scope : 최상단에 위치한 범위
        
        Built-in scope : 모든 것을 담고 있는 범위 ( 정의하지 않아도 접근 가능 )
        
        함수 내에서는 바깥 scope의 변수에 접근 가능하나 수정은 불가
        
        ❗작은 곳(안 쪽)에서부터 찾을 때까지 큰 곳(바깥)으로 찾아나감
    
    </aside>
    
    ```python
    print(sum[1, 2, 3])  ->  6
    
    sum = 10
    print(sum)  ->  10
    print(sum([1, 2, 3])  ->  error
    			=> 10([1, 2, 3])과 같음
    
    ---
    
    print(sum)  ->  built-in ~~~~
    a = 1
    sum = 10
    print(sum)  ->  10
    
    def test():
    	sum = 11
    	print(sum)  ->  11
    	print(a)  ->  1
    test()
    ```
    

![scope 순서도.png](Python%20-%20Functions%2022dd188e1d1c471eb6f64caf5796ad33/scope_%25EC%2588%259C%25EC%2584%259C%25EB%258F%2584.png)

### ‘global’ 키워드

- 변수의 scope를 전역 범위로 지정하기 위해 사용
- 일반적으로 함수 내에서 전역 변수를 수정하려는 경우에 사용

![global 키워드.png](Python%20-%20Functions%2022dd188e1d1c471eb6f64caf5796ad33/global_%25ED%2582%25A4%25EC%259B%258C%25EB%2593%259C.png)

- global 키워드는 가급적 사용하지 않는 것을 권장

---

## 🌟재귀 함수

⇒ 함수 내부에서 자기 자신을 호출하는 함수

- 특정 알고리즘 식을 표현할 때 변수의 사용이 줄어들며, 가독성 상승
- 1개 이상의 base case가 존재하고, 수렴하도록 작성
    
    ⇒ 끝나는 상황을 만들어주지 않으면 무한 루프 생성
    
    ```python
    #팩토리얼
    def factorial(n):
    	if n == 0:
    		return 1  ->  종료 조건
    	return n * factorial(n - 1)  ->  재귀 호출
    							=> 상위 폴더로 올라가는 것처럼 계속 대체되며 역으로 올라감
    
    result = factorial(5)
    print(result)  ->  120
    ```
    
    <aside>

        🗒️ 종료 조건을 명확하게
        반복되는 호출이 종료 조건을 향하도록
    
    </aside>
    

---

## 유용한 내장 함수

### map(function, iterable)

⇒ 순회 가능한 데이터 구조(iterable)의 모든 요소에 함수를 적용하고, 그 결과를 map object로 반환

```python
numbers = [1, 2, 3]
result = map(str, numbers)

print(result)  ->  <map object at 0x00000239C915D760>
print(list(result))  ->  ['1', '2', '3']
```

### zip(*iterable)

⇒ 임의의 iterable을 모아 tuple을 원소로 하는 zip object를 반환

```python
girls = ['jane', 'kate']
boys = ['peter', 'jin']
pair = zip(girls, boys)

print(pair)  ->  <zip object at 0x000001C76DE58700>
print(list(pair))  ->  [('jane', 'peter'), ('kate', 'jin')]

---

names = ['Alice', 'Bob', 'Charile']
ages = [30, 25, 35]
cities = ['New York', 'London', 'Paris']

for name, age city in zip(names, ages, cities):
	print(name, age, city)  ->  Alice 30 New York Bob 25 London Charile 35 Paris

---

keys = ['a', 'b', 'c']
values = [1, 2, 3]
my_dict = dict(zip(keys, values))
print(my_dict)  ->  {'a': 1, 'b': 2, 'c': 3}
```

---

## Lambda 함수

⇒ 이름 없이 정의되고 사용되는 익명 함수

- lambda 매개변수: 표현식
- 간단한 연산이나 함수를 한 줄로 표현할 때
- 함수를 매개변수로 전달하는 경우에도 유용하게 활용

```python
def addition(x, y):
	return x + y

result = addition(3, 5)
print(result)  ->  8

=

addition = lambda x, y: x + y

result = addition(3, 5)
print(result)  ->  8

---

numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x : x * 2, numbers))
print(result)  ->  [2, 4, 6, 8, 10]
```

---

## 패킹 - Packing

⇒ 여러 개의 값을 하나의 변수에 묶어서 담는 것

- 변수에 담긴 값들은 tuple 형태로 묶임

```python
packed_values = 1, 2, 3, 4, 5
print(packed_values)  ->  (1, 2, 3, 4, 5)

---

numbers = [1, 2, 3, 4, 5]
a, *b, c = numbers

print(a)  ->  1
print(b)  ->  [2, 3, 4]
print(c)  ->  5
```

---

## 언패킹 - Unpacking

⇒ 패킹된 변수의 값을 개별적인 변수로 분리하여 할당하는 것

- tuple이나 list 등의 객체의 요소들을 개별 변수에 할당

```python
lst = [1, 2, 3]
a, b, c = lst
print(a)  ->  1
print(b)  ->  2
print(c)  ->  3

---

results = [1, 2, 3]
print(results)  ->  [1, 2, 3]

for result in results :
	print(result. end = " ")  ->  1 2 3

print(*results)  ->  1 2 3

---

def test(a, b, c):
	print(a, b, c)  ->  1 2 3

dic = {'a' : 1, 'b' : 2, 'c' : 3}
test(**dic)
```

---

## 모듈 - Module

⇒ 한 파일로 묶인 변수와 함수의 모음

```python
#Python의 math 모듈
import math
print(math.pi)  ->  3.141592...
print(math.sqrt(4))  ->  2
```

<aside>

    🗒️ import문 필요
    help( )를 통해 모듈에 어떤게 있나 확인 가능
    ’ . (dot)’은 왼쪽 객체에서 오른쪽 이름을 찾으라는 의미
    from절을 활용하여 특정 모듈을 미리 참조하고 어떤 요소를 import할 지 명시
    → from math import * ⇒ math의 모든 요소를 가져 옴 ⇒ 파일이 무거워 짐

</aside>

---

## 패키지 - Package

⇒ 관련된 모듈들을 하나의 폴더에 모아 놓은 것

![패키지 조직도.png](Python%20-%20Functions%2022dd188e1d1c471eb6f64caf5796ad33/%25ED%258C%25A8%25ED%2582%25A4%25EC%25A7%2580_%25EC%25A1%25B0%25EC%25A7%2581%25EB%258F%2584.png)

### pip

⇒ 외부 패키지들을 설치하도록 도와주는 Python의 패키지 관리 시스템

<aside>

    🗒️ 패키지를 왜,,,?
    → 누군가가 만들어 놓은 것을 효율적으로 쓰기 위해
    → 재사용하기 위해

</aside>

### [Python 표준 라이브러리](https://docs.python.org/ko/3/library/index.html)

⇒ Python의 다양한 모듈과 패키지의 모음