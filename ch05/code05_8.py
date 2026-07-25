# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제5장 리스트와 슬라이싱
# 코드 5.8: in 연산자로 안전하게 삭제하기

n_list = [11, 22, 33, 44, 55, 66]

if 55 in n_list: # 55가 있으면 삭제
    n_list.remove(55)
if 88 in n_list: # 88은 없으므로 실행되지 않음
    n_list.remove(88)

print(n_list)
