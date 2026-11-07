# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제10장 파이썬의 응용
# 코드 10.7: 여러 URL 경로 연결과 동적 인자 받기

@app.route('/')
def home():
    return '<h1>홈 페이지</h1><a href="/about">소개</a>'

@app.route('/about')
def about():
    return '<h1>소개</h1><p>Flask로 만든 웹 앱입니다.</p>'

@app.route('/greet/<name>')
def greet(name):
    return f'<h1>안녕하세요, {name}!</h1>'
