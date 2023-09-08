# Python - 관통프로젝트

날짜: 2023년 7월 21일

## 목표 : 인터넷에 있는 날씨 정보를 가져와, 내가 원하는 정보만 출력

---

<aside>
	
    🗒️ 전문용어 이해하기

    - 서버 : 부탁 받으면 처리해주거나, 부탁대로 원하는 값을 돌려줌

    **[서버 그림]**

    - 클라이언트 : 부탁하는 역할
</aside>

---

## 오늘은❓

⇒ 서버에 요청하여 데이터 가져오기

<aside>
	
    🗒️ 어떻게 요청해?

    - 도메인 주소 입력
    - Python 라이브러리인 requests를 이용 (pip install requests)
</aside>

```python
#fakestoreapi에서 데이터 요청하기
import requests

url = 'https://fakestoreapi.com/carts'
response = requests.get(url)
data = response.json()

print(response)
print(data)

```

---

## API

⇒ 우리는 API에게 요청을 하고, API가 서버에서 요청한 데이터를 가져옴

<aside>
	
    🗒️ 어떻게 가져오는데?

    - 도메인.com/원하는 데이터(도메인에 따라 다름)에 접속
</aside>

### Open API

⇒ 외부에서 사용할 수 있도록 무료로 개방된 API

<aside>
	
    ❗ 주의사항

    - 악성 사용자가 DDOS 공격을 하면 서버가 버티질 못 함
    - API Key를 활용해 인증된 사용자만 사용하도록
    - API Key를 가진 악성 사용자가 DDOS 공격을 하면 서버가 버티질 못 함

    ⇒ 일일 혹은 월간 사용량을 제한함

</aside>

### ⇒ Open API를 사용하기 위해선 정상적인 API Key를 발급받아야 함

---

## JSON - JavaScript Object Notation

⇒ 경량의 텍스트 기반의 데이터 형식 / 단순히 데이터를 표현하는 표현 방법

<aside>
	
    🗒️ 특징

    - 데이터는 { } 로 둘러싸인 Key : Value 쌍의 집합으로 표현
    - Key = 문자열 / 값 = 다양한 데이터 유형의 형태
    - 값은 쉼표로 구분
</aside>

```python
import json

json_data = '''
{
    "name" : "김싸피",
    "age" : 28,
    "hobbies" : [
        "영화보기",
        "잠 자기"
    ]
}
'''

data = json.loads(json_data)
print(data)
```

<aside>
	
    🗒️ Python에서 json을 활용하는 기능

    - 파싱(Parsing) : 데이터를 의미 있는 구조로 분석하고 해석하는 과정
    - json.loads() : json 형식의 문자열을 파싱하여 python dict으로 변환
</aside>

---

## ⛅Openweathermap API

- 기상 데이터 및 날씨 정보를 제공하는 오픈 API
- 전세계 날씨 데이터를 가져옴
- API 사용량 제한

