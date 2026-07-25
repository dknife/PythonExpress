# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제10장 파이썬의 응용
# 코드 10.8: 템플릿을 사용하는 Flask 앱

from flask import Flask, render_template

app = Flask(__name__)

tasks = ['Buy groceries', 'Read Python book', 'Exercise']

@app.route('/')
def home():
    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
