# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제4장 함수와 입출력
# 코드 4.13: 유클리드 호제법으로 최대공약수 구하기

def gcd(a, b):
    if b == 0: # 기저 조건
        return a
    return gcd(b, a % b) # 재귀 단계

print(gcd(48, 18)) # 6
print(gcd(100, 75)) # 25
