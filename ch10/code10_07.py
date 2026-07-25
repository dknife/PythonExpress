# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제10장 파이썬의 응용
# 코드 10.7: 여러 URL 경로 연결과 동적 인자 받기

@app.route('/')
def home():
    return '<h1>Home Page</h1><a href="/about">About</a>'

@app.route('/about')
def about():
    return '<h1>About</h1><p>This is a Flask web app.</p>'

@app.route('/greet/<name>')
def greet(name):
    return f'<h1>Hello, {name}!</h1>'
