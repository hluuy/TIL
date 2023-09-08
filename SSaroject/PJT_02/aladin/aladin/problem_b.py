import requests
from pprint import pprint


def best_review_books():
    # 여기에 코드를 작성합니다.  
    URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'

    params = {
        'ttbkey': 'ttbdudwns12891705001',
        'Query': '파울로 코엘료',
        'QueryType': 'Author',
        'MaxResults' : 20,
        'start' : 1,
        'SearchTarget' : 'Book',
        'output' : 'js',
        'Version' : '20131101'
    }

    response = requests.get(URL, params=params).json()

    lst = response['item']

    result = []
    for l in lst:
        if l['customerReviewRank'] >= 9:
            result.append(l)
    return result



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':

    pprint(best_review_books())
