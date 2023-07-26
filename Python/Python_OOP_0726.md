# 목차
[1. 절차 지향 프로그래밍](#절차-지향-프로그래밍---procedural-Programming)  
[2. 객체 지향 프로그래밍](#객체-지향-프로그래밍---Object-Oriented-Programming)  
[3. 객체](#객체)  
[4. 클래스](#클래스)  
[5. Method](#메서드)  
# Python - OOP

날짜: 2023년 7월 26일

## 절차 지향 프로그래밍 - procedural Programming

⇒ 프로그램을 ‘데이터’와 ‘절차’로 구성하는 방식의 프로그래밍 패러다임

<aside>
	
    🗒️ 절차 지향 프로그래밍의 특징

    - “데이터”와 해당 데이터를 처리하는 “함수(절차)”가 분리되어 있으며, 함수 호출의 흐름이 중요
    - 코드의 순차적인 흐름과 함수 호출에 의해 프로그램이 진행
    - 실제로 실행되는 내용이 무엇이 무엇인가가 중요
    - 데이터를 다시 재사용하거나 하기보다는 처음부터 끝까지 실행되는 결과물이 중요한 방식
</aside>

### 소프트웨어 위기 - Software Crisis

⇒ 하드웨어의 발전으로 컴퓨터 계산용량과 문제의 복잡성이 급격히 증가함에 따라 소프트웨어에 발생한 충격

---

## 객체 지향 프로그래밍 - Object Oriented Programming

⇒ 데이터와 해당 데이터를 조작하는 메서드를 하나의 객체로 묶어 관리하는 방식의 프로그래밍 패러다임

**[절차 지향 vs 객체 지향][그림]**

<aside>
	
    🗒️ 절차 지향 : 함수가 데이터를 받아서 ~~
    객체 지향 : 데이터(객체)가 메서드를 들고와서~~ ex)데이터가 ~~를 한다

</aside>

---

## 객체

### 클래스 - Class

⇒ 파이썬에서 타입을 표현하는 방법

<aside>
	
    🗒️ 객체를 생성하기 위한 설계도
    데이터와 기능을 함께 묶는 방법을 제공

</aside>

### 객체 - Object

⇒ 클래스에서 정의한 것을 토대로 메모리에 할당된 것. ‘속성’과 ‘행동’으로 구성된 모든 것

![Untitled](https://github.com/hluuy/TIL/assets/103430344/aae9faa5-1a71-4f73-8f46-6777c689d41e)


가수 = 클래스 / 아이유, BTS,,, = 객체

- 클래스로 만든 객체를 인스턴스 라고도 함

<aside>

    - 아이유는 객체다 ( ⭕ )
    - 아이유는 인스턴스다 ( ❌ )
    - 아이유는 가수의 인스턴스다 ( ⭕ )
</aside>

```python
name = 'Alice'

print(type(name))
# <class 'str'>
```

<aside>
	
    🗒️ 변수 name의 타입은 str 클래스다.

    - 변수 name은 str 클래스의 인스턴스이다.
    - 우리가 사용해왔던 데이터 타입은 사실 모두 클래스였다.
</aside>

⭐ 문자열 타입의 변수는 str 클래스로 만든 인스턴스다.

```python
'', 'hello', '파이썬'
-> 문자열 타입(클래스)의 객체(인스턴스)

[1, 2, 3], [1], [], ['hi']
-> 리스트 타입(클래스)의 객체(인스턴스)
```

```python
"hello".upper()
문자열.대문자로()
객체.행동()

---

[1, 2, 3].sort()
리스트.정렬해()
객체.행동()
```

<aside>
	
    ⭐ 인스턴스.메서드()

</aside>

⇒ 하나의 객체(Object)는 특정 타입의 인스턴스(instance)이다.

<aside>
	
    🗒️ 객체의 특징

    - 타입(type) : 어떤 연산자(operator)와 조작(method)이 가능한가?
    - 속성(attribute) : 어떤 상태(데이터)를 가지는가?
    - 조작법(method) : 어떤 행위(함수)를 할 수 있는가?
</aside>

---

## 클래스

```python
# 클래스 정의
class Person:
	pass

# 인스턴스 생성
IU = Person()

# 메서드 호출
IU.메서드()

# 속성(변수) 접근
IU.attribute
```

```python
# 클래스 정의
class Person:
	# 속성(변수)
	blood_color = 'red'

	# 메서드, __ㅁㄴㅇ__ => 개발자가 직접 호출하지 않고 자동으로 실행되기 때문에 우리가 신경 쓸 게 아님
	def __init__(self, name):
		self.name = name

	def singing(self):
		return f'{self.name}가 노래합니다'

# 인스턴스 생성, 인자가 하나 필요하다
singer1 = Person('IU')
singer2 = Person('BTS')

# 메서드 호출
print(singer1.singing())
# IU가 노래합니다.
print(singer2.singing())
# BTS가 노래합니다.

# 속성(변수)
print(singer1.blood_color)
print(singer2.blood_color)
# red
# red
```

### 클래스 기본 활용

- 생성자 함수
    - 객체를 생성할 때 자동으로 호출되는 특별한 메서드
    - __init__이라는 이름의 메서드로 정의되며, 객체의 초기화를 담당
    - 생성자 함수를 통해 인스턴스를 생성하고 필요한 초기 값을 설정
- 인스턴스 변수
    - 인스턴스(객체)마다 별도로 유지되는 변수
    - 인스턴스마다 독립적인 값을 가지며, 인스턴스가 생성될 때마다 초기화 됨
- 클래스 변수
    - 클래스 내부에 선언된 변수
    - 클래스로 생성된 모든 인스턴스들이 공유하는 변수
- 인스턴스 메서드
    - 각각의 인스턴스에서 호출할 수 있는 메서드
    - 인스턴스 변수에 접근하고 수정하는 등의 작업을 수행

<aside>
	
    🗒️ 인스턴스와 클래스 간의 이름 공간(namespace)

    - 클래스를 정의하면, 클래스와 해당하는 이름 공간 생성
    - 인스턴스를 만들면, 인스턴스 객체가 생성되고 독립적인 이름 공간 생성
    - 인스턴스에서 특정 속성에 접근하면, 인스턴스 → 클래스 순으로 탐색
</aside>

```python
# Person 정의
class Person:
	name = 'unknown'

	# 인스턴스 메서드
	def talk(self):
		print(self.name)

p1 = Person()
p1.talk
# unknown

# p2 인스턴스 변수 설정 전/후
p2 = Person()
p2.talk()
# unknown
p2.name = 'Kim'
p2.talk()
# Kim

# 클래스 변수와 인스턴스 변수는 별개임으로 클래스에 변수가 선언되지 않아도 
# 인스턴스 단독 변수로 선언하여 사용 가능하다.
# 단 인스턴스 변수에 행동 함수는 만들 수 없다.
```

<aside>
	
    🗒️ 독립적인 이름 공간을 가지는 이점

    - 각 인스턴스는 독립적인 메모리 공간을 가지며, 클래스와 다른 인스턴스 간에는 서로의 데이터나 상태에 직접적인 접근이 불가능
    - 객체 지향 프로그래밍의 중요한 특성 중 하나로, 클래스와 인스턴스를 모듈화하고 각각의 객체가 독립적으로 동작하도록 보장
    - 이를 통해 클래스와 인스턴스는 다른 객체들과의 상호작용에서 서로 충돌이나 영향을 주지 않으면서 독립적으로 동작할 수 있음
    - 코드의 가독성, 유지보수성, 재사용성을 높이는데 도움을 줌
</aside>

---

## 클래스 변수 활용

⇒ 가수가 몇 명인지 확인하고 싶다면?

```python
class Person:
	count = 0
	
	def __init__(self, name):
	self.name = name
	Person.count += 1

person1 = Person('IU')
person2 = Person('BTS')

print(Person.count)
# 2

---

class Circle():
	pi = 3.14

	def __init__(self, r):
		self.r = r  # -> r은 인스턴스 변수(원마다 값이 다름)

c1 = Circle(5)
c2 - Circle(10)

print(Circle.pi)
# 3.14
print(c1.pi)
# 3.14
print(c2.pi)
# 3.14
---
Circle.pi = 5 # 클래스 변수 변경
print(Circle.pi)
# 5
print(c1.pi)
# 5
print(c2.pi)
# 5
---
c2.pi = 5 # 인스턴스 변수 변경
print(Circle.pi)
# 3.14
print(c1.pi)
# 3.14
print(c2.pi)
# 5
```

---

## 메서드

⇒ 행동의 역할

- 인스턴스 메서드 → 인스턴스가 사용하는 메서드
- 클래스 메서드 → 클래스가 사용하는 메서드
- 정적 메서드

### 인스턴스 메서드

⇒ 클래스로부터 생성된 각 인스턴스에서 호출할 수 있는 메서드

→ 인스턴스의 상태를 조작하거나 동작을 수행

<aside>
	
    🗒️ 인스턴스 메서드 구조

    - 클래스 내부에 정의되는 메서드의 기본
    - 반드시 첫 번째 매게변수로 인스턴스 자신(self)을 전달받음
</aside>

```python
class MyClass:
	
	def instance_method(self, arg1, ...): # -> 첫 번째 인자명을 아무렇게 설정해도 되지만, self로 고정
		pass
```

```python
# 인스턴스.메서드()
'abc'.upper()

# 클래스.메서드(인스턴스 자기자신)
str.upper('abc')
# -> self가 정의되지 않으면 돌아가지 않는다.
```

<aside>
	
    🗒️ self 동작 원리

    - upper 메서드를 사용해 문자열 ‘hello’를 대문자로 변경하기
        - ‘hello’.upper()
    - 하지만 실제 파이썬 내부 동작은 다음과 같이 이루어짐
        - str.upper(’hello’)
    - str 클래스가 upper 메서드를 호출했고, 그 첫번째 인자로 문자열 인스턴스가 들어간 것

⇒ 인스턴스 메서드의 첫 번째 매개변수가 반드시 인스턴스 자기 자신인 이유

</aside>

### 생성자 메서드 - constructor method

⇒ 인스턴스 객체가 생성될 때 자동으로 호출되는 메서드, 인스턴스 변수들의 초기값을 설정

```python
class Person:
	
	def __init__(self):
		print('인스턴스가 생성되었습니다.')

person1 = Person()
# 인스턴스가 생성되었습니다.
```

### 클래스 메서드 - class method

⇒ 클래스가 호출하는 메서드, 클래스 변수를 조작하거나 클래스 레벨의 동작을 수행

```python
# 클래스 메서드 구조
class MyClass:
	
	@classmethod # -> @classmethod 데코레이터를 사용하여 정의
	def class_method(cls, arg1, ...): # -> 첫 번째 인자는 cls로 설정하여 전달됨
		pass
```

```python
# 클래스 메서드 예시
class Person:
	count = 0

	def __init__(self, name):
		self.name = name
		Person.sount += 1

	@classmethod
	def number_of_population(cls):
		print(f'인구수는 {cls.count}입니다.')

person1 = Person('IU')
person2 = Person('BTS')

Person.number_of_population
# 인구 수는 2입니다.
```

### 스태틱 (정적) 메서드 - static method

⇒ 클래스와 인스턴스와 상관없이 독립적으로 동작하는 메서드

→ 주로 클래스와 관련이 있지만 인스턴스와 상호작용이 필요하지 않은 경우에 사용

```python
class MyClass:

	@staticmethod
	def static_method(arg1, ...): # -> 호출 시 필수적으로 작성해야 할 매개변수가 없음
		pass
```

<aside>
	
    🗒️ 메서드 정리

    - 인스턴스 메서드
        - 인스턴스의 상태를 변경하거나, 해당 인스턴스의 특정 동작을 수행
    - 클래스 메서드
        - 인스턴스의 상태에 의존하지 않는 기능을 정의
        - 클래스 변수를 조작하거나 클래스 레벨의 동작을 수행
    - 스태틱 메서드
        - 클래스 및 인스턴스와 관련이 없는 일반적인 기능을 수행
</aside>

<aside>
	
    🗒️ 각자의 역할

    - 클래스가 사용해야 할 것
        - 클래스 메서드
        - 스태틱 메서드
    - 인스턴스가 사용해야 할 것
        - 인스턴스 메서드
</aside>

```python
#메서드 정리 예시
class Myclass:

	def instance_method(self):
		return 'instance method', self

	@calssmethod
	def class_method(cls):
		return 'class method', cls

	@staticmethod
	def static_method():
		return 'static method'
```

<aside>
	
    🗒️ 클래스가 할 수 있는 것

    - 클래스는 모든 메서드를 호출 할 수 있음

    ❗ 하지만 클래스는 클래스 메서드와 스태틱 메서드만 사용하도록 한다

</aside>

<aside>
	
    🗒️ 인스턴스가 할 수 있는 것

    - 인스턴스는 모든 메서드를 호출 할 수 있음

    ❗ 하지만 인스턴스는 인스턴스 메서드만 사용하도록 한다

</aside>

<aside>
	
    🗒️ **할 수 있다 ≠ 써도 된다**
    각자의 메서드는 OOP 패러다임에 따라 명확한 목적에 따라 설계된 것이기 떄문에 클래스와 인스턴스 각각 올바른 메서드만 사용하도록 해야 한다.

</aside>

## 절차 지향과 객체 지향은 대조되는 개념이 아니다

⇒ 객체 지향은 기존 절차 지향을 기반으로 두고 보완하기 위해 객체라는 개념을 도입해 상속, 코드 재사용성, 유지보수성 등의 이점을 가지는 패러다임
