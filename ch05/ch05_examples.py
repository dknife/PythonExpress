"""
제5장: 리스트와 슬라이싱
알짜 파이썬 — 예제 코드 (원고에서 자동 추출)
"""

# ============================================================
# 리스트의 생성과 인덱싱
# ============================================================

# --- 개별 변수로 여러 값을 저장하기 ---
score0 = 87
score1 = 84
score2 = 95
score3 = 67
score4 = 88
score5 = 94
score6 = 63

score_list = [87, 84, 95, 67, 88, 94, 63]
print(score_list)

fruits = ['banana', 'apple', 'orange', 'kiwi']
print(fruits)

mixed = [100, 200, 'apple', 400] # 서로 다른 자료형 저장 가능
print(mixed)

# --- 여러 가지 리스트 생성 방법 ---
list1 = list() # 빈 리스트
list2 = [] # 빈 리스트
list3 = list(range(1, 10)) # [1, 2,..., 9]
list4 = list('ABCDEF') # ['A', 'B', 'C', 'D', 'E', 'F']

a = [11, 22, 33, 44, 55, 66]
print(a[0]) # 첫 번째 요소
print(a[3]) # 네 번째 요소
print(a[5]) # 여섯 번째(마지막) 요소
print(len(a)) # 리스트의 길이

a = [11, 22, 33, 44, 55, 66]
print(a[-1]) # 마지막 요소: 66
print(a[-2]) # 뒤에서 두 번째 요소: 55
print(a[-6]) # 첫 번째 요소: 11

# ============================================================
# 리스트의 연산과 내장함수
# ============================================================

a = [1, 2, 3]
b = [4, 5, 6]
print(a + b) # 리스트 연결
print(a * 3) # 리스트 반복

a_list = [10, 20, 30, 40]
print(10 in a_list) # True
print(50 in a_list) # False
print(50 not in a_list) # True

n_list = [11, 22, 33, 44, 55, 66]

if 55 in n_list: # 55가 있으면 삭제
    n_list.remove(55)
if 88 in n_list: # 88은 없으므로 실행되지 않음
    n_list.remove(88)

print(n_list)

nums = [20, 10, 40, 50, 30]
print('Min:', min(nums))
print('Max:', max(nums))
print('Sum:', sum(nums))
print('Length:', len(nums))
print('Sorted:', sorted(nums))

fruits = ['banana', 'orange', 'apple', 'kiwi']
print(min(fruits)) # 사전 순으로 가장 앞: apple
print(max(fruits)) # 사전 순으로 가장 뒤: orange

# ============================================================
# 리스트와 반복문
# ============================================================

fruits = ['apple', 'banana', 'cherry', 'date']

for fruit in fruits:
    print(fruit)

scores = [87, 84, 95, 67, 88]
total = 0

for score in scores:
    total += score

average = total / len(scores)
print(f'Sum: {total}, Average: {average:.1f}')

nations = ['Korea', 'China', 'India', 'Nepal']

for i, nation in enumerate(nations):
    print(f'No.{i}: {nation}')

a_list = ['a', 'b', 'c', 'd', 'e']
a_list.append('f')
print(a_list)

n_list = [11, 22, 33, 44, 55, 66]
del n_list[3] # 네 번째 항목(44) 삭제
print(n_list)

n_list = [11, 22, 33, 44, 55, 66]
n_list.remove(44)
print(n_list)

names = [] # 빈 리스트 생성

for i in range(3):
    name = input(f'Name {i+1}: ')
    names.append(name)

print('Entered names:', names)

a = [1, 2, 3]
b = a # b는 같은 리스트를 가리키는 참조
b.append(4)
print(a)
c = a.copy() # c는 진정한 복사본
c.append(5)
print(a)

# ============================================================
# 리스트 메소드와 슬라이싱
# ============================================================

list1 = [20, 10, 40, 50, 30]

list1.sort() # 오름차순 정렬
print('Ascending:', list1)

list1.sort(reverse=True) # 내림차순 정렬
print('Descending:', list1)

list1.reverse() # 순서 뒤집기
print('Reversed:', list1)

a_list = ['a', 'b', 'c', 'd', 'e']
print(a_list.index('c')) # 2
print(a_list.count('a')) # 1

a_list.insert(1, 'x') # 인덱스 1 위치에 'x' 삽입
print(a_list)

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a[2:5]) # 인덱스 2부터 4까지
print(a[:4]) # 처음부터 인덱스 3까지
print(a[6:]) # 인덱스 6부터 끝까지
print(a[::2]) # 2칸 간격으로 추출
print(a[::-1]) # 역순으로 추출

# ============================================================
# 실습을 통한 5장 개념 정리
# ============================================================

scores = [85, 90, 78, 92, 88]
print('Max :', max(scores))
print('Min :', min(scores))
print('Sum :', sum(scores))
print('Avg :', sum(scores) / len(scores))

a = [1, 2, 3]
b = [4, 5, 6]
c = sorted(a + b, reverse=True)
print(c)             # [6, 5, 4, 3, 2, 1]

nums = [10, 25, 7, 42, 19, 33]
evens = []
for n in nums:
    if n % 2 == 0:
        evens.append(n)
print(evens)         # [10, 42]

colors = ['red', 'green', 'blue', 'yellow']
print(colors[::-1])   # 슬라이싱 이용
colors.reverse()      # reverse() 메소드 이용 (원본이 뒤집힘)
print(colors)

def list_avg(lst):
    if len(lst) == 0:
        return 0
    return sum(lst) / len(lst)

print(list_avg([1, 2, 3, 4, 5]))   # 3.0
print(list_avg([]))                # 0

fruits = ['apple', 'banana', 'cherry', 'kiwi']
for i, name in enumerate(fruits):
    print(f'{i}: {name}')

nums = [10, 20, 30, 40, 50, 60, 70, 80]
print(nums[:3])      # [10, 20, 30]
print(nums[-3:])     # [60, 70, 80]
print(nums[::2])     # [10, 30, 50, 70]

items = []
items.append(30); items.append(50); items.append(70)
print(items)        # [30, 50, 70]
items.insert(1, 40)
print(items)        # [30, 40, 50, 70]
items.pop()
print(items)        # [30, 40, 50]
items.remove(30)
print(items)        # [40, 50]
