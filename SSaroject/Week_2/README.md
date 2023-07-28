# Python - 관통프로젝트 Week2

날짜: 2023년 7월 28일

- 관통 Ver.1 데이터 사이언스 기초
    - 데이터 사이언스 이해하기
    - 데이터 사이언스 프로세스 실습
        - 구글 주가 데이터 분석
- 관통 Ver.2 파이썬을 활용한 데이터 수집2

<aside>

    🗒️ 목표

    - 데이터 사이언스 분야에 대해 이해하기
    - 데이터 사이언스에서 자주 사용되는 패키지를 사용해보기
</aside>

<aside>

    🗒️ 학습할 내용 정리

    - Google 주식 데이터를 다운로드 받습니다.
    - 데이터 사이언스에서 자주 사용되는 패키지를 사용하여
    - 원하는 데이터만 뽑아내서 차트로 출력합니다.
</aside>

- 데이터를 수집하고 처리하여 출력하는 것

<aside>

    ❗ 완성 목표 ⇒ 2022년 구글 주가의 최고, 최저, 종가 그래프를 나타내보자

</aside>

<aside>

    🗒️ 진행순서

    - 데이터 사이언스 기초 이론 학습
    - 데이터들이 모여 있는 “캐글(Kaggle)”이라는 사이트에서, 실습 데이터 다운로드
        - 구글, 넷플릭스 주가 데이터
    - 데이터 사이언스에서 자주 쓰이는 패키지 학습
</aside>

---

## 데이터 사이언스

- 다양한 데이터로부터 새로운 지식과 정보를 추출하기 위해 과학적 방법론, 프로세스, 알고리즘, 시스템을 동원하는 융합 분야
- 컴퓨터 과학, 통계학, 수학 등 다양한 학문의 원리와 기술을 활용

<aside>

    ⭐ 필요한 정보를 추출하는 5가지 단계

    1. 문제 정의 : 해결하고자 하는 문제 정의
    2. 데이터 수집 : 문제 해결에 필요한 데이터 수집
    3. 데이터 전처리(정제) : 실질적인 분석을 수행하기 위해 데이터를 가공하는 단계
    → 수집한 데이터의 오류 제거(결측치, 이상한 데이터), 데이터 형식 변환 등
    4. 데이터 분석 : 전처리가 완료된 데이터에서 필요한 정보를 추출하는 단계
    5. 결과 해석 및 공유 : 의사 결정에 활용하기 위해 결과를 해석하고 시각화 후 공유하는 단계
</aside>

<aside>

    🗒️ 수 많은 데이터를 모아서, 필요한 정보만을 이용하여 내가 원하는 정보 혹은 새로운 지식을 알아내는 과학 분야 = 데이터 사이언스

</aside>

---

## 데이터 사이언스 프로세스 실습

### 프로세스 1. 문제 정의

⇒ 구글의 주식 가격은 앞으로 어떻게 될까 ?

### 프로세스 2. 데이터 수집

- 주식 가격을 분석하기 위해서는 기간 별 주식 가격에 대한 데이터가 필요합니다.
- 데이터 수집은 다양한 기술과 방법을 활용할 수 있습니다.
    - 웹 스크래핑(Web Scraping) : 웹 페이지에서 데이터를 추출하는 기술
    - 웹 크롤링(Web Crawling) : 웹 페이지를 자동으로 탐색하고 데이터를 수집하는 기술
    - Open API : 공개된 API를 통해 데이터를 수집
    - 데이터 공유 플랫폼 : 다양한 사용자가 데이터를 공유하고 활용할 수 있는 온라인 플랫폼
    → 캐글(Kaggle), Data.world, 데이콘(Dacon), 공공데이터포털 등

<aside>

    ❓ 캐글(Kaggle)??

    - 데이터 분석 경진대회 플랫폼
    - 기업 및 단체에서 데이터와 해결 과제를 등록하면, 데이터 과학자들이 이를 해결하는 방법을 개발하고 경쟁할 수 있는 플랫폼
    - 경진 대회, 데이터셋 공유, 토론 등의 기능이 가능하며 많은 데이터 과학자와 분석가들이 활용
