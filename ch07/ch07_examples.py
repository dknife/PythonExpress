"""
제7장: 모듈 활용
알짜 파이썬 — 예제 코드 (원고에서 자동 추출)
"""

# ============================================================
# 모듈과 import
# ============================================================

# --- import 문의 기본 형식 ---
import module_name1 [, module_name2,...]

# --- math 모듈을 import해서 사용 ---
import math
print(math.pi) # 3.141592653589793
print(math.sqrt(16)) # 4.0

# --- from import로 특정 요소만 가져오기 ---
from math import sqrt, pi
print(pi) # 3.141592653589793
print(sqrt(25)) # 5.0

# --- 별표로 모든 요소 가져오기 ---
from math import *
print(ceil(3.2)) # 4
print(floor(3.8)) # 3

# --- as로 모듈에 별칭 붙이기 ---
import datetime as dt # datetime -> dt
import random as rd # random -> rd
import math as m # math -> m
import turtle as t # turtle -> t

import datetime as dt
start_time = dt.datetime.now()
xmas = start_time.replace(month=12, day=25)  # 반환값을 새 변수에 저장
print(xmas)

# ============================================================
# 날짜와 시간 — datetime
# ============================================================

# --- 현재 날짜와 시간 얻기 ---
import datetime

# 현재 날짜와 시간
print(datetime.datetime.now())
# 2025-01-02 06:57:27.904565

# --- as 별칭으로 datetime 간결하게 쓰기 ---
import datetime as dt # dt라는 별칭 사용

start_time = dt.datetime.now()
print(start_time)

# --- from import로 datetime 직접 호출 ---
from datetime import datetime

start_time = datetime.now()
print(start_time)

# --- date.today()로 연·월·일 추출 ---
import datetime as dt

today = dt.date.today()
print(today) # 2026-04-06
print(today.year) # 2026
print(today.month) # 4
print(today.day) # 6

import datetime
print(dir(datetime))

import datetime as dt

start_time = dt.datetime.now()
# 월을 12, 일을 25로 변경
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
hundred = dt.timedelta(days = 100) # 100일

plus100day = dt.datetime.now() + hundred
print('100 days later =', plus100day)

minus100day = dt.datetime.now() - hundred
print('100 days ago =', minus100day)

# --- strftime()으로 날짜 문자열 포매팅 ---
import datetime as dt

now = dt.datetime.now()
print(now.strftime('%Y-%m-%d')) # 2026-04-06
print(now.strftime('%B %d, %Y')) # April 06, 2026
print(now.strftime('%H:%M:%S')) # 14:30:25

# ============================================================
# 수학과 난수 — math, random
# ============================================================

import math
print(dir(math)) # math 모듈의 모든 속성과 메소드 나열

# --- math 모듈의 상수와 주요 함수 ---
import math as m

print(m.pi) # 3.141592653589793 -- 원주율 상수
print(m.e) # 2.718281828459045 -- 자연상수 e
print(m.pow(3, 3)) # 27.0 -- 3의 3제곱
print(m.fabs(-99)) # 99.0 -- -99의 절대값
print(m.ceil(2.1)) # 3 -- 2.1의 올림
print(m.ceil(-2.1)) # -2 -- -2.1의 올림
print(m.floor(2.1)) # 2 -- 2.1의 내림
print(m.log(2.71828)) # 0.999999327... -- 자연로그
print(m.log(100, 10)) # 2.0 -- 밑이 10인 로그
print(m.sqrt(144)) # 12.0 -- 제곱근

# --- sin()에 각도를 직접 넣었을 때의 오류 ---
import math as m

print(m.sin(0.0)) # 0.0 -- 정상, sin(0) = 0
print(m.sin(90.0)) # 0.8939... -- sin(90도)가 아님!

# --- radians()로 각도를 라디안으로 변환 ---
import math as m

# pi/2를 직접 사용 -- 올바른 결과
print(m.sin(m.pi/2.0)) # 1.0

# 원주율 값
print(m.pi) # 3.141592653589793

# 90도를 라디안으로 변환한 후 sin 사용
print(m.radians(90)) # 1.5707963267948966 (pi/2)
print(m.sin(m.radians(90))) # 1.0 -- 올바른 결과!

