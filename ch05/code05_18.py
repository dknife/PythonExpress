# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제5장 리스트와 슬라이싱
# 코드 5.18: sort()와 reverse() 정렬 메소드

list1 = [20, 10, 40, 50, 30]

list1.sort() # 오름차순 정렬
print('Ascending:', list1)

list1.sort(reverse=True) # 내림차순 정렬
print('Descending:', list1)

list1.reverse() # 순서 뒤집기
print('Reversed:', list1)
