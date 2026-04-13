"""
제11장: 파이썬의 응용
으뜸 파이썬 Express — 예제 코드
"""

# ============================================================
# 나만의 단어장 앱
# ============================================================

import json
import random
import os

FILENAME = 'my_words.json'

def load_words():
    """Load vocabulary from file."""
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_words(words):
    """Save vocabulary to file."""
    with open(FILENAME, 'w', encoding='utf-8') as f:
        json.dump(words, f, ensure_ascii=False, indent=2)

def add_word(words):
    """Add a new word."""
    eng = input('English word : ').strip().lower()
    if eng in words:
        print(f'  "{eng}" is already registered.')
        return
    meaning = input('Meaning      : ').strip()
    words[eng] = meaning
    print(f'  "{eng}: {meaning}" added!')

def show_words(words):
    """Display all words."""
    if not words:
        print('  No words registered.')
        return
    print(f'  --- Total {len(words)} words ---')
    for eng, meaning in words.items():
        print(f'  {eng:20s} : {meaning}')

def search_word(words):
    """Search for a word."""
    eng = input('Word to search : ').strip().lower()
    if eng in words:
        print(f'  {eng} : {words[eng]}')
    else:
        print(f'  "{eng}" not found.')

def quiz(words):
    """Quiz mode: randomly ask 5 questions."""
    if len(words) < 2:
        print('  Need at least 2 words for a quiz.')
        return
    items = list(words.items())
    random.shuffle(items)
    count = min(5, len(items))
    score = 0
    print(f'\n  === Quiz Start ({count} questions) ===')
    for i, (eng, meaning) in enumerate(items[:count], 1):
        answer = input(f'  Q{i}. What does "{eng}" mean? ')
        if answer.strip() == meaning:
            print('  Correct!')
            score += 1
        else:
            print(f'  Wrong! The answer is "{meaning}".')
    print(f'\n  Result: {score} out of {count} correct')

def main():
    words = load_words()
    print('=== My Vocabulary App ===')
    while True:
        print('\n1.Add  2.List  3.Search  4.Quiz  5.Save  6.Quit')
        choice = input('Choice : ').strip()
        if choice == '1':
            add_word(words)
        elif choice == '2':
            show_words(words)
        elif choice == '3':
            search_word(words)
        elif choice == '4':
            quiz(words)
        elif choice == '5':
            save_words(words)
            print('  Saved!')
        elif choice == '6':
            save_words(words)
            print('  Vocabulary saved. Goodbye!')
            break
        else:
            print('  Invalid input.')

if __name__ == '__main__':
    main()

# ============================================================
# 비정형 데이터 정리 자동화
# ============================================================



# --- data\_cleaner.py \{ ---
import csv

INPUT_FILE = 'members_raw.txt'
OUTPUT_FILE = 'members.csv'

def unify_separator(line):
    """Replace / and , with | as a single separator."""
    line = line.replace('/', '|')
    line = line.replace(',', '|')
    if '|' not in line:
        # no / or , found: split by 2+ spaces
        parts = line.split()
        # regroup: name may be two words
        # find email (contains @) to locate fields
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

    # write CSV
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
# 달의 위상 시각화
# ============================================================

from datetime import datetime

LUNAR_CYCLE = 29.530588853  # synodic month (days)
KNOWN_NEW_MOON = datetime(1970, 1, 7, 20, 35)  # new moon (UTC)

def moon_age(date):
    """Calculate the moon's age (days since last new moon)."""
    diff = date - KNOWN_NEW_MOON
    days = diff.total_seconds() / 86400
    return days % LUNAR_CYCLE

import turtle

t = turtle.Turtle()
t.circle(100)          # draw a circle with radius 100
t.fillcolor('yellow')
t.begin_fill()
t.circle(100)
t.end_fill()           # fill the circle with yellow
turtle.done()

# --- moon\_phase.py \{ ---
import turtle
import math
from datetime import datetime

