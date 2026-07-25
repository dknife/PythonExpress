# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제4장 함수와 입출력
# 코드 4.11: 2차 방정식의 두 근을 반환

def get_root(a, b, c):
    r1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
    r2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
    return r1, r2 # 두 값을 반환

result1, result2 = get_root(1, 2, -8)
print('The roots are', result1, 'or', result2)