# --- random 모듈의 기본 난수 함수 ---
import random as rd

print(rd.random()) # 0.0 이상 1.0 미만의 실수
print(rd.randint(1, 6)) # 1 이상 6 이하의 정수 (주사위)
print(rd.randrange(0, 10)) # 0 이상 9 이하의 정수

# --- choice, shuffle, sample로 리스트 다루기 ---
import random as rd

colors = ['red', 'blue', 'green', 'yellow', 'purple']
print(rd.choice(colors)) # 리스트에서 무작위로 하나 선택

rd.shuffle(colors) # 리스트를 무작위로 섞기 (원본 변경)
print(colors) # 순서가 무작위로 바뀜

print(rd.sample(colors, 3)) # 3개를 비복원 추출

import random as rd

lotto = rd.sample(range(1, 46), 6) # 1~45 중 6개 선택
lotto.sort()
print('This week lotto numbers:', lotto)

# ============================================================
# 외부 패키지 설치 — pip
# ============================================================

# --- numpy 배열 연산의 간결함 ---
import numpy as np

a = np.array([1, 2, 3, 4, 5])
print(a * 2) # [2 4 6 8 10] -- 요소별 곱셈
print(a.mean()) # 3.0 -- 평균
print(a.sum()) # 15 -- 합계

# ============================================================
# 정규표현식 — re
# ============================================================

import re

text = 'My phone is 010-1234-5678 and home is 02-555-7777.'

m = re.search(r'\d{2,3}-\d{3,4}-\d{4}', text)
print(m.group()) # 처음 일치한 부분 문자열

nums = re.findall(r'\d{2,3}-\d{3,4}-\d{4}', text)
print(nums) # 일치한 모든 부분의 리스트

cleaned = re.sub(r'\d', '*', text) # 모든 숫자를 *로 치환
print(cleaned)

import re

text = 'Contact: alice@example.com, bob.smith@univ.ac.kr, not_an_email@'
emails = re.findall(r'[\w.]+@[\w.]+\.[a-zA-Z]+', text)
print(emails)

def is_valid_email(s):
    pattern = r'^[\w.]+@[\w.]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, s) is not None

print(is_valid_email('alice@example.com'))
print(is_valid_email('not_an_email@'))

# ============================================================
# 실습을 통한 7장 개념 정리
# ============================================================

from datetime import datetime
now = datetime.now()
print(f"Today's date : {now.year}-{now.month}-{now.day}")
ampm = 'AM' if now.hour < 12 else 'PM'
h = now.hour if now.hour <= 12 else now.hour - 12
if h == 0:
    h = 12
print(f'Current time : {ampm} {h}:{now.minute:02d}:{now.second:02d}')

from datetime import date
today = date.today()
bday  = date(today.year, 5, 15)   # 자신의 생일로 변경
if bday < today:
    bday = date(today.year + 1, 5, 15)
remaining = (bday - today).days
print(f'{remaining} days left until my birthday.')

from datetime import date
y = int(input('Birth year : '))
m = int(input('Birth month: '))
d = int(input('Birth day  : '))
born  = date(y, m, d)
days  = (date.today() - born).days
print(f'{days} days have passed since you were born.')
print(f'Day of the week you were born: {born.strftime("%A")}')

from datetime import date, timedelta
y = int(input('Start year : '))
m = int(input('Start month: '))
d = int(input('Start day  : '))
start = date(y, m, d)
print('100th-day anniversary :', start + timedelta(days=100))

import re
text = 'I bought 3 apples, 5 pears, 12 oranges for 8400 won.'
nums = re.findall(r'\d+', text)
total = 0
for n in nums:
    total += int(n)
print('Found:', nums)
print('Sum  :', total)

import random
choices = ['scissors', 'rock', 'paper']
user = input('scissors/rock/paper: ').strip()
cpu  = random.choice(choices)
print(f'Computer: {cpu}')
win_pairs = {('scissors','paper'), ('rock','scissors'), ('paper','rock')}
if user == cpu:
    print('Draw')
elif (user, cpu) in win_pairs:
    print('You win!')
else:
    print('You lose!')
