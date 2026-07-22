"""
제10장: 파이썬의 응용
알짜 파이썬 — 예제 코드 (원고에서 자동 추출)
"""

# ============================================================
# 나만의 단어장 앱
# ============================================================

# --- 단어장 앱 전체 코드 — WordApp 클래스 ---
import json
import random
from pathlib import Path


class WordApp:
    """A simple vocabulary application."""

    def __init__(self, filename='my_words.json'):
        self.filename = Path(filename)
        self.words = {}
        self.load()

    def load(self):
        """Load vocabulary from file into self.words."""
        if self.filename.exists():
            with self.filename.open('r', encoding='utf-8') as f:
                self.words = json.load(f)
        else:
            self.words = {}

    def save(self):
        """Save self.words to the file."""
        with self.filename.open('w', encoding='utf-8') as f:
            json.dump(self.words, f, ensure_ascii=False, indent=2)

    def add(self):
        """Add a new word."""
        eng = input('English word : ').strip().lower()
        if eng in self.words:
            print(f' "{eng}" is already registered.')
            return
        meaning = input('Meaning : ').strip()
        self.words[eng] = meaning
        print(f' "{eng}: {meaning}" added!')

    def show(self):
        """Display all words."""
        if not self.words:
            print(' No words registered.')
            return
        print(f' --- Total {len(self.words)} words ---')
        for eng, meaning in self.words.items():
            print(f' {eng:20s} : {meaning}')

    def search(self):
        """Search for a word."""
        eng = input('Word to search : ').strip().lower()
        if eng in self.words:
            print(f' {eng} : {self.words[eng]}')
        else:
            print(f' "{eng}" not found.')

    def quiz(self):
        """Quiz mode: randomly ask up to 5 questions."""
        if len(self.words) < 2:
            print(' Need at least 2 words for a quiz.')
            return
        items = list(self.words.items())
        random.shuffle(items)
        count = min(5, len(items))
        score = 0
        print(f'\n === Quiz Start ({count} questions) ===')
        for i, (eng, meaning) in enumerate(items[:count], 1):
            answer = input(f' Q{i}. What does "{eng}" mean? ')
            if answer.strip() == meaning:
                print(' Correct!')
                score += 1
            else:
                print(f' Wrong! The answer is "{meaning}".')
        print(f'\n Result: {score} out of {count} correct')

    def run(self):
        """Main menu loop."""
        print('=== My Vocabulary App ===')
        while True:
            print('\n1.Add 2.List 3.Search 4.Quiz 5.Save 6.Quit')
            choice = input('Choice : ').strip()
            if choice == '1':
                self.add()
            elif choice == '2':
                self.show()
            elif choice == '3':
                self.search()
            elif choice == '4':
                self.quiz()
            elif choice == '5':
                self.save()
                print(' Saved!')
            elif choice == '6':
                self.save()
                print(' Vocabulary saved. Goodbye!')
                break
            else:
                print(' Invalid input.')


if __name__ == '__main__':
    app = WordApp()
    app.run()

# ============================================================
# 비정형 데이터 정리 자동화
# ============================================================

# --- 비정형 데이터 정리 자동화 ---
import csv

INPUT_FILE = 'members_raw.txt'
OUTPUT_FILE = 'members.csv'

def unify_separator(line):
    """Replace / and, with | as a single separator."""
    line = line.replace('/', '|')
    line = line.replace(',', '|')
    if '|' not in line:
        # /나 ,가 없는 경우: 공백으로 분리
        parts = line.split()
        # 재조합: 이름은 두 단어일 수 있음
        # @가 포함된 이메일을 찾아 필드 위치 파악
        for i, p in enumerate(parts):
            if '@' in p:
                email_idx = i
                break
        else:
            return None
        name = ' '.join(parts[:email_idx - 1])
        phone = parts[email_idx - 1]
        email = parts[email_idx]
        city = ' '.join(parts[email_idx + 1:])
        return f'{name}|{phone}|{email}|{city}'
    return line

def normalize_phone(phone):
    """Normalize phone number to 010-XXXX-XXXX format."""
    digits = ''
    for ch in phone:
        if ch.isdigit():
            digits += ch
    if len(digits) != 11:
        return None
    return f'{digits[:3]}-{digits[3:7]}-{digits[7:]}'

