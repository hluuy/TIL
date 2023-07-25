import pprint
import requests

# 응답 중 정기예금 상품들의 옵션 리스트를 출력하도록 구성합니다.
# 이 때, 원하는 데이터만 추출하여 새로운 리스트를 만들어 반환하는 함수를 작성하시오.
# [힌트] 아래와 같은 순서로 데이터를 출력하며 진행합니다.
# 1. 응답을 json 형식으로 변환합니다.
# 2. key 값이 "result" 인 데이터를 출력합니다.
# 3. 위의 결과 중 key 값이 "optionList" 인 데이터를 변수에 저장합니다.
# 4. 3번에서 저장된 값을 반복하며, 원하는 데이터만 추출 및 가공하여 결과 리스트에 저장합니다.

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
    # wanted_option = {}
    result = get_deposit_products()
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    # key_name = result['result']
    # pprint.pprint(key_name.keys())
    # data_base = result['result']['baseList']
    data_option = result['result']['optionList']
    translation = {
        'dcls_month': '공시제출월',
        'fin_co_no': '금융회사 코드',
        'fin_prdt_cd': '금융상품 코드',
        'intr_rate': '저축 금리',
        'intr_rate2': '최고 우대 금리',
        'intr_rate_type': '저축 금리 유형',
        'intr_rate_type_nm': '저축 금리 유형명',
        'save_trm': '저축 기간'
    }
    
      
    translated_data_option = [{translation[key]: value for key, value in dictionary.items()} for dictionary in data_option]

    pprint.pprint(translated_data_option)
