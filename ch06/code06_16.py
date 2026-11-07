# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제6장 딕셔너리, 튜플, 집합
# 코드 6.16: 자료형을 조합한 과일 가게 프로그램

# 딕셔너리: 과일 가격
fruits_dic = {'사과': 6000, '멜론': 3000,
    '바나나': 5000, '오렌지': 4000}

# 리스트: 모든 키를 리스트로
fruit_names = list(fruits_dic.keys())
print('과일 목록:', fruit_names)

# 집합: 할인 대상 과일
discount_set = {'사과', '포도', '멜론'}
available_discount = discount_set & set(fruit_names)
print('할인 가능:', available_discount)

# 튜플: 가격 범위 (불변)
price_range = (min(fruits_dic.values()),
    max(fruits_dic.values()))
print('가격 범위:', price_range)
