"""
제11장: 파이썬다운 코딩과 넘파이
알짜 파이썬 — 예제 코드 (원고에서 자동 추출)
"""

# ============================================================
# 간결한 표현을 위한 람다 함수
# ============================================================

# 일반 함수를 이용한 덧셈
def add(x, y):
    return x + y

print('Sum of 100 and 200 :', add(100, 200))

# 람다 함수를 이용한 덧셈
add = lambda x, y: x + y
print('Sum of 100 and 200 :', add(100, 200))

# --- 람다 함수의 기본 문법 ---
lambda parameters : expression

# --- 람다 함수 정의와 즉시 호출 ---
# 람다 함수 정의와 호출
(lambda x, y : x + y)(100, 200) # 300을 반환

# 변수에 할당하지 않고 바로 호출
print('Sum of 100 and 200 :', (lambda x, y: x + y)(100, 200))

# ============================================================
# filter(), map()과 리스트 축약
# ============================================================

# --- filter() 함수의 문법 ---
filter(function, iterable)

def adult_func(n): # 나이가 19 이상이면 True, 아니면 False
    if n >= 19:
        return True
    else:
        return False

ages = [34, 39, 20, 18, 13, 54]
print('Adult list :')
for a in filter(adult_func, ages): # filter() 함수로 필터링
    print(a, end = ' ')

ages = [34, 39, 20, 18, 13, 54]
adult_ages = list(filter(lambda x: x >= 19, ages))
print('Adult list :', adult_ages)

n_list = [-30, 45, -5, -90, 20, 53, 77, -36]
minus_list = list(filter(lambda x: x < 0, n_list))
print('Negative list :', minus_list)

# --- map() 함수의 문법 ---
map(function, iterable,...)

a = [1, 2, 3, 4, 5, 6, 7]
square_a = []
for n in a:
    square_a.append(n ** 2) # n의 제곱을 square_a 리스트에 추가
print(square_a)

a = [1, 2, 3, 4, 5, 6, 7]
square_a = list(map(lambda x: x**2, a))
print(square_a)

a = [1, 2, 3, 4, 5, 6, 7]
square_a = list(map(lambda x: x**2, a))
cubic_a = list(map(lambda x: x**3, a))
print('square_a =', square_a)
print('cubic_a =', cubic_a)

# --- 리스트 축약 표현의 문법 ---
[expression for var in iterable] # map 기능
[expression for var in iterable if condition] # map + filter 기능

a = [1, 2, 3, 4, 5, 6, 7]
a = [x**2 for x in a] # 리스트의 각 요소에 x**2 적용
print(a)

a = [x**2 for x in range(1, 8)]
print(a)

st = 'Hello World'
s_list = [x.upper() for x in st]
print(s_list)

# --- filter와 람다 방식 ---
# filter와 람다를 사용한 방법
ages = [34, 39, 20, 18, 13, 54]
adult_ages = list(filter(lambda x: x >= 19, ages))
print('Adult list :', adult_ages)

# 리스트 축약 표현을 사용한 방법
ages = [34, 39, 20, 18, 13, 54]
print('Adult list :', [x for x in ages if x >= 19])

[x for x in range(10)]
[x * x for x in range(10)]
[x for x in range(10) if x % 2 == 0]
[x for x in range(10) if x % 2 == 1]
[x * x for x in range(10) if x % 2 == 0]
[x * x for x in range(10) if x % 2 == 1]

s = input('Enter 5 integers : ').split()
lst = [int(x) for x in s]
lst

# ============================================================
# 넘파이 라이브러리
# ============================================================

# --- 넘파이 관례적 임포트 ---
import numpy as np

import numpy as np

a = np.array([1, 2, 3]) # 리스트로 1차원 배열 생성
b = np.array([[1, 2], [3, 4]]) # 2차원 배열 생성
print('a =', a)
print('b =')
print(b)

a = np.array([1, 2, 3])
print('shape :', a.shape) # 배열의 형상
print('ndim :', a.ndim) # 차원의 개수
print('dtype :', a.dtype) # 원소의 자료형
print('size :', a.size) # 전체 원소의 개수
print('itemsize:', a.itemsize) # 원소 하나의 바이트 크기

