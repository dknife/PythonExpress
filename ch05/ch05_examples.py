"""
제5장: 리스트와 슬라이싱
으뜸 파이썬 Express — 예제 코드
"""

# ============================================================
# 리스트의 생성과 인덱싱
# ============================================================

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

mixed = [100, 200, 'apple', 400]  # different types allowed
print(mixed)

list1 = list()          # empty list
list2 = []              # empty list
list3 = list(range(1, 10))  # [1, 2, ..., 9]
list4 = list('ABCDEF')  # ['A', 'B', 'C', 'D', 'E', 'F']

a = [11, 22, 33, 44, 55, 66]
print(a[0])   # first element
print(a[3])   # fourth element
print(a[5])   # sixth (last) element
print(len(a)) # length of the list

a = [11, 22, 33, 44, 55, 66]
print(a[-1])  # last element: 66
print(a[-2])  # second from last: 55
print(a[-6])  # first element: 11

# ============================================================
# 리스트의 연산과 내장함수
# ============================================================

a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)    # list concatenation
print(a * 3)    # list repetition

a_list = [10, 20, 30, 40]
print(10 in a_list)      # True
print(50 in a_list)      # False
print(50 not in a_list)  # True

n_list = [11, 22, 33, 44, 55, 66]

if 55 in n_list:      # remove 55 if present
    n_list.remove(55)
if 88 in n_list:      # 88 is not present, so not executed
    n_list.remove(88)

print(n_list)

nums = [20, 10, 40, 50, 30]
print('Min:', min(nums))
print('Max:', max(nums))
print('Sum:', sum(nums))
print('Length:', len(nums))
print('Sorted:', sorted(nums))

fruits = ['banana', 'orange', 'apple', 'kiwi']
print(min(fruits))  # lexicographically first: apple
print(max(fruits))  # lexicographically last: orange

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
del n_list[3]  # delete fourth item (44)
print(n_list)

n_list = [11, 22, 33, 44, 55, 66]
n_list.remove(44)
print(n_list)

names = []  # create empty list

for i in range(3):
    name = input(f'Name {i+1}: ')
    names.append(name)

print('Entered names:', names)

a = [1, 2, 3]
b = a          # b is a reference to the same list
b.append(4)
print(a)
c = a.copy()   # c is a true copy
c.append(5)
print(a)

# ============================================================
# 리스트 메소드와 슬라이싱
# ============================================================

list1 = [20, 10, 40, 50, 30]

list1.sort()  # ascending sort
print('Ascending:', list1)

list1.sort(reverse=True)  # descending sort
print('Descending:', list1)

list1.reverse()  # reverse order
print('Reversed:', list1)

a_list = ['a', 'b', 'c', 'd', 'e']
print(a_list.index('c'))  # 2
print(a_list.count('a'))  # 1

a_list.insert(1, 'x')  # insert 'x' at index 1
print(a_list)


a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a[2:5])    # index 2 to 4
print(a[:4])     # start to index 3
print(a[6:])     # index 6 to end
print(a[::2])    # every 2nd element
print(a[::-1])   # reversed

s = 'Hello, Python!'
print(s[7:13])    # Python
print(s[:5])      # Hello
print(s[::-1])    # !nohtyP ,olleH
