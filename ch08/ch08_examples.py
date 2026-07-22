"""
제8장: 예외 처리와 파일
알짜 파이썬 — 예제 코드 (원고에서 자동 추출)
"""

# ============================================================
# 오류와 예외
# ============================================================

# --- 구문 오류의 대표적인 예 ---
# 닫는 따옴표 누락 -- 구문 오류
print('Hello World!)
# SyntaxError: EOL while scanning string literal

# if 문 뒤에 콜론 누락
if True
    print('hello')
# SyntaxError: expected ':'

a, b = input('Enter two numbers: ').split()
result = int(a) / int(b) # b가 0이면 ZeroDivisionError 발생!

a, b = input('Enter two numbers: ').split()
result = int(a) / int(b)

# ============================================================
# try-except 문
# ============================================================

try:
    a, b = input('Enter two numbers: ').split()
    result = int(a) / int(b)
    print('{}/{} = {}'.format(a, b, result))
except:
    print('Please check if the numbers are correct.')

try:
    b = 2 / 0
    a = 1 + 'hundred'
except ZeroDivisionError:
    print('Division by zero error')
except TypeError:
    print('Unsupported operand type error')

try:
    b = 2 / 0
    a = 1 + 'hundred'
except Exception as e:
    print('error :', e)

# --- 구체적 예외와 일반 Exception을 함께 처리 ---
try:
# b = 2 / 0
    a = 1 + 'hundred'
except ZeroDivisionError: # 0으로 나누기 예외 처리
    print('Division by zero error')
except TypeError: # 지원되지 않는 자료형 연산 처리
    print('Unsupported operand type error')
except Exception as e: # 그 밖의 모든 예외 처리
    print('error :', e)
    print('Please check division and operand types.')

# --- else로 정상 실행 결과 출력 ---
try:
    a, b = input('Enter two numbers: ').split()
    result = int(a) / int(b)
except ZeroDivisionError:
    print('Error: cannot divide by zero.')
except ValueError:
    print('Error: please enter integers.')
except:
    print('Error: enter two numbers like 10 2.')
else: # 예외가 없을 때만 실행
    print('{} / {} = {}'.format(a, b, result))

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print('Division by zero error')
    else:
        print('Result:', result)
    finally:
        print('Done')

print('divide(100, 2) call:')
divide(100, 2)
print('divide(100, 0) call:')
divide(100, 0)

raise Exception('Exception raised')

def get_ans(ans):
    if ans in ['yes', 'no']:
        print('Valid input.')
    else:
        raise ValueError('Please enter yes or no.')

while True:
    try:
        ans = input('Enter yes or no: ')
        get_ans(ans)
        break
    except Exception as e:
        print('error:', e)

# ============================================================
# 파일 입출력
# ============================================================

# --- write()로 파일에 문자열 쓰기 ---
f = open('hello.txt', 'w') # 1) 쓰기 모드로 파일 열기
f.write('Hello World!\n') # 2) 파일에 문자열 쓰기
f.write('Python file I/O\n')
f.close() # 3) 파일 닫기

# --- writelines()로 여러 줄 한 번에 쓰기 ---
lines = ['First line\n', 'Second line\n', 'Third line\n']
f = open('lines.txt', 'w')
f.writelines(lines)
f.close()

# --- read, readline, readlines 비교 ---
# 파일 전체를 하나의 문자열로 읽기
f = open('hello.txt', 'r')
content = f.read()
print(content)
f.close()

# 한 번에 한 줄씩 읽기
f = open('hello.txt', 'r')
line1 = f.readline() # 첫 번째 줄
line2 = f.readline() # 두 번째 줄
print(line1, line2)
f.close()

# 모든 줄을 리스트로 읽기
f = open('hello.txt', 'r')
lines = f.readlines() # ['Hello World!\n', 'Python file I/O\n']
print(lines)
f.close()

f = open('hello.txt', 'r')
for line in f:
    print(line, end='') # 줄바꿈 중복 방지
f.close()

# with 문으로 파일 쓰기
with open('data.txt', 'w') as f:
    f.write('Name: Hong Gildong\n')
    f.write('Age: 20\n')
    f.write('Major: Computer Science\n')
# 블록이 끝나면 f.close()가 자동으로 호출됨

# with 문으로 파일 읽기
with open('data.txt', 'r') as f:
    for line in f:
        print(line, end='')

from pathlib import Path

p = Path('data') / 'scores.txt' # / 연산자로 경로 연결
print(p.exists()) # True/False
print(p.suffix) # '.txt'
print(p.stem) # 'scores'
print(p.parent) # PosixPath('data')

# 한 줄로 읽고 쓰기
p.write_text('hello', encoding='utf-8')
text = p.read_text(encoding='utf-8')

# 성적 데이터를 파일에 저장
students = [
    'Hong Gildong,85,90,78',
    'Kim Cheolsu,92,88,95',
    'Lee Younghee,76,82,89'
]

with open('scores.txt', 'w') as f:
    for s in students:
        f.write(s + '\n')

# 파일에서 성적을 읽어 평균 계산
with open('scores.txt', 'r') as f:
    for line in f:
        data = line.strip().split(',')
        name = data[0]
        scores = [int(x) for x in data[1:]]
        avg = sum(scores) / len(scores)
        print(f'{name}: Average {avg:.1f}')

try:
    with open('nonexistent.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print('Error: File does not exist.')
except PermissionError:
    print('Error: Permission denied.')

# ============================================================
# 실습을 통한 8장 개념 정리
# ============================================================

a = int(input('a: '))
b = int(input('b: '))
try:
    print(f'{a} / {b} = {a / b}')
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다')

while True:
    try:
        n = int(input('Enter an integer: '))
        break
    except ValueError:
        print('숫자만 입력하세요. 다시 시도하세요.')
print(f'{n} ** 2 = {n * n}')

with open('message.txt', 'w', encoding='utf-8') as f:
    f.write('Hello Python\n')
with open('message.txt', 'r', encoding='utf-8') as f:
    print(f.read())

nums = [10, 20, 30, 40, 50]

with open('numbers.txt', 'w', encoding='utf-8') as f:
    for n in nums:
        f.write(f'{n}\n')

total = 0
with open('numbers.txt', 'r', encoding='utf-8') as f:
    for line in f:
        total += int(line.strip())
print('Sum :', total)    # 150

def count_lines(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return sum(1 for _ in f)
    except FileNotFoundError:
        return -1

print(count_lines('numbers.txt'))
print(count_lines('no_such_file.txt'))    # -1

with open('scores.txt', 'w', encoding='utf-8') as f:
    f.write('85\n92\nabc\n77\n90\n')   # 숫자가 아닌 줄 하나 포함

total, count = 0, 0
with open('scores.txt', 'r', encoding='utf-8') as f:
    for line in f:
        try:
            total += int(line.strip())
            count += 1
        except ValueError:
            print('Skipped:', line.strip())

print(f'Valid: {count}, Avg: {total / count}')