</aside>

<aside>

    ❓ **CSV** ??

    - 몇 가지 필드를 쉽표로 구분한 텍스트 데이터 및 텍스트 파일
    - 일반적으로 표 형식의 데이터를 CSV형태로 많이 사용
    - 저장, 전송 및 처리 속도가 빠르며, 처리 가능한 프로그램이 다양

    ⇒ windows에서는 저장 인코딩 방식이 달라서 수정을 하게 되면 파일이 깨진다.

</aside>

### 데이터 전처리(정제)

- 데이터 전처리 단계를 분석을 진행하기 전 데이터를 정제하는 단계
- 다음과 같은 과정을 포함
    - 불완전하거나 오류가 있는 데이터를 제거하여 데이터의 품질을 개선
    - 중복 데이터 제거
    - 분석하기 적절한 형식으로 데이터를 변환
- 데이터 전처리 및 분석에 사용되는 파이썬 패키지
    - Numpy, Pandas, Matplotlib
    
    <aside>

        ❓ **Numpy**
    
        - 다차원 배열을 쉽게 처리하고 효율적으로 사용할 수 있도록 지원하는 파이썬 패키지
        - 장점
            - Numpy 행렬 연산은 데이터가 많을수록 Python 반복문에 비해 훨씬 빠르다.
            - 다차원 행렬 자료 구조를 제공하여 개발하기 편하다.
        - 특징
            - CPython에서만 사용 가능
            - 행렬 인덱성(Array Indexing) 기능 제공
        - 다차원 배열을 조작, 속도 빠르며 편리한 메서드 지원
    </aside>
    
    <aside>

        ❓ **Pandas**
    
        - Numpy의 한계
            - 유연성(데이터에 레이블을 붙이거나, 누락된 데이터로 작업)이 부족함
            - 그룹화, 피벗 등 구조화가 부족함
        - Pandas는 마치 프로그래밍 버전의 엑셀을 다루듯 고성능의 데이터 구조를 만들 수 있음
        - Numpy 기반으로 만들어진 패키지로, Series(1차원 배열) 과 DataFrame(2차원 배열) 이라는 효율적인 자료구조 제공
        - 가장 많은 양의 데이터를 처리해야 한다.
        - Numpy가 하기 힘든 전처리와 분석에 굉장히 특화되어 있다.
        - df.describe()를 아마 가장 많이 사용할 것
        - 새로운 데이터 컬럼을 만들 때, 보고 싶은 데이터만 볼 수 있도록 해주는 것이 장점
    </aside>
    
    <aside>

        ❓ **Matplotlib**
    
        - Python에서 데이터 시각화를 위해 가장 널리 사용되는 라이브러리
        - 다양한 종류의 그래프와 도표를 생성하고 데이터를 시각적으로 표현할 수 있다.
    </aside>
    

## 실습

<aside>

    🗒️ 캐글을 활용하여 데이터를 다운로드 받아 활용

    - 데이터 셋 : ”Google Stock Price: Daily, Weekly & Monthly (2023)(구글 주식 데이터)”
    - 데이터 셋 요약 : 2013-05-01 ~ 최근까지의 일/주/월 별 데이터

    실습 파일 명 : google_stock_price_example.ipynb

    데이터 전처리 및 시각화 연습

</aside>

---

## 관통 Ver1 - PTJ02 도전 과제

<aside>

    🗒️ 프로젝트 명 : 파이썬과 Pandas를 사용한 데이터 처리
    목표 : 넷플릭스 주가 데이터 분석
    특징 : 데이터 사이언스 프로세스 활용, 캐글을 통해 데이터 다운로드

</aside>

