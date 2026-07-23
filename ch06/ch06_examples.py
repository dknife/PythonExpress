"""
제6장: 딕셔너리, 튜플, 집합
알짜 파이썬 — 예제 코드 (원고에서 자동 추출)
"""

# ============================================================
# 딕셔너리
# ============================================================

person = {'name': 'Hong Gildong', 'age': 26, 'weight': 82}
print(person['name'])
print(person['age'])
print(person['weight'])

students = {2024001: 'Lee Sunsin', 2024002: 'Kim Yusin', 2024003: 'Kang Gamchan'}
print(students[2024001])
print(students[2024003])

person = {'name': 'Hong Gildong', 'age': 26, 'weight': 82}

# 항목 추가
person['job'] = 'King of Yuldo'
print(person)

# 항목 수정
person['age'] = 27
print(person)

# 항목 삭제
del person['weight']
print(person)

person = {'name': 'Hong Gildong', 'age': 26, 'weight': 82}

print(person.keys())
print(person.values())
print(person.items())

person = {'name': 'Hong Gildong', 'age': 26, 'weight': 82}

for key in person:
    print(f'{key} : {person[key]}')

# ============================================================
# 튜플
# ============================================================

t1 = (1, 2, 3, 4) # 소괄호 사용
t2 = 10, 20, 30 # 괄호 생략 가능
t3 = tuple([1, 2, 3]) # 리스트로부터 생성
t4 = () # 빈 튜플

print(t1)
print(t2)
print(type(t1))

t = (0, 1, 2, 3, 4)
print(t[0]) # 0
print(t[-1]) # 4

# t[0] = 100 # TypeError 발생!

# 패킹
point = (3, 4)

# 언패킹
x, y = point
print(f'x = {x}, y = {y}')

# 변수 교환
a, b = 10, 20
a, b = b, a # 파이썬의 간편한 변수 교환
print(f'a = {a}, b = {b}')

def get_min_max(numbers):
    return min(numbers), max(numbers) # 튜플로 반환

data = [45, 23, 78, 12, 67]
minimum, maximum = get_min_max(data)
print(f'Min: {minimum}, Max: {maximum}')

# ============================================================
# 집합
# ============================================================

s1 = {1, 2, 3, 4, 5}
s2 = set([1, 2, 2, 3, 3, 3]) # 중복 자동 제거
s3 = set('hello') # 문자열로부터 생성
s4 = set() # 빈 집합 ({}은 빈 딕셔너리)

print(s1)
print(s2)
print(s3)

numbers = [1, 3, 2, 3, 1, 5, 2, 4, 5]
unique = list(set(numbers))
print(unique)

A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}

print('Union:', A | B) # 또는 A.union(B)
print('Intersection:', A & B) # 또는 A.intersection(B)
print('Difference:', A - B) # 또는 A.difference(B)
print('Symmetric diff:', A ^ B) # 또는 A.symmetric_difference(B)

s = {1, 2, 3}

s.add(4) # 원소 추가
print(s)

s.remove(2) # 원소 삭제 (없으면 KeyError)
print(s)

s.discard(99) # 원소 삭제 (없어도 오류 없음)
print(s)

print(3 in s) # 원소 존재 확인: True

# ============================================================
# 자료형 비교와 선택
# ============================================================

# 리스트 -> 튜플 -> 집합 변환
my_list = [1, 2, 3, 2, 1]

my_tuple = tuple(my_list)
print('Tuple:', my_tuple)

my_set = set(my_list)
print('Set:', my_set)

back_to_list = list(my_set)
print('List:', back_to_list)

person = {'name': 'Hong Gildong', 'age': 26}

print(list(person)) # 키의 리스트
print(list(person.values())) # 값의 리스트
print(list(person.items())) # (키, 값) 튜플의 리스트

# 딕셔너리: 과일 가격
fruits_dic = {'apple': 6000, 'melon': 3000,
    'banana': 5000, 'orange': 4000}

# 리스트: 모든 키를 리스트로
fruit_names = list(fruits_dic.keys())
print('Fruit list:', fruit_names)

# 집합: 할인 대상 과일
discount_set = {'apple', 'grape', 'melon'}
available_discount = discount_set & set(fruit_names)
print('Discountable:', available_discount)

# 튜플: 가격 범위 (불변)
price_range = (min(fruits_dic.values()),
    max(fruits_dic.values()))
print('Price range:', price_range)

# ============================================================
# 실습을 통한 6장 개념 정리
# ============================================================

fruits = {'apple': 1500, 'banana': 800, 'grape': 3000}
for name, price in fruits.items():
    print(f'{name}: {price} won')

s = 'hello world'
count = {}
for ch in s:
    count[ch] = count.get(ch, 0) + 1
print(count)

math = {'Kim', 'Lee', 'Park', 'Choi'}
eng  = {'Lee', 'Choi', 'Jung', 'Han'}
print('Both      :', math & eng)    # 교집합
print('Math only :', math - eng)    # 차집합
print('Either    :', math | eng)    # 합집합

nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print(sorted(set(nums)))    # [1, 2, 3, 4, 5, 6, 9]

def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

print(distance((0, 0), (3, 4)))   # 5.0
print(distance((1, 2), (4, 6)))   # 5.0

def stats(nums):
    return min(nums), max(nums), sum(nums) / len(nums)

lo, hi, avg = stats([72, 88, 91, 65, 80])
print(f'Min: {lo}, Max: {hi}, Avg: {avg}')

scores = {'Kim': 85, 'Lee': 92, 'Park': 78, 'Choi': 90}
top = max(scores, key=scores.get)
print(f'Top student: {top} ({scores[top]})')

a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]
print(sorted(set(a) & set(b)))   # [3, 4, 5]
print(sorted(set(a) - set(b)))   # [1, 2]
print(sorted(set(a) | set(b)))   # [1, 2, 3, 4, 5, 6, 7]
