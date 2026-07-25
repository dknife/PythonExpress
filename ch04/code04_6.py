# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제4장 함수와 입출력
# 코드 4.6: 기본값을 가진 매개변수

def greet(name, greeting='Hello'):
    print(f'{greeting}, {name}!')

greet('Alice') # 기본값 사용
greet('Bob', 'Nice to meet you') # 기본값 대신 전달한 값 사용