<aside>

    🗒️ 공통 요구사항

    - 데이터 셋 : “Netflix Stock Price Prediction
    - 데이터 요약 : 2018-02-05 ~ 2022-02-04까지의 일별 데이터
</aside>

<aside>

    ❗ 세부 요구사항

    - A. 데이터 전처리 - 데이터 읽어오기
    - B. 데이터 전처리 - 2021년 이후의 종가 데이터 출력하기
    - C. 데이터 분석 - 2021년 이후 최고, 최저가 출력하기
    - D. 데이터 분석 - 2021년 이후 월 별 평균 종가 출력하기
    - E. 데이터 시각화 - 2022년 1월 이후 월 별 최고, 최저, 종가 시각화
</aside>

---

## A. 데이터 전처리 - 데이터 읽어오기

<aside>

    ❗ 요구사항

    - Pandas를 사용하여 csv 파일(NLFX.csv)을 DataFrame으로 읽어옵니다.
    - 이 때, [’Data’, ‘Open’, ‘High’, ‘Low’, ‘Close’] 필드만 읽어오도록 구성합니다.
</aside>

```python
# 데이터를 원하는 형태로 처리하기 위해 패키지 요청
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 조회하고 싶은 csv파일의 경로를 설정하여 할당
csv_file = 'data/NFLX.csv'

# 조회하고픈 파일의 원하는 컬럼을 정하여 df에 할당
df = pd.read_csv(csv_file, usecols = ['Date', 'Open', 'High', 'Low', 'Close'])

# 해당 dataframe 출력
df
```

---

## B. 데이터 전처리 - 2021년 이후의 종가 데이터 출력하기

<aside>

    ❗ 요구사항

    - csv 파일을 DataFrame으로 읽어와 2021년 이후의 데이터만 필터링
    - 필터링이 완료된 DataFrame의 종가 데이터를 Matplotlib을 사용하여 시각화
</aside>

<aside>

    ⭐ [Hint]

    - 필터링이 가능한 형식으로 데이터 타입을 변경한 후 필터링을 진행
    - Pandas의 to_datetime()을 활용
</aside>

```python
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 경로
csv_path = "data/NFLX.csv"

# CSV 파일 읽어오기 (첫 번째, 마지막 열 제외)
df = pd.read_csv(csv_path, usecols= ['Date', 'Open', 'High', 'Low', 'Close'])

# DataFrame 출력
df

# 날짜 데이터 변환
df["Date"] = pd.to_datetime(df["Date"])

# 2022년 이후 데이터 필터링
df_after_2021 = df[df["Date"] >= "2021"]

# 그래프 그리기 (가로, 세로 축에 표시될 데이터를 차례로 기입)
plt.plot(df_after_2021['Date'], df_after_2021['Close'])

# 그래프 제목 설정
plt.title('NFLX Close Price')

# x축 레이블 설정
plt.xlabel('Date')

# y축 레이블 설정
plt.ylabel('Close')

# 그래프 표시
plt.show()
```

![Untitled](/uploads/e982fa9814732560cc3a6fd2ce9b1c35/Untitled.png)

---

## C. 데이터 분석 - 2021년 이후 최고, 최저 종가 출력하기

<aside>

    ❗ 요구사항

    - csv 파일을 DataFrame으로 읽어와 2021년 이후의 데이터만 필터링
    - 종가(Close) 필드를 활용하여, 2021년 이후 가장 높은 종가와 가장 낮은 종가를 출력
    - Pandas의 내장 함수를 사용
</aside>

```python
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 경로
csv_path = "data/NFLX.csv"

# CSV 파일 읽어오기 (첫 번째, 마지막 열 제외)
df = pd.read_csv(csv_path, usecols=['Date', 'Open', 'High', 'Low', 'Close'])

# 2021년 이후 데이터 필터링
df_after_2021 = df[df["Date"] >= "2021"]

# Pandas의 내장 함수인 .max()와 .min()을 이용하여 원하는 컬럼의 최대, 최소 값 구하기
max_price = df_after_2021['Close'].max()
min_price = df_after_2021['Close'].min()

# 출력
print('최고 종가: ', max_price)
print('최저 종가: ', min_price)

# 최고 종가:  691.690002
# 최저 종가:  359.700012
```

