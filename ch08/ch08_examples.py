"""
제8장: 예외 처리와 파일
으뜸 파이썬 Express — 예제 코드
"""

# ============================================================
# 오류와 예외
# ============================================================

# missing closing quote -- syntax error
print('Hello World! )
# SyntaxError: EOL while scanning string literal

# missing colon after if statement
if True
    print('hello')
# SyntaxError: expected ':'

a, b = input('Enter two numbers: ').split()
result = int(a) / int(b)  # ZeroDivisionError if b is 0!

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

try:
#   b = 2 / 0
    a = 1 + 'hundred'
except ZeroDivisionError:        # handle division by zero
    print('Division by zero error')
except TypeError:                # handle unsupported operand type
    print('Unsupported operand type error')
except Exception as e:           # handle all other exceptions
    print('error :', e)
    print('Please check division and operand types.')

try:
    a, b = input('Enter two numbers: ').split()
    result = int(a) / int(b)
except ZeroDivisionError:
    print('Error: cannot divide by zero.')
except ValueError:
    print('Error: please enter integers.')
except:
    print('Error: enter two numbers like 10 2.')
else:    # runs only if no exception occurred
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

>>> raise Exception('Exception raised')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    raise Exception('Exception raised')
Exception: Exception raised

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

f = open('hello.txt', 'w')    # 1) open file in write mode
f.write('Hello World!\n')     # 2) write string to file
f.write('Python file I/O\n')
f.close()                      # 3) close file

lines = ['First line\n', 'Second line\n', 'Third line\n']
f = open('lines.txt', 'w')
f.writelines(lines)
f.close()

# read entire file as a single string
f = open('hello.txt', 'r')
content = f.read()
print(content)
f.close()

# read one line at a time
f = open('hello.txt', 'r')
line1 = f.readline()  # first line
line2 = f.readline()  # second line
print(line1, line2)
f.close()

# read all lines as a list
f = open('hello.txt', 'r')
lines = f.readlines()  # ['Hello World!\n', 'Python file I/O\n']
print(lines)
f.close()

f = open('hello.txt', 'r')
for line in f:
    print(line, end=")  # avoid duplicate newlines
f.close()

# write file using with statement
with open('data.txt', 'w') as f:
    f.write('Name: Hong Gildong\n')
    f.write('Age: 20\n')
    f.write('Major: Computer Science\n')
# f.close() is called automatically when the block ends

# read file using with statement
with open('data.txt', 'r') as f:
    for line in f:
        print(line, end=")

# save grade data to file
students = [
    'Hong Gildong,85,90,78',
    'Kim Cheolsu,92,88,95',
    'Lee Younghee,76,82,89'
]

with open('scores.txt', 'w') as f:
    for s in students:
        f.write(s + '\n')

# read grades from file and compute averages
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

# specify encoding when reading/writing Korean text files
with open('korean.txt', 'w', encoding='utf-8') as f:
    f.write('Hello World\n')

with open('korean.txt', 'r', encoding='utf-8') as f:
    content = f.read()
