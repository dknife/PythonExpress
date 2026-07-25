# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제3장 조건문과 반복문
# 코드 3.20: while True와 break를 이용한 입력 처리

while True:
    text = input('Enter text (quit to exit): ')
    if text == 'quit':
        print('Goodbye!')
        break
    print(f'You entered: {text}')
