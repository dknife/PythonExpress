"""
제7장: 모듈 활용
으뜸 파이썬 Express — 예제 코드
"""

# ============================================================
# 모듈과 import
# ============================================================

import module_name1 [, module_name2, ...]

import math
print(math.pi)        # 3.141592653589793
print(math.sqrt(16))  # 4.0

from math import sqrt, pi
print(pi)        # 3.141592653589793
print(sqrt(25))  # 5.0

from math import *
print(ceil(3.2))   # 4
print(floor(3.8))  # 3

import datetime as dt      # datetime -> dt
import random as rd        # random -> rd
import math as m           # math -> m
import turtle as t         # turtle -> t

import datetime as dt
start_time = dt.datetime.now()
start_time.replace(month = 12, day = 25)

# ============================================================
# 날짜와 시간 \{
# ============================================================

import datetime

# current date and time
print(datetime.datetime.now())
# datetime.datetime(2025, 1, 2, 6, 57, 27, 904565)

import datetime as dt     # use alias dt

start_time = dt.datetime.now()
print(start_time)

from datetime import datetime

start_time = datetime.now()
print(start_time)

import datetime as dt

today = dt.date.today()
print(today)        # 2026-04-06
print(today.year)   # 2026
print(today.month)  # 4
print(today.day)    # 6

import datetime
print(dir(datetime))

import datetime as dt

start_time = dt.datetime.now()
# change month to 12 and day to 25
new_time = start_time.replace(month = 12, day = 25)
print(new_time)

import datetime as dt

today = dt.date.today()
print(f'Today is {today.year}/{today.month}/{today.day}.')

xMas = dt.datetime(2026, 12, 25)
gap = xMas - dt.datetime.now()

print(f'Christmas is {gap.days} days {gap.seconds // 3600} hours away.')

import datetime as dt

print('Today =', dt.datetime.now())
hundred = dt.timedelta(days = 100)   # 100 days

plus100day = dt.datetime.now() + hundred
print('100 days later =', plus100day)

minus100day = dt.datetime.now() - hundred
print('100 days ago =', minus100day)

import datetime as dt

now = dt.datetime.now()
print(now.strftime('%Y-%m-%d'))       # 2026-04-06
print(now.strftime('%B %d, %Y'))      # April 06, 2026
print(now.strftime('%H:%M:%S'))       # 14:30:25


# ============================================================
# 수학과 난수 \{
# ============================================================

import math
print(dir(math))  # list all attributes and methods of math module

import math as m

print(m.pi)           # 3.141592653589793 -- pi constant
print(m.e)            # 2.718281828459045 -- e constant
print(m.pow(3, 3))    # 27.0 -- 3 to the power of 3
print(m.fabs(-99))    # 99.0 -- absolute value of -99
print(m.ceil(2.1))    # 3 -- ceiling of 2.1
print(m.ceil(-2.1))   # -2 -- ceiling of -2.1
print(m.floor(2.1))   # 2 -- floor of 2.1
print(m.log(2.71828)) # 0.999999327... -- natural logarithm
print(m.log(100, 10)) # 2.0 -- log base 10 of 100
print(m.sqrt(144))    # 12.0 -- square root

import math as m

print(m.sin(0.0))    # 0.0 -- correct, sin(0) = 0
print(m.sin(90.0))   # 0.8939... -- NOT sin(90 degrees)!

import math as m

# using pi/2 directly -- correct result
print(m.sin(m.pi/2.0))       # 1.0

# pi value
print(m.pi)                  # 3.141592653589793

# convert 90 degrees to radians, then use sin
print(m.radians(90))         # 1.5707963267948966 (pi/2)
print(m.sin(m.radians(90)))  # 1.0 -- correct result!

import random as rd

print(rd.random())         # float between 0.0 and 1.0
print(rd.randint(1, 6))    # integer between 1 and 6 (dice roll)
print(rd.randrange(0, 10)) # integer between 0 and 9

import random as rd

colors = ['red', 'blue', 'green', 'yellow', 'purple']
print(rd.choice(colors))    # pick one randomly from list

rd.shuffle(colors)          # shuffle list in-place
print(colors)               # order changed randomly

print(rd.sample(colors, 3)) # sample 3 without replacement

import random as rd

lotto = rd.sample(range(1, 46), 6)  # pick 6 from 1~45
lotto.sort()
print('This week lotto numbers:', lotto)

# ============================================================
# 외부 패키지 설치 \{
# ============================================================



import numpy as np

a = np.array([1, 2, 3, 4, 5])
print(a * 2)       # [2 4 6 8 10] -- element-wise multiplication
print(a.mean())    # 3.0 -- average
print(a.sum())     # 15  -- sum

