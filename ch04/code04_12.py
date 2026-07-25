# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제4장 함수와 입출력
# 코드 4.12: 재귀로 구현한 팩토리얼

def factorial(n):
    if n <= 1: # 기저 조건
        return 1
    return n * factorial(n - 1) # 재귀 단계

print(factorial(5)) # 120
print(factorial(7)) # 5040