print(np.zeros(5)) # 0으로 채운 배열
print(np.ones((2, 3))) # 1로 채운 2x3 배열
print(np.arange(0, 10, 2)) # 0부터 10 미만까지 간격 2
print(np.linspace(0, 1, 5)) # 0부터 1까지 균등 간격 값 5개
print(np.random.rand(3)) # 0과 1 사이의 난수 3개
print(np.random.randint(0, 10, size=5)) # 0~9 범위의 정수 난수 5개

import numpy as np
import time

n = 1_000_000

# 파이썬 리스트
py_list = list(range(n))
start = time.time()
result = [x**2 for x in py_list]
py_time = time.time() - start

# 넘파이 배열
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

student_mid = [70, 85, 90, 75] # 중간시험 점수
student_fin = [90, 65, 70, 85] # 기말시험 점수
student_sum = student_mid + student_fin
print(student_sum)
# student_sum / 2 # TypeError: unsupported operand type(s)

import numpy as np

student_mid = np.array([70, 85, 90, 75]) # 중간시험 점수
student_fin = np.array([90, 65, 70, 85]) # 기말시험 점수
student_sum = student_mid + student_fin
print('Total :', student_sum)
print('Average :', student_sum / 2)

sal = np.array([300, 360, 400, 380]) # 사원 4명의 급여
sal_bonus = sal + 100 # 각 급여에 상여금 100 더하기
sal_inc = sal * 1.2 # 각 급여를 20% 인상
print('After bonus:', sal_bonus)
print('After 20% raise:', sal_inc)

a = np.array([[1, 2], [3, 4]]) # 2차원 배열 a
b = np.array([[10, 20], [30, 40]]) # 2차원 배열 b

print('a + b =\n', a + b)
print('a * b =\n', a * b) # 원소별 곱셈
print('a @ b =\n', a @ b) # 행렬 곱셈

a = [[1, 2], [3, 4]]
b = [[1, 0], [0, 1]] # 단위행렬
print(np.matmul(a, b)) # 결과는 a 자신

a = np.array([10, 20, 30, 40, 50])

print(a[0]) # 첫 번째 원소
print(a[1:4]) # 슬라이싱
print(a[-1]) # 마지막 원소

# 불리언 인덱싱: 조건에 맞는 원소만 추출
print(a[a > 25]) # 25보다 큰 원소만

b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(b[0, 2]) # 0행 2열의 원소: 3
print(b[1, :]) # 1행 전체: [4, 5, 6]
print(b[:, 0]) # 0열 전체: [1, 4, 7]
print(b[0:2, 1:3]) # 0~1행, 1~2열 부분 배열

data = np.array([23, 45, 67, 7, 2, 30, 34, 82])
print('Max :', data.max())
print('Min :', data.min())
print('Mean :', data.mean())
print('Sum :', data.sum())
print('Sort :', np.sort(data))

a = np.array([[1, 1], [2, 2], [3, 3]])
print(a.flatten()) # 1차원 배열로 평탄화

# ============================================================
# 실습을 통한 11장 개념 정리
# ============================================================

squares = [n * n for n in range(1, 11)]
print(squares)     # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

words = ['apple', 'banana', 'cherry']
length_map = {w: len(w) for w in words}
print(length_map)    # {'apple': 5, 'banana': 6, 'cherry': 6}

nums = [3, 8, 15, 4, 22, 7, 19]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)         # [8, 4, 22]

import numpy as np

a = np.arange(1, 11)      # [ 1  2  3  4  5  6  7  8  9 10]
print('Mean :', a.mean())
print('Sum  :', a.sum())
print('Std  :', a.std())
print('Max  :', a.max())

import numpy as np

scores = np.array([
    [85, 92, 78],
    [90, 88, 95],
    [76, 80, 70],
])
boosted = scores + 5           # 브로드캐스팅
print(boosted)
print('학생별 평균 :', boosted.mean(axis=1))

import numpy as np
import time

N = 10_000_000

# 1) 순수 파이썬: range에 대한 리스트 축약 표현
start = time.time()
ys_py = [x * x + 2 * x + 1 for x in range(N)]
t_py = time.time() - start

# 2) 넘파이: ndarray의 벡터화 연산
arr = np.arange(N)
start = time.time()
ys_np = arr * arr + 2 * arr + 1
t_np = time.time() - start

print(f'Python list  : {t_py:.3f} sec')
print(f'NumPy array  : {t_np:.3f} sec')
print(f'Speedup      : {t_py / t_np:.1f}x')