[⛅Openweathermap Current Weather Data](https://openweathermap.org/current) 참조

```python
city_name = 'Busan,KR'
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}"

import requests
#api요청 보내기
response = requests.get(url).json()
#dict에서 온도 데이터만 꺼내오기
temp = response['main']['temp']
#화씨 온도에서 섭씨 온도로 변환
temp -= 273.15
print(int(temp // 1),'\'c')

=> json파일의 데이터를 가져 왔을 때는 dict 형태로 받아 옴
```

---

## 🤜오늘의 도전과제 🤛

### 🔥🔥🔥🔥 금융 데이터 수집 🔥🔥🔥🔥

<aside>
	
    🗒️ 어떻게 해야할까,,,

    1. 금융상품통합 비교공시 API에 접속하여 url과 api key 발급
    2. api를 통해 데이터 요청 후 리턴 데이터 확인
    3. 그 중 원하는 데이터 목록 작성
    4. 해당 데이터 요청
    5. 원하는 형식으로 출력
</aside>

1. [금융감독원 오픈API](https://finlife.fss.or.kr/finlife/main/contents.do?menuNo=700029)에 접속하여 API key 발급
2. API 사용 예제에 발급 받은 Key를 넣어 데이터를 받아오는지 확인

```python
#해당 코드에 넣어 Key가 정상적으로 작동되는지 확인
import pprint
import requests

def get_deposit_products():
    api_key = ""

    url = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
    params = {
        'auth': api_key,
        # 금융회사 코드 020000(은행), 030200(여신전문), 030300(저축은행), 050000(보험), 060000(금융투자)
        'topFinGrpNo': '020000',
        'pageNo': 1
    }
    # 응답을 json 형태로 변환
    response = requests.get(url, params=params).json()
    return response

if __name__ == '__main__':
    #json 형태의 데이터 반환
    result = get_deposit_products()
    # pprint.pprint() : json을 보기 좋은 형식으로 출력
    pprint.pprint(result)
```

---

### 1. 데이터 추출 - Key 값 출력하기

- 전체 정기예금의 응답을 json 형채로 변환 후 아래와 같이 Key 값만 출력하도록 구성

```python
dict_keys(['prdt_div', 'total_count', 'max_page_no', 'now_page_no', 'err_cd', 'err_msg', 'baseList', 'optionList'])
```

- 공식 문서의 요청 변수 및 예제 요청결과 부분을 참고

<aside>
	
    ⭐ 아래와 같은 순서로 데이터를 출력하며 진행합니다.
    1. 응답을 json 형식으로 변환합니다.
    2. key 값이 “result”인 데이터에 모든 정보가 담겨 있습니다.
    3. key 값이 “result”인 데이터의 key 값만 출력합니다.

</aside>

```python
import pprint
import requests

# 전체 정기예금의 응답을 json 형태로 변환하여 key 값만 출력하시오.
# 공식문서의 요청변수와 예제 요청결과(JSON) 부분을 참고합니다.
# [힌트] 아래와 같은 순서로 데이터를 출력하며 진행합니다.
# 1. 응답을 json 형식으로 변환합니다.
# 2. key 값이 "result" 인 데이터에 모든 정보가 담겨 있습니다.
# 3. key 값이 "result" 인 데이터의 key 값만 출력합니다.

def get_deposit_products():
  # 본인의 API KEY 로 수정합니다.
  api_key = "api_key"

  url = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
  params = {
        'auth': 'api_key',
        # 금융회사 코드 020000(은행), 030200(여신전문), 030300(저축은행), 050000(보험), 060000(금융투자)
        'topFinGrpNo': '020000',
        'pageNo': 1
    }
    # 응답을 json 형태로 변환
  response = requests.get(url, params=params).json()
  return response
#=> 해당 api에서 값을 받아오고 받아온 파일을 response 이름의 dict에 입력

data = get_deposit_products()['result']
#get_deposit_products()(=response)라는 dict파일에서 최상단 의 key 값을 받아오기 위해 result의 내용을 data에 입력
print(data.keys())
#key값만 출력하기 위해 .keys()를 사용하여 data의 key값들만 출력
```

> 주어진 코드에서의 아래 부분인 if __name__ == ‘__main__’: 부분을 알 지 못해 벽에 막혔었다. 뭔지 모르니 없다고 치고 오늘 오전에 했던 날씨 api 받아오는 예제를 참고하였더니 갑자기 풀려서 당황스럽다.
> 

였는데 if __name__ == ‘__main__’: 이 부분을 사용해야해서 다시 수정

```python
import pprint
#json파일을 읽기 쉽게 pprint 모듈 사용
import requests
#서버에서 요청을 받기 위해 request 모듈 사용

# 전체 정기예금의 응답을 json 형태로 변환하여 key 값만 출력하시오.
# 공식문서의 요청변수와 예제 요청결과(JSON) 부분을 참고합니다.
# [힌트] 아래와 같은 순서로 데이터를 출력하며 진행합니다.
# 1. 응답을 json 형식으로 변환합니다.
# 2. key 값이 "result" 인 데이터에 모든 정보가 담겨 있습니다.
# 3. key 값이 "result" 인 데이터의 key 값만 출력합니다.

def get_deposit_products():
  # 본인의 API KEY 로 수정합니다.
  api_key = "8a6d8998967dee123c8fe3e2031dbe43"

  url = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
  params = {
        'auth': api_key,
        # 금융회사 코드 020000(은행), 030200(여신전문), 030300(저축은행), 050000(보험), 060000(금융투자)
        'topFinGrpNo': '020000',
        'pageNo': 1
    }
    # 응답을 json 형태로 변환
  response = requests.get(url, params=params).json()
  return response

# data = get_deposit_products()['result']
# print(data.keys())

    
    
# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_deposit_products()  
		#get_deposit_products()의 값을 result이름의 dict에 입력
    key_name = result['result']
		#result의 최상단의 dict인 result 값을 key_name에 입력
    pprint.pprint(key_name.keys())
		#.keys()를 통해 key_name의 key값들만 출력
```

---

### 2. 데이터 추출 - 전체 정기예금 상품 리스트

- 응답 중 정기예금 상품 리스트 정보만 출력하도록 구성합니다.

<aside>
	
    ⭐ 아래와 같은 순서로 데이터를 출력하며 진행합니다.
    1. 응답을 json 형식으로 변환합니다.
    2. key 값이 “result”인 데이터를 출력합니다.
    3. 위의 결과 중 key 값이 “baseList’인 데이터를 출력합니다.

</aside>

```python
import pprint
import requests

# 전체 정기예금의 응답을 json 형태로 변환하여 key 값만 출력하시오.
# 공식문서의 요청변수와 예제 요청결과(JSON) 부분을 참고합니다.
# [힌트] 아래와 같은 순서로 데이터를 출력하며 진행합니다.
# 1. 응답을 json 형식으로 변환합니다.
# 2. key 값이 "result" 인 데이터에 모든 정보가 담겨 있습니다.
# 3. key 값이 "result" 인 데이터의 key 값만 출력합니다.

def get_deposit_products():
  # 본인의 API KEY 로 수정합니다.
  api_key = "8a6d8998967dee123c8fe3e2031dbe43"

  url = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
  params = {
        'auth': api_key,
        # 금융회사 코드 020000(은행), 030200(여신전문), 030300(저축은행), 050000(보험), 060000(금융투자)
        'topFinGrpNo': '020000',
        'pageNo': 1
    }
    # 응답을 json 형태로 변환
  response = requests.get(url, params=params).json()
  return response

# data = get_deposit_products()['result']
# print(data.keys())

    
    
# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_deposit_products()
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    #key_name = result['result']
    #pprint.pprint(key_name.keys())
    data_base = result['result']['baseList']
		#result의 최상단의 dict인 result dict 안의 baseList 값들을 data_base에 입력
    pprint.pprint(data_base)
		#data_base값을 pprint를 사용하여 읽기 쉽게 출력
```

---

### 3. 데이터 가공 - 전체 정기예금 옵션 리스트

- 응답 중 정기예금 상품들의 옵션 리스트를 출력하도록 구성합니다.
- 이때, 원하는 데이터만 추출하여 새로운 리스트를 만들어 반환하는 함수를 작성하시오.

<aside>
	
    ⭐ 아래와 같은 순서로 데이터를 출력하며 진행합니다.
    1. 응답을 json 형식으로 변환합니다.
    2. key 값이 “result”인 데이터를 출력합니다.
    3. 위의 결과 중 key 값이 “optionList’인 데이터를 변수에 저장합니다.
    4. 3번에서 저장된 값을 반복하며, 원하는 데이터만 추출 및 가공하여 결과 리스트에 저장합니다.

</aside>

```python

```
