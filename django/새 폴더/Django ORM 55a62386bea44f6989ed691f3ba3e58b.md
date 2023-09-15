# Django ORM

날짜: 2023년 9월 15일

## ORM

- Object Relational Mapping
- 객체 지향 프로그램이 언어를 사용하여 호환되지 않는 유형의 시스템 간의 데이터를 변환하는 기술

<aside>
🗒️ ORM의 역할

- django : Python objcet
- Database : SQL

둘의 언어가 다르기 때문에 소통이 불가능함

→ ORM이 중간에서 번역을 해줌

[[DB] ORM이란 - Heee's Development Blog](https://gmlwjd9405.github.io/2019/02/01/orm.html)

</aside>

---

## QuerySet API

- ORM에서 데이터를 검색, 필터링, 정렬 및 그룹화 하는데 사용하는 도구
- API를 사용하여 SQL이 아닌 Python 코드로 데이터를 처리
- SQL로 옮겨질 수 있는 문법

<aside>
❓ [QuerySet](https://docs.djangoproject.com/en/4.2/ref/models/querysets/)?

- DB로부터 전달받은 모델의 객체 목록
- DB로부터 데이터를 읽고, 필터를 걸거나 정렬을 할 수 있음
- django에서 QuerySet API를 DB로 전달하면 SQL로 변환하여 전달
- DB에서 SQL을 django로 전달하면 QuerySet( 다중 )이나 Instance( 단일 )로 변환하여 전달
- 단, DB가 단일한 객체를 반환할 때는 모델( class )의 인스턴스로 반환됨

[Django ORM(Querysets) · HonKit](https://tutorial.djangogirls.org/ko/django_orm/)

</aside>

<aside>
🗒️ Query

- 데이터베이스에 특정한 데이터를 보여 달라는 요청
- “쿼리문을 작성한다.” ⇒ 원하는 데이터를 얻기 위해 데이터베이스에 요청을 보낸 코드를 작성
- 파이썬 코드 → ORM → SQL / SQL → ORM → QuerySet
</aside>

```python
-----------------
QuerySet API 구문
-----------------

Article.objects.all()

# Article : Model class
# objects : Manager
# all() : Querysey API
# 메서드( all() )
# Model class.objects까지는 거의 고정
```

---

## QuerySet API 실습

<aside>
🗒️ 사전준비

- 외부 라이브러리 설치 및 설정

```bash
-------------------
외부 라이브러리 설치
-------------------

$ pip install ipython ( 인터프리터 언어인 파이썬을 리눅스와 쉘 같이 이용할 수 있도록 )
$ pip install django-extensions ( 
```

</aside>

### CRUD - Create