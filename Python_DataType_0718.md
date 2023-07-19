# Python - Data Type

날짜: 2023년 7월 18일

## Date Type
⇒ 값의 종류와 그 값에 적용 가능한 연산과 동작을 결정하는 속성

→ 값들을 구분하고, 어떻게 다루어야 하는지 알 수 있음  

→ 각 타입들은 각자에게 맞는 적합한 도구를 가지고 있음  

→ 타입을 명시적으로 지정하면 변수의 의도를 더 쉽게 이해 할 수 있음

---

## Numeric Type

1. **int - 정수 자료형**
    1. 진수 표현
    
    <aside>

       🗒️ 2진수 : 0b, 8진수 : 0o, 16진수 : 0x
    
    </aside>
    
    ```python
    print(0b10) = 2            print(bin(12)) = 0b1100
    print(0o30) = 24    <->    print(oct(12)) = 0o14
    print(0x10) = 16           print(hex(12)) = 0xc
    ```
    
1. **float - 실수 자료형**
    1. 0.1은 실제로 0.1이 아닌 수렴하는 근사 값을 표현
    2. 유한 정밀도 : 한 숫자에 대해 저장하는 용량이 제한됨
    
    <aside>
    
        ❗ *주의사항*
        컴퓨터 = 2진수  /  사람은 10진수 사용

        
        0.1 = 0.0001100110011…..
        무한으로 표현할 수 없기에 10진법의 근사 값을 표시

   
        0.1의 경우 36028…6397 / 2 ** 55이며 0.1에 가까움
    
        ⇒ 두 수의 차이가 매우 작은 수보다 작은 지 확인하거나 math 모듈을 활용
    
    </aside>
    
    c. 지수 표현 방식
    
    <aside>
        
        1) 314 * 0.001 ⇒ number = 314e-2 = 3.14  
        
        2) print(type(number)) ⇒ float
   
        3) print(number) ⇒ 3.14
   
    
    </aside>
    

---

## Sequence Type
⇒ 여러 개의 값들을 순서대로 나열하여 저장하는 자료형

<aside>

    
    🗒️ 특징

    1. 순서(Sequence) : 값들이 순서대로 저장 ( 정렬은 하지 않은 상태 )
    2. 인덱싱(Indexing) : 각 값에 고유한 인덱스를 가지며, 특정 위치의 값을 선택하고 수정
    3. 슬라이싱(Slicing) : 인덱스 범위를 조절해 부분적인 값 추출 가능
    
