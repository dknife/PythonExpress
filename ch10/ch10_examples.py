"""
제10장: 파이썬다운 코딩과 넘파이
으뜸 파이썬 Express — 예제 코드
"""

# ============================================================
# 간결한 표현을 위한 람다 함수
# ============================================================

# addition using a regular function
def add(x, y):
    return x + y

print('Sum of 100 and 200 :', add(100, 200))

# addition using a lambda function
add = lambda x, y: x + y
print('Sum of 100 and 200 :', add(100, 200))

lambda parameters : expression

# lambda definition and call
(lambda x, y : x + y)(100, 200)   # returns 300

# call directly without assigning to a variable
print('Sum of 100 and 200 :', (lambda x, y: x + y)(100, 200))

# ============================================================
# filter(), map()과 리스트 축약
# ============================================================

filter(function, iterable)

def adult_func(n):  # True if age >= 19, False otherwise
    if n >= 19:
        return True
    else:
        return False

ages = [34, 39, 20, 18, 13, 54]
print('Adult list :')
for a in filter(adult_func, ages):  # filtering using filter()
    print(a, end = ' ')

ages = [34, 39, 20, 18, 13, 54]
adult_ages = list(filter(lambda x: x >= 19, ages))
print('Adult list :', adult_ages)

n_list = [-30, 45, -5, -90, 20, 53, 77, -36]
minus_list = list(filter(lambda x: x < 0, n_list))
print('Negative list :', minus_list)

map(function, iterable, ...)

a = [1, 2, 3, 4, 5, 6, 7]
square_a = []
for n in a:
    square_a.append(n ** 2)  # add n squared to square_a list
print(square_a)

a = [1, 2, 3, 4, 5, 6, 7]
square_a = list(map(lambda x: x**2, a))
print(square_a)

a = [1, 2, 3, 4, 5, 6, 7]
square_a = list(map(lambda x: x**2, a))
cubic_a = list(map(lambda x: x**3, a))
print('square_a =', square_a)
print('cubic_a =', cubic_a)

[expression for var in iterable]             # map functionality
[expression for var in iterable if condition]  # map + filter functionality

a = [1, 2, 3, 4, 5, 6, 7]
a = [x**2 for x in a]  # apply x**2 to each element of the list
print(a)

a = [x**2 for x in range(1, 8)]
print(a)

st = 'Hello World'
s_list = [x.upper() for x in st]
print(s_list)

# filter + lambda approach
ages = [34, 39, 20, 18, 13, 54]
adult_ages = list(filter(lambda x: x >= 19, ages))
print('Adult list :', adult_ages)

# list comprehension approach
ages = [34, 39, 20, 18, 13, 54]
print('Adult list :', [x for x in ages if x >= 19])

>>> [x for x in range(10)]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> [x * x for x in range(10)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> [x for x in range(10) if x % 2 == 0]
[0, 2, 4, 6, 8]
>>> [x for x in range(10) if x % 2 == 1]
[1, 3, 5, 7, 9]
>>> [x * x for x in range(10) if x % 2 == 0]
[0, 4, 16, 36, 64]
>>> [x * x for x in range(10) if x % 2 == 1]
[1, 9, 25, 49, 81]

>>> s = input('Enter 5 integers : ').split()
Enter 5 integers : 10 20 30 40 50
>>> lst = [int(x) for x in s]
>>> lst
[10, 20, 30, 40, 50]

# ============================================================
# 넘파이 라이브러리
# ============================================================

# install from terminal
# $ pip install numpy

import numpy as np

import numpy as np

a = np.array([1, 2, 3])           # create 1D array from list
b = np.array([[1, 2], [3, 4]])    # create 2D array
print('a =', a)
print('b =')
print(b)

a = np.array([1, 2, 3])
print('shape  :', a.shape)      # shape of array
print('ndim   :', a.ndim)       # number of dimensions
print('dtype  :', a.dtype)      # data type of elements
print('size   :', a.size)       # total number of elements
print('itemsize:', a.itemsize)  # byte size of each element

print(np.zeros(5))           # array filled with 0s
print(np.ones((2, 3)))       # 2x3 array filled with 1s
print(np.arange(0, 10, 2))   # 0 to under 10, step 2
print(np.linspace(0, 1, 5))  # 5 evenly spaced values from 0 to 1
print(np.random.rand(3))     # 3 random numbers between 0 and 1
print(np.random.randint(0, 10, size=5))  # 5 random integers 0~9

import numpy as np
import time

n = 1_000_000

# Python list
py_list = list(range(n))
start = time.time()
result = [x**2 for x in py_list]
py_time = time.time() - start

# NumPy array
np_arr = np.arange(n)
start = time.time()
result = np_arr ** 2
np_time = time.time() - start

print(f'List comprehension : {py_time:.4f} sec')
print(f'NumPy vectorization: {np_time:.4f} sec')
print(f'NumPy is {py_time/np_time:.1f}x faster')

# ============================================================
# 배열 연산과 인덱싱
# ============================================================

student_mid = [70, 85, 90, 75]   # midterm scores
student_fin = [90, 65, 70, 85]   # final scores
student_sum = student_mid + student_fin
print(student_sum)
# student_sum / 2  # TypeError: unsupported operand type(s)

import numpy as np

student_mid = np.array([70, 85, 90, 75])  # midterm scores
student_fin = np.array([90, 65, 70, 85])  # final scores
student_sum = student_mid + student_fin
print('Total :', student_sum)
print('Average :', student_sum / 2)

sal = np.array([300, 360, 400, 380])  # salaries of 4 employees
sal_bonus = sal + 100       # add 100 bonus to each
sal_inc = sal * 1.2          # 20% raise for each
print('100만 원 보너스 추가 후:', sal_bonus)
print('20% 인상된 급여:', sal_inc)

a = np.array([[1, 2], [3, 4]])      # 2D array a
b = np.array([[10, 20], [30, 40]])  # 2D array b

print('a + b =\n', a + b)
print('a * b =\n', a * b)    # element-wise multiplication
print('a @ b =\n', a @ b)    # matrix multiplication

a = [[1, 2], [3, 4]]
b = [[1, 0], [0, 1]]    # identity matrix
print(np.matmul(a, b))   # result is a itself

a = np.array([10, 20, 30, 40, 50])

print(a[0])       # first element
print(a[1:4])     # slicing
print(a[-1])      # last element

# boolean indexing: extract elements matching condition
print(a[a > 25])  # elements greater than 25 only

b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(b[0, 2])      # row 0, col 2: 3
print(b[1, :])      # entire row 1: [4, 5, 6]
print(b[:, 0])      # entire col 0: [1, 4, 7]
print(b[0:2, 1:3])  # rows 0~1, cols 1~2 subarray

data = np.array([23, 45, 67, 7, 2, 30, 34, 82])
print('Max  :', data.max())
print('Min  :', data.min())
print('Mean :', data.mean())
print('Sum  :', data.sum())
print('Sort :', np.sort(data))

a = np.array([[1, 1], [2, 2], [3, 3]])
print(a.flatten())  # flatten to 1D array
