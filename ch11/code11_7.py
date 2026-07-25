# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제11장 파이썬다운 코딩과 넘파이
# 코드 11.7: 일반 함수로 성인 나이 필터링

def adult_func(n): # 나이가 19 이상이면 True, 아니면 False
    if n >= 19:
        return True
    else:
        return False

ages = [34, 39, 20, 18, 13, 54]
print('Adult list :')
for a in filter(adult_func, ages): # filter() 함수로 필터링
    print(a, end = ' ')