![index](https://github.com/hluuy/TIL/assets/103430344/3c41a78d-c0b8-4f10-98d4-4775f2289a4d)

    
    → [ 2 : 4 ] = ‘ ll ’, [ : 3 ] = ‘hel’, [ 3 : ] = ‘lo’, [ 0 : 5 : 2 ] = h
    
    4. 길이(Length) : len( )를 사용하여 저장된 값의 길이를 구할 수 있음
    5. 반복(Iteration) : 반복문을 사용하여 저장된 값들을 반복적으로 처리 가능
</aside>

1. **str - 문자열**
    1. 문자들의 순서가 있는 변경 불가능한 Sequence 자료형
    2. 단일 문자나 여러 문자의 조합을 ‘ ‘, “ “ 로 감싸서 표현
        - 중첩 따옴표 : 따옴표 안에 따옴표를 표현 할 경우, 두 종류가 달라야 함
        - Escape Sequence : ‘ \ ‘를 통해 특수한 기능을 하는 문자 조합
            
            \n : 줄 바꿈  \t : 탭  \\ : 백슬래시  \’ : 작은 따옴표  \” : 큰 따옴표
            
    
    <aside>
        
        🗒️ **String Interpolation**
    
        - f-string : 문자열에 f 또는 F 접두어를 붙이고 표현식을 { }로 작성하여 문자열에 표현식의 값 표시 가능
    </aside>
    
    ```python
    bugs = 'roaches'
    counts = 13             -> 값이 변함에 따라 출력 값도 달라질 수 있음 
    area = 'living room'
    
    print(f'Debugging{bugs} {counts} {area}')
    
    ---
    
    greeting = 'hi'
    print(f'{greeting : ^10}')  ->  좌측에서부터 10칸 중 중간에 hi가 위치함
    
    # ^ : 중간, < : 왼쪽 끝,  > : 오른쪽 끝
    ```
    
    ```python
    my_str = 'hello'
    my_str[1] = 'z' -> 문자열은 바꿀 수 없기에 에러가 뜸
    ```
    
2. **list**
    1. 여러 개의 값을 순서대로 저장하는 변경 가능한 Sequence 자료형
    2. 0개 이상의 객체를 포함하며 데이터 목록 저장
    3. [  ] 로 표기
    4. index, slice, length 모두 가능
    5. 데이터 객체 변경 가능
    
    ```python
    my_list = [1, 2, 3, 'python', ['hello', 'world', '!!!']]
    my_list[4][1] = world
    
    print(len(my_list)) = 5
    print(my_list[4][-1]) = !!!
    print(my_list[-1][1][0]) = w
    
    ---
    
    리스트는 변경 가능
    my_list = [1, 2, 3]
    my_list[0] = 100
    print(my_list) = [100, 2, 3]
    ```
    

1. **tuple**
    1. 여러 개의 값을 순서대로 저장하는 변경 불가능한 Sequence 자료형
    2. 0개 이상의 객체를 포함하여 데이터 목록 저장
    3. (  ) 로 표기
    4. 데이터는 어떤 자료형도 저장할 수 있음
    5. 데이터 객체 변경 불가
    
    ```python
    my_tuple = (1, 'a', 3, 'b', 5)
    my_tuple[1] = 'z' -> error

    my_tuple_1 = ( )
    my_tuple_2 = (1, )
    my_tuple_3 = (1, 'a', 3, 'b', 5)
    ```
    
    <aside>
        
        🗒️ 그럼 tuple을 왜,,,?
        → 불변한 특성을 사용한 안전하게 여러 개의 값을 전달, 그룹화, 다중할당 등
           개발자가 직접 사용하기 보다 ‘python 내부 동작’에서 주로 사용
    
    </aside>
    
3. **range**
    1. 연속된 정수 Sequence를 생성하는 변경 불가능한 자료형
    
    <aside>
        
        🗒️ range(n) : 0 ~ n-1까지의 숫자 sequence
        range(n, m) : n ~ m-1까지의 숫자 sequence
    
    </aside>
    
    ```python
    my_range_1 = range(5)
    my_range_2 = range(1, 10)
    
    print(my_range_1)
    print(my_range_2)
    
    print(list(my_range_1)) -> [0, 1, 2, 3, 4]
    print(list(my_range_2)) -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    => 리스트 형으로 변경 시, 데이터 확인 가능
    ```
    

---

## Non-sequence Types

1. dict
    1. **key - value 쌍**으로 이루어진 순서와 중복이 없는 변경 가능한 자료형
    2. key는 변경 불가능한 자료형만 사용 가능
    ex) str, int, float, tuple, range,,,
    3. value는 모든 자료형 사용 가능
    4. {  }로 표기
    
    ```python
    my_dict = { 'apple' : 12, 'list' : [1, 2, 3] }
    
    print(my_dict['apple'])
    print(my_dict['list'])
    
    my_dict['apple'] = 100  ->  'apple' 값은 100으로 변경 됨
    ```
    
2. set
    1. **순서와 중복**이 없는 변경 가능한 자료형
    2. 수학에서의 집합과 동일한 연산 처리 가능
    3. {  }로 표기
    
    ```python
    my_set_1 = set()
    my_set_2 = {1, 2, 3}
    my_set_3 = {1, 1, 1}
    
    print(my_set_1)  ->  set()
    print(my_set_2)  ->  {1, 2, 3}
    print(my_set_3)  ->  {1}
    
    => 순서가 없어서 요소들이 몇 번째인지 알 수 없음
    
    ---
    
    my_set_1 = {1, 2, 3}
    my_set_2 = {3, 6, 9}
    
    print(my_set_1 | my_set_2)  ->  {1, 2, 3, 6, 9} 합집합
    print(my_set_1 - my_set_2)  ->  {1, 2} 차집합
    print(my_set_1 & my_set_2)  ->  {3} 교집합
    ```
    

---

## Other Types

1. None
    1. Python에서 ‘값이 없음’을 표현하는 자료형
    
    ```python
    variable = None
    print(variable) = None
    ```
    
2. Boolean
    1. 참과 거짓을 표현하는 자료형
    2. 비교 / 논리 연산의 평가 결과로 사용됨
    3. 주로 조건 / 반복문과 함께 사용
    
3. Collection
    
    
    ![collection](https://github.com/hluuy/TIL/assets/103430344/40cf8532-93c5-4488-a1e5-eec97abc05f5)


---

## 불변과 가변

```python
my_str = 'hello'
my_str[0] = 'z'  ->  str 변경 불가로 error

---

my_list = [1, 2, 3]
my_list[0] = 100
print(my_list)  ->  [100, 2, 3]

---

list_1 = [1, 2, 3]
list_2 = list_1  ->  [1, 2, 3]에 대한 주소를 같이 공유해서 사용

list_1[0] = 100
print(list_1)  ->  [100, 2, 3]
print(list_2)  ->  [100, 2, 3]
=> 아래 그림 참조조
```

![가변](https://github.com/hluuy/TIL/assets/103430344/b9d4a34e-b7b2-4efc-aff2-5be932c7dedf)