---

## D. 데이터 분석 - 2021년 이후 월 별 평균 종가 출력하기

<aside>

    ❗ 요구사항

    - csv 파일을 DataFrame으로 읽어와 2021년 이후의 데이터만 필터링
    - 월 별로 그룹화하여 평균 종가를 계산한 새로운 DataFrame을 만들어 그래프로 시각화
</aside>

```python
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 경로
csv_path = "data/NFLX.csv"

# CSV 파일 읽어오기 (첫 번째, 마지막 열 제외)
df = pd.read_csv(csv_path, usecols=['Date', 'Open', 'High', 'Low', 'Close'])

# 날짜 데이터 변환
df['Date'] = pd.to_datetime(df['Date'])

# 2021년 이후 데이터 필터링
df_after_2021 = df[df["Date"] >= "2021"]

# 월 별 평균을 구하기 위해 Date 컬럼을 인덱스로 설정하고 resample() 함수를 이용
# 이후 ['Close'].mean()을 통해 그룹된 Date안의 Close 값들의 평균을 구함
monthly_average = df_after_2021.set_index('Date').resample('M')['Close'].mean()

# 시리즈인 monthly_average를 pd.DataFrame()함수를 통해 DataFrame으로 변환하여 df_monthly_average에 할당
df_monthly_average = pd.DataFrame(monthly_average)
# 현재 Date 값이 인덱스로 나타나는데 Date를 .reset_index()를 통해 컬럼으로 변환
df_monthly_average = df_monthly_average.reset_index()
# 출력하면 첫 번째 열은 인덱스 값, 두 번째 열은 Date, 세 번째 열은 Close의 월 별 평균 값이 나온다
df_monthly_average

# 가로와 세로 축에 표시될 데이터 기입
plt.plot(df_monthly_average['Date'], df_monthly_average['Close'])

# 그래프 제목 설정
plt.title('Monthly Average close Price')

# x축 레이블 설정
plt.xlabel('Date')

# y축 레이블 설정
plt.ylabel('Close')

# 그래프 출력
plt.show()
```

![Untitled_1](/uploads/9fce56a7e7e990ddb3890d8638279901/Untitled_1.png)

---

## E. 데이터 시각화 - 2022년 이후 최고, 최저, 종가 시각화하기

<aside>

    ❗ 요구사항

    - csv 파일을 DataFrame으로 읽어와 2022년 이후의 데이터만 필터링
    - Matplotlib를 활용하여 3가지 필드를 한 번에 분석할 수 있도록 시각화
</aside>

```python
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 경로
csv_path = "data/NFLX.csv"

# CSV 파일 읽어오기 (첫 번째, 마지막 열 제외)
df = pd.read_csv(csv_path, usecols=['Date', 'Open', 'High', 'Low', 'Close'])

# 날짜 데이터 변환
df['Date'] = pd.to_datetime(df['Date'])

# 2022년 이후 데이터 필터링
df_after_2022 = df[df["Date"] >= "2022"]
df_after_2022

# 그릴 그래프의 x축과 y축에 들어 갈 정보를 정하고, label을 통해 이름을 정한다
plt.plot(df_after_2022['Date'], df_after_2022['High'], label = 'High')
plt.plot(df_after_2022['Date'], df_after_2022['Low'], label = 'Low')
plt.plot(df_after_2022['Date'], df_after_2022['Close'], label = 'Close')

# 그래프 제목 설정
plt.title('High, Low and Close Prices sinve January 2022')

# 그래프의 x축 레이블 설정
plt.xlabel('Date')

# 그래프의 y축 레이블 설정
plt.ylabel('Price')

# x축의 Date 값이 너무 길어 겹쳐 보이기에 가독성을 높이려 겹치지 않게 45도씩 회전
plt.xticks(rotation=45)

# 어떤 그래프가 어떤 항목을 나타내는지 알 수 없기에 어떠한 그래프가 어떤 내용인지 설명을 추가
plt.legend()

# 그래프 출력
plt.show
```

