# 목차
[1. Set](#세트)  
[2. Dictionary](#딕셔너리)  
[3. 얕은 복사와 깊은 복사](#복사)  
# Python - Data Sturcture 2

날짜: 2023년 7월 25일

## 비시퀀스 데이터 구조

---

## 세트

⇒ 고유한 항목들의 정렬되지 않은 컬렉션

- .add(x) : 세트에 x를 추가

```python
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)
# {1, 2, 3, 4}
```

- .clear() : 세트의 모든 항목을 제거

```python
my_set = {1, 2, 3}
my_set.clear()
print(my_set)
# set()
```

- .remove(x) : 세트에서 항목 x를 제거

```python
my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)
# {1, 3}

my_set.remove(10)
print(my_set)
# KeyError
```

- .discard() : 세트 s에서 항목 x를 제거. remove와 달리 에러가 생기지 않음

```python
my_set = {1, 2, 3}
my_set.discard(2)
print(my_set)
# {1, 3}

my_set.discard(10)
# None
```

- .pop() : 세트에서 임의의 요소를 제거하고 반환

<aside>
	
    ❗ 실행할 때마다 다른 요소를 얻는다는 의미에서의 “무작위”가 아니라 “임의”라는 의미에서 “무작위”

</aside>

```python
my_set = {1, 2, 3}
element = my_set.pop()

print(element)
# 1
print(my_set)
# {2, 3}

---
my_set = {1, 2, 3, 9, 100, 4, 87, 39, 10, 52}
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())

=> 정수는 정수 값 자체가 해시 값 => 해시 값이 고정되기 때문에 pop을 하면 항상 동일하게 나타남

---

my_set = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'}
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())

=> 문자열은 실행할 때마다 해시 값이 바뀜 => 항상 변하기 때문에 pop을 할 때마다 값이 변함
```

<aside>
	
    🗒️ 해시 테이블 (Hash Table)

    - 데이터를 효율적으로 저장하고 검색하기 위해 사용되는 자료 구조
    - 세트 내의 각 요소는 해시 함수를 통해 해시 값으로 변환되고,이를 기반으로 테이블에 저장
    - 딕셔너리의 키는 고유해야 하므로, 키를 해시 함수를 통해 해시 값으로 변환하여 테이블에 저장
</aside>

- .updata(iterable) : 세트에 다른 iterable 요소를 추가

```python
my_set = {1, 2, 3}
my_set.updata([4, 5, 1])
print(my_set)
# {1, 2, 3, 4, 5}
```

| 메서드 | 설명 | 연산자 |
| --- | --- | --- |
| set1.difference(set2) | set1에는 들어있지만 set2에는 없는 항목으로 세트를 생성 후 반환 | set1 - set2 |
| set1.intersection(set2) | set1과 set2 모두 들어있는 항목으로 세트를 생성 후 반환 | set1 & set2 |
| set1.issubset(set2) | set1의 항목이 모두 set2에 들어있으면 True를 반환 | set1 <= set2 |
| set1.issuperset(set2) | set1이 set2의 항목을 모두 포함하면 True를 반환 | set1 >= set2 |
| set1union(set2) | set1 또는 set2에(혹은 둘 다) 들어있는 항목으로 세트를 생성 후 반환 | set1 | set2 |

---

## 딕셔너리

⇒ 고유한 항목들의 정렬되지 않은 컬렉션

- .clear() : 딕셔너리의 모든 키 / 값 쌍을 제거
- .get(key[,default]) : 키 연결된 값을 반환하거나 키가 없으면 None 혹은 기본 값을 반환

```python
person = {'name': 'Alice', 'age': 25}

print(person.get('name'))
# Alice
print(persom.get('country'))
# None
print(person.get('country', 'Unknown'))
# Unknown
```

- .keys() : 딕셔너리 키를 모은 객체를 반환

```python
person = {'name': 'Alice', 'age': 25}
print(person.keys())
# dict_keys(['name', 'age'])

for k in person.keys():
	print(k)
"""
name
age
"""
```

- .values() : 딕셔너리 값을 모은 객체를 반환

```python
person = {'name': 'Alice', 'age': 25}
print(person.keys())
# dict_keys(['name', 'age'])

for v in person.values():
	print(v)
"""
Alice
25
"""
```

- .items() : 딕셔너리 키 / 값 쌍을 모은 객체를 반환

```python
person = {'name': 'Alice', 'age': 25}

print(person.items())
# dict_items([('name', 'Alice'), ('age', 25])
for k, v in person.items():
	print(k, v)
"""
name Alice
age 25
"""
```

- .pop(key[,default]) : 키를 제거하고 연결됐던 값을 반환(없으면 에러나 default를 반환)

```python
person = {'name': 'Alice', 'age': 25}

print(person.pop('age'))
# 25
print(person)
# {'name': 'Alice"}
print(person.pop('country', None))
# None
print(person.pop('country'))
# KeyError
```

- .setdefault(key[,default]) : 키와 연결된 값을 반환, 키가 없다면 default와 연결한 키를 딕셔너리에 추가하고 default를 반환

```python
person = {'name': 'Alice', 'age': 25}

print(person.setdefault('country', 'KOREA'))
# KOREA
print(person)
# {'name': 'Alice', 'age': 25, 'country': 'KOREA'}
```

- .update([other]) : other가 제공하는 키 / 값 쌍으로 딕셔너리를 갱신, 키존 키는 덮어씀

```python
person = {'name': 'Alice', 'age': 25}
other_person = {'name': 'Jane', 'gender': 'Female'}

person.update(other_person)
print(person)
# {'name': 'Jane', 'age' : 25, 'gender': 'Female'}

person.update(age=50)
print(person)
# {'name': 'Jane', 'age' : 50, 'gender': 'Female'}

person.update(country='KOREA')
print(person)
# {'name': 'Jane', 'age' : 50, 'gender': 'Female', 'country': 'KOREA'}
```

---

## 복사

### 데이터 타입과 복사

- 파이썬에서는 데이터의 분류에 따라 복사가 달라짐
- “변경 가능한 데이터 타입”과 “변경 불가능한 데이터 타입”을 다르게 다룸

---

## 복사 유형

- 할당 - Assignment : 할당 연산자( = )를 통한 복사는 해당 객체에 대한 객체 참조를 복사
- 얕은 복사
    - 슬라이싱을 통해 생성된 객체는 원본 객체와 독립적으로 존재
    - copy를 통해 객체를 생성할 수 있음
    
    ```python
    # 슬라이싱
    b = a[:]
    b[0] = 100
    print(a, b)
    # [1, 2, 3] [100, 2, 3]
    
    # copy
    c = a.copy()
    c[0] = 100
    print(a, c)
    # [1, 2, 3] [100, 2, 3]
    ```
    

<aside>
	
    ❗ 얕은 복사의 한계
    2차원 리스트와 같이 변경가능한 객체 안에 변경 가능한 객체가 있는 경우

</aside>

```python
a = [1, 2, [1, 2]]
b = a[:]
print(a, b)
# [1, 2, [1, 2]] [1, 2, [1, 2]]

b[2][0] = 100
print(a, b)
# [1, 2, [100, 2]] [1, 2, [100, 2]]
```

- 깊은 복사 : 내부에 중첩된 모든 객체까지 새로운 객체 주소를 참조하도록 함

```python
import copy

original_list = [1, 2, [1, 2]]
deep_copied_list = copy.deepcopy(original_list)

deep_copied_list[2][0] = 100

print(original_list)
# [1, 2, [1, 2]]
print(deep_copied_list)
# [1, 2, [100, 2]]
```