LUNAR_CYCLE = 29.530588853   # synodic month (days)
KNOWN_NEW_MOON = datetime(1970, 1, 7, 20, 35)  # new moon (UTC)
RADIUS = 120

def moon_age(date):
    """Calculate the moon's age in days."""
    diff = date - KNOWN_NEW_MOON
    days = diff.total_seconds() / 86400
    return days % LUNAR_CYCLE

def draw_filled_circle(t, x, y, r, color):
    """Draw a filled circle at (x, y) with radius r."""
    t.penup()
    t.goto(x, y - r)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()

def draw_moon(t, age):
    """Draw the moon shape based on its age."""
    phase = age / LUNAR_CYCLE   # 0.0 ~ 1.0
    bg = '#1a1a2e'              # dark sky
    bright = '#fffacd'          # lemon chiffon
    dark = bg                   # shadow = background

    # draw bright full circle first
    draw_filled_circle(t, 0, 0, RADIUS, bright)

    # calculate shadow ellipse width
    # phase 0~0.5: shadow shrinks from right
    # phase 0.5~1: shadow grows from right
    if phase <= 0.5:
        ratio = 1 - 2 * phase  # 1 -> 0
        shadow_from_right = True
    else:
        ratio = 2 * phase - 1  # 0 -> 1
        shadow_from_right = False

    # draw shadow as vertical slices (oval overlay)
    if ratio > 0.02:
        t.penup()
        shadow_rx = RADIUS * ratio
        steps = 200
        t.fillcolor(dark)
        t.begin_fill()
        for i in range(steps + 1):
            angle = math.pi * i / steps - math.pi / 2
            sy = RADIUS * math.sin(angle)
            if shadow_from_right:
                sx = shadow_rx * math.cos(angle)
            else:
                sx = -shadow_rx * math.cos(angle)
            # half circle (dark side)
            t.goto(sx, sy)
        # close with bright-side half circle
        for i in range(steps, -1, -1):
            angle = math.pi * i / steps - math.pi / 2
            sy = RADIUS * math.sin(angle)
            if shadow_from_right:
                sx = RADIUS * math.cos(angle)
            else:
                sx = -RADIUS * math.cos(angle)
            t.goto(sx, sy)
        t.end_fill()

def main():
    date_str = input('Enter date (YYYY-MM-DD), '
                     'or press Enter for today: ').strip()
    if date_str:
        date = datetime.strptime(date_str, '%Y-%m-%d')
    else:
        date = datetime.now()

    age = moon_age(date)
    print(f'Date : {date.strftime("%Y-%m-%d")}')
    print(f'Age  : {age:.1f} days')

    # set up turtle
    screen = turtle.Screen()
    screen.bgcolor('#1a1a2e')
    screen.title(f'Moon Phase - {date.strftime("%Y-%m-%d")}')
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.pencolor('#1a1a2e')

    draw_moon(t, age)

    # label
    t.penup()
    t.goto(0, -RADIUS - 40)
    t.pencolor('white')
    t.write(f'{date.strftime("%Y-%m-%d")}\n'
            f'Moon age: {age:.1f} days',
            align='center',
            font=('Arial', 14, 'normal'))
    turtle.done()

if __name__ == '__main__':
    main()


# ============================================================
# 웹 앱 만들기: Flask
# ============================================================

# install from terminal
# $ pip install flask

# --- hello\_flask.py \{ ---
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello, Flask!</h1><p>My first web app.</p>'

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def home():
    return '<h1>Home Page</h1><a href="/about">About</a>'

@app.route('/about')
def about():
    return '<h1>About</h1><p>This is a Flask web app.</p>'

@app.route('/greet/<name>')
def greet(name):
    return f'<h1>Hello, {name}!</h1>'

# --- app.py \{ ---
from flask import Flask, render_template

app = Flask(__name__)

tasks = ['Buy groceries', 'Read Python book', 'Exercise']

@app.route('/')
def home():
    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)


# --- todo\_app.py \{ ---
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

