# 목차
[1. 상속](#상속---Inheritance)  
[2. 클래스 상속](#클래스-상속)  
[3. 다중 상속](#다중-상속)  
[4. 에러와 예외](#Errors--Exception---에러와-예외)  

# Python - OOP2

날짜: 2023년 7월 27일

## 상속 - Inheritance

⇒ 기존 클래스의 속성과 메서드를 물려받아 새로운 하위 클래스를 생성하는 것

<aside>
	
    🗒️ 상속이 필요한 이유

    - 코드 재사용
        - 상속을 통해 기존 클래스의 속성과 메서드를 재사용할 수 있음
        - 새로운 클래스를 작성할 때 기존 클래스의 기능을 그대로 활용할 수 있으며, 중복된 코드를 줄일 수 있음
    - 계층 구조
        - 상속을 통해 클래스들 간의 계층 구조를 형성할 수 있음
        - 부모 클래스와 자식 클래스 간의 관계를 표현하고, 더 구체적인 클래스를 만들 수 있음
    - 유지 보수의 용이성
        - 상속을 통해 기존 클래스의 수정이 필요한 경우, 해당 클래스만 수정하면 되므로 유지 보수가 용이해짐
        - 코드의 일관성을 유지하고, 수정이 필요한 범위를 최소화할 수 있음
</aside>

---

## 클래스 상속

❗상속 없이 구현하는 경우

```python
# 학생/교수 정보를 나타내기 어려움

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def talk(self):
	print(f'반갑습니다. {self.name}입니다.')

s1 = Person('김학생', 23)
s1.talk()
# 반갑습니다. 김학생입니다.

p1 = Person('박교수', 59)
p1.talk()
# 반갑습니다. 박교수입니다.
```

```python
class Professor:
	def __init__(self, name, age, department):
		self.name = name
		self.age = age
		self.department = department

	def talk(self):
	print(f'반갑습니다. {self.name}입니다.')

class Student:
	def __init__(self, name, age, gpa):
		self.name = name
		self.age = age
		self.gpa = gpa

	def talk(self):
	print(f'반갑습니다. {self.name}입니다.')

# 중복되는 코드가 너무 많음 = 낭비
```

```python
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def talk(self):
		print(f'반갑습니다. {self.name}입니다.')

class Professor(Person):
	def __init__(self, name, age, department):
		self.name = name
		self.age = age
		self.department = department

class Student:
	def __init__(self, name, age, gpa):
		self.name = name
		self.age = age
		self.gpa = gpa

p1 = Professor('박교수', 49, '컴퓨터공학과')
s1 = Student('김학생', 20, 3.5)

p1.talk
# 반갑습니다. 박교수입니다.

s1.talk
# 반갑습니다. 김학생입니다.
```

```python
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def talk(self):
		print(f'반갑습니다. {self.name}입니다.')

class Professor(Person):
	def __init__(self, name, age, department):
		Person.__init__(self, name, age)
		self.department = department

class Student:
	def __init__(self, name, age, gpa):
		Person.__init__(self, name, age)
		self.gpa = gpa

p1 = Professor('박교수', 49, '컴퓨터공학과')
s1 = Student('김학생', 20, 3.5)

# 이렇게 사용해도 되지만, 상위 클래스의 이름이 바뀌었을 경우, 수 많은 클래스들에서
# 상위 클래스의 이름을 바꿔줘야한다.
# 여러가지 부모 클래스를 상속할 수 있지만, 순서대로 상속하여 처리되는 특성상,
# 그 수가 많아지면 또 힘들어짐
```

## ⭐super()

⇒ 부모 클래스의 메서드를 호출하기 위해 사용되는 내장 함수

```python
# super() 사용 예시
# 변경 전

class Person:
	def __init__(self, name, age, number, email):
		self.name = name
		self.age = age
		self.number = number
		self.email = email

class Student(Person):
	def __init__(self, name, age, number, email, student_id):
		self.name = name
		self.age = age
		self.number = number
		self.email = email
		self.student_id = student_id

# 변경 후

class Person:
	def __init__(self, name, age, number, email):
		self.name = name
		self.age = age
		self.number = number
		self.email = email

class Student(Person):
	def __init__(self, name, age, number, email, student_id):
		super().__init__(name, age, number, email)
		self.student_id = student_id
```

---

## 다중 상속

- 두 개 이상의 클래스를 상속 받는 경우
- 상속받은 모든 클래스의 요소를 활용 가능함
- 중복된 속성이나 메서드가 있는 경우 상속 순서에 의해 결정됨

```python
a 클래스 - talk()
b 클래스 - talk()
c 클래스 - talk()

d 클래스에서 a, b, c 클래스를 상속 받았을 때, talk()가 중복되는데 이 순서는
상속받는 순서대로 결정된다.
```

```python
# 다중 상속 예시

class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f'안녕, {self.name}'
    

class Mom(Person):
    gene = 'XX'

    def swim(self):
        return '엄마가 수영'
    

class Dad(Person):
    gene = 'XY'

    def walk(self):
        return '아빠가 걷기'
    

class FirstChild(Dad, Mom):
    def swim(self):
        return '첫째가 수영'
    
    def cry(self):
        return '첫째가 응애'
    

baby1 = FirstChild('아가')
print(baby1.cry())
# 첫째가 응애
print(baby1.swim())
# 첫째가 수영
print(baby1.walk())
# 아빠가 걷기
print(baby1.gene)
# XY -> Dad 클래스를 먼저 상속했기 때문에 Dad의 gene 값을 가져온다
print(baby1.greeting())
# 안녕, 아가
```

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f'안녕, {self.name}'
    

class Mom(Person):
    gene = 'XX'

    def __init__(self, name):
        super().__init__(name)

    def swim(self):
        return '엄마가 수영'
    

class Dad(Person):
    gene = 'XY'

    def __init__(self, name):
        super().__init__(name)

    def walk(self):
        return '아빠가 걷기'
    

class FirstChild(Dad, Mom):        
    mom_gene = Mom.gene  # 엄마의 유전자를 사용하고 싶지만 상속 순서는 바꿀 수 없을 때, 엄마의 유전자를 가져와 할당한다.
	
    def __init__(self, name):
        super().__init__(name)
        
    def swim(self):
        return '첫째가 수영'    
        
    def cry(self):
        return '첫째가 응애'
    

baby1 = FirstChild('아가')
print(baby1.cry())  # 첫째가 응애
print(baby1.swim())  # 첫째가 수영
print(baby1.walk())  # 아빠가 걷기
print(baby1.gene)  # XY -> Dad 클래스를 먼저 상속했기 때문에 Dad의 gene 값을 가져옵니다
print(baby1.greeting())  # 안녕, 아가
```

## 상속 관련 함수와 메서드

- mro()
    - Method Resolution Order
    - 해당 인스턴스의 클래스가 어떤 부모 클래스를 가지는지 확인하는 메서드
    - 기존의 인스턴스 → 클래스 순으로 이름 공간을 탐색하는 과정에서 상속 관계에 있으면 인스턴스 → 자식 클래스 → 부모 클래스로 확장

```python
print(FirstChild.mro())
# [<class '__main__.FirstChild'>, <class '__main__.Dad'>, <class '__main__.Mom'>, <class '__main__.Person'>, <class 'object'>]
# 참조되는 순서대로 나타남
```

---

## Errors & Exception - 에러와 예외

- 버그 : 소프트웨어에서 발생하는 오류 또는 결함, 프로그램의 예상된 동작과 실제 동작 사이의 불일치

### Debugging

⇒ 소프트웨어에서 발생하는 버그를 찾아내고 수정하는 과정, 프로그램의 오작동 원인을 식별하여 수정하는 작업

<aside>
	
    🗒️ 디버깅 방법

    - print 함수 활용
    - 개발 환경(text editor, IDE) 등에서 제공하는 기능 활용
    - Python tutor 활용
    - 뇌 컴파일, 눈 디버깅 등
</aside>

### Error - 에러

⇒ 프로그램 실행 중에 발생하는 예외 상황

- 문법 에러 - Syntax Error
    - 프로그램의 구문이 올바르지 않은 경우 발생
    - 오타, 괄호 및 콜론 누락 등의 문법적 오류

### Exception - 예외

⇒ 프로그램 실행 중에 감지되는 에러

- 내장 예외 - Built-in Exception
    - 예외 상황을 나타내는 예외 클래스들 ( 파이썬에서 이미 정의되어 있으며, 특정 예외 상황에 대한 처리를 위해 사용)
    - ZeroDivisionError : 나누기 또는 모듈로 연산의 두 번째 인자가 0일 때 발생
    - NameError : 지역 또는 전역 이름을 찾을 수 없을 때 발생
    - TypeError
        - 타입 불일치
        - 인자 누락
        - 인자초과
        - 인자 타입 불일치
    - ValueError : 연산이나 함수에 문제가 없지만 부적절한 값을 가진 인자를 받았고, 상황이 IndexError 처럼 더 구체적인 예외로 설명되지 않은 경우 발생
    - IndexError : 시퀀스 인덱스가 범위를 벗어날 때 발생
    - KeyError : 딕셔너리에 해당 키가 존재하지 않는 경우
    - ModuleNotFoundError : 모듈을 찾을 수 없을 때 발생
    - ImportError : 임포트 하려는 이름을 찾을 수 없을 때 발생
    - KeyboardInterrupt : 사용자가 Ctrl-c 또는 Del를 누를 때 발생
    - IndentationError : 잘못된 들여쓰기와 관련된 문법 오류

### 예외처리

<aside>
	
    🗒️ try와 except 절을 사용하여 예외 처리

    - try 블록 안에는 예외가 발생할 수 있는 코드를 작성
    - except 블록 안에는 예외가 발생했을 때 처리할 코드를 작성
    - 예외가 발생하면 프로그램 흐름은 try 블록을 빠져나와 해당 예외에 대응하는 except 블록으로 이동
</aside>

```python
# 예외 처리 예시
try:
	result = 10 / 0
except ZeroDivisionError:
	print('0으로 나눌 수 없습니다.')

---

try:
	num = int(input('숫자입력 : '))
except ValueError:
	print('숫자가 아닙니다.')
"""
숫자입력 : a
숫자가 아닙니다.
"""
```

```python
# 복수 예외 처리 연습
# 100을 사용자가 입력한 값으로 나누고 출력하는 코드를 작성해보시오.
try:
    num = int(input('100으로 나눌 값을 입력해 : '))
    print(100 / num)
except ValueError:
    print('숫자를 입력하라고')
except ZeroDivisionError:
    print('왜 0을 입력하는거야??????')
except:
    print('에러가 발생했어')
```

<aside>
	
    ❗ 내장 예외의 상속 계층구조 주의
    내장 예외 함수가 계층구조로 인해 하위 개념의 예외 함수가 뒤에 나올 경우, 상위 개념이 먼저 진행되고 이 후의 하위 개념에는 도달하지 못한다.

</aside>

따라서 내장 예외 클래스는 상속 계층구조를 가지기 때문에 except 절로 분기 시 반드시 하위 클래스를 먼저 확인 할 수 있도록 작성해야 함

---

## EAFP - Easier to Ask for Forgiveness than Permission

⇒ 예외처리를 중심으로 코드를 작성하는 접근 방식 ( try - except )

## LBYL - Lool Before You Leap

⇒ 값 검사를 중심으로 코드를 작성하는 접근 방식 ( if - else )

```python
# 접근 방식 비교
#EAFP
try:
    result = my_dict['key']
    print(result)
except KeyError:
    print('Key가 존재하지 않습니다.')

#LBYL
if 'key' in my_dict:
    result = my_dict['key']
    print(result)
else:
    print('key가 존재하지 않습니다.')

# 나오는 결과 값은 동일함
# 파이썬에서는 EAFP를 추천하지만 그 이유는 명시하지 않았고,
# 인터넷 대부분의 코드에서는 LBYL의 형태로 이루어져 있음
```

| EAFP | LBYL |
| --- | --- |
| 일단 실행하고 예외를 처리 | 실행하기 전에 조건을 검사 |
| 코드를 실행하고 예외가 발생하면 예외처리를 수행 | 코드 실행 전에 조건문 등을 사용하여 예외 상황을 미리 검사하고, 예외 상황을 피하는 방식 |
| 코드에서 예외가 발생할 수 있는 부분을 미리 예측하여 대비하는 것이 아니라, 예외가 발생한 후에 예외를 처리 | 코드가 좀 더 예측 가능한 동작을 하지만, 코드가 더 길고 복잡해질 수 있음 |
| 예외 상황을 예측하기 어려운 경우에 유용 | 예외 상황을 미리 방지하고 싶을 때 유용 |

---

## as 키워드

⇒ as 키워드를 활용하여 에러 메시지를 except 블록에서 사용할 수 있음

```python
my_list = []

try:
    number = my_list[1]
except IndexError as error:
    print(f'{error}가 발생했습니다.')

# list index out of range가 발생했습니다.
```

파이썬 자습서 ~9.5.1까지 코드 한 번씩 쳐보면서 공부하기

무리하지말고 조금씩 하다보면 뭐 어떻게든 되겠지
