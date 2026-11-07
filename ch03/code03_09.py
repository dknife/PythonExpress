# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제3장 조건문과 반복문
# 코드 3.9: 중첩 조건문  —  nested_if.py

age = int(input('나이를 입력하세요: '))
if age >= 20:
    if age >= 65:
        print('경로 우대 할인')
    else:
        print('일반 성인')
else:
    print('미성년자')
