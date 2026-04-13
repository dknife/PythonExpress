"""
제6장: 딕셔너리, 튜플, 집합
으뜸 파이썬 Express — 예제 코드
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

# add an item
person['job'] = 'King of Yuldo'
print(person)

# modify an item
person['age'] = 27
print(person)

# delete an item
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

t1 = (1, 2, 3, 4)      # using parentheses
t2 = 10, 20, 30        # parentheses optional
t3 = tuple([1, 2, 3])  # created from list
t4 = ()                 # empty tuple

print(t1)
print(t2)
print(type(t1))


t = (0, 1, 2, 3, 4)
print(t[0])    # 0
print(t[-1])   # 4

# t[0] = 100   # TypeError raised!

# packing
point = (3, 4)

# unpacking
x, y = point
print(f'x = {x}, y = {y}')

# swapping variables
a, b = 10, 20
a, b = b, a  # Python's convenient variable swap
print(f'a = {a}, b = {b}')

def get_min_max(numbers):
    return min(numbers), max(numbers)  # return as tuple

data = [45, 23, 78, 12, 67]
minimum, maximum = get_min_max(data)
print(f'Min: {minimum}, Max: {maximum}')

# ============================================================
# 집합
# ============================================================

s1 = {1, 2, 3, 4, 5}
s2 = set([1, 2, 2, 3, 3, 3])  # duplicates auto-removed
s3 = set('hello')              # created from string
s4 = set()                     # empty set ({} is empty dict)

print(s1)
print(s2)
print(s3)

numbers = [1, 3, 2, 3, 1, 5, 2, 4, 5]
unique = list(set(numbers))
print(unique)

A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}

print('Union:', A | B)            # or A.union(B)
print('Intersection:', A & B)     # or A.intersection(B)
print('Difference:', A - B)       # or A.difference(B)
print('Symmetric diff:', A ^ B)   # or A.symmetric_difference(B)

s = {1, 2, 3}

s.add(4)        # add element
print(s)

s.remove(2)     # remove element (KeyError if absent)
print(s)

s.discard(99)   # remove element (no error if absent)
print(s)

print(3 in s)   # membership check: True

# ============================================================
# 자료형 비교와 선택
# ============================================================

# list -> tuple -> set conversion
my_list = [1, 2, 3, 2, 1]

my_tuple = tuple(my_list)
print('Tuple:', my_tuple)

my_set = set(my_list)
print('Set:', my_set)

back_to_list = list(my_set)
print('List:', back_to_list)

person = {'name': 'Hong Gildong', 'age': 26}

print(list(person))            # list of keys
print(list(person.values()))   # list of values
print(list(person.items()))    # list of (key, value) tuples

# dictionary: fruit prices
fruits_dic = {'apple': 6000, 'melon': 3000,
              'banana': 5000, 'orange': 4000}

# list: all keys as a list
fruit_names = list(fruits_dic.keys())
print('Fruit list:', fruit_names)

# set: discount target fruits
discount_set = {'apple', 'grape', 'melon'}
available_discount = discount_set & set(fruit_names)
print('Discountable:', available_discount)

# tuple: price range (immutable)
price_range = (min(fruits_dic.values()),
               max(fruits_dic.values()))
print('Price range:', price_range)