def clean_data(input_file, output_file):
    """Read raw text, clean it, and write to CSV."""
    cleaned = []
    errors = []

    with open(input_file, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line or line.startswith('#'):
                continue

            unified = unify_separator(line)
            if unified is None:
                errors.append((line_num, 'Cannot parse'))
                continue

            parts = unified.split('|')
            parts = [p.strip() for p in parts]

            if len(parts) != 4:
                errors.append((line_num, 'Field count error'))
                continue

            name, phone, email, city = parts
            phone = normalize_phone(phone)
            if phone is None:
                errors.append((line_num, 'Invalid phone'))
                continue

            cleaned.append({
                'name': name, 'phone': phone,
                'email': email, 'city': city
            })

    # CSV 파일로 저장
    fields = ['name', 'phone', 'email', 'city']
    with open(output_file, 'w', newline='',
              encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(cleaned)

    print(f'Completed: {len(cleaned)} records saved '
          f'to {output_file}')
    if errors:
        print(f'Warnings ({len(errors)} lines skipped):')
        for num, msg in errors:
            print(f'  Line {num}: {msg}')

if __name__ == '__main__':
    clean_data(INPUT_FILE, OUTPUT_FILE)

# ============================================================
# 프랙탈 그리기
# ============================================================

# --- turtle로 정사각형 그리기 ---
import turtle

t = turtle.Turtle()
t.speed(0)
for _ in range(4):
    t.forward(120) # 한 변 그리기
    t.left(90) # 90도 회전
turtle.done()

# --- 재귀 나무 그리기 ---
import turtle

ANGLE = 30 # 가지가 꺾이는 각도(단위: 도)
RATIO = 0.7 # 단계마다 줄어드는 길이 비율

def tree(t, length, depth):
    if depth == 0: # 종료 조건
        return
    t.forward(length) # 현재 가지 그리기
    t.left(ANGLE)
    tree(t, length * RATIO, depth - 1) # 왼쪽 부분 나무
    t.right(2 * ANGLE)
    tree(t, length * RATIO, depth - 1) # 오른쪽 부분 나무
    t.left(ANGLE)
    t.backward(length) # 시작 위치로 복귀

def main():
    screen = turtle.Screen()
    screen.bgcolor('white')
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.color('saddlebrown')
    t.left(90) # 위쪽을 향하도록 회전
    t.penup()
    t.goto(0, -200)
    t.pendown()
    tree(t, 110, 9)
    turtle.done()

if __name__ == '__main__':
    main()

# --- 코흐 눈송이 그리기 ---
import turtle

def koch(t, length, depth):
    if depth == 0:
        t.forward(length)
        return
    length /= 3
    koch(t, length, depth - 1); t.left(60)
    koch(t, length, depth - 1); t.right(120)
    koch(t, length, depth - 1); t.left(60)
    koch(t, length, depth - 1)

def main():
    screen = turtle.Screen()
    screen.bgcolor('midnightblue')
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.color('white')
    t.penup()
    t.goto(-150, 90)
    t.pendown()
    for _ in range(3): # 눈송이 = 코흐 곡선 3개
        koch(t, 300, 4)
        t.right(120)
    turtle.done()

if __name__ == '__main__':
    main()

# ============================================================
# 웹 앱 만들기: Flask
# ============================================================

# --- 첫 번째 Flask 웹 앱 ---
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello, Flask!</h1><p>My first web app.</p>'

if __name__ == '__main__':
    app.run(debug=True)

# --- 여러 URL 경로 연결과 동적 인자 받기 ---
@app.route('/')
def home():
    return '<h1>Home Page</h1><a href="/about">About</a>'

@app.route('/about')
def about():
    return '<h1>About</h1><p>This is a Flask web app.</p>'

@app.route('/greet/<name>')
def greet(name):
    return f'<h1>Hello, {name}!</h1>'

# --- 템플릿을 사용하는 Flask 앱 ---
from flask import Flask, render_template

app = Flask(__name__)

tasks = ['Buy groceries', 'Read Python book', 'Exercise']

@app.route('/')
def home():
    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)

# --- 할 일 관리 웹 앱 ---
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
tasks = []

@app.route('/')
def home():
    return render_template('todo.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect('/')

@app.route('/delete/<int:index>')
def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

# ============================================================
# 실습을 통한 10장 개념 정리
# ============================================================

# WordApp 클래스에 다음 메소드 추가
def delete(self):
    eng = input('Word to delete : ').strip().lower()
    if eng in self.words:
        del self.words[eng]
        print(f'  "{eng}" deleted!')
    else:
        print(f'  "{eng}" not found.')

import turtle
def tree(t, length, depth):
    if depth == 0: return
    t.pensize(depth)
    t.pencolor('saddlebrown' if depth > 3 else 'forestgreen')
    t.forward(length); t.left(25)
    tree(t, length * 0.7, depth - 1)
    t.right(50)
    tree(t, length * 0.7, depth - 1)
    t.left(25); t.pensize(depth); t.backward(length)

t = turtle.Turtle(); t.speed(0); t.hideturtle()
t.left(90); t.penup(); t.goto(0, -200); t.pendown()
tree(t, 110, 9); turtle.done()

import turtle
def sierpinski(t, length, depth):
    if depth == 0:
        for _ in range(3):
            t.forward(length); t.left(120)
        return
    h = length / 2
    sierpinski(t, h, depth - 1); t.forward(h)
    sierpinski(t, h, depth - 1)
    t.backward(h); t.left(60); t.forward(h); t.right(60)
    sierpinski(t, h, depth - 1)
    t.left(60); t.backward(h); t.right(60)

t = turtle.Turtle(); t.speed(0); t.hideturtle(); t.color('teal')
t.penup(); t.goto(-150, -130); t.pendown()
sierpinski(t, 300, 5); turtle.done()

def extract_lines(in_file, out_file, keyword):
    with open(in_file, 'r', encoding='utf-8') as fin, \
         open(out_file, 'w', encoding='utf-8') as fout:
        for line in fin:
            if keyword in line:
                fout.write(line)

extract_lines('log.txt', 'error_only.txt', 'ERROR')

import json

raw = '''[
  {"name": "Alice", "score": 92},
  {"name": "Bob",   "score": 75},
  {"name": "Carol", "score": 88}
]'''

students = json.loads(raw)              # 문자열을 list[dict]로 변환
top = [s for s in students if s['score'] >= 85]
print(json.dumps(top, ensure_ascii=False, indent=2))
