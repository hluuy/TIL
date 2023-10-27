# csv 생성을 위해 import
import csv
import requests

# TMDB API Base URL
base_url = 'https://api.themoviedb.org/3/'
# TMDB API
API_KEY = ''

# 인기도 순 영화 정보 
get_popular = '/movie/popular'
# django PJT에서 필요로 하는 field목록
fields = ['title', 'overview', 'release_date', 'poster_path']

new_data = []   # response받은 영화 정보를 저장할 리스트
pk = 1          # csv 파일에 입력할 pk 1번부터 시작.

# 1 페이지당 20개의 영화정보, 20페이지 요청
for i in range(1, 20):
    # 요청 경로 : base_url + get_popular + api_key & page
    response = requests.get(f'{base_url}{get_popular}', params={'api_key':API_KEY, 'page':i} ).json()
    # 응답 받은 정보중, 영화 정보가 담긴 results만 순회하여 사용
    # results 리스트에는 각 영화 정보가 dict형태로 전달
    for res in response['results']:
        # 내가 필요한 field만 담을 dict 생성, pk는 영화 pk가 아니라 그냥 숫자를 사용할 예정
        # 만약 영화 pk를 쓸거라면 대체 가능
        movie_info = {
            'pk': pk
        }
        # 내 서비스에 필요한 field만 사용할 예정인데
        for field in fields:
            # TMDB에서 해당 필드에 데이터가 없을 경우도 있음
            # 예를 들어 release_date가 누락된 경우가 있을 수 있으므로, 찾고자하는 field가 포함된 영화정보만
            if res.get(field):
                # 내가 쓸 dict에 추가
                movie_info[field] = res[field]
            else:
                # field가 하나라도 누락되면 데이터 무결성을 헤칠 수 있으므로 무시
                break
        else:
            # break 되지 않고 정상적으로 dict 형성했다면
            # pk 1 증가시키고, 해당 데이터 리스트에 추가
            pk += 1
            new_data.append(movie_info)


# CSV 만들 준비
# CSV에는 pk 값도 담을 것이므로 field 목록에 pk 추가
fields = ['pk', 'title', 'overview', 'release_date', 'poster_path']
filename = 'movie_data.csv'

# movie_data.csv 파일을 생성하고 열어서 작성 시작
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    # 내 영화 정보들은 dict 형태로 저장했으므로 csv 파일을 열떄 dict를 읽어 쓸 수 있는 
    # DictWriter 사용, field명을 첫번째 줄에 표기
    csvwriter = csv.DictWriter(csvfile, fieldnames=fields)
    csvwriter.writeheader()
    # 각 행에 내 영화정보 삽입
    csvwriter.writerows(new_data)

# 생성된 movie_data.csv 파일을 확인하고, 정상적으로 만들어졌다면
# sqlite로 db.sqlite를 열어
# .mode csv
# .import file_name table_name
# 명령어를 사용하여 데이터 삽입
# fixtures의 dummy data 20개가 이미 삽입되어 있는 상태였다면 20개의 데이터가 UNIQUE한 값이 중복되어 넣을 수 없다고 할 것

# FAQ
# Q.actors 정보는 왜 없이 만들어요?
# A. actors 정보는 MTM 관계로, movies_movie 테이블에는 해당 컬럼 존재하지 않음
    # 만약 배우 정보도 담고싶다면 TMDB에서 각 영화의 pk를 토대로 배우 정보를 모아와야할 것.
    # 단, 주의할 점은, 현재 배우도, 영화도 pk값을 AUTO INCREAMENT로 증가하는 값으로만 되어 있음
    # 즉, 영화와 배우의 M:N관계 형성에 필요한 고유값 PK를 특정 할 수 없음.
    # TMDB의 영화와 배우의 정보를 토대로 M:N 관계를 형성하고 싶다면 TMDB에서 제공하는 영화와 배우의 PK 정보를 내 db에 담아야 할것
    # 이후, 중개모델 movies_movie_actors에 삽입할 두 모델의 관계를 csv 파일로 생성하여 추가하여야 함.

# Q. TMDB에서는 movie 정보와 actor 정보가 따로 있는데 어떻게 적절한 정보를 받아 올 수 있나요?
# A. 예를들어 get_popular로 영화정보를 가지고 온다면, 한번에 20개의 영화 정보를 받아오게 됨.
    # 이때, response.results에 들어있는 각 영화를 반복문으로 순회하면서 각 영화 PK를 토대로
    # 다시 TMDB에 요청을 보내면 됨. 영화 상세 정보가 필요하다면 detail/<movie_pk>/ 등의 형식으로 생성된 TMDB API에 재요청 보내고
    # 그렇게 받아온 정보중에 내가 필요한 정보만 별도로 전처리 하여 사용하면 됨
    # 내가 필요한 데이터의 모양으로 적절하게 전처리해 보기