# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제3장 조건문과 반복문
# 코드 3.20: while True와 break를 이용한 입력 처리

while True:
    text = input('문장을 입력하세요(끝내려면 종료): ')
    if text == '종료':
        print('안녕히 가세요!')
        break
    print(f'입력한 내용: {text}')