![Untitled_2](/uploads/9c8af7edc133597443c9a69cffb82574/Untitled_2.png)

---

<aside>

    🗒️ 두 번째 프로젝트를 하며,,,

    사실 저번 주의 프로젝트와는 다르게 이번 주 프로젝트는 오전의 유튜브 강의를 듣고, 예제 교안을 본다면 크게 어려운 내용은 없었던 것 같다.
    하지만 중간중간 교안에는 없던 내용들. 
    예를 들어 Pandas의 내장 함수인 max()와 min()을 사용한다던가( 사실 이 함수는 python에서도 사용한 적이 있기에 크게 어려움은 없었다. ), 변환한 DataFrame 안에서 원하는 열의 내용만 가져 오는 것, 그리고 월 별 평균 값을 구하기 위해 Date 열을 인덱스로 옮겨 원하는 정보를 얻은 해당 정보를 토대로 그래프를 그리기 위해 다시 Date 열을 인덱스에서 컬럼으로 옮기는 과정이 어려웠다.
    사실 인덱스로 변환하는 과정에서 변환했다는 사실을 인지하지 못하고 왜 안되는지 생각을 했었다. 검색하는 과정에서 설명을 제대로 읽지 않고 ‘음 그렇구나’하고 대충 긁어와서 붙여넣기를 하다보니 생긴 문제였다.
    나는 아직 아무것도 모르는 초짜이기에 모르는게 많은 것도, 이를 검색이나 질문을 통하여 해소를 정말 많이 해야 한다고 생각한다. 그런 과정에서 오늘과 같은 내가 긁어왔음에도 불구하고 정확하게 어떤 걸 긁어왔는지, 어떻게 작동하는지, 어떠한 결과 값을 반환하는지 모르는 상황이 발생한다면 다른 사람들에 비해서 문제 해결 능력이 떨어지는 나는 더욱 당황할 것이다. 실제로 오늘도 당황과 답답함과 막막함이 공존하는 시간이 존재했다.
    공부를 하는 이유는 아는 것을 늘리기 위함이 아니라 모르는 것을 줄이기 위해 한다고 생각한다. 그러기 위해선 내가 매일매일 얻게 될 정보들을 100%까지는 무리더라도 최소한 어떻게 돌아가는지 대충 알도록 공부를 해야겠다고 생각이 든 프로젝트였다.

</aside>

<aside>

    💡 오늘의 reminder

    - 데이터 사이언스와 해결 과정
    - csv 파일에 대해서
    - Numpy의 기능과 특징
        - csv 파일 불러오기
    - Pandas의 기능과 특징
        - 전처리와 분석에 특화
        - DataFrame을 통한 엑셀과 비슷한 모양의 고성능 처리
        - 필터링하여 원하는 정보만 보기 가능
    - Matplotlib의 기능과 특징
        - 그래프로 데이터를 시각화 할 수 있음
    - usecols 함수를 통해 원하는 컬럼만 골라서 표시 가능
    - pd.to_datetime 함수를 통해 문자열 형태인 날짜를 ‘datetime64’ 자료형으로 변환
    - Pandas의 내장 함수인 max()와 min()을 통해 원하는 지역의 최대, 최소 값 반환 가능
    - set.index() 함수를 통해 원하는 컬럼을 인덱스로 변환
    - resample() 함수를 통해 시계열 데이터를 다룰 때 특정 주기로 데이터를 재조정
        - 오늘 사용한 ‘M’은 월(month)를 의미하는 빈도 문자
    - DataFrame 형태의 경우 따로 print()하지 않고 이름만으로 해당 DataFrame 출력 가능
</aside>
