# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제10장 파이썬의 응용
# 코드 10.6: 첫 번째 Flask 웹 앱

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello, Flask!</h1><p>My first web app.</p>'

if __name__ == '__main__':
    app.run(debug=True)
